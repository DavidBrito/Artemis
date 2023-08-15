import sqlite3
from models.security_control import SecurityControl

class SecurityControlController:
    def create_control(self, control_id, name, question, group, weight, control_type):
        control = SecurityControl(control_id, name, question, group, weight, control_type)
        control.save_to_database()

    def get_control_by_name(self, name):
        controls = SecurityControl.get_all_controls()
        for control in controls:
            if control.name == name:
                return control.to_dict()
        return None

    def update_control(self, name, new_question, new_group, new_weight, new_control_type):
        controls = SecurityControl.get_all_controls()
        for control in controls:
            if control.name == name:
                control.question = new_question
                control.group = new_group
                control.weight = new_weight
                control.control_type = new_control_type
                control.save_to_database()
                return True
        return False

    def delete_control(self, name):
        controls = SecurityControl.get_all_controls()
        for control in controls:
            if control.name == name:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute('DELETE FROM security_controls WHERE name = ?', (name,))
                conn.commit()
                conn.close()
                return True
        return False

    def get_all_controls(self):
        controls = SecurityControl.get_all_controls()
        return [control.to_dict() for control in controls]
    
    def associate_control_with_risk(self, control_name, risk_id, interaction_type, weight):
        controls = SecurityControl.get_all_controls()
        for control in controls:
            if control.name == control_name:
                control.update_control_risk_matrix(risk_id, interaction_type, weight)
                return True
        return False

    def get_controls_for_risk(self, risk_id):
        controls = SecurityControl.get_all_controls()
        risk_controls = []
        for control in controls:
            associations = control.get_associated_risks()
            for association in associations:
                if association["id_risk"] == risk_id:
                    risk_controls.append(control.to_dict())
        return risk_controls
