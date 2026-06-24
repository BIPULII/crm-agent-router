
from database import create_tables, save_prediction_log
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from router_model import predict_intent
from actions import handle_action

app = FastAPI(
    title="Tiny CRM Agent Router API",
    description="This API predicts CRM user intent and returns a routed action result.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Tiny CRM Agent Router API is running"
    }


@app.post("/predict")
def predict(request: UserRequest):
    prediction = predict_intent(request.message)

    action_result = handle_action(
        prediction["intent"],
        request.message
    )

    return {
        "message": request.message,
        "intent": prediction["intent"],
        "confidence": prediction["confidence"],
        "route": prediction["route"],
        "action_result": action_result
    }