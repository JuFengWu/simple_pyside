#!venv/bin/python3

import sys
from PySide2.QtWidgets import QApplication, QMainWindow , QMessageBox
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_connection()
        
    def ui_connection(self):
        self.setIDButton = self.ui.setIDButton
        self.setIDButton.clicked.connect(self.buttonClick)
        
    def buttonClick(self):
        message_box = QMessageBox()
        message_box.setWindowTitle ("bbb")
        message_box.setInformativeText("aaa")
        message_box.exec_() 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
