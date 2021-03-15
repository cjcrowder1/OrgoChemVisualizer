"""
This is the module OrgoChemVisualizer.

It is used to visualize simple organic chemistry reactions.
"""

import sys
import os
import numpy as np

import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets, QtCore

import chemanim as ca


class AnimationViewer(pg.GraphicsView):
    """ main class for viewing orgo chemicals """
    def __init__(self):
        super(AnimationViewer, self).__init__()

        #self.setAspectLocked()
        #self.setLimits(xMin=-10, xMax=10, yMin=-10, yMax=10)
        #self.setXRange(-10, 10)
        #self.setYRange(-10, 10)

        rect = QtCore.QRectF(-10, -10, 20, 20)
        self.setRange(rect)
        #self.setAspectLocked(True)

        mol1 = ca.H2O()
        mol2 = ca.CO2()
        mol3 = ca.HBr()
        mol4 = ca.CH3Br()
        mol5 = ca.OH()
        mol6 = ca.Br()
        mol7 = ca.C3H7Br()
        mol8 = ca.C4H9Br()
        mol9 = ca.H3O()
        mol10 = ca.C3H6()
        mol11 = ca.C3H7()
        mol12 = ca.CH3OH()
        mol13 = ca.Br2()
        mol14 = ca.C2H5OH()
        mol15 = ca.H2SO4()
        mol16 = ca.C2H5OH2()
        mol17 = ca.HSO4()
        mol18 = ca.C2H4()
        mol19 = ca.H2SO4f()
        mol20 = ca.H2Of()

        self.addItem(mol1)
        self.addItem(mol2)
        self.addItem(mol3)
        self.addItem(mol4)
        self.addItem(mol5)
        self.addItem(mol6)
        self.addItem(mol7)
        self.addItem(mol8)
        self.addItem(mol9)
        self.addItem(mol10)
        self.addItem(mol11)
        self.addItem(mol12)
        self.addItem(mol13)
        self.addItem(mol14)
        self.addItem(mol15)
        self.addItem(mol16)
        self.addItem(mol17)
        self.addItem(mol18)
        self.addItem(mol19)
        self.addItem(mol20)

        # testing text box
        example_text = "This is a text. I wonder what this will look like."
        step = 2
        posX = -3
        posY = -5
        text1 = ca.TextItem(example_text, posX, posY, step=step)
        self.addItem(text1)

        # testing animated arrow
        #p1 = pg.plot()
        #c = p1.plot(x=np.sin(np.linspace(0, 2*np.pi, 1000)), y=np.cos(np.linspace(0, 6*np.pi, 1000)))
        #a = pg.CurveArrow(c)
        #a.setStyle(headLen=20)
        #self.addItem(a)
        #anim = a.makeAnimation(loop=-1)
        #anim.start()

        self.arrow = ca.CurveArrow(0, -2, 5, -3)
        self.addItem(self.arrow.plot)
        self.arrow.start()


        #arrow = pg.ArrowItem()
        #self.addItem(arrow)
        #arrow_anim = QtCore.QPropertyAnimation(arrow, b'Pos')
        #arrow_anim.setDuration(8000)
        #arrow_anim.setStartValue(QtCore.QPointF(0, -13))
        #arrow_anim.setKeyValueAt(0.3, QtCore.QPointF(0, -13))
        #arrow_anim.setEndValue(QtCore.QPointF(0, -13))
        #arrow_anim.start()

#Initial animation for H2O
        self.R3S1 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S1.setDuration(8000)
        self.R3S1.setStartValue(QtCore.QPointF(0, -13))

        self.R3S1.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S1.setEndValue(QtCore.QPointF(0, -13))

        self.R3S1.start()

#Initial animation for CH3Br
        self.R2S1 = QtCore.QPropertyAnimation(mol4, b'pos')
        self.R2S1.setDuration(8000)
        self.R2S1.setStartValue(QtCore.QPointF(0, 0))

        self.R2S1.setKeyValueAt(0.3, QtCore.QPointF(0, 0))

        self.R2S1.setEndValue(QtCore.QPointF(0, 0))

        self.R2S1.start()

#Initial animation for OH-
        self.R2S2 = QtCore.QPropertyAnimation(mol5, b'pos')
        self.R2S2.setDuration(8000)
        self.R2S2.setStartValue(QtCore.QPointF(0, 0))

        self.R2S2.setKeyValueAt(0.3, QtCore.QPointF(2, 0.25))

        self.R2S2.setEndValue(QtCore.QPointF(2, 0.25))

        self.R2S2.start() 

