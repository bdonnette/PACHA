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

import os
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
