# pyuic5 design.ui -o design.py
from PyQt5 import QtWidgets
import design_dev
import sys
import info_page
import os
os.system('pyuic5 design_dev.ui -o design_dev.py')


def set_table(widget, table):
    headers = table.columns.values.tolist()
    widget.setRowCount(0)
    widget.clear()
    widget.setColumnCount(len(headers))
    widget.setHorizontalHeaderLabels(headers)
    for i, row in table.iterrows():
        print(widget.rowCount() + 1)
        widget.setRowCount(widget.rowCount() + 1)
        for j in range(widget.columnCount()):
            widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
    return

class Ui(QtWidgets.QMainWindow, design_dev.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # page_1
        self.main_page_but.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_page))
        # page_2
        self.info_page_but.clicked.connect(self.info_page_loader)
        # refresh year on info_page
        self.submit_but.clicked.connect(self.set_info_page)
        # page_3
        self.button_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        # page_4
        #self.button_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        # page_5
        #self.button_page_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        # page_6
        #self.button_page_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        # page_7
        #self.button_page_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        # page_8
        #self.button_page_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.otschot_page))

        self.show()
    
    def info_page_loader(self):
        list_dir = os.listdir('analysis')
        ys = []
        for i in range(len(list_dir)):
            if list_dir[i][:len('EtsySoldOrderItems')] == 'EtsySoldOrderItems':
                ys.append(list_dir[i][len('EtsySoldOrderItems'):len('EtsySoldOrderItems') + 4])
        ys = sorted(ys)
        self.comboBox_3.addItems(ys)
        return self.set_info_page()
    
    def set_info_page(self):
        active_items, sold_count, sold_sum, ten_sold, ten_count = info_page.info(int(self.comboBox_3.currentText()))
        set_table(self.tableWidget_2, ten_sold)
        set_table(self.tableWidget_3, ten_count)
        self.lineEdit.setText(str(active_items))
        self.lineEdit_2.setText(str(sold_count))
        self.lineEdit_3.setText(str(round(sold_sum, 2)) + ' usd')
        return self.stackedWidget.setCurrentWidget(self.info_page)
        

app = QtWidgets.QApplication(sys.argv)
w = Ui()
sys.exit(app.exec_())
