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


# test
class Symbols():
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
        texts = self.get_texts()
    

        self.setData(pos=pos, adj=adj, pxMode=False, size=1, 
                     symbol=Symbols.valve, text=texts, fontSize=0.5, 
                     antialias=True)

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
        return ["H", "C", "Br", "H", "H"]

class OH(Chemical):
    def __init__(self):
        super(OH, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)

    def get_positions(self):
        return np.array([
                        [-2, -1],
                        [-1, -1],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                         ])
    
    def get_texts(self):
        return ["H", "O-"]

class CH3OH(Chemical):
    def __init__(self):
        super(CH3OH, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)
    
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
    def get_texts(self):
        return ["H", "O", "C", "H", "H", "H"]

class Br(Chemical):
    def __init__(self):
        super(Br, self).__init__()
       
        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()

        self.setData(pos=pos, adj=adj, pxMode=True, text=texts)
    
    def get_positions(self):
        return np.array([
                        [1, 0],
                        ], dtype=float)
    
    def get_edges(self):
        return np.array([
                        [0, 0],
                        ])
    
    def get_texts(self):
        return ["Br-"]


