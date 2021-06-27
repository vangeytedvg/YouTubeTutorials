from PyQt5 import QtWidgets, QtGui, Qt
from math import sqrt
from frmPythagoras import Ui_frmMain


class Pythagoras(QtWidgets.QMainWindow, Ui_frmMain):
    def __init__(self):
        # Encapsulated member variables
        self._ab_squared = 0
        self._ac_squared = 0
        self._bc = 0
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
        self.lblACvalue.setText(f"{str(self.slideAC.value())}")
        self._ac_squared = int(self.slideAC.value()) ** 2
        self.lblACsquared.setText(str(self._ac_squared))
        self.calculateHypothenuse(self.slideAB.value(), self.slideAC.value())

    def handle_slideAB_changed(self):
        """
        Handle A->B value
        :return:
        """
        self.lblABvalue.setText(f"{str(self.slideAB.value())}")
        self._ab_squared = int(self.slideAB.value()) ** 2
        self.lblABsquared.setText(str(self._ab_squared))
        self.calculateHypothenuse(self.slideAB.value(), self.slideAC.value())

    def calculateHypothenuse(self, ab: int, ac:int):
        abac = self._ab_squared + self._ac_squared
        self._bc = abac
        self.lblBCsquared.setText(str(abac))
        hypotenuse = sqrt(self._bc)
        fmt = "{:,.2f}".format(hypotenuse)
        self.lblHypothenuse.setText(str(fmt))
        pass


if __name__ == '__main__':
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    main_form = Pythagoras()
    main_form.show()
    sys.exit(app.exec_())