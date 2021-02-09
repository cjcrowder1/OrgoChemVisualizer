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

        self.addItem(mol1)
        self.addItem(mol2)
        self.addItem(mol3)
        self.addItem(mol4)
        self.addItem(mol5)
        self.addItem(mol6)

        self.anim = QtCore.QPropertyAnimation(mol1, b'pos')
        self.anim.setDuration(8000)
        self.anim.setStartValue(QtCore.QPointF(0, 0))

        self.anim.setKeyValueAt(0.3, QtCore.QPointF(1, 0))

        self.anim.setEndValue(QtCore.QPointF(4, 4))

        self.anim.start()

#Initial animation for CH3Br
        self.anim = QtCore.QPropertyAnimation(mol4, b'pos')
        self.anim.setDuration(8000)
        self.anim.setStartValue(QtCore.QpointF(0, 0))

        self.anim.setKeyValueAt(0.3, QtCore.QPointF(0, 2))

        self.anim.setEndValue(QtCore.QPointF(3, 3))

        self.anim.start()


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
