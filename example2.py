# -*- coding: utf-8 -*-
#
# @Author : Fu zi hao
#
# Form implementation generated from reading ui file 'example2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from DBUtils.PooledDB import PooledDB
from PyQt5.QtGui import QIcon
import pymysql
import sys
import yaml


class Ui_MainWindow(object):
    def getDbData(self):
        with open('./config/db.yaml', encoding='utf-8') as f:
            result = yaml.safe_load(f)
        return result

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        MainWindow.setWindowIcon(QIcon("./cartoon1.ico"))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./3.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 30, 500, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 830, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 830, 100, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 830, 100, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 830, 100, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 560, 440, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 620, 190, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 620, 190, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(560, 620, 190, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 700, 240, 40))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(400, 700, 240, 40))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 770, 220, 40))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 770, 220, 40))
        self.lineEdit_8.setObjectName("lineEdit_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(650, 560, 110, 40))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(650, 700, 110, 40))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(650, 770, 110, 40))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.comboBox.activated[str].connect(self.comb_one)
        self.comboBox_2.activated[str].connect(self.comb_two)
        self.comboBox_3.activated[str].connect(self.comb_three)
        self.pushButton.clicked.connect(self.calculated_field)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.t_clear)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setStyleSheet("background:rgb(0,0,0,0);border-style:outset")
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setShowGrid(False)  # Grid lines are not visible
        self.pushButton.setStyleSheet("QPushButton{background:transparent}QPushButton:hover{background:#6DDF6D}\
                                        QPushButton{color:rgb(30,144,150)}")
        self.pushButton_2.setStyleSheet("QPushButton{background:transparent}QPushButton:hover{background:#6DDF6D}\
                                        QPushButton{color:rgb(30,144,150)}")
        self.pushButton_3.setStyleSheet("QPushButton{background:transparent}QPushButton:hover{background:#6DDF6D}\
                                                QPushButton{color:rgb(30,144,150)}")
        self.pushButton_4.setStyleSheet("QPushButton{background:transparent}QPushButton:hover{background:#6DDF6D}\
                                                QPushButton{color:rgb(30,144,150)}")
        self.comboBox.setStyleSheet("QComboBox{background:transparent}QComboBox:hover{background:transparent}"
                                    "QComboBox{color:rgb(30,144,150)}")
        self.comboBox_2.setStyleSheet("QComboBox{background:transparent}QComboBox:hover{background:transparent}"
                                      "QComboBox{color:rgb(30,144,150)}")
        self.comboBox_3.setStyleSheet("QComboBox{background:transparent}QComboBox:hover{background:transparent}"
                                      "QComboBox{color:rgb(30,144,150)}")
        self.lineEdit.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_2.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_3.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_4.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_5.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_6.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_7.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")
        self.lineEdit_8.setStyleSheet("background:rgb(0,0,0,15);border-width:0;border-style:outset")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fuzihao-test2，源码已上传Github及个人网站"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", ""))
        self.comboBox.setItemText(0, _translate("MainWindow", "平均"))
        self.comboBox.setItemText(1, _translate("MainWindow", "总数"))
        self.comboBox.setItemText(2, _translate("MainWindow", "最大"))
        self.comboBox.setItemText(3, _translate("MainWindow", "最小"))
        self.comboBox.setItemText(4, _translate("MainWindow", "求和"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "升序"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "降序"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "全局"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "开头"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "结尾"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "特殊字符"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.pushButton_3.setText(_translate("MainWindow", "搜索"))
        self.pushButton_4.setText(_translate("MainWindow", "清屏"))

    def comb_one(self, o):
        text = self.lineEdit.text()
        if o == '平均':
            sql = 'SELECT AVG({text}) FROM t1;'.format(text=text)
        elif o == '总数':
            sql = 'SELECT COUNT({text}) FROM t1;'.format(text=text)
        elif o == '最大':
            sql = 'SELECT MAX({text}) FROM t1;'.format(text=text)
        elif o == '最小':
            sql = 'SELECT MIN({text}) FROM t1;'.format(text=text)
        elif o == '求和':
            sql = 'SELECT SUM({text}) FROM t1;'.format(text=text)
        self.tableWidget.clear()
        print(sql)
        self.show(sql)

    def comb_two(self, t):
        text_input = self.lineEdit_5.text()
        text_input2 = self.lineEdit_6.text()
        if t == '升序':
            sql = "SELECT id, species,price FROM t1 GROUP BY {name1} ORDER BY {name2} ASC".format(name1=text_input,
                                                                                                  name2=text_input2)
        elif t == '降序':
            sql = "SELECT id, species,price FROM t1 GROUP BY {name1} ORDER BY {name2} DESC".format(name1=text_input,
                                                                                                   name2=text_input2)
        print(sql)
        self.tableWidget.clear()
        self.show(sql)

    def comb_three(self, s):
        text1 = self.lineEdit_7.text()
        text2 = self.lineEdit_8.text()
        if s == '全局':
            sql = "SELECT id, species FROM t1 WHERE {text1} REGEXP '{text2}';".format(text1=text1, text2=text2)
        elif s == '开头':
            sql = "SELECT id, species FROM t1 WHERE {text1} REGEXP '^{text2}';".format(text1=text1, text2=text2)
        elif s == '结尾':
            sql = "SELECT id, species FROM t1 WHERE {text1} REGEXP '{text2}$';".format(text1=text1, text2=text2)
        elif s == '特殊字符':
            sql = r"SELECT id, species FROM t1 WHERE {text1} REGEXP '{text2}';".format(text1=text1, text2=r'\\' +
                                                                                                          text2)
        print(sql)
        self.tableWidget.clear()
        self.show(sql)

    def calculated_field(self):
        t1 = self.lineEdit_2.text()
        t2 = self.lineEdit_3.text()
        t3 = self.lineEdit_4.text()
        sql = 'SELECT {text1},{text3}, {text1}{text2}' \
              '{text3} FROM t1'.format(text1=t1, text2=t2, text3=t3)
        print(sql)
        self.tableWidget.clear()
        self.show(sql)

    def search(self):
        t1 = self.lineEdit_2.text()
        t2 = self.lineEdit_3.text()
        t3 = self.lineEdit_4.text()
        sql = "SELECT id,species FROM t1 WHERE {text1} IN (SELECT {text1} FROM t2 WHERE {text2} = '{text3}')".format \
            (text1=t1, text2=t2, text3=t3)
        print(sql)
        self.tableWidget.clear()
        self.show(sql)

    def show(self, sql):
        I = self.getDbData()
        pool = PooledDB(pymysql, 5, host=str(I['db1']['host']),
                        port=int(I['db1']['port']),
                        user=str(I['db1']['user']),
                        password=str(I['db1']['password']),
                        db=str(I['db1']['db'])
                        , setsession=['SET AUTOCOMMIT = 1'])
        connection = pool.connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print("result:", result)
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j])
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
        cursor.close()
        connection.close()

    def t_clear(self):
        self.tableWidget.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


