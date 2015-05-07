# -*- coding: utf-8 -*-

# created with 'pyuic4 widget_1.ui > widget_1.py'

# Form implementation generated from reading ui file 'widget_1.ui'
#
# Created: Thu May  7 08:24:08 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(324, 300)
        self.x_vel = QtGui.QSlider(Form)
        self.x_vel.setGeometry(QtCore.QRect(80, 200, 160, 21))
        self.x_vel.setMinimum(-5)
        self.x_vel.setMaximum(5)
        self.x_vel.setOrientation(QtCore.Qt.Horizontal)
        self.x_vel.setObjectName(_fromUtf8("x_vel"))
        self.y_vel = QtGui.QSlider(Form)
        self.y_vel.setGeometry(QtCore.QRect(150, 20, 21, 160))
        self.y_vel.setMinimum(-5)
        self.y_vel.setMaximum(5)
        self.y_vel.setOrientation(QtCore.Qt.Vertical)
        self.y_vel.setObjectName(_fromUtf8("y_vel"))
        self.resetButton = QtGui.QPushButton(Form)
        self.resetButton.setGeometry(QtCore.QRect(110, 240, 87, 27))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "First QT", None))
        self.resetButton.setText(_translate("Form", "PushButton", None))

