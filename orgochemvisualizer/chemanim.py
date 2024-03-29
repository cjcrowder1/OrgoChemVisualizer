"""
This module contains classes to draw chemicals.

It will first use a "displayed formula", but then eventually it would be
nice to add in skeletal formula for more typical orgo representations
"""

# test edit

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore

# see https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts
# \u2009 is a 'thin space' character that makes it easier to see superscript
SUPNEG = '\u2009'+'\u207B'
SUPTWO = '\u2009'+'\u00B2'


class Chemical(pg.GraphItem):
    """ Class for drawing chemicals. Initial position is a
    2-item numpy 1D-array.
    """

    def __init__(self):
        self.textItems = []
        self.center = QtCore.QPointF(0, 0)

        # for some reason this super init has to be below
        # the above 3 initializations
        super(Chemical, self).__init__()

    def setData(self, **kwds):
        self.text = kwds.pop('text', [])
        self.data = kwds

        if 'adj' in self.data:
            self.n_connections = self.data['adj'].shape[0]

        if 'bonds' in self.data:
            self.n_singles = sum(val == "s" for val in self.data['bonds'])
            self.n_doubles = sum(val == 'd' for val in self.data['bonds'])
        # in case 'bonds' isn't given, assume all singles
        else:
            if 'adj' in self.data:
                self.data['bonds'] = ['s']*self.data['adj'].shape[0]
                self.n_singles = self.data['adj'].shape[0]
                self.n_doubles = 0
            else:
                self.n_singles = 0
                self.n_doubles = 0

        if 'adj' in self.data:
            self.n_bonds = self.n_singles + 2*self.n_doubles

        if 'pos' in self.data:
            # originals, then 2 new points per edge
            self.n_atoms = self.data['pos'].shape[0]
            self.npts = self.n_atoms + 2*self.n_bonds
            new_pos = np.zeros((self.npts, 2), dtype=float)

            # points in atom locations
            for ti in range(self.n_atoms):
                new_pos[ti, 0] = self.data['pos'][ti, 0]
                new_pos[ti, 1] = self.data['pos'][ti, 1]

            n_singles_count = 0
            # ghost points adjusted for single or double bonds
            for edge, ti in enumerate(range(self.n_atoms,
                                            self.n_atoms + 2*self.n_connections,
                                            2)):
                point1 = self.data['pos'][self.data['adj'][edge, 0]]
                point2 = self.data['pos'][self.data['adj'][edge, 1]]

                if self.data['bonds'][edge] == 's':
                    r1, r2 = generate_single_bond_nodes(point1, point2)
                    new_pos[ti, :] = r1
                    new_pos[ti+1, :] = r2
                    n_singles_count += 1
                elif self.data['bonds'][edge] == 'd':
                    r1, r2, r3, r4 = generate_double_bond_nodes(point1, point2)
                    new_pos[ti, :] = r1
                    new_pos[ti+1, :] = r2
                    new_pos[ti + 2*self.n_connections - 2*n_singles_count, :] = r3
                    new_pos[ti + 2*self.n_connections - 2*n_singles_count + 1, :] = r4

            # reset values to adjust for single or double bonds
            self.data['pos'] = new_pos
            self.data['size'] = [5]*self.n_atoms + [0]*2*self.n_bonds
            self.data['symbol'] = self.data['symbol'] + ['o']*2*self.n_bonds
            self.data['adj'] = np.zeros((self.n_bonds, 2), dtype=int)
            for ti in range(self.n_bonds):
                self.data['adj'][ti] = [self.n_atoms + 2*ti,
                                        self.n_atoms + 2*ti + 1]

            # adjust the ridiculous size of Br
            for count, sym in enumerate(self.data['symbol']):
                if sym == strToSym('Br'):
                    self.data['size'][count] *= 0.68
                elif sym == strToSym('Br'+SUPNEG):
                    self.data['size'][count] *= 0.55
                elif sym == strToSym('Br'+SUPTWO):
                    self.data['size'][count] *= 0.55

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

    def set_pos(self, x, y):
        self.center.setX(x)
        self.center.setY(y)
        for row in self.pos:
            row[0] += x
            row[1] += y
        self.updateGraph()


class KeyFrame:
    """ Class for animating chemicals."""
    def __init__(self, labels=[], molecules=[],
                 arrows=[], animations=[]):
        self.labels = labels
        self.molecules = molecules
        self.arrows = arrows
        self.animations = animations

    def start(self):
        pass


#class Reaction:
#    """Generic Reaction template."""
#    def __init__(self):
#        self.molecules = []
#        self.frames = []


