import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image
import io
import requests

load_dotenv()

# Verify HF_TOKEN is loaded
hf_token = os.environ.get("HF_TOKEN")
if not hf_token:
    st.error("HF_TOKEN not found in environment variables. Please set it in .env file.")
    st.stop()

client = InferenceClient(api_key=hf_token)

# Page configuration
st.set_page_config(
    page_title="Qwen Vision Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 Qwen Vision Chatbot")
st.markdown("Convert between text and images using Qwen AI Model")

# Sidebar for mode selection
mode = st.sidebar.radio(
    "Select Mode:",
    ["📝 Image to Text", "🎨 Text to Image"]
)

# Mode 1: Image to Text
if mode == "📝 Image to Text":
    st.header("📝 Image to Text (Vision Analysis)")
    st.markdown("Upload an image and get AI-generated description")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png", "gif", "webp"]
        )
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with col2:
        st.subheader("AI Analysis")
        
        # Custom prompt input
        prompt = st.text_area(
            "Enter your question about the image:",
            value="Describe this image in detail.",
            height=100
        )
        
        if st.button("🔍 Analyze Image", key="analyze_btn"):
            if uploaded_file:
                with st.spinner("Analyzing image with Qwen..."):
                    try:
                        import base64
                        
                        # Save uploaded file to temporary location for processing
                        uploaded_file.seek(0)
                        image_data = uploaded_file.read()
                        
                        # Verify image is valid and re-encode it properly
                        image = Image.open(io.BytesIO(image_data))
                        
                        # Convert to bytes in a specific format to ensure it's valid
                        img_buffer = io.BytesIO()
                        image.save(img_buffer, format='PNG')
                        img_buffer.seek(0)
                        image_bytes = img_buffer.getvalue()
                        image_base64 = base64.b64encode(image_bytes).decode()
                        
                        stream = client.chat.completions.create(
                            model="Qwen/Qwen3.5-9B:together",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": prompt
                                        },
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": f"data:image/png;base64,{image_base64}"
                                            }
                                        }
                                    ]
                                }
                            ],
                            stream=True,
                        )
                        
                        # Display streaming response
                        response_text = ""
                        response_container = st.empty()
                        
                        for chunk in stream:
                            # Check if choices list exists and is not empty
                            if chunk.choices and len(chunk.choices) > 0:
                                # Check if delta exists and has content
                                if chunk.choices[0].delta and hasattr(chunk.choices[0].delta, 'content'):
                                    content = chunk.choices[0].delta.content
                                    if content:
                                        response_text += content
                                        response_container.markdown(response_text)
                        
                        st.success("✅ Analysis complete!")
                        
                    except Exception as e:
                        st.error(f"❌ Error analyzing image: {str(e)}")
                        st.info("💡 Tip: Try using a PNG or JPEG image. Some image formats may not be supported.")
            else:
                st.warning("⚠️ Please upload an image first.")

# Mode 2: Text to Image
else:  # Text to Image
    st.header("🎨 Text to Image (Image Generation)")
    st.markdown("Generate images from text descriptions using AI")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Text Prompt")
        text_prompt = st.text_area(
            "Describe the image you want to generate:",
            value="A beautiful sunset over mountains",
            height=150,
            key="text_prompt"
        )
        
        st.subheader("Settings")
        # Model selection for text-to-image
        model_choice = st.selectbox(
            "Select Generation Model:",
            [
                "black-forest-labs/FLUX.1-schnell"
            ]
        )
        
        generate_btn = st.button("✨ Generate Image", key="generate_btn")
    
    with col2:
        st.subheader("Generated Image")
        
        if generate_btn:
            if text_prompt.strip():
                with st.spinner("🎨 Generating image... This may take a moment..."):
                    try:
                        # Use HuggingFace Inference API for image generation
                        image = client.text_to_image(
                            prompt=text_prompt,
                            model=model_choice
                        )
                        
                        # Display generated image
                        st.image(image, caption="Generated Image", use_container_width=True)
                        
                        # Option to download
                        img_byte_arr = io.BytesIO()
                        image.save(img_byte_arr, format='PNG')
                        img_byte_arr.seek(0)
                        
                        st.download_button(
                            label="📥 Download Image",
                            data=img_byte_arr,
                            file_name="generated_image.png",
                            mime="image/png"
                        )
                        
                        st.success("✅ Image generated successfully!")
                        
                    except Exception as e:
                        st.error(f"❌ Error generating image: {str(e)}")
                        st.info("💡 Tip: Make sure your HF_TOKEN has access to the selected model.")
            else:
                st.warning("⚠️ Please enter a text prompt.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center'>"
    "<p>Powered by Qwen AI Model via HuggingFace 🚀</p>"
    "</div>",
    unsafe_allow_html=True
)