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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escalations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

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


def save_ticket(message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (message, status, created_at)
        VALUES (?, ?, ?)
    """, (message, "Open", get_current_time()))

    ticket_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return ticket_id


def save_followup(message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO followups (message, status, created_at)
        VALUES (?, ?, ?)
    """, (message, "Scheduled", get_current_time()))

    followup_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return followup_id


def save_escalation(message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO escalations (message, priority, status, created_at)
        VALUES (?, ?, ?, ?)
    """, (message, "Medium", "Escalated", get_current_time()))

    escalation_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return escalation_id


def save_prediction_log(message, intent, confidence, route, action_result):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prediction_logs 
        (message, intent, confidence, route, action_result, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        message,
        intent,
        confidence,
        route,
        action_result,
        get_current_time()
    ))

    conn.commit()
    conn.close()


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


def get_all_tickets():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, status, created_at
        FROM tickets
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


def get_all_followups():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, status, created_at
        FROM followups
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows