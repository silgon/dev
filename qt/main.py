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

    def on_button(self):
        print 'Button clicked!'


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
