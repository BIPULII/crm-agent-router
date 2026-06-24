import sqlite3
from datetime import datetime

DB_NAME = "crm_router.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            status TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            status TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            intent TEXT,
            confidence REAL,
            route TEXT,
            action_result TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_ticket(message):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO tickets (message, status, created_at)
        VALUES (?, ?, ?)
    """, (message, "Open", created_at))

    ticket_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return ticket_id


def save_followup(message):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO followups (message, status, created_at)
        VALUES (?, ?, ?)
    """, (message, "Scheduled", created_at))

    followup_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return followup_id


def save_prediction_log(message, intent, confidence, route, action_result):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO prediction_logs 
        (message, intent, confidence, route, action_result, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (message, intent, confidence, route, action_result, created_at))

    conn.commit()
    conn.close()