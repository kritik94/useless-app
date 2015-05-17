import sys
from PyQt4 import QtGui, QtCore
import customStyle as style


class RenderArea(QtGui.QWidget):

    def __init__(self, blocks, parent=None):
        super(RenderArea, self).__init__(parent)

        self.pen = QtGui.QPen()
        self.brush = QtGui.QBrush()

        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setAutoFillBackground(True)

        self.points = [
            QtCore.QPoint(0, 200),
            QtCore.QPoint(622, 200)
        ]

        self.blocks = blocks
        self.dragging = None
        self.drag_offset = QtCore.QPoint()

    def paintEvent(self, event):
        p_block = QtGui.QPainter(self)
        p_block.setPen(style.blockStyle())
        p_block.setRenderHint(QtGui.QPainter.Antialiasing)
        for block in self.blocks:
            p_block.drawRect(block.rect)
            p_block.drawText(block.textPos, block.named, 
                block.textOpt)

    def mousePressEvent(self, event):
        for block in self.blocks:
            if block.rect.contains(event.pos()):
                self.dragging = block
                self.drag_offset = block.rect.topLeft() - event.pos()
                break
        else:
            print('No')
            self.dragging = None

    def mouseMoveEvent(self, event):
        if self.dragging is None:
            return

        point = event.pos() + self.drag_offset
        self.dragging.rect.moveTo(point)
        point += QtCore.QPointF(0, self.dragging.rect.height())
        self.dragging.textPos.moveTo(point)

        self.update()

    def mouseReleaseEvent(self, event):
        self.dragging = None


class logicBlock():
    def __init__(self, x, y, w, h, named="Basic"):
        self.rect = QtCore.QRectF(x, y, w, h)
        self.named = named
        self.textPos = QtCore.QRectF(x, y+h, w, 15)
        self.textOpt = QtGui.QTextOption(QtCore.Qt.AlignHCenter)


class App(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.mousePressed = False
        self.setFixedSize(640, 480)
        self.setWindowTitle("Signal generator")
        self.blocks = []
        self.renderArea = RenderArea(self.blocks)
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.renderArea, 0, 0, 1, 1)
        self.setLayout(mainLayout)

        self.dev()

    def dev(self):
        self.blocks.append(logicBlock(100, 100, 50, 50, 'Based1'))
        self.blocks.append(logicBlock(100, 200, 50, 50, 'Based2'))
        self.blocks.append(logicBlock(200, 100, 50, 50, 'Based3'))
        self.blocks.append(logicBlock(200, 200, 50, 50, 'Based4'))



def main():
    app = QtGui.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()