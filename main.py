from PyQt5 import QtWidgets, QtGui, Qt
from frmPythagoras import Ui_frmMain


class Pythagoras(QtWidgets.QMainWindow, Ui_frmMain):
    def __init__(self):
        super(Pythagoras, self).__init__()
        self.setupUi(self)
        self.slideAC.valueChanged.connect(self.handle_slideAC_changed)
        self.slideAB.valueChanged.connect(self.handle_slideAB_changed)

    def handle_slideAC_changed(self):
        self.lblAC.setText(str(self.slideAC.value()))

    def handle_slideAB_changed(self):
        self.lblAB.setText(str(self.slideAB.value()))


if __name__ == '__main__':
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    main_form = Pythagoras()
    main_form.show()
    sys.exit(app.exec_())