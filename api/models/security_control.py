import sqlite3

class SecurityControl:
    def __init__(self, control_id, name, question, group, weight, control_type):
        self.control_id = control_id
        self.name = name
        self.question = question
        self.group = group
        self.weight = weight
        self.control_type = control_type

    @classmethod
    def get_all_controls(cls):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM security_controls')
        control_records = cursor.fetchall()
        conn.close()

        controls = []
        for record in control_records:
            control = cls(*record)
            controls.append(control)
        return controls

    def save_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO security_controls (name, question, group_name, weight, control_type)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.name, self.question, self.group, self.weight, self.control_type))
        conn.commit()
        conn.close()

    def update_control_risk_matrix(self, risk_id, interaction_type, weight):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO control_risk_matrix (id_control, id_risk, type, weight)
            VALUES (?, ?, ?, ?)
        ''', (self.control_id, risk_id, interaction_type, weight))
        conn.commit()
        conn.close()

    def to_dict(self):
        return {
            "name": self.name,
            "question": self.question,
            "group": self.group,
            "weight": self.weight,
            "control_type": self.control_type
        }
