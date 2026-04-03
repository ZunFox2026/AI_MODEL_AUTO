import os
import uvicorn
from fastapi import FastAPI, Request
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

# Đọc model name
with open("model_config.txt", "r") as f:
    MODEL_NAME = f.read().strip()

# Load model và tokenizer
print(f"Loading model {MODEL_NAME}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()
print("Model loaded")

@app.get("/")
def read_root():
    return {"message": f"AI Model {MODEL_NAME} is running", "status": "ok"}

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    max_length = data.get("max_length", 100)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
