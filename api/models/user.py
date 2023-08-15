import sqlite3

class User:
    def __init__(self, user_id):
        self.id = user_id
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def authenticate(self, username, password):
        query = "SELECT username, password FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        user_data = self.cursor.fetchone()

        if user_data and user_data[1] == password:
            return User(user_data[0])
        
        return None

    def fetch_user_details(self):
        query = "SELECT username, email FROM users WHERE username = ?"
        self.cursor.execute(query, (self.id,))
        user_data = self.cursor.fetchone()

        if user_data:
            username, email = user_data
            return {"username": username, "email": email}

        return None

    def register_user(self, username, password, email):
        check_username_query = "SELECT COUNT(*) FROM users WHERE username = ?"
        self.cursor.execute(check_username_query, (username,))
        username_exists = self.cursor.fetchone()[0] > 0

        if username_exists:
            return {"message": "Username already taken"}, 400

        insert_user_query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
        self.cursor.execute(insert_user_query, (username, password, email))
        self.conn.commit()

        return {"message": "User registered successfully"}, 201