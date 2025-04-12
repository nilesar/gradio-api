# 🗣️ Multilingual TTS App using Coqui TTS & Gradio


This project is a **Multilingual Text-to-Speech (TTS) application** built using the [Coqui TTS](https://github.com/coqui-ai/TTS) library and [Gradio](https://gradio.app/) for the user interface. It allows you to input text and generate natural-sounding speech in **English and Bengali**, with both male and female voices available.

> ✨ Built as a fun and educational contribution at **IIT(BHU), VARANASI** ❤️

---

## 🚀 Features

- 🔊 Multilingual support: English and Bengali
- 👦👧 Supports both male and female voices for Bengali
- ⚡ Powered by Coqui's open-source TTS models
- 🖥️ Real-time speech synthesis with Gradio interface
- 🎛️ Simple UI to test and download generated audio
- 💾 Outputs audio as `.wav` file in `/output` directory

---

## 🧠 How It Works

1. User enters text and selects a TTS model.
2. The app loads the corresponding Coqui TTS model.
3. Speech is generated and saved to an `output.wav` file.
4. The resulting audio is played back in the browser.

---

## 📦 Requirements

- Python 3.8+
- PyTorch with CUDA (optional but recommended for faster synthesis)
- [TTS (Coqui)](https://pypi.org/project/TTS/)
- Gradio

### 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/multilingual-tts-gradio.git
cd multilingual-tts-gradio

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install torch
pip install TTS
pip install gradio
