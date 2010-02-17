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
        #self.Form.setObjectName(text)
        self.layout = QtGui.QGridLayout(self.Form)
        #self.line.setObjectName(text)
        self.widget1 = QtGui.QWidget(self.Form)
        self.pix = pp.p_pixmap(self.widget1)
        self.layout.addWidget(self.widget1, 1, 1, 1, 4)
        self.pix.changeColor(value)

        
if (__name__ == "__main__"):
    # unit test
    app = QtGui.QApplication(sys.argv)
    line = HMI_line("Ligne", 0)
    w2 = QtGui.QWidget(line.Form)
    button = QtGui.QPushButton("HMI_Line test", w2)
    line.layout.addWidget(w2, 1, 2, 1, 3)
    line.Form.adjustSize()
    geo = line.Form.geometry()
    geo.setWidth(220)
    geo.setHeight(50)
    line.Form.setGeometry(geo)

    line.Form.show()
    sys.exit(app.exec_())
