from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from router_model import predict_intent
from actions import handle_action
from database import (
    create_tables,
    save_prediction_log,
    get_all_logs,
    get_all_tickets,
    get_all_followups
)

app = FastAPI(
    title="Tiny CRM Agent Router API",
    description="This API predicts CRM user intent and performs routed CRM actions.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()


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

    save_prediction_log(
        message=request.message,
        intent=prediction["intent"],
        confidence=prediction["confidence"],
        route=prediction["route"],
        action_result=action_result["message"]
    )

    return {
        "message": request.message,
        "intent": prediction["intent"],
        "confidence": prediction["confidence"],
        "route": prediction["route"],
        "action_result": action_result
    }


@app.get("/logs")
def logs():
    rows = get_all_logs()

    return [
        {
            "id": row[0],
            "message": row[1],
            "intent": row[2],
            "confidence": row[3],
            "route": row[4],
            "action_result": row[5],
            "created_at": row[6]
        }
        for row in rows
    ]


@app.get("/tickets")
def tickets():
    rows = get_all_tickets()

    return [
        {
            "id": f"TCK-{row[0]:04d}",
            "message": row[1],
            "status": row[2],
            "created_at": row[3]
        }
        for row in rows
    ]


@app.get("/followups")
def followups():
    rows = get_all_followups()

    return [
        {
            "id": f"FUP-{row[0]:04d}",
            "message": row[1],
            "status": row[2],
            "created_at": row[3]
        }
        for row in rows
    ]