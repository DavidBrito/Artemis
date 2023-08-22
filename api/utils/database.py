import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

def init_db():
    db_path = os.environ.get("DATABASE_PATH", "data/database.db")
    controls_config_path = os.environ.get("SECURITY_CONTROLS_CONFIG", "config/security_controls_config.txt")
    risks_config_path = os.environ.get("RISKS_CONFIG", "config/matrix_config.txt")
    matrix_config_path = os.environ.get("MATRIX_CONFIG", "config/matrix_config.txt")

    conn = sqlite3.connect(db_path)
    
    try:
        _init_users(conn)
        _init_controls(conn, controls_config_path)
        _init_risks(conn, risks_config_path)
        
        _init_matrix(conn, matrix_config_path)
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
            category TEXT NOT NULL,
            reference TEXT NOT NULL,
            notes TEXT NOT NULL
        )
    ''')

    with open(config_path, 'r') as file:
        for line in file:
            control_data = line.strip().split(',')
            if len(control_data) == 7:
                control_id, name, question, group_name, category, reference, notes  = control_data
                cursor.execute('''
                    INSERT INTO security_controls (id, name, question, group_name, category, reference, notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (int(control_id), name, question, group_name, category, reference, notes))

    conn.commit()

def _init_risks(conn, config_path):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS risks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    with open(config_path, 'r') as file:
        for line in file:
            control_data = line.strip().split(',')
            if len(control_data) == 3:
                risk_id, name, description = control_data
                cursor.execute('''
                    INSERT INTO risks (id, name, description)
                    VALUES (?, ?, ?)
                ''', (int(risk_id), name, description))

    conn.commit()

def _init_matrix(conn, config_path):
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE control_risk_matrix (
        id INTEGER PRIMARY KEY,
        security_control_id INTEGER NOT NULL,
        risk_id INTEGER NOT NULL,
        risk_type TEXT NOT NULL,
        risk_weight TEXT NOT NULL,
        FOREIGN KEY (security_control_id) REFERENCES security_controls(id),
        FOREIGN KEY (risk_id) REFERENCES risks(id)
    );
    ''')

    with open(config_path, 'r') as file:
        for line in file:
            control_data = line.strip().split(',')
            if len(control_data) == 5:
                matrix_id, security_control_id, risk_id, risk_type, risk_weight = control_data
                cursor.execute('''
                    INSERT OR IGNORE INTO control_risk_matrix (id, security_control_id, risk_id, risk_type, risk_weight)
                    VALUES (?, ?, ?, ?, ?)
                ''', (int(matrix_id), int(security_control_id), int(risk_id), risk_type, float(risk_weight)))

    conn.commit()