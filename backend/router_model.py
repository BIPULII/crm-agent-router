import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "./tiny_crm_router"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model.to(device)
model.eval()

id_to_label = {
    0: "search_customer_info",
    1: "summarize_conversation",
    2: "create_lead_or_ticket",
    3: "schedule_followup",
    4: "workflow_safety_check",
    5: "escalate_to_human"
}

route_map = {
    "search_customer_info": "Customer Search Agent",
    "summarize_conversation": "Conversation Summary Agent",
    "create_lead_or_ticket": "Lead/Ticket Creation Agent",
    "schedule_followup": "Task Scheduling Agent",
    "workflow_safety_check": "Workflow Safety Check Agent",
    "escalate_to_human": "Human Support Agent"
}


def predict_intent(user_input: str, threshold: float = 0.50):
    encoding = tokenizer(
        user_input,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=64
    )

    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        probabilities = torch.softmax(outputs.logits, dim=1)
        confidence, predicted_class = torch.max(probabilities, dim=1)

    intent_id = predicted_class.item()
    confidence_score = confidence.item()
    intent_name = id_to_label[intent_id]

    if confidence_score < threshold:
        return {
            "intent": "escalate_to_human",
            "confidence": round(confidence_score, 4),
            "route": "Escalate to Human or Main LLM"
        }

    return {
        "intent": intent_name,
        "confidence": round(confidence_score, 4),
        "route": route_map[intent_name]
    }