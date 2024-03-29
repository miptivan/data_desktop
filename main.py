# pyuic5 design.ui -o design.py
from PyQt5 import QtWidgets, QtCore
import pandas as pd
import numpy as np
import basket
import sys
import info_page
import main_page
import items_page
import ABC_analysis
import matplotlib.pyplot as plt
import os
os.system('pyuic5 design_dev.ui -o design_dev.py')
import design_dev
import season_analysis
import copy


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
    widget.setColumnCount(len(headers))
    widget.setHorizontalHeaderLabels(headers)
    widget.setRowCount(len(table))
    i = 0
    for _, row in table.iterrows():
        row = row.values.tolist()
        #widget.setRowCount(i)
        for j in range(widget.columnCount()):
            widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
        i += 1
    return

def unique_set_table(widget, table):
    headers = table[0]
    widget.setRowCount(0)
    widget.setColumnCount(len(headers))
    widget.setHorizontalHeaderLabels(headers)
    widget.setRowCount(len(table) - 1)
    for i in range(1, len(table)):
        for j in range(widget.columnCount()):
            widget.setItem(i-1, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
    return


class Ui(QtWidgets.QMainWindow, design_dev.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        global ys
        self.setupUi(self)
        self.path = 'analysis'
        self.flag_items = 0
        self.abc_flag = 0
        self.main_flag = 0
        self.season_flag = 0
        self.forecast_flag = 0
        self.label_23.setText('Произведено недосаточно продаж для анализа, относительно новый товар') ### Сам текст, выводимый при недостаточном колличестве продаж
        if len(ys) == 0:
            self.settings_loader()
        else:
            self.main_page_loader()
    
        self.browserButton.clicked.connect(self.pushButton_handler)
        # page_1
        self.main_page_but.clicked.connect(self.main_page_loader)
        # page_2
        self.info_page_but.clicked.connect(self.info_page_loader)
        # refresh year on info_page
        self.submit_but.clicked.connect(self.set_info_page)
        # page_3
        self.items_page_but.clicked.connect(self.set_item_page)
        self.items_submit.clicked.connect(self.set_item_page)
        # page_4
        self.abc_analysis_but.clicked.connect(self.abc_page_loader)
        self.a_but.clicked.connect(self.set_letter_a)
        self.b_but.clicked.connect(self.set_letter_b)
        self.c_but.clicked.connect(self.set_letter_c)
        # page_5
        self.basket_but.clicked.connect(self.basket_loader)
        # page_6
        self.settings_page_but.clicked.connect(self.settings_loader)
        # page_7
        self.pushButton_4.clicked.connect(self.season_page_loader)
        self.pushButton.clicked.connect(self.season_subpage_loader)
        # page_8
        self.pushButton_3.clicked.connect(self.forecast_loader)

        self.show()
    
    def info_page_loader(self):
        global ys
        self.comboBox_3.clear()
        self.comboBox_3.addItems(ys)
        return self.set_info_page()
    
    def set_info_page(self):
        active_items, sold_count, sold_sum, ten_sold, ten_count = info_page.info(int(self.comboBox_3.currentText()), self.path)
        set_table(self.tableWidget_2, ten_sold)
        set_table(self.tableWidget_3, ten_count)
        self.lineEdit.setText(str(active_items))
        self.lineEdit_2.setText(str(sold_count))
        self.lineEdit_3.setText(str(round(sold_sum, 2)) + ' usd')
        return self.stackedWidget.setCurrentWidget(self.info_page)
    
    def main_page_loader(self):
        if self.main_flag == 0:
            global ys
            first_sale, all_count, all_sold, active_items = main_page.main_info(ys, self.path)
            print(active_items.columns)
            active_items['Item Total'] = 
            active_items = active_items[['Item Total', 'Item Name']]
            set_table(self.tableWidget_6, active_items)
            self.label_5.setText(first_sale)
            self.sold.setText(all_count)
            self.profit.setText(all_sold)
            self.main_flag = 1
        return self.stackedWidget.setCurrentWidget(self.main_page)
    
    def items_set_table(self, widget, table):
        headers = table.columns.values.tolist() + ['Сезонность']
        headers.reverse()
        widget.setRowCount(0)
        widget.setColumnCount(len(headers))
        widget.setHorizontalHeaderLabels(headers)
        widget.setRowCount(len(table))
        i = 0
        self.btns = []
        for _, row in table.iterrows():
            row = row.values.tolist()
            row.reverse()
            #widget.setRowCount(i)
            for j in range(widget.columnCount()):
                if j != 0:
                    widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j - 1])))
                else:
                    self.btns.append(QtWidgets.QPushButton(widget))
                    self.btns[i].setText("Перейти")
                    widget.setCellWidget(i, j, self.btns[i])
                    self.btns[i].clicked.connect(lambda checked, item=copy.deepcopy(row[-1]): self.items_seasonal(item))
            i += 1
        return
    
    def items_seasonal(self, item):
        self.flag_items = 1
        self.items_item = item
        self.season_subpage_loader()
        self.flag_items = 0
        return

    def set_item_page(self):
        global ys
        ABC_analysis.abc(ys, self.path)
        state = self.comboBox.currentText()
        all_items, active_items, disactive_items = items_page.items_info(ys, self.path)
        if state == 'Все':
            self.items_set_table(self.tableWidget, all_items)
        elif state == 'Активные':
            self.items_set_table(self.tableWidget, active_items)
        else:
            self.items_set_table(self.tableWidget, disactive_items)
        return self.stackedWidget.setCurrentWidget(self.items_page)
    
    def abc_page_loader(self):
        if self.abc_flag == 0:
            global ys
            ABC_analysis.abc(ys, self.path)
            abc = pd.read_csv(self.path + '/ABC_table_' + '_'.join([str(y) for y in ys]) + '.csv')
            abc_items = abc['group'].value_counts()
            fig, ax = plt.subplots(figsize=(6, 4))  # создаем график
            ax.bar(range(3), [
                abc_items.loc['A'],
                abc_items.loc['B'],
                abc_items.loc['C']
            ])
            ax.set_title('Количество товаров в группе')
            ticklabels = ['A', 'B', 'C']
            plt.xticks(range(len(ticklabels)), labels=ticklabels)

            self.plot.canvas.axes.clear()
            self.plot.canvas.figure.clear()
            self.plot.canvas.figure = fig
            self.plot.canvas.axes = ax
            res = []
            for l in ['A', 'B', 'C']:
                res.append([l, abc_items.loc[l], round(abc[abc['group'] == l]['total_percentage'].sum()*100, 2)])
            set_table(self.tableWidget_4, pd.DataFrame(data=res, columns=['group', 'count', 'percentage of profit']))
            self.abc_flag = 1
        return self.stackedWidget.setCurrentWidget(self.abc_analysis)
    
    def set_letter_a(self):
        self.letter = 'A'
        return self.abc_subpage_loader()
    
    def set_letter_b(self):
        self.letter = 'B'
        return self.abc_subpage_loader()
    
    def set_letter_c(self):
        self.letter = 'C'
        return self.abc_subpage_loader()

    def abc_subpage_loader(self):
        global ys
        ABC_analysis.abc(ys, self.path)
        abc = pd.read_csv(self.path + '/ABC_table_' + '_'.join([str(y) for y in ys]) + '.csv')
        abc = abc[abc['group'] == self.letter]
        abc = abc[['Item Name', 'Item Total']]
        summ = abc['Item Total'].values.sum()
        abc['Group percent'] = round(abc['Item Total']/summ*100, 2)
        abc = abc[['Item Name', 'Item Total', 'Group percent']]
        abc.columns = ['Item', 'Total, usd', 'Group percent']
        set_table(self.tableWidget_7, abc)
        self.label_22.setText('Товары группы ' + self.letter)
        return self.stackedWidget.setCurrentWidget(self.abc_subpage)
    
    def basket_loader(self):
        global ys
        basket.bascket_info(ys, self.path)
        bascket_df = pd.read_csv(self.path + '/basket_table_' + '_'.join([str(y) for y in ys]) + '.csv')
        del bascket_df['Unnamed: 0']
        set_table(self.tableWidget_5, bascket_df)
        return self.stackedWidget.setCurrentWidget(self.basket_page)
    
    def pushButton_handler(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory()
        self.path = str(filename)
        self.lineEdit_4.setText(self.path)
        return self.settings_loader
    
    def settings_loader(self):
        self.lineEdit_4.setText(self.path)
        return self.stackedWidget.setCurrentWidget(self.settings_page)
    
    def season_page_loader(self):
        if self.season_flag == 0:
            global ys
            season_analysis.seasonal_all(ys, self.path)
            with open(self.path + '/all_seasons_' + '_'.join([str(y) for y in ys]) + '.txt', 'r') as f:
                ss = f.read().split('\n')
                trend = [float(s) if s != 'None' else None  for s in ss[0].split(', ')]
                seasonal = [float(s) if s != 'None' else None for s in ss[1].split(', ')]
                resid = [float(s) if s != 'None' else None for s in ss[2].split(', ')]
                level = [float(s) if s != 'None' else None for s in ss[3].split(', ')]
            active_items = pd.read_csv(self.path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
            items = list(pd.unique(active_items['Item Name']))
            for it in items:
                if len(active_items[active_items['Item Name'] == it].groupby('month')['Item Total'].sum()) < 24:
                    items.remove(it)
            self.comboBox_2.clear()
            self.comboBox_2.addItems(items)
            active_items = active_items.groupby('month')['Item Total'].sum()
            active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['month', 'Item Total'])  # ?????????
            active_items = active_items.iloc[:-1]
            fig, ax = plt.subplots(figsize=(4, 3), nrows=2, ncols=1)  # создаем график
            ax[0].plot(range(len(active_items['Item Total'])), active_items['Item Total'].values, label='real')
            ax[0].plot(range(len(trend)), np.array(trend)*np.array(level)*np.array(seasonal), label='trend*level*seasonal')
            ax[0].legend()
            ax[0].set_xticks(range(0, len(trend), 12))
            ax[0].set_xticklabels(ys)
            ax[1].plot(range(1, 13), seasonal[:12])
            ax[1].set_title('Seasonal')
            ax[0].set_title('All income')
            ax[1].set_xlabel('month')

            self.widget.canvas.axes.clear()
            self.widget.canvas.figure.clear()
            self.widget.canvas.figure = fig
            self.widget.canvas.axes = ax

            self.season_flag = 1
        return self.stackedWidget.setCurrentWidget(self.season_page)
    
    def season_subpage_loader(self):
        global ys
        season_analysis.seasonal_all(ys, self.path)
        item = self.comboBox_2.currentText()
        if self.flag_items == 1:
            item = self.items_item
        self.label_21.setText('Анализ сезонности для товара:\n' + item)
        active_items = pd.read_csv(self.path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
        active_items = active_items[active_items['Item Name'] == item]
        del active_items['Unnamed: 0']
        if len(active_items['month'].unique()) < 24: ### Вот условие для вывода текста, что данных не хватает
            self.label_23.show()
            self.widget_2.hide()
            self.tableWidget_8.hide() ### до сюда, можно сделать, чтобы просто возвращало на страницу с товарами обратно
        else:
            self.label_23.hide()
            self.tableWidget_8.show()
            self.widget_2.show()
            self.widget_2.Clear()
            dates = pd.DatetimeIndex(active_items['Sale Date'])

            season_analysis.item_seasonal(ys, self.path, item)
            with open(self.path + '/' + item.replace('"', '') + '_' + '_'.join([str(y) for y in ys]) + '.txt', 'r') as f:
                ss = f.read().split('\n')
                trend = [float(s) if s != 'None' else None  for s in ss[0].split(', ')]
                seasonal = [float(s) if s != 'None' else None for s in ss[1].split(', ')]
                resid = [float(s) if s != 'None' else None for s in ss[2].split(', ')]
                level = [float(s) if s != 'None' else None for s in ss[3].split(', ')]
            table = [['year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Agu', 'Sep', 'Oct', 'Nov', 'Dec']]
            for y in ys:
                table.append([y])
            for i in range(1, len(table)):
                df = active_items[active_items['y'] == float(ys[i-1])]
                df_1 = df.groupby('month')['Item Total'].sum()
                for j in range(1, 13):
                    if len(df[df['real_month'] == j]) == 0:
                        table[i].append('0, 0 usd')
                    else:
                        table[i].append(str(df[df['real_month'] == j].count().values[0]) + ', ' + str(df_1.loc[df[df['real_month'] == j]['month'].values].values[0]) + ' usd')
            unique_set_table(self.tableWidget_8, table)
            active_items = active_items.groupby('month')['Item Total'].sum()
            active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['month', 'Item Total'])
            active_items = active_items.iloc[:-1]
            for m in range(int(active_items['month'].min()), int(active_items['month'].max())):
                if m not in (active_items['month'].unique()):
                    active_items.loc[len(active_items)] = [m, 0.001]
            active_items = active_items.sort_values('month')
            fig, ax = plt.subplots(figsize=(2, 2), nrows=2, ncols=1)  # создаем график
            ax[0].plot(range(len(active_items['Item Total'])), active_items['Item Total'].values, label='real')
            ax[0].plot(range(len(trend)), np.array(trend)*np.array(level)*np.array(seasonal), label='trend*level*seasonal')
            ax[0].legend()
            ax[0].set_xticks(range(0, len(trend), 12))
            yss = set()
            for ind in dates:
                if ind.year not in yss:
                    yss.add(ind.year)
            yss = sorted(list(yss))
            ax[0].set_xticklabels(yss)
            ax[1].plot(range(1, 13), seasonal[:12])
            ax[1].set_title('Seasonal')
            ax[0].set_title('All income')
            ax[1].set_xlabel('month')

            #self.widget_2.canvas.axes.clear()
            #self.widget_2.canvas.figure.clear()
            del self.widget_2.canvas.axes
            del self.widget_2.canvas.figure
            self.widget_2.canvas.figure = fig
            self.widget_2.canvas.axes = ax

        return self.stackedWidget.setCurrentWidget(self.season_subpage)
    
    def forecast_loader(self):
        if self.forecast_flag == 0:
            global ys
            season_analysis.seasonal_all(ys, self.path)
            with open(self.path + '/all_seasons_' + '_'.join([str(y) for y in ys]) + '.txt', 'r') as f:
                ss = f.read().split('\n')
                forecast = [float(s) if s != 'None' else None for s in ss[4].split(', ')]
            active_items = pd.read_csv(self.path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
            active_items['Sale Date'] = pd.to_datetime(active_items['Sale Date'])
            start_month = active_items[active_items['month'] == active_items['month'].min()].iloc[0]['Sale Date'].month
            print(start_month)
            month_0 = active_items['real_month'].iloc[0]
            active_items = active_items.groupby('month')['Item Total'].sum()
            active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['month', 'Item Total'])  # ?????????
            active_items = active_items.iloc[:-1]
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(range(len(active_items['Item Total'])), active_items['Item Total'].values, label='historical')
            #ax.plot(range(len(active_items['Item Total'])), model.season*(model.trend*model.level) + model.resid)
            ax.plot(range(len(active_items['Item Total']) - 1, len(active_items['Item Total']) + len(forecast)), np.hstack((active_items['Item Total'].values[-1], forecast)), label='forecast')
            ax.legend()
            ax.set_title('Forecast for next 12 months')
            print(active_items['Item Total'], forecast)
            ax.set_xticks(range(len(active_items['Item Total']) + len(forecast)))
            #labels = ys + [str(int(ys[-1]) + i) for i in range(1, len(forecast) // 12 + 1)]
            if start_month != 1:
                ii = 1
            else:
                ii = 0
            labels = []
            for i in range(len(active_items['Item Total']) + len(forecast)):
                if (i + start_month) % 12 != 1:
                    """if ((i + start_month) % 12) % 2 == 1:
                        labels.append((i + start_month) % 12)
                    else:"""
                    labels.append('')
                else:
                    labels.append((i + start_month)//12 + ii + int(ys[0]))
            months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Agu', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
            ax.set_xticklabels(labels)
            table = [[ months[(month_0 + active_items['month'].iloc[-1] + i) % 12 + 1] for i in range(12)]]
            for i in range(len(forecast)):
                forecast[i] = int(round(forecast[i]))
            table.append(forecast)
            table = np.array(table)
            table = table.T
            table = list(table)
            table.insert(0, ['month', 'total'])
            unique_set_table(self.tableWidget_9, table)
            self.widget_3.canvas.figure = fig
            self.widget_3.canvas.axes = ax
            self.forecast_flag = 1
        return self.stackedWidget.setCurrentWidget(self.page_6)
        

app = QtWidgets.QApplication(sys.argv)
w = Ui()
sys.exit(app.exec_())
