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

# Signal relay + widget


class MyButton(object):
    def __init__(self, text = "", value = 0):
        self.button = QtGui.QPushButton(text)
        self.value = value
        QtCore.QObject.connect(
            self.button,
            QtCore.SIGNAL('clicked()'),
            self.send)

    def send(self):
        self.button.emit(QtCore.SIGNAL("ToggleMachineView(int)"), self.value)


class HMI_Machine(object):
    ''' Class to embark Widgets related to a single machine, making the final
        outlook and code easy.
        The HMI element shows machine # number, has a grid widget,
        and a synthex, to be displayed on the general widget
        '''
    def __init__(self, number = 1):
        self.number  = number
        self.grid    = QtGui.QGridLayout()
        self.synthex = MyButton("  Machine %d" % (number), number)

    def config(self):
        self.widgets = {}
        self.dkey = "i%dj%d"

        # Fake config
        for i in range(1,4):
            for j in range (1,3):
                akey = self.dkey % (i,j)
                self.widgets[akey] = QtGui.QPushButton(
                                       "M %d Param %d, %d" % (self.number, i, j))
                self.grid.addWidget(self.widgets[akey], i, j, 1, 1)

        self.widget = QtGui.QWidget()
        self.widget.setLayout(self.grid)

    def show(self):
        self.widget.show()

    def hide(self):
        self.widget.hide()
