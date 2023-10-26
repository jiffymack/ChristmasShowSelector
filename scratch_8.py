from __future__ import print_function
import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        # Read items from a text file and store them in a list
        with open('items.txt', 'r') as f:
            items = f.read().splitlines()

        # Create a QListWidget and populate it with items from the list
        self.listWidget = QListWidget(self)
        self.listWidget.addItems(items)

        # Connect the item selection event to a function
        self.listWidget.itemActivated.connect(self.on_item_activated)

        # Create a layout and add widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)

        # Set the layout for the window
        self.setLayout(layout)

        self.setWindowTitle('Item List from File')
        self.setGeometry(0, 0, 1280, 800)
        self.show()

    def on_item_activated(self, item):
        print('Selected Item: {}'.format(item.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
