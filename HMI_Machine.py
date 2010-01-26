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
import sys
from PyQt4 import QtCore, QtGui

# Signal relay + widget


class MyButton(object):
    def __init__(self, text = "", value = 0):
        self.value = value
        self.Form = QtGui.QWidget()
        self.Form.setObjectName("Form")
        self.Form.resize(180, 36)
        self.button = QtGui.QPushButton(text, self.Form)
        self.button.setGeometry(QtCore.QRect(40, 0, 148, 28))
        self.label = QtGui.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 27, 27))
        self.num = -1

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

        QtCore.QMetaObject.connectSlotsByName(self.Form)

        QtCore.QObject.connect(
            self.button,
            QtCore.SIGNAL('clicked()'),
            self.send)

    def send(self):
        self.button.emit(QtCore.SIGNAL("ToggleMachineView(int)"), self.value)
 
       # test code for colors
        self.num += 1
        if (3 < self.num):
                self.num = 0
        self.changeColor(self.num)
        # end test code

    def changeColor(self, num):
        if (2 < num or num < 0):
            num = 3

        self.num = num
        self.label.setPixmap(self.pixmaps[num])

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
                                       "M %d Param %d, %d" % 
                                       (self.number, i, j))
                self.grid.addWidget(self.widgets[akey], i, j, 1, 1)

        # True config to be made of HMI_line's
        self.widget = QtGui.QWidget()
        self.widget.setLayout(self.grid)

    def move(self, x, y):
        self.widget.move(x, y+28)

    def show(self):
        self.widget.show()

    def hide(self):
        self.widget.hide()
