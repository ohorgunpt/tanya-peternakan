import gradio as gr
from google import genai
import os

# Konfigurasi API Key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def tanya_ternak(message, history):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=f"""
            Kamu adalah asisten ahli peternakan Indonesia yang ramah dan profesional.
            Jawab dengan jelas, praktis, dan mudah dipahami.

            Pertanyaan: {message}
            """
        )

        return response.text

    except Exception as e:
        return f"Maaf, ada kendala teknis: {str(e)}"

demo = gr.ChatInterface(
    fn=tanya_ternak,
    title="🐮 Tanya-Peternakan AI",
    description="Konsultasi masalah sapi, domba, kambing, ayam, dan ternak lainnya.",
)

if __name__ == "__main__":
    demo.launch()
