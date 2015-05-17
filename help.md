# QPen 

Класс, который настраивает, как именно должен рисовать QPainter

## Методы

### QPen.setStyle(Qt.PenStyle)
Задаёт стиль рисования линий

виды:

- QtCore.Qt.SolidLine
- QtCore.Qt.DashLine
- QtCore.Qt.DotLine
- QtCore.Qt.DasDotLine
- QtCore.Qt.DasDotDotLine
- QtCore.Qt.CustomDashLine

### QPen.setCapStyle(Qt.PenCapStyle)
Задаёт стиль последней точки в линии/

Виды:

- QtCore.Qt.SquareCap (по умолчанию)
- QtCore.Qt.FlatCap
- QtCore.Qt.RoundCap