import sys
from PyQt4 import QtCore, QtGui
from widget_1 import Ui_Form

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # connect signals
        self.ui.resetButton.clicked.connect(self.on_button)
        self.ui.x_vel.valueChanged.connect(self.on_x_vel)
        self.ui.y_vel.valueChanged.connect(self.on_y_vel)

    def on_button(self):
        self.ui.x_vel.setValue(0)
        self.ui.y_vel.setValue(0)
    def on_x_vel(self):
        self.ui.x_label.setText(str(self.ui.x_vel.value()))
    def on_y_vel(self):
        self.ui.y_label.setText(str(self.ui.y_vel.value()))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
