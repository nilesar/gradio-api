import torch
import gradio as gr
from TTS.api import TTS
import os

# Use CUDA if available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load TTS model
tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch").to(device)

# Ensure output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

def generate_audio(text):
    output_path = os.path.join(output_dir, "output.wav")
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# Define the Gradio interface as an API
iface = gr.Interface(
    fn=generate_audio,
    inputs=gr.Textbox(label="Enter text for speech synthesis"),
    outputs=gr.Audio(label="Generated Speech"),
    title="Coqui TTS API",
    description="Enter text and generate speech using Coqui TTS.",
)

# Allow access from the internet
iface.launch(server_name="0.0.0.0", server_port=10000)
