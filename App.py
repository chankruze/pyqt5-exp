"""
Author: chankruze (chankruze@geekofia.in)
Created: Mon Dec 28 2020 11:58:23 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

width, height = 900, 600

# command line arguments passed to the application ([])
app = QApplication(sys.argv[1:])

# Every GUI app must have exactly one instance of QApplication.
# Many parts of Qt don't work until you have executed the above line.
# You will therefore need it in virtually every(Py)Qt app you write.

# window
window = QWidget()
window.resize(width, height)
# layout
# QVBoxLayout => stack widgets vertically
# QHBoxLayout => stack widgets horizontally
# more at https://doc.qt.io/qt-5/layout.html
layout = QVBoxLayout()
# add smaller widgets to layout
layout.addWidget(QPushButton('Button Top'))
layout.addWidget(QPushButton('Button Bottom'))
# set layout to window
window.setLayout(layout)
# render window
window.show()

# hand control over to Qt and ask it to "run the application until the user closes it".
app.exec_()
