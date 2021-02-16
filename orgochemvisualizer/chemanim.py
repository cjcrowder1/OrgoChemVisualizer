"""
This module contains classes to draw chemicals.

It will first use a "displayed formula", but then eventually it would be
nice to add in skeletal formula for more typical orgo representations
"""

# test edit

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui


class Chemical(pg.GraphItem):
    """ Class for drawing chemicals. Initial position is a
    2-item numpy 1D-array """

    def __init__(self):
        self.textItems = []

        # for some reason this super init has to be below
        # the above 3 initializations
        super(Chemical, self).__init__()

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
            item.setFont(QtGui.QFont("Helvetica [Cronyx]", 1))
            self.textItems.append(item)
            item.setParentItem(self)

    def updateGraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i, item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])


def LinInterp(p, q, t):
    """ Linearly interpolates between two points p and q to a point r(t),
    where t is between 0 and 1.

    Note that r(0)=p, and r(1)=q."""
    r = t*p + (1 - t)*q
    return r


def strToSym(string):
    symbol = QtGui.QPainterPath()
    f = QtGui.QFont()
    f.setPointSize(1)
    symbol.addText(0, 0, f, string)
    br = symbol.boundingRect()
    scale = min(1. / br.width(), 1. / br.height())
    tr = QtGui.QTransform()
    scale2 = 0.075*len(string)
    tr.scale(scale*scale2, scale*scale2)
    tr.translate(-br.x() - br.width() / 2., -br.y() - br.height() / 2.)
    return tr.map(symbol)


# test
class TestSymbols():
    # something like a bowtie
    valves = np.asarray([
                [0.4330127, 0.25],
                [0.4330127, -0.25],
                [-0.4330127, 0.25],
                [-0.4330127, -0.25],
                [0.4330127, 0.25]
                ])

    valve = pg.arrayToQPath(valves[:, 0], valves[:, 1], connect='all')


class H2O(Chemical):
    def __init__(self):
        super(H2O, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('O')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True, pen=pg.mkPen('w'))

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


class CO2(Chemical):
    def __init__(self):
        super(CO2, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym("O"), strToSym("C"), strToSym("O")]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

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


class HBr(Chemical):
    def __init__(self):
        super(HBr, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym("H"), strToSym("Br")]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-2, 0],
                        [0, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        ])


class CH3Br(Chemical):
    def __init__(self):
        super(CH3Br, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym("H"), strToSym("C"), strToSym("Br"),
               strToSym("H"), strToSym("H")]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

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


class OH(Chemical):
    def __init__(self):
        super(OH, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('O')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-2, -1],
                        [-1, -1],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                         ])


class CH3OH(Chemical):
    def __init__(self):
        super(CH3OH, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('O'), strToSym('C'),
               strToSym('H'), strToSym('H'), strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-2, 0],
                        [-1, 0],
                        [0, 0],
                        [1, 0],
                        [0, 1],
                        [0, -1],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        [1, 2],
                        [3, 2],
                        [4, 2],
                        [5, 2],
                        ])


class Br(Chemical):
    def __init__(self):
        super(Br, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('Br')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [1, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 0],
                        ])
