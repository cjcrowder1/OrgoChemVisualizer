"""
This is the module OrgoChemVisualizer.

It is used to visualize simple organic chemistry reactions.
"""

import sys
import os
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import mymath

class orgochemvisualizer(QtWidgets.QMainWindow):
    """ main class for OrgoChemVisualizer """
    def __init__(self):
        super(orgochemvisualizer, self).__init__()
        self.init_ui()

    def init_ui(self):
        uiPath = os.path.join("orgochemvisualizer","ui","orgochemvisualizer.ui")
        self.ui = uic.loadUi(uiPath)

        self.ui.setWindowTitle('OrgoChemVisualizer')
        #self.ui.setWindowIcon(QtGui.QIcon('logo.png'))

        # this is just a test that mymath was imported as expected
        a = mymath.my_square_root(324.0)

        self.scene = QtGui.QGraphicsScene()
        self.ui.mywidget.setScene(self.scene)

        ellipse1 = QtGui.QGraphicsEllipseItem(0,0,100,10)
        ellipse1.setBrush(QtGui.QBrush(QtCore.Qt.red, style = QtCore.Qt.SolidPattern))        
        self.scene.addItem(ellipse1) # add ellipse!
        
        # there's gotta be a better way to do this, but I don't have it now.
        self.ui.checkBox1.setChecked(True)
        self.ui.checkBox1.stateChanged.connect(lambda:self.checkbox_state(self.ui.checkBox1))
        self.ui.checkBox2.setChecked(True)
        self.ui.checkBox2.stateChanged.connect(lambda:self.checkbox_state(self.ui.checkBox2))
        self.ui.checkBox3.setChecked(True)
        self.ui.checkBox3.stateChanged.connect(lambda:self.checkbox_state(self.ui.checkBox3))
        self.ui.checkBox4.setChecked(True)
        self.ui.checkBox4.stateChanged.connect(lambda:self.checkbox_state(self.ui.checkBox4))
        self.ui.checkBox5.setChecked(True)
        self.ui.checkBox5.stateChanged.connect(lambda:self.checkbox_state(self.ui.checkBox5))
        # this doesn't work as expected, but it is the closest alternative
        #self.checkboxes = (self.ui.checkboxes.itemAt(i).widget() for i in range(self.ui.checkboxes.count())) 
        #for item in self.checkboxes:
        #    item.setChecked(True)
        #    item.stateChanged.connect(lambda:self.checkbox_state(item))

        self.ui.show()

    def checkbox_state(self,b):
        if b.isChecked():
            print(b.text()+" is selected")
        else:
            print(b.text()+" is deselected")


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('OrgoChemVisualizer')
    orgochemvisualizer()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()