class Reaction2:
    """Will start off with just reaction 2, and will eventually move parts that
    can be generalized into the generic 'Reaction' class above."""
    def __init__(self, viewer):
        self.viewer = viewer

        # define text
        intro_text = "This is an SN2 reaction with Alkyl Halides involving the nucleophile Hydroxide and the Alkyl Halide Bromomethane."
        self.text_frame0 = TextItem(intro_text, 0, -5)

        step1_text = "The hydroxide molecule approaches Bromomethane."
        self.text_frame1 = TextItem(step1_text, -6, -4.5, step=1)

        step2_text = "Since the hydroxide molecule is negatively charged, one of the electron pairs on the Oxygen attacks the positvely charged Carbon."
        self.text_frame2 = TextItem(step2_text, -6, -4.5, step=2)

        step3_text = "At the same time as the Oxygen attacks the Carbon and begins forming a new bond, the Carbon-Bromine bond is broken since Bromine is a good leaving group."
        self.text_frame3 = TextItem(step3_text, -6, -4.5, step=3)

        step4_text = "The final result is a new bond between the Oxygen in the hydroxide group and the Carbon, and a negatively charged Bromide."
        self.text_frame4 = TextItem(step4_text, -6, -4.5, step=4)

        # define molecules
        self._CH3Br = CH3Br()
        self._OH = OH()
        self._CH3OH = CH3OH()
        self._Br = Br()
        self.molecules = [self._CH3Br, self._OH, self._CH3OH, self._Br]

        # set initial positions of chemicals
        self._OH.set_pos(4, 4)
        self._CH3Br.set_pos(-2, 0)
        self._CH3OH.set_pos(-2, 0)
        self._Br.set_pos(0, 1)

        # define arrow animations
        self.arrowAtReaction = CurveArrow(3, -1, -0.5, 0.5)

        # define molecule animations
        # animation positions are RELAVTIVE TO CURRENT. Not absolute.
        self.R2S2 = QtCore.QPropertyAnimation(self._OH, b'pos')
        self.R2S2.setDuration(1000)
        self.R2S2.setStartValue(QtCore.QPointF(0, 0))
        self.R2S2.setEndValue(QtCore.QPointF(-4, -3))

        self.R2S4 = QtCore.QPropertyAnimation(self._Br, b'pos')
        self.R2S4.setDuration(1500)
        self.R2S4.setStartValue(QtCore.QPointF(0, 0))
        self.R2S4.setKeyValueAt(0.33, QtCore.QPointF(0, 0))
        self.R2S4.setEndValue(QtCore.QPointF(4, 4))

    def _remove_molecules(self):
        for molecule in self.molecules:
            self.viewer.removeItem(molecule)

    def start_frame(self, frame):
        if frame == 0:
            # add new items that are not on scene
            self.viewer.addItem(self.text_frame0)
            self.viewer.addItem(self._OH)
            self.viewer.addItem(self._CH3Br)

        elif frame == 1:
            # remove items from previous step that are no longer needed
            self.viewer.removeItem(self.text_frame0)

            # add new items that are not on scene
            self.viewer.addItem(self.text_frame1)

            # remove items from previous step that are no longer needed
            self.R2S2.start()

        elif frame == 2:
            # remove items from previous step that are no longer needed
            self.viewer.removeItem(self.text_frame1)

            # add new items that are not on scene
            self.viewer.addItem(self.text_frame2)
            self.viewer.addItem(self.arrowAtReaction.plot)

            # start animations
            self.arrowAtReaction.start()

        elif frame == 3:
            # remove items from previous step that are no longer needed
            self.viewer.removeItem(self.text_frame2)

            # add new items that are not on scene
            self.viewer.addItem(self.text_frame3)

        elif frame == 4:
            # remove items from previous step that are no longer needed
            self.viewer.removeItem(self.text_frame3)
            self.viewer.removeItem(self.arrowAtReaction.plot)
            self.viewer.removeItem(self._OH)
            self.viewer.removeItem(self._CH3Br)

            # add new items that are not on scene
            self.viewer.addItem(self.text_frame4)
            self.viewer.addItem(self._CH3OH)
            self.viewer.addItem(self._Br)

            # start animations
            self.R2S4.start()

        else:
            print(f"frame {frame} not recognized")


def LinInterp(p, q, t):
    """ Linearly interpolates between two points p and q to a point r(t),
    where t is between 0 and 1.

    Note that r(0)=p, and r(1)=q."""
    r = t*p + (1 - t)*q
    return r


