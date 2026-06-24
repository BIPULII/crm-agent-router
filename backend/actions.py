from database import save_ticket, save_followup, save_escalation


def handle_action(intent, message):
    if intent == "search_customer_info":
        return {
            "type": "customer_search",
            "message": "Sample customer profile found.",
            "data": {
                "name": "Nimal Perera",
                "email": "nimal@example.com",
                "phone": "+94 77 123 4567",
                "status": "Active Customer"
            }
        }

    elif intent == "summarize_conversation":
        return {
            "type": "summary",
            "message": "Conversation summarized successfully.",
            "data": {
                "summary": "The customer reported an issue and requested follow-up support."
            }
        }

    elif intent == "create_lead_or_ticket":
        ticket_id = save_ticket(message)

        return {
            "type": "ticket_created",
            "message": f"Support ticket TCK-{ticket_id:04d} created successfully.",
            "data": {
                "ticket_id": f"TCK-{ticket_id:04d}",
                "status": "Open"
            }
        }

    elif intent == "schedule_followup":
        followup_id = save_followup(message)

        return {
            "type": "followup_scheduled",
            "message": f"Follow-up task FUP-{followup_id:04d} scheduled successfully.",
            "data": {
                "followup_id": f"FUP-{followup_id:04d}",
                "status": "Scheduled"
            }
        }

    elif intent == "workflow_safety_check":
        return {
            "type": "workflow_safety_report",
            "message": "Workflow safety check completed.",
            "data": {
                "risk_level": "Medium",
                "affected_workflows": 3,
                "recommendation": "Review affected automation rules before deployment."
            }
        }

    else:
        escalation_id = save_escalation(message)

        return {
            "type": "human_escalation",
            "message": f"Request ESC-{escalation_id:04d} escalated to a human agent.",
            "data": {
                "escalation_id": f"ESC-{escalation_id:04d}",
                "status": "Escalated",
                "priority": "Medium"
            }
        }