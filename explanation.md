# Tiny CRM Agent Router Using a Small Language Model

## 1. Project Overview

This project is a small AI-based CRM intent router. The main purpose of the project is to understand a user’s CRM-related request and identify what the user wants to do.

The system takes a user message as input, predicts the intent of that message using a fine-tuned small language model, and routes the request to the most suitable CRM agent or module.

For example, when the user enters:

“Summarize this customer conversation”

the system predicts the intent as:

`summarize_conversation`

and routes it to:

`Conversation Summary Agent`

At this stage, the system does not perform real CRM operations such as creating actual tickets or saving data in a database. It works as an intent classification and routing prototype.

---

## 2. Project Objective

The main objective of this project is to train and use a small language model for CRM-related intent classification.

The specific objectives are:

1. To create a small CRM intent dataset.
2. To fine-tune a pretrained small language model for intent classification.
3. To classify user requests into predefined CRM intents.
4. To return the predicted intent, confidence score, and route.
5. To connect the trained model with a FastAPI backend.
6. To create a simple React frontend for user interaction.
7. To show prediction results and prediction history in the frontend.

---

## 3. Problem Addressed by the Project

In a CRM system, users may enter different types of requests. For example:

* “Find customer details for Nimal”
* “Create a ticket for this complaint”
* “Remind me to call this lead tomorrow”
* “Check whether this workflow will break”

The system must understand the purpose behind each request. This purpose is called the intent.

Instead of sending every request directly to a large AI model or manually selecting the module, this project uses a small fine-tuned model to predict the intent and decide the correct route.

This helps to demonstrate how small language models can be used in agentic AI systems as lightweight decision-making components.

---

## 4. Intent Classes Used in the Project

The model was trained to classify user messages into six CRM-related intent classes.

| Intent                   | Meaning                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------ |
| `search_customer_info`   | The user wants to search or view customer/contact details.                           |
| `summarize_conversation` | The user wants to summarize a chat, call, email, or customer conversation.           |
| `create_lead_or_ticket`  | The user wants to create a new lead, support ticket, complaint, or CRM record.       |
| `schedule_followup`      | The user wants to schedule a reminder, callback, meeting, or follow-up task.         |
| `workflow_safety_check`  | The user wants to check whether a CRM workflow, field, or automation change is safe. |
| `escalate_to_human`      | The user request is unclear, risky, or needs human support.                          |

---

## 5. Dataset Creation

A small custom dataset was created for the CRM intent classification task.

The dataset contains example user messages and their correct intent labels.

Example dataset records:

| User Message                               | Label                    |
| ------------------------------------------ | ------------------------ |
| Find customer details for Nimal            | `search_customer_info`   |
| Summarize this customer conversation       | `summarize_conversation` |
| Create a support ticket for this complaint | `create_lead_or_ticket`  |
| Remind me to call this lead tomorrow       | `schedule_followup`      |
| Check whether this workflow will break     | `workflow_safety_check`  |
| This request is confusing                  | `escalate_to_human`      |

The dataset was generated using different sentence templates and small text variations. This helped the model learn different ways users may express the same intent.

---

## 6. Pretrained Model Used

The pretrained model used in this project is:

`distilbert-base-uncased`

This model is a smaller and faster version of BERT. It already has general English language understanding because it was pretrained before.

In this project, the model was not trained from zero. Instead, it was fine-tuned for a specific CRM intent classification task.

Before fine-tuning:

`distilbert-base-uncased` was a general English language model.

After fine-tuning:

It became a CRM intent classifier that can identify the correct intent from CRM-related user messages.

---

## 7. Model Training Process

The model training process was done using Google Colab.

The main training steps were:

1. Install required libraries such as Transformers, PyTorch, pandas, and scikit-learn.
2. Define the six CRM intent classes.
3. Create the CRM intent dataset.
4. Convert text labels into numeric labels.
5. Split the dataset into training and testing data.
6. Tokenize the text using the DistilBERT tokenizer.
7. Load `DistilBertForSequenceClassification`.
8. Fine-tune the model using the CRM dataset.
9. Evaluate the trained model.
10. Save the trained model as `tiny_crm_router`.

The model was trained to read a user message and predict one of the six predefined CRM intents.

---

## 8. Confidence-Based Routing

The system does not only return the predicted intent. It also calculates a confidence score.

The confidence score shows how sure the model is about its prediction.

Example:

```json
{
  "intent": "summarize_conversation",
  "confidence": 0.91,
  "route": "Conversation Summary Agent"
}
```

A confidence threshold was added to make the system safer.

If the confidence is low, the request is routed to human support or a main LLM instead of directly trusting the prediction.

Example:

```json
{
  "intent": "escalate_to_human",
  "confidence": 0.62,
  "route": "Escalate to Human or Main LLM"
}
```

This is useful in agentic AI systems because uncertain requests should not be handled automatically without review.

---

## 9. FastAPI Backend Implementation

A backend API was created using FastAPI.

The backend loads the trained model from the saved model folder:

`tiny_crm_router`

The backend has a prediction endpoint:

`POST /predict`

The frontend sends a user message to this endpoint. The backend then:

1. Receives the user message.
2. Sends the message to the trained model.
3. Predicts the intent.
4. Calculates the confidence score.
5. Selects the correct route.
6. Returns the result as JSON.