def compute_ortho_vec(p, q):
    """Computes orthonormal vector to line generated by two points
    p and q.
    """

    ax = p[0] - q[0]
    ay = p[1] - q[1]
    length = np.sqrt(ax**2 + ay**2)

    return np.array([ay, -ax])/length


def generate_single_bond_nodes(point1, point2):
    """Generates single bond ghost nodes."""
    percent_offset = 0.35
    new1 = LinInterp(point1, point2, percent_offset)
    new2 = LinInterp(point1, point2, 1 - percent_offset)

    return new1, new2


def generate_double_bond_nodes(point1, point2):
    """Generates double bond ghost nodes."""
    percent_offset = 0.05

    # first find orthonormal vector for 2 points
    ortho = compute_ortho_vec(point1, point2)

    # then generate 2 intermediate notes
    int1, int2 = generate_single_bond_nodes(point1, point2)

    # then use orthonormal vector to "branch off" from intermediate nodes
    # to make 4 new nodes
    new1 = int1 + percent_offset*ortho
    new2 = int2 + percent_offset*ortho
    new3 = int1 - percent_offset*ortho
    new4 = int2 - percent_offset*ortho

    return new1, new2, new3, new4


class CurveArrow(pg.CurveArrow):
    """Custom CurveArrow class to provide consistent style.

    Arrow points from (pos0X, pos0Y) to (pos1X, pos1Y).

    Right now is along straight line. In future will travel along curve.

    Example:
    >>> arrow = ca.CurveArrow(0, 0, 5, 0)
    >>> addItem(arrow.plot)
    >>> arrow.start()
    """
    def __init__(self, pos0X, pos0Y, pos1X, pos1Y):
        self.plot = pg.PlotDataItem(x=np.linspace(pos0X, pos1X, 100),
                                    y=np.linspace(pos0Y, pos1Y, 100),
                                    pen=pg.mkPen('r'))
        super(CurveArrow, self).__init__(self.plot)
        self.setStyle(headLen=15)
        self.anim = self.makeAnimation(loop=-1, duration=1000)

    def start(self):
        self.anim.start()


class TextItem(pg.TextItem):
    """Custom TextItem class to provide consistent style.

    Takes 3 arguments: text, posX and posY. posX and posY refer
    to the location of the center (as of right now. Can use
    `anchor` argument to change this)."""
    def __init__(self, text, posX=0, posY=0, step=None):
        pen = pg.mkPen(cosmetic=True, width=1, color='w', size=0.01)
        brush = pg.mkBrush(50, 50, 50, 100)
        super(TextItem, self).__init__(border=pen, fill=brush,
                                       anchor=(0.5, 0.5))

        font = QtGui.QFont()
        size = 12
        font.setPointSize(size)

        printText = ""
        if step is not None:
            printText += "<u>Step " + str(step) + "</u>:<br>"
        printText += text
        self.setHtml(printText)
        self.setPos(posX, posY)
        self.setFont(font)

        sizeScale = 0.05
        self.setScale(sizeScale)
        self.setTextWidth(200)


def strToSym(string):
    """Converts string to symbol, which can then be displayed."""
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


class H2O(Chemical):
    """Class for H2O."""
    def __init__(self):
        super(H2O, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('O')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True, pen=pg.mkPen('w'))

    def get_positions(self):
        return np.array([
                        [-0.5, -13],
                        [0.5, -13],
                        [0, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        ])


class CO2(Chemical):
    """Class for CO2."""
    def __init__(self):
        super(CO2, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym("O"), strToSym("C"), strToSym("O")]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-1, 13],
                        [0, 13],
                        [1, 13],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        [1, 2],
                        ])


class HBr(Chemical):
    """Class for HBr."""
    def __init__(self):
        super(HBr, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym("H"), strToSym("Br")]
        bonds = ['s']

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, bonds=bonds,
                     antialias=True)

    def get_positions(self):
        return np.array([
                        [-5.5, -9],
                        [-4, -9],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        ])


class CH3Br(Chemical):
    """Class for CH3Br."""
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
    """Class for OH."""
    def __init__(self):
        super(OH, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('O')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-0.5, 0],
                        [0.5, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                         ])


class CH3OH(Chemical):
    """Class for CH3OH."""
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
                        [1.5, 0],
                        [0.5, 0],
                        [-0.5, 0],
                        [-1.5, 0],
                        [-0.5, 1],
                        [-0.5, -1],
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
    """Class for Br."""
    def __init__(self):
        super(Br, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('Br'+SUPNEG)]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [0, 0],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 0],
                        ])


