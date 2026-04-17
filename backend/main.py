from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import torch
import pickle
from utils import text_preprocessing
from model import RNN

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# load model
model = RNN(input_size=5000)
model.load_state_dict(torch.load('model/sentiment_state_dict.pt', map_location=device))
model.to(device)
model.eval()


# request schema
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    text_matrix = text_preprocessing(data.text)

    xb = torch.tensor(text_matrix.toarray(), dtype=torch.float32).to(device)

    with torch.no_grad():
        xb = xb.unsqueeze(1)

        output = model(xb)
        output = torch.sigmoid(output).squeeze(1)

        pred = output.item()
        if(pred < 0.4):
            sentiment = 'negative'
        elif(pred > 0.6):
            sentiment = 'positive'
        else:
            sentiment = 'neutral'

        prob = output.item()

    return {
        "sentiment": sentiment,
        "confidence": prob,

    }