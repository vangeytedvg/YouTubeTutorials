from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QSize


class RotatedQLabel(QLabel):
    """
    Rotated Label subclasses QLabel
    """

    def __init__(self, *args):
        """
        Ctor
        :param args:
        """
        QLabel.__init__(self, *args)
        # Set a default angle
        self.__angle = -90

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        self.__angle = value

    def paintEvent(self, event):
        """
        Draw the label
        :param event:
        """
        QLabel.paintEvent(self, event)
        painter = QPainter(self)
        painter.translate(0, self.height()-1)
        painter.rotate(self.__angle)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QLabel.render(self, painter)

    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())
