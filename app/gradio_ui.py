# gradio_ui.py
import os
import gradio as gr
from routes_1 import chatbot_response  # import from routes.py
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def gradio_interface():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox(label="Enter your message")
        api_key = gr.Textbox(label="API Key", type="password")
        btn = gr.Button("Send")

        def respond(message, key, history):
            if key != API_KEY:
                history = history or []
                history.append({"role": "assistant", "content": "Error: Invalid API key"})
                return history
            
            history = history or []
            history.append({"role": "user", "content": message})

            response_msg, severity, resources = chatbot_response(message)
            bot_reply = f"{response_msg}\nSeverity: {severity}\nResources: {', '.join(resources) if resources else 'None'}"
            history.append({"role": "assistant", "content": bot_reply})

            return history

        btn.click(respond, inputs=[msg, api_key, chatbot], outputs=chatbot)

    return demo.launch(share=True)

gradio_app = gradio_interface()
if __name__ == "__main__":
    gradio_app.launch(share=True)