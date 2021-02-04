"""
This module contains classes to draw chemicals.

It will first use a "displayed formula", but then eventually it would be
nice to add in skeletal formula for more typical orgo representations
"""

# test edit

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtCore


class Chemical(pg.GraphItem):
    """ Class for drawing chemicals. Initial position is a
    2-item numpy 1D-array """

    def __init__(self):
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []

        # for some reason this super init has to be below
        # the above 3 initializations
        super(Chemical, self).__init__()

        self.scatter.sigClicked.connect(self.clicked)

    def setData(self, **kwds):
        self.text = kwds.pop('text', [])
        self.data = kwds
        if 'pos' in self.data:
            self.npts = self.data['pos'].shape[0]
            self.data['data'] = np.empty(self.npts, dtype=[('index', int)])
            self.data['data']['index'] = np.arange(self.npts)
        self.setTexts(self.text)
        self.updateGraph()

    def setTexts(self, text):
        for i in self.textItems:
            i.scene().removeItem(i)
        self.textItems = []
        for t in text:
            item = pg.TextItem(t)
            self.textItems.append(item)
            item.setParentItem(self)

    def updateGraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i, item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])

    def mouseDragEvent(self, ev):
        if ev.button() != QtCore.Qt.LeftButton:
            ev.ignore()
            return

        if ev.isStart():
            # We are already one step into the drag.
            # Find the point(s) at the mouse cursor when the button was first
            # pressed:
            pos = ev.buttonDownPos()
            pts = self.scatter.pointsAt(pos)
            if len(pts) == 0:
                ev.ignore()
                return
            for ti in range(self.npts):
                self.dragPoint = pts[0]

            ind = pts[0].data()[0]
            self.dragOffset = self.data['pos'][ind] - pos

        elif ev.isFinish():
            self.dragPoint = None
            return
        else:
            if self.dragPoint is None:
                ev.ignore()
                return

        ind = self.dragPoint.data()[0]

        diff = np.zeros((self.npts, 2))
        for ti in range(self.npts):
            diff[ti, :] = self.data['pos'][ti] - self.data['pos'][ind]

        for ti in range(self.npts):
            self.data['pos'][ti] = diff[ti, :] + ev.pos() + self.dragOffset

        self.updateGraph()
        ev.accept()

    def clicked(self, pts):
        print("clicked: %s" % pts)


def LinInterp(p, q, t):
    """ Linearly interpolates between two points p and q to a point r(t),
    where t is between 0 and 1.

    Note that r(0)=p, and r(1)=q."""
    r = t*p + (1 - t)*q
    return r


class H2O(Chemical):
    def __init__(self):
        super(H2O, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)

    def get_positions(self):
        return np.array([
                        [-0.5, -0.5],
                        [0.5, -0.5],
                        [0, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        ])

    def get_texts(self):
        return ["H", "H", "O"]


class CO2(Chemical):
    def __init__(self):
        super(CO2, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)

    def get_positions(self):
        return np.array([
                        [-1, 0],
                        [0, 0],
                        [1, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        ])

    def get_texts(self):
        return ["O", "C", "O"]

class HBr(Chemical):
    def __init__(self):
        super(HBr, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)

    def get_positions(self):
        return np.array([
                        [-2, 0],
                        [0, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        ])
    
    def get_texts(self):
        return ["H", "Br"]

class CH3Br(Chemical):
    def __init__(self):
        super(CH3Br, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)

    def get_positions(self):
        return np.array([
                        [-1, 0],
                        [0, 0],
                        [1, 0],
                        [0, 1],
                        [0, -1],
                        ], dtype=float)
    
    def get_edges(self):
        return np.array([
                        [0, 1],
                        [2, 1],
                        [3, 1],
                        [4, 1],
                        ])
    
    def get_texts(self):
        return ["H", "C", "H", "Br", "H"]
        
        