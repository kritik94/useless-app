import sys
from PyQt4 import QtGui, QtCore

'''
Информация по настройке QPen смотреть здесь:
http://pyqt.sourceforge.net/Docs/PyQt4/qpen.html

Информация по настройке QPainter смотреть здесь:
http://pyqt.sourceforge.net/Docs/PyQt4/qpainter.html
'''

def blockStyle():
    pen = QtGui.QPen()
    pen.setStyle(QtCore.Qt.SolidLine)
    pen.setWidth(2) # width in px
    pen.setColor(QtCore.Qt.black)
    pen.setCapStyle(QtCore.Qt.SquareCap)
    pen.setJoinStyle(QtCore.Qt.MiterJoin)
    return pen

def textStyle():
    pen = QtGui.QPen()
    pen.setStyle(QtCore.Qt.SolidLine)
    pen.setWidth(1) # width in px
    pen.setColor(QtCore.Qt.black)
    pen.setCapStyle(QtCore.Qt.SquareCap)
    pen.setJoinStyle(QtCore.Qt.MiterJoin)
    return pen

def painterStyle():
    painter = QtGui.QPainter(self)
    painter.setPen(blockStyle())
    return painter

