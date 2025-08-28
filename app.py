import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

#Class pydantic
class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1)

#definir le chemin abolu
BASE_DIR = Path(__file__).resolve().parent

# initialiser le projet
app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR/"templates")
app.mount("/static", StaticFiles(directory=BASE_DIR/"static"), name="static")

# Variables pour Hugging Face
MODEL_NAME = os.getenv("HF_MODEL", "distilbert-base-uncased-finetuned-sst-2-english")
CACHE_DIR = os.getenv("HF_HOME", "/tmp/huggingface")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=-1)


# Page HTML avec formulaire (GET)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request,"index.html", {"request": request, "result": None})

# Envoyer le formulaire 
@app.post("/", response_class=JSONResponse)
async def analyze_json(input: PredictRequest):
    text = input.text.strip()
    
    result = classifier(text)[0]
    label = result["label"].lower()
    score = result["score"]

    return {
        "text": text,
        "sentiment": label,
        "confidence": round(score, 3)
    }

# Route de santé
@app.get("/health", response_class=JSONResponse)
async def health_check():
    return {"status": "ok"}



#uvicorn app:app --reload --host 127.0.0.1 --port 7860












