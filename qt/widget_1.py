# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_1.ui'
#
# Created: Thu May  7 11:22:10 2015
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
        Form.setEnabled(True)
        Form.resize(328, 300)
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
        self.y_label = QtGui.QTextEdit(Form)
        self.y_label.setEnabled(False)
        self.y_label.setGeometry(QtCore.QRect(210, 80, 104, 21))
        self.y_label.setObjectName(_fromUtf8("y_label"))
        self.x_label = QtGui.QTextEdit(Form)
        self.x_label.setEnabled(False)
        self.x_label.setGeometry(QtCore.QRect(210, 120, 104, 21))
        self.x_label.setObjectName(_fromUtf8("x_label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "First QT", None))
        self.resetButton.setText(_translate("Form", "Reset Vals", None))
        self.y_label.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.x_label.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))