Example request:

```json
{
  "message": "Create a ticket for this complaint"
}
```

Example response:

```json
{
  "intent": "create_lead_or_ticket",
  "confidence": 0.89,
  "route": "Lead/Ticket Creation Agent"
}
```

The backend also supports FastAPI Swagger documentation through:

`http://127.0.0.1:8000/docs`

This allows easy testing of the API.

---

## 10. React Frontend Implementation

A simple React frontend was created using Vite.

The frontend allows the user to enter a CRM-related request in a text box and click a button to predict the intent.

The frontend sends the request to the FastAPI backend using a POST request.

After receiving the response, the frontend displays:

1. Predicted intent
2. Confidence score
3. Selected route

The frontend also includes a prediction history section. This shows previous user messages and their prediction results.

Frontend features include:

* Text input area
* Predict Intent button
* Loading state
* Error message handling
* Prediction result display
* Prediction history display

---

## 11. Current System Architecture

The current system architecture is:

```text
React Frontend
    ↓
FastAPI Backend
    ↓
Fine-tuned DistilBERT Model
    ↓
Intent Prediction
    ↓
Confidence Check
    ↓
Route Selection
    ↓
Result Displayed in Frontend
```

This architecture shows how a small language model can be connected with a backend and frontend to create a working AI-powered routing prototype.

---

## 12. Current Project Workflow

The current project workflow is:

1. The user enters a CRM request in the React frontend.
2. The frontend sends the message to the FastAPI backend.
3. The backend tokenizes the message.
4. The trained DistilBERT model predicts the intent.
5. The backend calculates the confidence score.
6. The router selects the correct route based on the predicted intent.
7. The backend sends the result back to the frontend.
8. The frontend displays the intent, confidence, route, and prediction history.

---

## 13. Example Test Inputs and Expected Outputs

| User Request                                   | Expected Intent          | Expected Route              |
| ---------------------------------------------- | ------------------------ | --------------------------- |
| Find the email address of this customer        | `search_customer_info`   | Customer Search Agent       |
| Summarize this customer conversation           | `summarize_conversation` | Conversation Summary Agent  |
| Create a ticket for this complaint             | `create_lead_or_ticket`  | Lead/Ticket Creation Agent  |
| Remind me to call this lead tomorrow           | `schedule_followup`      | Task Scheduling Agent       |
| Check whether this workflow will break         | `workflow_safety_check`  | Workflow Safety Check Agent |
| This request is unclear and needs human review | `escalate_to_human`      | Human Support Agent         |

The actual confidence values may be slightly different because they are generated by the trained model.

---

## 14. Tools and Technologies Used

| Tool / Technology         | Purpose                                |
| ------------------------- | -------------------------------------- |
| Python                    | Model training and backend development |
| Google Colab              | Model training environment             |
| PyTorch                   | Deep learning framework                |
| Hugging Face Transformers | Loading and fine-tuning DistilBERT     |
| scikit-learn              | Dataset splitting and evaluation       |
| pandas                    | Dataset handling                       |
| FastAPI                   | Backend API development                |
| Uvicorn                   | Running the FastAPI server             |
| React                     | Frontend development                   |
| Vite                      | React project setup                    |
| Git and GitHub            | Version control and project hosting    |

---

## 15. Current Limitations

At this stage, the project is a working prototype, but it has some limitations.

1. The system only predicts intent and route.
2. It does not yet perform real CRM actions.
3. It does not yet save tickets, reminders, or prediction logs in a database.
4. The dataset is still small, so the confidence can be low for some new sentences.
5. The trained model folder is not uploaded to GitHub because the model file is large.
6. The system does not yet connect to a real CRM database or production CRM API.

---

## 16. What Has Been Completed

The following parts have been completed:

1. CRM intent schema was defined.
2. Custom CRM intent dataset was created.
3. DistilBERT pretrained model was fine-tuned.
4. The trained model was saved as `tiny_crm_router`.
5. FastAPI backend was created.
6. Backend prediction endpoint was implemented.
7. React frontend was created.
8. Frontend was connected to the backend.
9. Prediction result display was implemented.
10. Prediction history was added.
11. GitHub repository was created.
12. Large files such as virtual environment, node modules, and trained model were ignored using `.gitignore`.

---

## 17. What the Project Demonstrates

This project demonstrates how a small language model can be used in an agentic AI system.

The model acts as a router that understands the user’s intent and selects the correct CRM module or agent.

This proves that a small fine-tuned model can be useful for focused tasks such as CRM request classification. It also shows that not every request needs to be sent directly to a large language model. A small model can handle simple and clear requests quickly and efficiently.

---

## 18. Conclusion

This project successfully implements a Tiny CRM Agent Router using a fine-tuned small language model. The system can classify CRM-related user requests into six predefined intents and route them to the correct CRM agent.

The project includes a trained DistilBERT-based intent classifier, a FastAPI backend, and a React frontend. The frontend allows users to enter requests and view the predicted intent, confidence score, selected route, and prediction history.

At the current stage, the project works as an intent classification and routing prototype. Future improvements can include database integration, real ticket creation, follow-up scheduling, feedback collection, improved dataset training, and connection with real CRM services.
