import sqlite3
from models.risk import Risk

class RiskController:
    def create_risk(self, risk_id, name, description, reference):
        risk = Risk(risk_id, name, description, reference)
        risk.save_to_database()

    def get_risk_by_id(self, risk_id):
        risks = Risk.get_all_risks()
        for risk in risks:
            if risk.risk_id == risk_id:
                return risk.to_dict()
        return None

    def update_risk(self, risk_id, new_name, new_description, new_reference):
        risks = Risk.get_all_risks()
        for risk in risks:
            if risk.risk_id == risk_id:
                risk.name = new_name
                risk.description = new_description
                risk.reference = new_reference
                risk.save_to_database()
                return True
        return False

    def delete_risk(self, risk_id):
        risks = Risk.get_all_risks()
        for risk in risks:
            if risk.risk_id == risk_id:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute('DELETE FROM risks WHERE risk_id = ?', (risk_id,))
                conn.commit()
                conn.close()
                return True
        return False

    def get_all_risks(self):
        risks = Risk.get_all_risks()
        return [risk.to_dict() for risk in risks]

    def associate_risk_with_control(self, risk_id, control_id, interaction_type, weight):
        risks = Risk.get_all_risks()
        for risk in risks:
            if risk.risk_id == risk_id:
                risk.update_risk_control_matrix(control_id, interaction_type, weight)
                return True
        return False

    def get_controls_for_risk(self, risk_id):
        risks = Risk.get_all_risks()
        for risk in risks:
            if risk.risk_id == risk_id:
                return risk.get_associated_controls()
        return []

    def get_risks_for_control(self, control_id):
        risks = Risk.get_all_risks()
        control_risks = []
        for risk in risks:
            associations = risk.get_associated_controls()
            for association in associations:
                if association["id_control"] == control_id:
                    control_risks.append(risk.to_dict())
        return control_risks

