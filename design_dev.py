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
        MainWindow.resize(1300, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 700))
        MainWindow.setStyleSheet("*{\n"
"font-family: Verdana;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.frame.setMinimumSize(QtCore.QSize(900, 700))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 700))
        self.frame.setStyleSheet("background-color: rgb(94, 191, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1261, 672))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.main_page_but = QtWidgets.QPushButton(self.layoutWidget)
        self.main_page_but.setMinimumSize(QtCore.QSize(150, 0))
        self.main_page_but.setMaximumSize(QtCore.QSize(150, 16777215))
        self.main_page_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_page_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.main_page_but.setObjectName("main_page_but")
        self.verticalLayout_12.addWidget(self.main_page_but)
        self.info_page_but = QtWidgets.QPushButton(self.layoutWidget)
        self.info_page_but.setMinimumSize(QtCore.QSize(150, 0))
        self.info_page_but.setMaximumSize(QtCore.QSize(150, 16777215))
        self.info_page_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_page_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.info_page_but.setObjectName("info_page_but")
        self.verticalLayout_12.addWidget(self.info_page_but)
        self.settings_page_but = QtWidgets.QPushButton(self.layoutWidget)
        self.settings_page_but.setMinimumSize(QtCore.QSize(150, 0))
        self.settings_page_but.setMaximumSize(QtCore.QSize(150, 16777215))
        self.settings_page_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_page_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.settings_page_but.setObjectName("settings_page_but")
        self.verticalLayout_12.addWidget(self.settings_page_but)
        self.items_page_but = QtWidgets.QPushButton(self.layoutWidget)
        self.items_page_but.setMinimumSize(QtCore.QSize(150, 0))
        self.items_page_but.setMaximumSize(QtCore.QSize(150, 16777215))
        self.items_page_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.items_page_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.items_page_but.setObjectName("items_page_but")
        self.verticalLayout_12.addWidget(self.items_page_but)
        self.basket_but = QtWidgets.QPushButton(self.layoutWidget)
        self.basket_but.setMinimumSize(QtCore.QSize(150, 0))
        self.basket_but.setMaximumSize(QtCore.QSize(150, 16777215))
        self.basket_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.basket_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.basket_but.setObjectName("basket_but")
        self.verticalLayout_12.addWidget(self.basket_but)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_12.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_12.addWidget(self.pushButton_4)
        self.abc_analysis_but = QtWidgets.QPushButton(self.layoutWidget)
        self.abc_analysis_but.setMinimumSize(QtCore.QSize(150, 0))
        self.abc_analysis_but.setMaximumSize(QtCore.QSize(150, 16777215))
        self.abc_analysis_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.abc_analysis_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.abc_analysis_but.setObjectName("abc_analysis_but")
        self.verticalLayout_12.addWidget(self.abc_analysis_but)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        self.stackedWidget = QtWidgets.QStackedWidget(self.layoutWidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1100, 670))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1100, 670))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(40)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setToolTip("")
        self.stackedWidget.setAccessibleDescription("")
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.gridLayout = QtWidgets.QGridLayout(self.main_page)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.main_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.main_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.main_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.sold = QtWidgets.QLineEdit(self.main_page)
        self.sold.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.sold.setFont(font)
        self.sold.setAutoFillBackground(False)
        self.sold.setStyleSheet("border: none;")
        self.sold.setText("")
        self.sold.setAlignment(QtCore.Qt.AlignCenter)
        self.sold.setObjectName("sold")
        self.verticalLayout_10.addWidget(self.sold)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.main_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.profit = QtWidgets.QLineEdit(self.main_page)
        self.profit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.profit.setFont(font)
        self.profit.setAutoFillBackground(False)
        self.profit.setStyleSheet("border: none;")
        self.profit.setText("")
        self.profit.setAlignment(QtCore.Qt.AlignCenter)
        self.profit.setObjectName("profit")
        self.verticalLayout_6.addWidget(self.profit)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.main_page)
        self.label_19.setMinimumSize(QtCore.QSize(1100, 70))
        self.label_19.setMaximumSize(QtCore.QSize(1100, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_6.setSizePolicy(sizePolicy)
        self.tableWidget_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_6.setAutoFillBackground(False)
        self.tableWidget_6.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(94, 191, 255);\n"
"border: none;\n"
"height: 32px;\n"
"}")
        self.tableWidget_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_6.setShowGrid(True)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.horizontalHeader().setVisible(False)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(338)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget_6, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.main_page)
        self.settings_page = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.settings_page.setFont(font)
        self.settings_page.setObjectName("settings_page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.settings_page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem4, 4, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.settings_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.settings_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"}")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_10.addWidget(self.lineEdit_4)
        self.browserButton = QtWidgets.QPushButton(self.settings_page)
        self.browserButton.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.browserButton.setObjectName("browserButton")
        self.horizontalLayout_10.addWidget(self.browserButton)
        self.gridLayout_8.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.settings_page)
        self.label_2.setMinimumSize(QtCore.QSize(1100, 70))
        self.label_2.setMaximumSize(QtCore.QSize(1100, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.settings_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_8.addWidget(self.label_20, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.settings_page)
        self.items_page = QtWidgets.QWidget()
        self.items_page.setObjectName("items_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.items_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.items_page)
        self.label_3.setMinimumSize(QtCore.QSize(1100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(1100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.comboBox = QtWidgets.QComboBox(self.items_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"    padding: 5px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.items_submit = QtWidgets.QPushButton(self.items_page)
        self.items_submit.setMinimumSize(QtCore.QSize(150, 0))
        self.items_submit.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.items_submit.setObjectName("items_submit")
        self.horizontalLayout_7.addWidget(self.items_submit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtWidgets.QTableWidget(self.items_page)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_9.addWidget(self.tableWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.items_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.info_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_13 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox_3 = QtWidgets.QComboBox(self.info_page)
        self.comboBox_3.setMinimumSize(QtCore.QSize(108, 34))
        self.comboBox_3.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"    padding: 5px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.submit_but = QtWidgets.QPushButton(self.info_page)
        self.submit_but.setEnabled(True)
        self.submit_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.submit_but.setObjectName("submit_but")
        self.horizontalLayout_2.addWidget(self.submit_but)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border: 1px solid white;\n"
"border-radius: 2px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.info_page)
        self.tableWidget_2.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}\n"
"QTableWidget{\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"}")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.info_page)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: 1px solid white;\n"
"border-radius: 2px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.info_page)
        self.tableWidget_3.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}\n"
"QTableWidget{\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"}")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tableWidget_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.info_page)
        self.basket_page = QtWidgets.QWidget()
        self.basket_page.setObjectName("basket_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.basket_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.basket_page)
        self.label_9.setMinimumSize(QtCore.QSize(1100, 70))
        self.label_9.setMaximumSize(QtCore.QSize(1100, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.basket_page)
        self.tableWidget_5.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(94, 191, 255);\n"
"border: none;\n"
"height: 32px;\n"
"}")
        self.tableWidget_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_5, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.basket_page)
        self.page_6 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(False)
        font.setWeight(50)
        self.page_6.setFont(font)
        self.page_6.setObjectName("page_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_3 = MplWidget(self.page_6)
        self.widget_3.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_13.addWidget(self.widget_3)
        self.tableWidget_9 = QtWidgets.QTableWidget(self.page_6)
        self.tableWidget_9.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(0)
        self.tableWidget_9.setRowCount(0)
        self.horizontalLayout_13.addWidget(self.tableWidget_9)
        self.gridLayout_5.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.season_page = QtWidgets.QWidget()
        self.season_page.setObjectName("season_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.season_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_17 = QtWidgets.QLabel(self.season_page)
        self.label_17.setMinimumSize(QtCore.QSize(700, 70))
        self.label_17.setMaximumSize(QtCore.QSize(700, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.widget = MplWidget(self.season_page)
        self.widget.setMinimumSize(QtCore.QSize(0, 500))
        self.widget.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_6.addWidget(self.widget, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_11.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.season_page)
        self.comboBox_2.setMinimumSize(QtCore.QSize(108, 34))
        self.comboBox_2.setMaximumSize(QtCore.QSize(500, 34))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"    padding: 5px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_11.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(self.season_page)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.season_page)
        self.season_subpage = QtWidgets.QWidget()
        self.season_subpage.setObjectName("season_subpage")
        self.layoutWidget1 = QtWidgets.QWidget(self.season_subpage)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 1102, 159))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_21.setMinimumSize(QtCore.QSize(1100, 100))
        self.label_21.setMaximumSize(QtCore.QSize(1100, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_8.addWidget(self.label_21)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_23.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setText("")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_8.addWidget(self.label_23)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.season_subpage)
        self.tableWidget_8.setGeometry(QtCore.QRect(360, 166, 741, 500))
        self.tableWidget_8.setMinimumSize(QtCore.QSize(0, 500))
        self.tableWidget_8.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tableWidget_8.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(94, 191, 255);\n"
"border: none;\n"
"height: 32px;\n"
"}")
        self.tableWidget_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.widget_2 = MplWidget(self.season_subpage)
        self.widget_2.setGeometry(QtCore.QRect(3, 75, 350, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(350, 500))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 700))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")
        self.tableWidget_8.raise_()
        self.layoutWidget.raise_()
        self.widget_2.raise_()
        self.stackedWidget.addWidget(self.season_subpage)
        self.abc_analysis = QtWidgets.QWidget()
        self.abc_analysis.setObjectName("abc_analysis")
        self.layoutWidget2 = QtWidgets.QWidget(self.abc_analysis)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 0, 1102, 661))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_18.setMinimumSize(QtCore.QSize(1100, 0))
        self.label_18.setMaximumSize(QtCore.QSize(1100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_13.addWidget(self.label_18)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.plot = MplWidget(self.layoutWidget2)
        self.plot.setMinimumSize(QtCore.QSize(500, 500))
        self.plot.setMaximumSize(QtCore.QSize(500, 500))
        self.plot.setObjectName("plot")
        self.horizontalLayout_5.addWidget(self.plot)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.layoutWidget2)
        self.tableWidget_4.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget_4.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(94, 191, 255);\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.tableWidget_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.a_but = QtWidgets.QPushButton(self.layoutWidget2)
        self.a_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.a_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.a_but.setObjectName("a_but")
        self.horizontalLayout_6.addWidget(self.a_but)
        self.b_but = QtWidgets.QPushButton(self.layoutWidget2)
        self.b_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.b_but.setObjectName("b_but")
        self.horizontalLayout_6.addWidget(self.b_but)
        self.c_but = QtWidgets.QPushButton(self.layoutWidget2)
        self.c_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_but.setStyleSheet("QPushButton{\n"
"background-color: #5ebfff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2babff;\n"
"color: #ffffff;\n"
"height: 50px;\n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"padding: 5px;\n"
"font-weight: bold;\n"
"}")
        self.c_but.setObjectName("c_but")
        self.horizontalLayout_6.addWidget(self.c_but)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_13.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.abc_analysis)
        self.abc_subpage = QtWidgets.QWidget()
        self.abc_subpage.setObjectName("abc_subpage")
        self.label_22 = QtWidgets.QLabel(self.abc_subpage)
        self.label_22.setGeometry(QtCore.QRect(12, 12, 1100, 70))
        self.label_22.setMinimumSize(QtCore.QSize(1100, 70))
        self.label_22.setMaximumSize(QtCore.QSize(1100, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.abc_subpage)
        self.tableWidget_7.setGeometry(QtCore.QRect(230, 90, 661, 561))
        self.tableWidget_7.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.tableWidget_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_7.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(94, 191, 255);\n"
"border: none;\n"
"height: 32px;\n"
"}")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.abc_subpage)
        self.horizontalLayout_9.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(9)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_page_but.setText(_translate("MainWindow", "Главная"))
        self.info_page_but.setText(_translate("MainWindow", "Отчёт"))
        self.settings_page_but.setText(_translate("MainWindow", "Настройки"))
        self.items_page_but.setText(_translate("MainWindow", "Товары"))
        self.basket_but.setText(_translate("MainWindow", "Анализ корзины"))
        self.pushButton_3.setText(_translate("MainWindow", "Прогноз на период"))
        self.pushButton_4.setText(_translate("MainWindow", "Анализ сезонности"))
        self.abc_analysis_but.setText(_translate("MainWindow", "Анализ доходности"))
        self.label_4.setText(_translate("MainWindow", "Первая продажа:"))
        self.label_5.setText(_translate("MainWindow", "12 марта 2020"))
        self.label_6.setText(_translate("MainWindow", "Продано"))
        self.sold.setPlaceholderText(_translate("MainWindow", "100"))
        self.label_7.setText(_translate("MainWindow", "Заработано"))
        self.profit.setPlaceholderText(_translate("MainWindow", "100"))
        self.label_19.setText(_translate("MainWindow", "ETSY"))
        self.label.setText(_translate("MainWindow", "Папка с данными:"))
        self.browserButton.setText(_translate("MainWindow", "Выбрать"))
        self.label_2.setText(_translate("MainWindow", "Настройки"))
        self.label_20.setText(_translate("MainWindow", "Выберите папку, в которой лежат .csv файлы с данными о магазине."))
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
        self.label_15.setText(_translate("MainWindow", "ТОП 10\n"
"по количеству продаж"))
        self.label_14.setText(_translate("MainWindow", "ТОП 10\n"
"по доходу"))
        self.label_9.setText(_translate("MainWindow", "Анализ корзины"))
        self.label_16.setText(_translate("MainWindow", "Прогноз на период"))
        self.label_17.setText(_translate("MainWindow", "Анализ сезонности"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "Анализ доходности ABC"))
        self.a_but.setText(_translate("MainWindow", "A"))
        self.b_but.setText(_translate("MainWindow", "B"))
        self.c_but.setText(_translate("MainWindow", "C"))
        self.label_22.setText(_translate("MainWindow", "Пустой лейбл"))

from mplwidget import MplWidget
