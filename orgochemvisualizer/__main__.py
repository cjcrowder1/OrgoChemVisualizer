"""
This is the module OrgoChemVisualizer.

It is used to visualize simple organic chemistry reactions.
"""

import sys
import os
import numpy as np

import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets

import chemanim as ca


class AnimationViewer(pg.GraphicsLayoutWidget):
    """ main class for viewing orgo chemicals """
    def __init__(self):
        super(AnimationViewer, self).__init__()
        v = self.addViewBox()
        v.setAspectLocked()
        v.setLimits(xMin=-10, xMax=10, yMin=-10, yMax=10)
        v.setXRange(-10, 10)
        v.setYRange(-10, 10)

        mol1 = ca.H2O()
        mol2 = ca.CO2()
        mol3 = ca.HBr()
        mol4 = ca.CH3Br()
        

        v.addItem(mol1)
        v.addItem(mol2)
        v.addItem(mol3)
        v.addItem(mol4)



class MainWindow(QtWidgets.QMainWindow):
    """ main class for OrgoChemVisualizer """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('OrgoChemVisualizer')
        self.resize(600, 600)

        self.av = AnimationViewer()

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.av)

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
