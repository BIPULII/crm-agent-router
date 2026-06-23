from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from router_model import predict_intent

app = FastAPI(
    title="Tiny CRM Agent Router API",
    description="This API predicts CRM user intent and routes it to the correct agent.",
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
    result = predict_intent(request.message)
    return result