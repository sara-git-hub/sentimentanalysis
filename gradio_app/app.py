import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

interface = gr.Interface(
    fn=classifier,
    inputs=gr.Textbox(lines=5, placeholder="Écrivez votre texte ici..."),
    outputs="text",
    title="Analyse de Sentiment",
    description="Entrez un texte pour analyser son sentiment"
)

if __name__ == "__main__":
    interface.launch(share=True, server_port=7860, server_name="0.0.0.0")