#Initial animation for CH3OH
        self.R2S3 = QtCore.QPropertyAnimation(mol12, b'pos')
        self.R2S3.setDuration(8000)
        self.R2S3.setStartValue(QtCore.QPointF(0, 0))

        self.R2S3.setKeyValueAt(0.3, QtCore.QPointF(0, 0))

        self.R2S3.setEndValue(QtCore.QPointF(0, 0))

        self.R2S3.start()

#Initial animation for HBr
        self.R1S2 = QtCore.QPropertyAnimation(mol3, b'pos')
        self.R1S2.setDuration(8000)
        self.R1S2.setStartValue(QtCore.QPointF(0, 0))

        self.R1S2.setKeyValueAt(0.3, QtCore.QPointF(0, 0))

        self.R1S2.setEndValue(QtCore.QPointF(0, 0))

        self.R1S2.start()

#Initial animation for Br-
        self.R1S3 = QtCore.QPropertyAnimation(mol13, b'pos')
        self.R1S3.setDuration(8000)
        self.R1S3.setStartValue(QtCore.QPointF(0, 0))

        self.R1S3.setKeyValueAt(0.3, QtCore.QPointF(-2.5, 1))

        self.R1S3.setEndValue(QtCore.QPointF(-2.5, 1))

        self.R1S3.start()

#Initial animation for C2H5OH
        self.R3S2 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S2.setDuration(8000)
        self.R3S2.setStartValue(QtCore.QPointF(0, -13))

        self.R3S2.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S2.setEndValue(QtCore.QPointF(0, -13))

        self.R3S2.start()

#Initial animation for H2SO4
        self.R3S3 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S3.setDuration(8000)
        self.R3S3.setStartValue(QtCore.QPointF(0, 0))

        self.R3S3.setKeyValueAt(0.3, QtCore.QPointF(1, 1))

        self.R3S3.setEndValue(QtCore.QPointF(1, 1))

        self.R3S3.start()

#Initial animation for C2H5OH2
        self.R3S4 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S4.setDuration(8000)
        self.R3S4.setStartValue(QtCore.QPointF(0, -13))

        self.R3S4.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S4.setEndValue(QtCore.QPointF(0, -13))

        self.R3S4.start()

#Initial animation for HSO4
        self.R3S5 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S5.setDuration(8000)
        self.R3S5.setStartValue(QtCore.QPointF(0, -13))

        self.R3S5.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S5.setEndValue(QtCore.QPointF(0, -13))

        self.R3S5.start()

#Initial animation for C2H4
        self.R3S6 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S6.setDuration(8000)
        self.R3S6.setStartValue(QtCore.QPointF(0, -13))

        self.R3S6.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S6.setEndValue(QtCore.QPointF(0, -13))

        self.R3S6.start()

#Initial animation for second H2SO4
        self.R3S7 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S7.setDuration(8000)
        self.R3S7.setStartValue(QtCore.QPointF(0, -13))

        self.R3S7.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S7.setEndValue(QtCore.QPointF(0, -13))

        self.R3S7.start()

#Initial animation for H2O product
        self.R3S8 = QtCore.QPropertyAnimation(mol1, b'pos')
        self.R3S8.setDuration(8000)
        self.R3S8.setStartValue(QtCore.QPointF(0, -13))

        self.R3S8.setKeyValueAt(0.3, QtCore.QPointF(0, -13))

        self.R3S8.setEndValue(QtCore.QPointF(0, -13))

        self.R3S8.start()

class ReactionSelection(QtWidgets.QWidget):
    """ class containing settings for selecting which reaction to view """
    def __init__(self, parent=None):
        super(ReactionSelection, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        reaction_label = QtGui.QLabel("Choose which reaction to view")
        self.viewHBrRadio = QtGui.QRadioButton("Addition to HBr to Alkenes")
        self.viewSN2Radio = QtGui.QRadioButton("SN2")
        self.viewE1Radio = QtGui.QRadioButton("E1")

        self.viewHBrRadio.setChecked(True)

        layout.addWidget(reaction_label)
        layout.addWidget(self.viewHBrRadio)
        layout.addWidget(self.viewSN2Radio)
        layout.addWidget(self.viewE1Radio)

        self.setLayout(layout)


class Settings(QtWidgets.QWidget):
    """ main settings class """
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.start_btn = QtWidgets.QPushButton("Start", self)
        self.rs = ReactionSelection()

        layout.addWidget(self.start_btn)
        layout.addWidget(self.rs)
        layout.addStretch(1)

        self.setLayout(layout)


class MainWindow(QtWidgets.QMainWindow):
    """ main class for OrgoChemVisualizer """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('OrgoChemVisualizer')
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.resize(800, 600)

        self.av = AnimationViewer()
        self.set = Settings()

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.av)
        main_layout.addWidget(self.set)

        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('OrgoChemVisualizer')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
