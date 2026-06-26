# backend/database.py

import sqlite3
from datetime import datetime

DB_NAME = "crm_router.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Tickets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT,
            priority TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)

    # Follow-ups table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT,
            due_date TEXT,
            created_at TEXT NOT NULL
        )
    """)

    # Escalations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escalations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT,
            created_at TEXT NOT NULL
        )
    """)

    # Prediction logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            intent TEXT NOT NULL,
            confidence REAL NOT NULL,
            route TEXT NOT NULL,
            action_result TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Save a ticket
def save_ticket(message, assigned_to="Support Team A", priority="Medium"):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = get_current_time()
    cursor.execute("""
        INSERT INTO tickets (message, status, assigned_to, priority, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (message, "Open", assigned_to, priority, created_at, created_at))

    ticket_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return ticket_id


# Save a follow-up
def save_followup(message, assigned_to="Support Team A", due_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = get_current_time()
    if due_date is None:
        due_date = created_at

    cursor.execute("""
        INSERT INTO followups (message, status, assigned_to, due_date, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (message, "Scheduled", assigned_to, due_date, created_at))

    followup_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return followup_id


# Save an escalation
def save_escalation(message, assigned_to="Supervisor", priority="Medium"):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = get_current_time()
    cursor.execute("""
        INSERT INTO escalations (message, priority, status, assigned_to, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (message, priority, "Escalated", assigned_to, created_at))

    escalation_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return escalation_id


# Save prediction logs
def save_prediction_log(message, intent, confidence, route, action_result):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = get_current_time()
    cursor.execute("""
        INSERT INTO prediction_logs (message, intent, confidence, route, action_result, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (message, intent, confidence, route, action_result, created_at))

    conn.commit()
    conn.close()


# Fetch all logs
def get_all_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, intent, confidence, route, action_result, created_at
        FROM prediction_logs
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Fetch all tickets
def get_all_tickets():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, status, assigned_to, priority, created_at, updated_at
        FROM tickets
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Fetch all follow-ups
def get_all_followups():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, status, assigned_to, due_date, created_at
        FROM followups
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Fetch all escalations
def get_all_escalations():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, priority, status, assigned_to, created_at
        FROM escalations
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows