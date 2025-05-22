from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
import gradio_ui
from routes_1 import router

app = FastAPI(title="Mental Health Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

app.mount("/chat", WSGIMiddleware(gradio_ui.gradio_app))

@app.get("/")
def root():
    return {"message": "Mental Health Chatbot API is running."}
