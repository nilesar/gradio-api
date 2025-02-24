import torch
import gradio as gr
from TTS.api import TTS
import os

# Use CUDA if available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Dictionary of available models
models = {
    "English - Male": "tts_models/en/ljspeech/fast_pitch",
    "Bengali - Male": "tts_models/bn/custom/vits-male",
    "Bengali - Female": "tts_models/bn/custom/vits-female",
}

def generate_audio(text, model_name):
    if model_name not in models:
        return "Invalid model selection"
    
    tts = TTS(model_name=models[model_name]).to(device)
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "output.wav")
    
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Multilingual TTS --(IIT(BHU)VARANASI)")
    gr.Markdown("Enter text and select a model to generate speech using Coqui TTS😊.")
    
    text_input = gr.Textbox(label="Enter text for speech synthesis")
    model_dropdown = gr.Dropdown(choices=list(models.keys()), label="Select Voice Model❤️")
    audio_output = gr.Audio(label="Generated Speech😊")
    
    generate_button = gr.Button("Generate Speech Of your choice")
    generate_button.click(fn=generate_audio, inputs=[text_input, model_dropdown], outputs=audio_output)
    
    gr.Markdown("### Built at IIT(BHU)VARANASI❤️")

demo.launch(server_name="127.0.0.1", server_port=5000)
