# pyuic5 design.ui -o design.py
from PyQt5 import QtWidgets
import design
import sys
import os
os.system('pyuic5 design.ui -o design.py')


class Ui(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # page_1
        self.button_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        # page_2
        self.button_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        # page_3
        self.button_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = Ui()
sys.exit(app.exec_())
