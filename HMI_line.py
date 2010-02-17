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
import PACHA_pixmap as pp

# Devra probablement contenir un widget ou plus...

class HMI_line(object):
    ''' Interaction item, recorded as a "line". Displays one specific
    information. Can be thought of as something to take place in
    one line in the interaction grid.'''

    def __init__(self, text = "line", value = 0):
        self.value = value
        self.Form = QtGui.QWidget()
        self.Form.setObjectName(text)
        self.label = QtGui.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 27, 27))

        
