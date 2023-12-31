# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing. ok ok ok ok

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import serial

ser = serial.Serial(port='/dev/ttyUSB0',baudrate =9600,timeout=1)
flag=1
now=0
now2=0
data = ''
selection1=0.0
selection2=0.0
#GPIO.setup(23, GPIO.OUT)
n=16 ## set number of selections
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.listWidget.setStyleSheet("\n"
"background: Transparent;""\n"
"background-image: url(:/newPrefix/187161.jpg);")
        self.listWidget.setObjectName("listWidget")
        with open('selectionList.txt') as reader:
            Selections = reader.readlines()
        i=0  
        for Selection in Selections:
            a=Selection.split(',')
            a[1]=a[1].strip()
            #print(a[1])
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(36)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(20, 5*i+i*45, 71, 41))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap(a[1]))
            self.label.setScaledContents(True)
            self.label.setObjectName("label"+str(i))
            i=i+1
        i=0
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.listWidget.itemSelectionChanged.connect(self.on_change)
        self.listWidget.itemActivated.connect(self.on_update)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        with open('selectionList.txt') as reader:
            Selections = reader.readlines()
        m=0
        for Selection in Selections:
            a=Selection.split(',')
            a[0]=a[0].strip()
            #print(a[0])
            item = self.listWidget.item(m)
            item.setText(_translate("MainWindow", str(a[0])))
            m=m+1
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
    
    def on_change(self):
        print("start")
        print([item.text() for item in self.listWidget.selectedItems()])
    
    def on_update(self):
        global flag
        global now
        global now2
        global selection1
        global selection2
        if selection2-selection1>0.5:
            print(self.listWidget.currentRow())
            v=self.listWidget.currentRow()
            s="r"+str(v+1)+" p\n\r"
            print(s)
            now2=time.time()
        
            #if flag==1:
            ser.write(s.encode())
            #flag=0
            #now=time.time()
            time.sleep(0.2)
            data=ser.readall()
            if not data=='':
                print(data.decode('utf-8'))
                flag=0
            selection1=time.time()
            #if flag==0 and now2-now>2:
            #flag=1
            #if([item.text() for item in self.listWidget.selectedItems()]==['Selection 3']):
            #print('matched')
import newqrc_rc
def update2():
    global selection2
    selection2=time.time()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    timer = QTimer()
    timer.timeout.connect(update2)
    timer.setInterval(10)
    timer.start()
    sys.exit(app.exec_())
