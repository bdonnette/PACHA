# encoding : utf-8
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 or later of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#

import os, sys
from PyQt4 import QtCore, QtGui

class p_pixmap(object):
    ''' Encapsulates black, green, orange and red lights
    and adequate update methods'''

    def __init__(self, form):
        self.label = QtGui.QLabel(form)
        self.label.setGeometry(QtCore.QRect(0, 0, 27, 27))
        self.num = 0

        self.pixmaps = []
        pixnames = ['greenlight.png',
                    'orangelight.png',
                    'redlight.png',
                    'nolight.png']
        for name in pixnames:
            self.pixmaps.append(QtGui.QPixmap(
                    os.path.realpath(os.path.dirname(__file__)) +
                    "/graphics/" + name))
        self.label.setPixmap(self.pixmaps[3])


    def changeColor(self, num):
        ''' Changes the color of the icon 
        0 : non reachable / arg problem
        1 : normal
        2 : warning
        3 : Alert '''
        if (3 < num or num < 0):
            num = 3

        self.num = num
        self.label.setPixmap(self.pixmaps[num])

if (__name__ == "__main__"):
    # unit test
    app = QtGui.QApplication(sys.argv)
    wid = QtGui.QWidget()
    line = QtGui.QGridLayout(wid)
    w1 = QtGui.QWidget(wid)
    w2 = QtGui.QWidget(wid)
    pix = p_pixmap(w1)
    pix.changeColor(2)
    button = QtGui.QPushButton("bouton", w2)

    line.addWidget(w1, 1, 1)
    line.addWidget(w2, 1, 2, 1, 3)

    wid.show()
    sys.exit(app.exec_())