from PyQt5 import QtWidgets
from ui.ui_security_control_form import Ui_SecurityControlForm
from ui.ui_security_control_dialog import Ui_SecurityControlDialog

class SecurityControlWidget(QtWidgets.QWidget, Ui_SecurityControlForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setColumnCount(2)
        self.user_data = [
            ("Alice", 25),
            ("Bob", 30),
            ("Charlie", 22)
        ]
        self.populate_table()

        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.edit_btn.clicked.connect(self.open_edit_dialog)
        self.new_btn.clicked.connect(self.open_add_dialog)
        self.delete_btn.clicked.connect(self.delete_user)

    def populate_table(self):
        self.tableWidget.setRowCount(len(self.user_data))
        for row, (name, age) in enumerate(self.user_data):
            name_item = QtWidgets.QTableWidgetItem(name)
            age_item = QtWidgets.QTableWidgetItem(str(age))

            self.tableWidget.setItem(row, 0, name_item)
            self.tableWidget.setItem(row, 1, age_item)

    def open_edit_dialog(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if selected_rows:
            selected_row = selected_rows[0].row()
            user_data = self.user_data[selected_row]

            edit_dialog = Ui_SecurityControlDialog(user_data, self)
            if edit_dialog.exec_() == QtWidgets.QDialog.Accepted:
                new_name = edit_dialog.name_edit.text()
                new_age = edit_dialog.age_spin.value()

                self.user_data[selected_row] = (new_name, new_age)
                self.populate_table()

    def open_add_dialog(self):
        new_control_data = ("New User", 0)
        dialog = Ui_SecurityControlDialog(new_control_data, self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            name = dialog.name_edit.text()
            age = dialog.age_spin.value()

            self.user_data.append((name, age))
            self.populate_table()
    
    def delete_user(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if selected_rows:
            selected_row = selected_rows[0].row()
            
            user_name = self.user_data[selected_row][0]
            confirmation = QtWidgets.QMessageBox.question(
                self,
                "Confirm Deletion",
                f"Are you sure you want to delete user '{user_name}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            if confirmation == QtWidgets.QMessageBox.Yes:
                self.user_data.pop(selected_row)
                self.populate_table()
