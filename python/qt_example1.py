#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT 

class QProgBar(QProgressBar):
 
    value = 0
 
    @pyqtSlot()
    def increaseValue(progressBar):
        progressBar.setValue(progressBar.value)
        progressBar.value = progressBar.value+1

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QMainWindow()

# Set window size.
w.resize(320, 240)

# Set window title
w.setWindowTitle("Hello World!")

# Create main menu
mainMenu = w.menuBar()
fileMenu = mainMenu.addMenu('&File')

# Add exit button
exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
exitButton.setShortcut('Ctrl+Q')
exitButton.setStatusTip('Exit application')
exitButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)

# Create progressBar.
bar = QProgBar(w)
bar.resize(320,50) 
bar.setValue(0)
bar.move(0,50)

# create timer for progressBar
timer = QTimer()
bar.connect(timer,SIGNAL("timeout()"),bar,SLOT("increaseValue()"))
timer.start(400)

# Create combobox
combo = QComboBox(w)
combo.addItem("Python")
combo.addItem("Perl")
combo.addItem("Java")
combo.addItem("C++")
combo.move(20,100)

# Show window
w.show()

sys.exit(a.exec_())
