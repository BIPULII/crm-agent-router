
---

# Tiny CRM Agent Router — Project Overview (Updated)

## 1. Project Purpose

The **Tiny CRM Agent Router** is a web-based AI prototype that predicts the intent of CRM-related user requests and routes them to the appropriate agent. The system uses a fine-tuned small language model (SLM) to classify messages, calculate confidence, and determine the action route.

The project now includes:

* **Reset button** — clears input, results, and prediction history.
* **Prediction history** — shows all previous messages with intent, confidence, route, and action result.
* **Confidence color indicator** — visualizes the model’s certainty.
* **Action result display** — shows the outcome of the routed action.

---

## 2. How the System Works

1. The user enters a CRM-related request in the frontend input box.
2. Clicking **Predict Intent** sends the message to the backend FastAPI server.
3. The backend:

   * Processes the message with the trained SLM.
   * Predicts the intent.
   * Calculates confidence.
   * Selects the correct route.
   * Simulates or executes the action.
4. The frontend displays:

   * Predicted **Intent**
   * **Confidence** (with color coding: green, orange, red)
   * **Route**
   * **Action Result**
   * **Prediction History**

---

## 3. Example Usage

### User Input:

```
summarize the meeting
```

### Frontend Display:

**Buttons:**

```
Predict Intent   Reset
```

**Prediction Result:**

* **Intent:** summarize_conversation
* **Confidence:** 58.80% (orange color)
* **Route:** Conversation Summary Agent

**Action Result:**

```
Status: Conversation summarized successfully.
{
  "summary": "The customer reported an issue and requested follow-up support."
}
```

**Prediction History:**

| Message                  | Intent                 | Confidence | Route                         | Action                                       |
| ------------------------ | ---------------------- | ---------- | ----------------------------- | -------------------------------------------- |
| summarize the meeting    | summarize_conversation | 58.80%     | Conversation Summary Agent    | Conversation summarized successfully.        |
| create ticket for user 1 | escalate_to_human      | 34.37%     | Escalate to Human or Main LLM | Request ESC-0001 escalated to a human agent. |

---

## 4. Frontend Features

* **Input Area:** Users enter CRM-related requests.
* **Predict Intent Button:** Sends input to the backend and triggers prediction.
* **Reset Button:** Clears input, results, and prediction history.
* **Prediction Result Card:** Shows intent, confidence, route, and action result.
* **Prediction History Card:** Displays all previous predictions in chronological order.

---

## 5. Backend Features

* **FastAPI API:** Provides `/predict` endpoint for frontend requests.
* **SLM Model:** Fine-tuned DistilBERT (`distilbert-base-uncased`) for intent classification.
* **Action Simulation:** Returns structured action results for each intent.
* **SQLite Database (optional for logging):** Can store tickets, follow-ups, escalations, and prediction logs.

---

## 6. Benefits

* Users can track multiple requests and see the AI’s predictions.
* Reset button improves usability during testing and demos.
* History provides audit trail for testing and debugging.
* Confidence color guides the user on the reliability of predictions.

---

## 7. Next Improvements (Future Work)

* Connect action results to a real CRM system.
* Add analytics dashboard for total tickets, follow-ups, and escalations.
* Implement confidence-based routing thresholds.
* Add multi-agent handling for more advanced CRM automation.

---

