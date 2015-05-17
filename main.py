import sys
from PyQt4 import QtGui, QtCore

class RenderArea(QtGui.QWidget):

    def __init__(self, parent=None):
        super(RenderArea, self).__init__(parent)

        self.pen = QtGui.QPen()
        self.brush = QtGui.QBrush()

        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setAutoFillBackground(True)

        self.points = [
            QtCore.QPoint(0, 212),
            QtCore.QPoint(622, 212)
        ]
        self.path = QtGui.QPainterPath()
        self.path.moveTo(0, 212)
        self.path.lineTo(620, 212)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(2)
        pen.setColor (QtCore.Qt.blue)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        pen.setJoinStyle(QtCore.Qt.RoundJoin)
        painter.setPen(pen)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawPath(self.path)

        painter.restore()

class App(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.mousePressed = False

        self.setFixedSize(640, 480)
        self.setWindowTitle("Signal generator")

        self.renderArea = RenderArea()
        self.numberOfPoints = QtGui.QSpinBox()
        self.numberOfPoints.setRange(2, 32)
        self.numberOfPoints.setSpecialValueText("2")
        self.updatePointButton = QtGui.QPushButton("Изменить количество точек", self)
        self.resultField = QtGui.QLineEdit()
        self.resultField.setReadOnly(True)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.renderArea, 0, 0, 1, 4)
        mainLayout.addWidget(self.numberOfPoints, 2, 0)
        mainLayout.addWidget(self.updatePointButton, 2, 1)
        mainLayout.addWidget(self.resultField, 2, 2)
        self.setLayout(mainLayout)



def main():
    app = QtGui.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()