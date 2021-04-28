# pyuic5 design.ui -o design.py
from PyQt5 import QtWidgets
import pandas as pd
import design_dev
import sys
import info_page
import main_page
import items_page
import ABC_analysis
import matplotlib.pyplot as plt
#from graphic_widget import canvas
import os
os.system('pyuic5 design_dev.ui -o design_dev.py')


list_dir = os.listdir('analysis')
ys = set()
for i in range(len(list_dir)):
    if list_dir[i][:len('EtsySoldOrderItems')] == 'EtsySoldOrderItems':
        ys.add(list_dir[i][len('EtsySoldOrderItems'):len('EtsySoldOrderItems') + 4])
ys = list(ys)
ys = sorted(ys)


def set_table(widget, table):
    headers = table.columns.values.tolist()
    widget.setRowCount(0)
    widget.clear()
    widget.setColumnCount(len(headers))
    widget.setHorizontalHeaderLabels(headers)
    for i, row in table.iterrows():
        widget.setRowCount(widget.rowCount() + 1)
        for j in range(widget.columnCount()):
            widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
    return

class Ui(QtWidgets.QMainWindow, design_dev.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_main_page()
        # page_1
        self.main_page_but.clicked.connect(self.set_main_page)
        # page_2
        self.info_page_but.clicked.connect(self.info_page_loader)
        # refresh year on info_page
        self.submit_but.clicked.connect(self.set_info_page)
        # page_3
        self.items_page_but.clicked.connect(self.item_page_loader)
        # page_4
        self.abc_analysis_but.clicked.connect(self.abc_page_loader)
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
        global ys
        self.comboBox_3.clear()
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
    
    def main_page_loader(self):
        return self.set_main_page()
    
    def set_main_page(self):
        global ys
        first_sale, all_count, all_sold, active_items = main_page.main_info(ys)
        set_table(self.table_top, active_items)
        self.label_5.setText(first_sale)
        self.sold.setText(all_count)
        self.profit.setText(all_sold)
        return self.stackedWidget.setCurrentWidget(self.main_page)
    
    def item_page_loader(self):
        return self.set_item_page()
    
    def set_item_page(self):
        state = self.comboBox_3.currentText()
        first_sale, all_count, all_sold, active_items = items_page.items_info(ys)
        set_table(self.table_top, active_items)
        self.label_5.setText(first_sale)
        self.sold.setText(all_count)
        self.profit.setText(all_sold)
        return self.stackedWidget.setCurrentWidget(self.main_page)
    
    def abc_page_loader(self):
        global ys
        ABC_analysis.abc(ys)
        abc = pd.read_csv('analysis/ABC_table' + '_'.join([str(y) for y in ys]) + '.csv')
        abc_items = abc['group'].value_counts()
        fig, ax = plt.subplots(figsize=(5, 3))  # создаем график
        ax.bar(range(3), [
            abc_items.loc['A'],
            abc_items.loc['B'],
            abc_items.loc['C']
        ])
        ticklabels = ['A', 'B', 'C']
        plt.xticks(range(len(ticklabels)), labels=ticklabels)

        self.plot.canvas.axes.clear()
        self.plot.canvas.figure = fig
        self.plot.canvas.axes = ax # ???????????????????????????????????????????????????????
        res = []
        for l in ['A', 'B', 'C']:
            res.append([l, abc_items.loc[l], round(abc[abc['group'] == l]['total_percentage'].sum()*100, 2)])
        set_table(self.tableWidget_4, pd.DataFrame(data=res, columns=['group', 'count', 'percentage of profit']))
        return self.stackedWidget.setCurrentWidget(self.abc_analysis)
        

app = QtWidgets.QApplication(sys.argv)
w = Ui()
sys.exit(app.exec_())
