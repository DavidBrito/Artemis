import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

def init_db():
    db_path = os.environ.get("DATABASE_PATH", "data/database.db")
    controls_config_path = os.environ.get("SECURITY_CONTROLS_CONFIG", "config/security_controls_config.txt")
    conn = sqlite3.connect(db_path)
    
    try:
        _init_users(conn)
    except Exception as e:
        print(e)

    try:
        _init_controls(conn, controls_config_path)
    except Exception as e:
        print(e)

    conn.close()


def _init_users(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO users (id, username, password, email) VALUES (?, ?, ?, ?)
    ''', ('1', 'admin', 'admin', 'admin@admin.com'))

    conn.commit()


def _init_controls(conn, config_path):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS security_controls (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            question TEXT NOT NULL,
            group_name TEXT NOT NULL,
            weight INTEGER NOT NULL,
            control_type TEXT NOT NULL
        )
    ''')

    with open(config_path, 'r') as file:
        for line in file:
            control_data = line.strip().split(';')
            if len(control_data) == 5:
                name, question, group, weight, control_type = control_data
                cursor.execute('''
                    INSERT INTO security_controls (name, question, group_name, weight, control_type)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, question, group, int(weight), control_type))

    conn.commit()
