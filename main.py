from PyQt5 import QtWidgets, QtGui, Qt
from frmPythagoras import Ui_frmMain


class Pythagoras(QtWidgets.QMainWindow, Ui_frmMain):
    def __init__(self):
        """
        CTor
        """
        super(Pythagoras, self).__init__()
        self.setupUi(self)
        """ Event handlers """
        self.slideAC.valueChanged.connect(self.handle_slideAC_changed)
        self.slideAB.valueChanged.connect(self.handle_slideAB_changed)

    def handle_slideAC_changed(self):
        """
        Handle A->C value
        """
        self.lblACvalue.setText(f"{str(self.slideAC.value())} meter")
        self.lblACsquared.setText(str(int(self.slideAC.value()) ** 2))
        self.calculateHypothenuse(self.slideAB.value(), self.slideAC.value())

    def handle_slideAB_changed(self):
        """
        Handle A->B value
        :return:
        """
        self.lblABvalue.setText(f"{str(self.slideAB.value())} meter")
        self.lblABsquared.setText(str(int(self.slideAB.value()) ** 2))
        self.calculateHypothenuse(self.slideAB.value(), self.slideAC.value())

    def calculateHypothenuse(self, ab: int, ac:int):
        hypothenuse = (ab**2) + (ac**2)
        self.lblBCsquared.setText(str(hypothenuse))


if __name__ == '__main__':
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    main_form = Pythagoras()
    main_form.show()
    sys.exit(app.exec_())