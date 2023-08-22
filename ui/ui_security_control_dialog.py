from PyQt5.QtWidgets import QDialog,QLineEdit, QFormLayout, QSpinBox, QDialogButtonBox

class Ui_SecurityControlDialog(QDialog):
    def __init__(self, security_control_data, parent=None):
        super().__init__(parent)
        self.security_control_data = security_control_data
        self.setWindowTitle("Edit User")

        self.dialog_layout = QFormLayout()
        self.name_edit = QLineEdit()
        self.age_spin = QSpinBox()
        self.dialog_layout.addRow("Name:", self.name_edit)
        self.dialog_layout.addRow("Age:", self.age_spin)
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog_layout.addWidget(self.button_box)
        self.setdialog_Layout(self.dialog_layout)

        self.name_edit.setText(security_control_data[0])
        self.age_spin.setValue(security_control_data[1])

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)