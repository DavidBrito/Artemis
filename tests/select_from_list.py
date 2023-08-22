from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QHBoxLayout(central)
        self.spin = QtWidgets.QSpinBox()
        layout.addWidget(self.spin)
        self.table = QtWidgets.QTableWidget(2, 2)
        layout.addWidget(self.table)
        self.table.verticalHeader().setVisible(False)
        for col, label in enumerate(('a', 'c')):
            header = QtWidgets.QTableWidgetItem(label)
            self.table.setHorizontalHeaderItem(col, header)
            if col:
                continue
            for row in range(self.table.rowCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.table.setItem(row, col, item)

        self.spin.setValue(self.table.rowCount())
        self.spin.valueChanged.connect(self.setRowCount)

    def setRowCount(self, count):
        if count == self.table.rowCount():
            return
        # if there are too many rows, remove them
        while self.table.rowCount() > count:
            self.table.removeRow(self.table.rowCount() - 1)
        # if rows are going to be added, create checkable items for them
        while self.table.rowCount() < count:
            row = self.table.rowCount()
            self.table.insertRow(row)
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.table.setItem(row, 0, item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
