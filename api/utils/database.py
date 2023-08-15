import sqlite3

__all__ = ["init_db"]

def init_db(app):
    conn = sqlite3.connect(f"{app.config['APP_DIR']}/database.db")
    
    _init_users(conn, app)
    _init_controls(conn, app)

    conn.close()


def _init_users(conn, app):
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
        INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
    ''', ('admin', 'admin'))

    conn.commit()


def _init_controls(conn, app):
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

    with open(f"{app.config['APP_DIR']}/seeds/security_controls_config.txt", 'r') as file:
        for line in file:
            control_data = line.strip().split(';')
            if len(control_data) == 5:
                name, question, group, weight, control_type = control_data
                cursor.execute('''
                    INSERT INTO security_controls (name, question, group_name, weight, control_type)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, question, group, int(weight), control_type))

    conn.commit()
