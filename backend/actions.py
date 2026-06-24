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
        return {
            "type": "ticket_created",
            "message": "Support ticket TCK-0001 created successfully.",
            "data": {
                "ticket_id": "TCK-0001",
                "status": "Open"
            }
        }

    elif intent == "schedule_followup":
        return {
            "type": "followup_scheduled",
            "message": "Follow-up task FUP-0001 scheduled successfully.",
            "data": {
                "followup_id": "FUP-0001",
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
        return {
            "type": "human_escalation",
            "message": "Request escalated to a human agent.",
            "data": {
                "status": "Escalated",
                "priority": "Medium"
            }
        }