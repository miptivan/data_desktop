# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_dev.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        MainWindow.setStyleSheet("*{\n"
"font-family: Verdana;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QMainWindow{\n"
"}\n"
"QPushButton{\n"
"background-color: #f1641e;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid black;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.frame.setMinimumSize(QtCore.QSize(900, 700))
        self.frame.setStyleSheet("background-color: rgb(94, 191, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 10, 700, 800))
        self.stackedWidget.setMinimumSize(QtCore.QSize(700, 800))
        self.stackedWidget.setMaximumSize(QtCore.QSize(700, 430))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(40)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.label = QtWidgets.QLabel(self.main_page)
        self.label.setGeometry(QtCore.QRect(210, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.main_page)
        self.label_4.setGeometry(QtCore.QRect(90, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.main_page)
        self.label_5.setGeometry(QtCore.QRect(320, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.main_page)
        self.label_6.setGeometry(QtCore.QRect(70, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.main_page)
        self.label_7.setGeometry(QtCore.QRect(410, 160, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.sold = QtWidgets.QLineEdit(self.main_page)
        self.sold.setEnabled(False)
        self.sold.setGeometry(QtCore.QRect(50, 190, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.sold.setFont(font)
        self.sold.setAutoFillBackground(False)
        self.sold.setStyleSheet("border: none;")
        self.sold.setText("")
        self.sold.setAlignment(QtCore.Qt.AlignCenter)
        self.sold.setObjectName("sold")
        self.profit = QtWidgets.QLineEdit(self.main_page)
        self.profit.setEnabled(False)
        self.profit.setGeometry(QtCore.QRect(410, 200, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.profit.setFont(font)
        self.profit.setAutoFillBackground(False)
        self.profit.setStyleSheet("border: none;")
        self.profit.setText("")
        self.profit.setAlignment(QtCore.Qt.AlignCenter)
        self.profit.setObjectName("profit")
        self.table_top = QtWidgets.QTableWidget(self.main_page)
        self.table_top.setGeometry(QtCore.QRect(100, 290, 411, 192))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.table_top.setFont(font)
        self.table_top.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.table_top.setObjectName("table_top")
        self.table_top.setColumnCount(0)
        self.table_top.setRowCount(0)
        self.table_top.horizontalHeader().setVisible(True)
        self.table_top.horizontalHeader().setCascadingSectionResizes(False)
        self.table_top.horizontalHeader().setDefaultSectionSize(200)
        self.table_top.horizontalHeader().setHighlightSections(True)
        self.table_top.horizontalHeader().setSortIndicatorShown(False)
        self.table_top.horizontalHeader().setStretchLastSection(True)
        self.table_top.verticalHeader().setCascadingSectionResizes(False)
        self.table_top.verticalHeader().setHighlightSections(True)
        self.table_top.verticalHeader().setSortIndicatorShown(False)
        self.table_top.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.main_page)
        self.otschot_page = QtWidgets.QWidget()
        self.otschot_page.setObjectName("otschot_page")
        self.label_2 = QtWidgets.QLabel(self.otschot_page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.otschot_page)
        self.items_page = QtWidgets.QWidget()
        self.items_page.setObjectName("items_page")
        self.label_3 = QtWidgets.QLabel(self.items_page)
        self.label_3.setGeometry(QtCore.QRect(160, 0, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.items_page)
        self.widget.setGeometry(QtCore.QRect(50, 80, 571, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.items_submit = QtWidgets.QPushButton(self.widget)
        self.items_submit.setMinimumSize(QtCore.QSize(150, 0))
        self.items_submit.setObjectName("items_submit")
        self.horizontalLayout_7.addWidget(self.items_submit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_9.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.items_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.info_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_13 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox_3 = QtWidgets.QComboBox(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.submit_but = QtWidgets.QPushButton(self.info_page)
        self.submit_but.setEnabled(True)
        self.submit_but.setObjectName("submit_but")
        self.horizontalLayout_2.addWidget(self.submit_but)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.info_page)
        self.tableWidget_2.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.info_page)
        self.tableWidget_3.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.info_page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 732, 48))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_16 = QtWidgets.QLabel(self.page_6)
        self.label_16.setGeometry(QtCore.QRect(0, 20, 732, 48))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_17 = QtWidgets.QLabel(self.page_7)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 732, 48))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_18 = QtWidgets.QLabel(self.page_8)
        self.label_18.setGeometry(QtCore.QRect(50, 0, 561, 48))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.widget1 = QtWidgets.QWidget(self.page_8)
        self.widget1.setGeometry(QtCore.QRect(0, 60, 667, 466))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.plot = QtWidgets.QWidget(self.widget1)
        self.plot.setMinimumSize(QtCore.QSize(400, 0))
        self.plot.setObjectName("plot")
        self.horizontalLayout_5.addWidget(self.plot)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget_4.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_5.addWidget(self.tableWidget_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.a_but = QtWidgets.QPushButton(self.widget1)
        self.a_but.setObjectName("a_but")
        self.horizontalLayout_6.addWidget(self.a_but)
        self.b_but = QtWidgets.QPushButton(self.widget1)
        self.b_but.setObjectName("b_but")
        self.horizontalLayout_6.addWidget(self.b_but)
        self.c_but = QtWidgets.QPushButton(self.widget1)
        self.c_but.setObjectName("c_but")
        self.horizontalLayout_6.addWidget(self.c_but)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget_5.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_5)
        self.stackedWidget.addWidget(self.page_8)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 440, 157, 62))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 380, 157, 62))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 320, 157, 62))
        self.pushButton_3.setObjectName("pushButton_3")
        self.main_page_but = QtWidgets.QPushButton(self.frame)
        self.main_page_but.setGeometry(QtCore.QRect(10, 20, 157, 62))
        self.main_page_but.setStyleSheet("")
        self.main_page_but.setObjectName("main_page_but")
        self.info_page_but = QtWidgets.QPushButton(self.frame)
        self.info_page_but.setGeometry(QtCore.QRect(10, 80, 157, 62))
        self.info_page_but.setObjectName("info_page_but")
        self.settings_page_but = QtWidgets.QPushButton(self.frame)
        self.settings_page_but.setGeometry(QtCore.QRect(10, 140, 157, 62))
        self.settings_page_but.setObjectName("settings_page_but")
        self.items_page_but = QtWidgets.QPushButton(self.frame)
        self.items_page_but.setGeometry(QtCore.QRect(10, 200, 157, 62))
        self.items_page_but.setObjectName("items_page_but")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 157, 62))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "\"ETSY\""))
        self.label_4.setText(_translate("MainWindow", "Первая продажа:"))
        self.label_5.setText(_translate("MainWindow", "12 марта 2020"))
        self.label_6.setText(_translate("MainWindow", "Продано"))
        self.label_7.setText(_translate("MainWindow", "Заработано"))
        self.sold.setPlaceholderText(_translate("MainWindow", "100"))
        self.profit.setPlaceholderText(_translate("MainWindow", "100"))
        self.label_2.setText(_translate("MainWindow", "Страница 2"))
        self.label_3.setText(_translate("MainWindow", "Список товаров"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Все"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Активные"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Неактивные"))
        self.items_submit.setText(_translate("MainWindow", "Выполнить"))
        self.label_8.setText(_translate("MainWindow", "Отчёт по годам"))
        self.label_13.setText(_translate("MainWindow", "Выберите год: "))
        self.submit_but.setText(_translate("MainWindow", "Выполнить"))
        self.label_11.setText(_translate("MainWindow", "Активных товаров:"))
        self.label_10.setText(_translate("MainWindow", "Продано всего:"))
        self.label_12.setText(_translate("MainWindow", "Сумма выручки:"))
        self.label_15.setText(_translate("MainWindow", "ТОП 10 по количеству продаж"))
        self.label_14.setText(_translate("MainWindow", "ТОП 10 по доходу"))
        self.label_9.setText(_translate("MainWindow", "Анализ корзины"))
        self.label_16.setText(_translate("MainWindow", "Прогноз на период"))
        self.label_17.setText(_translate("MainWindow", "Анализ сезонности"))
        self.label_18.setText(_translate("MainWindow", "Анализ доходности ABC"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column1"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column2"))
        self.a_but.setText(_translate("MainWindow", "A"))
        self.b_but.setText(_translate("MainWindow", "B"))
        self.c_but.setText(_translate("MainWindow", "C"))
        self.pushButton_5.setText(_translate("MainWindow", "Анализ доходности"))
        self.pushButton_4.setText(_translate("MainWindow", "Анализ сезонности"))
        self.pushButton_3.setText(_translate("MainWindow", "Прогноз на период"))
        self.main_page_but.setText(_translate("MainWindow", "Главная"))
        self.info_page_but.setText(_translate("MainWindow", "Отчёт"))
        self.settings_page_but.setText(_translate("MainWindow", "Настройки"))
        self.items_page_but.setText(_translate("MainWindow", "Товары"))
        self.pushButton_2.setText(_translate("MainWindow", "Анализ корзины"))

