from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class RotatedQLabel(QWidget):
    def __init__(self, parent):
        """
        CTor of RotatedQLabel
        :param text: Text to display
        :param angle: Angle of rotation
        """
        super().__init__(parent)
        self.__label_text = ""
        self.__angle = ""

    @property
    def label_text(self):
        return self.__label_text

    @label_text.setter
    def label_text(self, value):
        self.__label_text = value

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        if value == 0 or value > 360:
            raise ValueError("Angle should be between 0 and 360!")
        self.__angle = value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)
        painter.translate(20, 100)
        painter.rotate(self.__angle)
        painter.drawText(0, 0, self.__label_text)
        painter.end()
