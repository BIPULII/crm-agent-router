# Tiny CRM Agent Router using SLM

This project trains a small language model to classify CRM-related user requests into predefined intents. The trained model works as an agentic AI router that sends each request to the correct CRM agent.

## Main Features

- CRM intent classification
- Small language model fine-tuning using DistilBERT
- Confidence-based routing
- FastAPI backend
- React frontend
- Prediction history display

## Intent Classes

1. search_customer_info
2. summarize_conversation
3. create_lead_or_ticket
4. schedule_followup
5. workflow_safety_check
6. escalate_to_human

## System Flow

User Message  
→ React Frontend  
→ FastAPI Backend  
→ Trained SLM Model  
→ Intent Prediction  
→ Agent Route

## Backend Run Command

```bash
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload --port 8000