class C3H7Br(Chemical):
    """Class for C3H7Br.

    This is in line format, could also do a more simplified
    format of the molecule"""

    def __init__(self):
        super(C3H7Br, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'),
               strToSym('C'), strToSym('C'), strToSym('H'), 
               strToSym('Br'), strToSym('C'), strToSym('H'),
               strToSym('H'), strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)
    def get_positions(self):
        return np.array([
                        [6, -5], 
                        [5, -6],
                        [6, -7], 
                        [6, -6], 
                        [7, -6], 
                        [7, -7],
                        [7, -5],
                        [8, -6],
                        [8, -5], 
                        [8, -7],
                        [9, -6],
                        ], dtype=float)
    def get_edges(self):
        return np.array([
                        [0, 3],
                        [1, 3],
                        [2, 3],
                        [3, 4],
                        [5, 4], 
                        [6, 4], 
                        [4, 7], 
                        [8, 7], 
                        [9, 7],
                        [10, 7],
                        ])


class C4H9Br(Chemical):
    """Class for C4H9Br."""
    def __init__(self):
        super(C4H9Br, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'),
               strToSym('C'), strToSym('C'), strToSym('H'), 
               strToSym('Br'), strToSym('C'), strToSym('H'),
               strToSym('H'), strToSym('C'), strToSym('H'), 
               strToSym('H'), strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)
    def get_positions(self):
        return np.array([
                        [-8, 17], 
                        [-9, 18],
                        [-8, 19], 
                        [-8, 18], 
                        [-7, 18], 
                        [-7, 19],
                        [-7, 17],
                        [-6, 18],
                        [-6, 17], 
                        [-6, 19],
                        [-5, 18],
                        [-5, 17],
                        [-5, 19],
                        [-4, 18],
                        ], dtype=float)
    def get_edges(self):
        return np.array([
                        [0, 3],
                        [1, 3],
                        [2, 3],
                        [3, 4],
                        [5, 4], 
                        [6, 4], 
                        [4, 7], 
                        [8, 7], 
                        [9, 7],
                        [7, 10],
                        [11, 10],
                        [12, 10],
                        [13, 10],
                        ])


class H3O(Chemical):
    """Class for H3O."""
    def __init__(self):
        super(H3O, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'), strToSym('O')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True, pen=pg.mkPen('w'))

    def get_positions(self):
        return np.array([
                        [-3, -13],
                        [-2, -12],
                        [-1, -11],
                        [-2, -13],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 3],
                        [1, 3],
                        [2, 3],
                        ])


class C3H6(Chemical):
    """Class for C3H6.

    Alkene needs double bond"""
    def __init__(self):
        super(C3H6, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'), strToSym('C'),
                strToSym('C'), strToSym('H'), strToSym('C'), strToSym('H'), 
                strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True, pen=pg.mkPen('w'))

    def get_positions(self):
        return np.array([
                        [-9, -7],
                        [-10, -6],
                        [-9, -5],
                        [-9, -6],
                        [-8, -6],
                        [-8, -5],
                        [-7, -6],                            
                        [-7, -7],
                        [-7, -5],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 3],
                        [1, 3],
                        [2, 3],
                        [3, 4], 
                        [5, 4],
                        [4, 6], 
                        [7, 6],                             
                        [8, 6],
                        ])


class C3H7(Chemical):
    """Class for C3H7.

    Needs a + charge"""
    def __init__(self):
        super(C3H7, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'), strToSym('C'),
                strToSym('C'), strToSym('H'), strToSym('C'), strToSym('H'), 
                strToSym('H'), strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True, pen=pg.mkPen('w'))

    def get_positions(self):
        return np.array([
                        [-1, -7],
                        [-2, -6],
                        [-1, -5],
                        [-1, -6], 
                        [0, -6],
                        [0, -5],
                        [1, -6],
                        [1, -7],
                        [2, -6],
                        [1, -5],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 3],
                        [1, 3],
                        [2, 3],
                        [3, 4], 
                        [5, 4],
                        [4, 6], 
                        [7, 6], 
                        [8, 6],
                        [9, 6],
                        ])


class Br2(Chemical):
    """Class for Br2."""
    def __init__(self):
        super(Br2, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('Br'+SUPTWO)]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [3, -9],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 0],
                        ])


