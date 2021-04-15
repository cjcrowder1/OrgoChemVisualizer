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

        #self.scene = self.scene

        # initialize reaction2 object

        # testing text box
        example_text = "This is a text. I wonder what this will look like."
        step = 2
        posX = -3
        posY = -5
        text1 = ca.TextItem(example_text, posX, posY, step=step)
        self.addItem(text1)

        # testing animated arrow
        self.arrow = ca.CurveArrow(0, -2, 5, -3)
        self.addItem(self.arrow.plot)
        #self.arrow.start()

        # testing animated arrow
        self.arrow = ca.CurveArrow(0, 3, 0.5, 3)
        self.addItem(self.arrow.plot)
        #self.arrow.start()

    def show_reaction(self, name):
        self.sceneObj.clear()
        #self.scene.clear()

        if name == "reaction1":
            mol3 = ca.HBr()
            mol13 = ca.Br2()
            self.addItem(mol3)
            self.addItem(mol13)

            print("reaction 1 was pressed!")
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

        elif name == "reaction2":
            # initialize reaction 2
            self.reaction2 = ca.Reaction2(self)
            self.reaction2.start()

            #see textboxes file to add text
            # testing text box
            example_text = "This is an SN2 reaction with Alkyl Halides involving the nucleophile Hydroxide and the Alkyl Halide Bromomethane."
            step = 0
            posX = 0
            posY = -5
            text1 = ca.TextItem(example_text, posX, posY, step=step)
            self.addItem(text1)

            # testing animated arrow
            self.arrow = ca.CurveArrow(-2, 0, 0.5, 0)
            self.addItem(self.arrow.plot)
            #self.arrow.start()

            # testing animated arrow
            # self.arrow = ca.CurveArrow(-5.25, -0.5, -4.95, -0.10)
            # self.addItem(self.arrow.plot)
            #self.arrow.start()

            # testing animated arrow
            # self.arrow = ca.CurveArrow(-3.25, 0.75, -2.75, 1)
            # self.addItem(self.arrow.plot)
            #self.arrow.start()

        elif name == "reaction3":
            mol1 = ca.H2O()
            mol14 = ca.C2H5OH()
            mol15 = ca.H2SO4()
            mol16 = ca.C2H5OH2()
            mol17 = ca.HSO4()
            mol18 = ca.C2H4()
            mol19 = ca.H2SO4f()
            mol20 = ca.H2Of()

            self.addItem(mol1)
            self.addItem(mol14)
            self.addItem(mol15)
            self.addItem(mol16)
            self.addItem(mol17)
            self.addItem(mol18)
            self.addItem(mol19)
            self.addItem(mol20)

            print("reaction 3 was pressed!")

            #Initial animation for H2O
            self.R3S1 = QtCore.QPropertyAnimation(mol1, b'pos')
            self.R3S1.setDuration(8000)
            self.R3S1.setStartValue(QtCore.QPointF(0, -0))
            self.R3S1.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S1.setEndValue(QtCore.QPointF(0, -0))
            self.R3S1.start()

            #Initial animation for C2H5OH
            self.R3S2 = QtCore.QPropertyAnimation(mol14, b'pos')
            self.R3S2.setDuration(8000)
            self.R3S2.setStartValue(QtCore.QPointF(0, -0))
            self.R3S2.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S2.setEndValue(QtCore.QPointF(0, -0))
            self.R3S2.start()

            #Initial animation for H2SO4
            self.R3S3 = QtCore.QPropertyAnimation(mol15, b'pos')
            self.R3S3.setDuration(8000)
            self.R3S3.setStartValue(QtCore.QPointF(0, 0))
            self.R3S3.setKeyValueAt(0.3, QtCore.QPointF(1, 1))
            self.R3S3.setEndValue(QtCore.QPointF(1, 1))
            self.R3S3.start()

            #Initial animation for C2H5OH2
            self.R3S4 = QtCore.QPropertyAnimation(mol16, b'pos')
            self.R3S4.setDuration(8000)
            self.R3S4.setStartValue(QtCore.QPointF(0, -0))
            self.R3S4.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S4.setEndValue(QtCore.QPointF(0, -0))
            self.R3S4.start()

            #Initial animation for HSO4
            self.R3S5 = QtCore.QPropertyAnimation(mol17, b'pos')
            self.R3S5.setDuration(8000)
            self.R3S5.setStartValue(QtCore.QPointF(0, -0))
            self.R3S5.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S5.setEndValue(QtCore.QPointF(0, -0))
            self.R3S5.start()

            #Initial animation for C2H4
            self.R3S6 = QtCore.QPropertyAnimation(mol18, b'pos')
            self.R3S6.setDuration(8000)
            self.R3S6.setStartValue(QtCore.QPointF(0, -0))
            self.R3S6.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S6.setEndValue(QtCore.QPointF(0, -0))
            self.R3S6.start()

            #Initial animation for second H2SO4
            self.R3S7 = QtCore.QPropertyAnimation(mol19, b'pos')
            self.R3S7.setDuration(8000)
            self.R3S7.setStartValue(QtCore.QPointF(0, -0))
            self.R3S7.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S7.setEndValue(QtCore.QPointF(0, -0))
            self.R3S7.start()

            #Initial animation for H2O product
            self.R3S8 = QtCore.QPropertyAnimation(mol20, b'pos')
            self.R3S8.setDuration(8000)
            self.R3S8.setStartValue(QtCore.QPointF(0, -0))
            self.R3S8.setKeyValueAt(0.3, QtCore.QPointF(0, -0))
            self.R3S8.setEndValue(QtCore.QPointF(0, -0))
            self.R3S8.start()

        else:
            print(f"Error: {name} reaction name not recognized.")


class KeyframeChooser(QtWidgets.QWidget):
    """ Widget for controlling which keyframe is being displayed. """
    def __init__(self, parent=None):
        super(KeyframeChooser, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        self.label = QtGui.QLabel("Click through the reaction:")
        self.next_btn = QtGui.QPushButton("Next")
        self.prev_btn = QtGui.QPushButton("Previous")

        L = QtGui.QHBoxLayout()
        W = QtWidgets.QWidget()

        L.addWidget(self.prev_btn)
        L.addWidget(self.next_btn)
        W.setLayout(L)

        layout.addWidget(self.label)
        layout.addWidget(W)

        self.setLayout(layout)


class ReactionSelection(QtWidgets.QWidget):
    """ class containing settings for selecting which reaction to view """
    def __init__(self, parent=None):
        super(ReactionSelection, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        reaction_label = QtGui.QLabel("Choose which reaction to view")
        self.viewHBrRadio = QtGui.QRadioButton("Addition to HBr to Alkenes")
        self.viewSN2Radio = QtGui.QRadioButton("SN2")
        self.viewE1Radio = QtGui.QRadioButton("E1")

        #self.viewHBrRadio.setChecked(True)

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

        self.start_btn = QtWidgets.QPushButton("Start (does nothing)", self)
        self.fc = KeyframeChooser()
        self.rs = ReactionSelection()

        layout.addWidget(self.start_btn)
        layout.addWidget(self.fc)
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

        self.set.rs.viewHBrRadio.toggled.connect(
            lambda: self.av.show_reaction("reaction1"))
        self.set.rs.viewSN2Radio.toggled.connect(
            lambda: self.av.show_reaction("reaction2"))
        self.set.rs.viewE1Radio.toggled.connect(
            lambda: self.av.show_reaction("reaction3"))


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('OrgoChemVisualizer')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
