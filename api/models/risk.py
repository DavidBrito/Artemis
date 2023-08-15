import sqlite3

class Risk:
    def __init__(self, risk_id, name, description, reference):
        self.risk_id = risk_id
        self.name = name
        self.description = description
        self.reference = reference

    @classmethod
    def get_all_risks(cls):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM risks')
        risk_records = cursor.fetchall()
        conn.close()

        risks = []
        for record in risk_records:
            risk = cls(*record)
            risks.append(risk)
        return risks

    def save_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO risks (risk_id, name, description, reference)
            VALUES (?, ?, ?, ?)
        ''', (self.risk_id, self.name, self.description, self.reference))
        conn.commit()
        conn.close()

    def to_dict(self):
        return {
            "risk_id": self.risk_id,
            "name": self.name,
            "description": self.description,
            "reference": self.reference
        }