class C2H5OH(Chemical):
    """Class for C2H5OH."""
    def __init__(self):
        super(C2H5OH, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'), 
                strToSym('C'), strToSym('C'), strToSym('H'), 
                strToSym('H'), strToSym('O'), strToSym('H')]
        
        self.setData(pos=pos, adj=adj, pxMode=False, 
                     symbol=sym, antialias=True)
    
    def get_positions(self):
        return np.array([
                        [-8, 5],
                        [-9, 6],
                        [-8, 7],
                        [-8, 6],
                        [-7, 6],
                        [-7, 5],
                        [-7, 7],
                        [-6, 6],
                        [-5, 6]
                        ], dtype=float)
    
    def get_edges(self):
        return np.array([
                        [0, 3], 
                        [1, 3],
                        [2, 3],
                        [3, 4],
                        [5, 4], 
                        [6, 4], 
                        [4, 7], 
                        [7, 8],
                        ])


class H2SO4(Chemical):
    """Class for H2SO4."""
    def __init__(self):
        super(H2SO4, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('O'), strToSym('S'), 
                strToSym('O'), strToSym('O'), strToSym('O'), 
                strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False, 
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-6, 7.5], 
                        [-6, 8.5],
                        [-5, 9.5],
                        [-6, 10.5],
                        [-4, 10.5],
                        [-4, 8.5],
                        [-4, 7.5],
                        ], dtype=float)
    
    def get_edges(self):
        return np.array([
                        [0, 1],
                        [1, 2],
                        [3, 2],
                        [4, 2],
                        [5, 2],
                        [6, 5],
                        ])


class C2H5OH2(Chemical):
    """Class for C2H5OH2.

    Needs plus sign"""
    def __init__(self):
        super(C2H5OH2, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('H'), 
                strToSym('C'), strToSym('C'), strToSym('H'), 
                strToSym('H'), strToSym('O'), strToSym('H'),
                strToSym('H')]
        
        self.setData(pos=pos, adj=adj, pxMode=False, 
                     symbol=sym, antialias=True)
    
    def get_positions(self):
        return np.array([
                        [-1, 5],
                        [-2, 6],
                        [-1, 7],
                        [-1, 6],
                        [0, 6],
                        [0, 5],
                        [0, 7],
                        [1, 6],
                        [2, 6],
                        [1, 7],
                        ], dtype=float)
    
    def get_edges(self):
        return np.array([
                        [0, 3], 
                        [1, 3],
                        [2, 3],
                        [3, 4],
                        [5, 4], 
                        [6, 4], 
                        [4, 7], 
                        [7, 8],
                        [7, 9],
                        ])


class HSO4(Chemical):
    """Class for HSO4.

    Needs minus sign"""
    def __init__(self):
        super(HSO4, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('O'), strToSym('S'), strToSym('O'), 
               strToSym('O'), strToSym('O'), strToSym('H')]

        bonds = np.array([
                        's',
                        'd',
                        'd',
                        's',
                        's',
                        ])

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, bonds=bonds,
                     antialias=True)

    def get_positions(self):
        return np.array([ 
                        [1, 8.5],
                        [2, 9.5],
                        [1, 10.5],
                        [3, 10.5],
                        [3, 8.5],
                        [3, 7.5],
                        ], dtype=float)
    
    def get_edges(self):
        return np.array([
                        [0, 1],
                        [2, 1],
                        [3, 1],
                        [4, 1],
                        [5, 4],
                        ])                       


class C2H4(Chemical):
    """Class for C2H4.

    Needs a double bond"""
    def __init__(self):
        super(C2H4, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('C'), 
               strToSym('C'), strToSym('H'), strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False, 
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [6, 5],
                        [6, 7],
                        [7, 6],
                        [8, 6],
                        [9, 5],
                        [9, 7],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        [2, 3],
                        [4, 3],
                        [5, 3],
                        ])


class H2SO4f(Chemical):
    """Class for H2SO4f.

    How does this differ from H2SO4?"""
    def __init__(self):
        super(H2SO4f, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('O'), strToSym('S'), 
                strToSym('O'), strToSym('O'), strToSym('O'), 
                strToSym('H')]

        self.setData(pos=pos, adj=adj, pxMode=False, 
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [7, 7.5],
                        [7, 8.5],
                        [8, 9.5],
                        [7, 10.5],
                        [9, 10.5],
                        [9, 8.5],
                        [9, 7.5],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        [1, 2],
                        [3, 2],
                        [4, 2],
                        [5, 2],
                        [6, 5],
                        ])


class H2Of(Chemical):
    """Class for H2Of.

    How does this differ from H2O?"""
    def __init__(self):
        super(H2Of, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym('H'), strToSym('H'), strToSym('O')]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True, pen=pg.mkPen('w'))

    def get_positions(self):
        return np.array([
                        [10, 5],
                        [12, 6],
                        [11, 5],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        ])
