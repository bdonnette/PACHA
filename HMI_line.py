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
        ''' This being an abstract class, not much to say
        apart from it has a widget including 2 widgets.
        Suitable for derivation and not for direct usage.'''
        self.value = value
        self.wForm = QtGui.QWidget()
        #self.Form.setObjectName(text)
        self.layout = QtGui.QGridLayout(self.wForm)
        #self.line.setObjectName(text)
        self.widget1 = QtGui.QWidget(self.wForm)
        self.pix = pp.p_pixmap(self.widget1)
        self.layout.addWidget(self.pix.label, 1, 1)
        self.pix.changeColor(value)
        self.width = 3

    def set_width(self, width):
        if (0 < width):
            self.width = width
        else:
            self.width = 3

def test():
    ''' Proceeds the unit test'''
    app = QtGui.QApplication(sys.argv)
    line = HMI_line("Ligne", 0)
    w2 = QtGui.QWidget(line.wForm)
    button = QtGui.QPushButton("HMI_Line test", w2)
    line.layout.addWidget(w2, 1, 2, 1, 3)
    line.wForm.adjustSize()
    geo = line.wForm.geometry()
    geo.setWidth(220)
    geo.setHeight(50)
    line.wForm.setGeometry(geo)

    line.wForm.show()
    sys.exit(app.exec_())

if (__name__ == "__main__"):
    # unit test
    test()
