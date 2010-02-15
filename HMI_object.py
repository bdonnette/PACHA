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

import sys
from PyQt4 import QtCore, QtGui

levels = {
    "unset":-1,
    "normal":0,
    "alert":1,
    "critical":2
    }

# Properly, these should be resources-like elements
pics = {
    "unset":"nolight.png",
    "normal":"greenlight.png",
    "alert":"orangeliht.png",
    "critical":"redlight.png"
    }

class HMI_icon(object):
    ''' Status-based icon, changes color with the value'''
    def __init__(self, parent = 0, value = "unset"):
        self.label = QtGui.QLabel(parent)
        self.label.setGeometry(QtCore.QRect(0, 0, 27, 27))
        self.level = value
        self.pixmaps = []
        for (index, name) in pics.iteritems():
            self.pixmaps[index] = QtGui.QPixmap(
                os.path.realpath(os.path.dirname(__file__)) +
                "/graphics/" + name)
        self.label.setPixmap(self.pixmap[value])

    def set_level(self, level = "normal"):
        self.level = level
        self.label.setPixmap(self.pixmap[self.level])
        
class HMI_object(object):
    ''' This class defines an HMI element (on which a line is to be based)
    so as to define a generic HMI element object
    to be derived into whatever element will have to be'''
    def __init__(self, label = "default"):
        ''' Gridded line to ease adaptability, with the following inside :
        - Colored icon for signalling,
        - Field name on a simple text box
        To be derived in classes embedding an additional widget
        '''
        self.grid = QtGui.QGridLayout()
        self.label = QtGui.QLabel(label)
        self.icon = HMI_icon(self.grid)
        # default placing
        self.grid.addWidget(self.icon.label, 1, 1)
        self.grid.addWidget(self.lable, 2, 1)
