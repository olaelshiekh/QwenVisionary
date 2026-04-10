# 🤖 Qwen Visionary

A powerful and intuitive chatbot built with **Streamlit** that leverages the **Qwen AI Model** for multimodal tasks. Convert between text and images seamlessly with a beautiful, user-friendly interface.

## ✨ Features

### 📝 Image to Text (Vision Analysis)
- **Upload Images**: Support for JPG, JPEG, PNG, GIF, and WEBP formats
- **Custom Prompts**: Ask specific questions about your images
- **Real-time Analysis**: Stream responses from Qwen's advanced vision capabilities
- **Error Handling**: Intelligent image validation and error recovery

### 🎨 Text to Image (Image Generation)
- **Text-to-Image Generation**: Create images from detailed text descriptions
- **Multiple Models**: Choose from multiple state-of-the-art generation models:
  - Stable Diffusion 3 Medium
  - Stable Diffusion 2.1
  - FLUX.1 Schnell
- **Download Capability**: Save generated images to your device
- **High-Quality Output**: Professional-grade image generation

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- HuggingFace API Token ([Get one here](https://huggingface.co/settings/tokens))
- pip or conda for package management

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/olaelshiekh/QwenVisionary.git
   cd QwenVisionary
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   HF_TOKEN=your_huggingface_api_token_here
   ```

### Running the Application

```bash
streamlit run app.py
```

The app will start at `http://localhost:8501` in your browser.

## 📦 Dependencies

- **streamlit** - Web application framework
- **huggingface-hub** - HuggingFace API client
- **python-dotenv** - Environment variable management
- **Pillow** - Image processing
- **requests** - HTTP library

See `requirements.txt` for complete list with versions.

## 🎯 Usage Guide

### Image to Text Mode
1. Click the sidebar and select **"📝 Image to Text"**
2. Upload an image from your computer
3. (Optional) Customize the prompt in the text area
4. Click **"🔍 Analyze Image"**
5. Wait for the AI to generate a detailed description

### Text to Image Mode
1. Click the sidebar and select **"🎨 Text to Image"**
2. Enter a detailed description of the image you want to create
3. (Optional) Choose a different generation model from the dropdown
4. Click **"✨ Generate Image"**
5. Download the generated image when ready

## 🔧 Technical Architecture

```
┌─────────────────────────────────────┐
│      Streamlit UI                    │
│  ┌──────────────────────────────┐   │
│  │ Image to Text Mode           │   │
│  │ Text to Image Mode           │   │
│  └──────────────────────────────┘   │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│   HuggingFace Inference Client      │
│  ┌──────────────────────────────┐   │
│  │ Vision Analysis (Qwen)       │   │
│  │ Image Generation (SD, FLUX)  │   │
│  └──────────────────────────────┘   │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│   HuggingFace AI Models             │
│  ┌──────────────────────────────┐   │
│  │ Qwen/Qwen3.5-9B             │   │
│  │ Stable Diffusion 3           │   │
│  │ FLUX.1                       │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

## 🔐 Security & Privacy

- API tokens are managed through `.env` files (never committed to git)
- Images are processed securely through HuggingFace's infrastructure
- No images are stored locally by the application
- All communication uses HTTPS encryption

## 🐛 Troubleshooting

### "HF_TOKEN not found"
- Ensure your `.env` file exists in the project root
- Verify the token is correctly formatted
- Check that the file is named exactly `.env`

### Image Analysis Error: "list index out of range"
- This typically means the API response was empty
- Try uploading a different image format (PNG or JPEG recommended)
- Verify your HF_TOKEN has appropriate permissions

### Image Generation Errors
- Ensure your HF_TOKEN has access to the selected model
- Try a simpler text prompt
- Check your HuggingFace account's usage limits

## 📝 Example Prompts

### For Image Analysis
- "Describe what you see in this image"
- "What objects are in this photo?"
- "Analyze the mood and composition"
- "What text appears in this image?"

### For Image Generation
- "A serene landscape with mountains, lake, and sunset"
- "A cozy coffee shop with warm lighting and wooden furniture"
- "Abstract art with vibrant colors and geometric shapes"
- "Portrait of a person in professional attire"

## 🎨 UI Features

- **Responsive Design**: Works seamlessly on desktop and tablet
- **Real-time Streaming**: See responses as they're generated
- **Dark Mode Support**: Adapts to your system's color preference
- **Intuitive Navigation**: Sidebar mode switching with radio buttons
- **Visual Feedback**: Loading states, success messages, and error handling

## 📈 Future Enhancements

- [ ] Chat history persistence
- [ ] Multiple image batch processing
- [ ] Custom model fine-tuning support
- [ ] Advanced image editing capabilities
- [ ] Multi-language support
- [ ] API endpoint deployment

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support & Contact

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/olaelshiekh/QwenVisionary/issues)
- Check existing documentation and FAQs
- Review the troubleshooting section above

## 🙏 Acknowledgments

- **Qwen Team** for the powerful vision and language models
- **HuggingFace** for the Inference API
- **Streamlit** for the amazing web framework
- **Stability AI** for Stable Diffusion models
- **Black Forest Labs** for FLUX.1 model

---

**Made with ❤️ by Ola Elshiekh**

⭐ If you find this project useful, please consider giving it a star!
