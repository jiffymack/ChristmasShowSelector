# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import os

#ser = serial.Serial(port='/dev/ttyUSB0',baudrate =9600,timeout=.1)
flag=1
now=0
now2=0
data = ''
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
            font.setPointSize(28)
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

    import os
    import time

    def on_update(self):
        global flag
        global now
        global now2

        # Get the current time in a human-readable format
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        # Combine 'v' and the current time separated by a comma
        v = self.listWidget.currentRow()
        entry = "{}, {}".format(v, current_time)

        # Write the entry to a text file called 's.txt' in the home directory, appending it to the file
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, "s.txt")

        # Check if the file exists and read its last line
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()  # Get the last line, remove leading/trailing whitespace

                    # Split the last line by comma to extract the first number and timestamp
                    last_v, last_timestamp = last_line.split(", ")

                    # Convert the last timestamp to a datetime object
                    last_time = time.strptime(last_timestamp, "%Y-%m-%d %H:%M:%S")
                    last_time_unix = time.mktime(last_time)

                    # Calculate the time difference between the current time and the last timestamp
                    time_difference = time.mktime(time.strptime(current_time, "%Y-%m-%d %H:%M:%S")) - last_time_unix

                    # Check conditions: if 'v' is different or the time difference is greater than 2 minutes
                    if int(last_v) != v or time_difference > 120:
                        with open(file_path, "a") as append_file:
                            append_file.write(entry + "\n")

        else:
            # If the file does not exist, create it and write the entry
            with open(file_path, "w") as new_file:
                new_file.write(entry + "\n")

        data = "A"  # ser.readall()
        if not data == '':
            print(data.decode('utf-8'))
        if flag == 0:
            flag = 1


import newqrc_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
