from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from math import sqrt
from frmPythagoras import Ui_frmMain


class Pythagoras(QtWidgets.QDialog, Ui_frmMain):
    def __init__(self):
        """
        CTor
        """
        super(Pythagoras, self).__init__()
        self.setupUi(self)
        # Disable the maximize button
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        # Encapsulated member variables
        self._ab_squared = 0
        self._ac_squared = 0
        self._bc = 0
        # Custom labels
        self.lblACvalue.angle = -90
        self.lblACvalue.setText("0")
        self.lblACvalue.setAlignment(Qt.AlignCenter)
        self.lblACvalue.setStyleSheet('font: 75 14pt "Noto Sans";color: rgb(255, 255, 0);')

        self.lblHypothenusediagonal.angle = 90
        self.lblHypothenusediagonal.setText("0")
        self.lblHypothenusediagonal.setAlignment(Qt.AlignCenter)
        self.lblHypothenusediagonal.setStyleSheet('font: 75 14pt "Noto Sans";color: rgb(255, 255, 0);')

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
        self.lblHypothenusediagonal.setText(str(fmt))


if __name__ == '__main__':
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    main_form = Pythagoras()
    main_form.show()
    sys.exit(app.exec_())