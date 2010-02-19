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
import HMI_dictate as hd
import PACHA_pixmap as pp
from HMI_action import *
from HMI_service import *
# Signal relay + widget


class MyButton(object):
    def __init__(self, text = "", value = 0):
        self.value = value
        self.Form = QtGui.QWidget()
        self.Form.setObjectName("Form")
        self.Form.resize(180, 32)
        self.button = QtGui.QPushButton(text, self.Form)
        self.button.setGeometry(QtCore.QRect(40, 0, 148, 28))

        self.pix = pp.p_pixmap(self.Form)

        QtCore.QMetaObject.connectSlotsByName(self.Form)

        QtCore.QObject.connect(
            self.button,
            QtCore.SIGNAL('clicked()'),
            self.send)

    def send(self):
        self.button.emit(QtCore.SIGNAL("ToggleMachineView(int)"), self.value)
        # test code for colors
        self.change_level(42, [0, 33, 66, 100])

    def change_level(self, level, scale = []):
        ''' Relays the signal, and is to scale if necessary 
        Substracts one for the first element is 0, not 1'''
        def test_level(x):
            return (x < level)

        if len(scale) != 4:
            if (level < 0 or 2 < level):
                level = 3
        else:
            level = len(filter(test_level, scale))
            if (2 < level):
                level = 3
        self.pix.changeColor(level-1)


class HMI_Machine(object):
    ''' Class to embark Widgets related to a single machine, making the
    final outlook and code easy.
    The HMI element shows machine # number, has a grid widget,
    and a synthex, to be displayed on the general widget
    '''
    def __init__(self, number = 1):
        self.number  = number
        self.grid    = QtGui.QGridLayout()
        self.synthex = MyButton("  Machine %d" % (number), number)

    def config(self):
        self.widgets = {}

        dkey = "machine %s : %s"
        # Fake config
        # dkey = "i%dj%d"
        # for i in range(1,4):
        #     for j in range (1,5):
        #         akey = dkey % (i,j)
        #         self.widgets[akey] = QtGui.QPushButton(
        #                                "M %d Param %d, %d" % 
        #                                (self.number, i, j))
        #         self.grid.addWidget(self.widgets[akey], i, j, 1, 1)

        host = "192.168.122.14"
        user = "root"
        password = "toto"
        command = "reboot"
        akey = dkey % (host, command)
        label = "Action : %s" % command
        self.widgets[akey] = HMI_action(host, user, password,
                                        command = "reboot",
                                        do_label = label,
                                        feedback_command = "ping %s")
        self.grid.addWidget(self.widgets[akey].wForm, 1, 1, 1, 4)

        i = 2
        # service line
        # service = "ntp"
        for service in ["ntp", "Apache", "ssh"]:
            bkey = "service %s" % service
            self.widgets[bkey] = HMI_service(host, service)

            self.grid.addWidget(self.widgets[bkey].wForm, i, 1, 1, 5)
            self.dictate = hd.HMI_dictate(host, user, password)
            self.grid.addWidget(self.dictate.Form, 1, 6, 20, 4)
            i +=1
            # self.RefreshWidget = QtGui.QPushButton("Refresh")
            # self.grid.addWidget(self.RefreshWidget, 25, 1, 1, 4)
            # True config to be made of HMI_line's
        self.widget = QtGui.QWidget()
        self.widget.setGeometry(0, 28, 490, 456)
        self.widget.setLayout(self.grid)

    def move(self, x, y):
        self.widget.move(x, y+28)

    def show(self):
        self.widget.show()

    def hide(self):
        self.widget.hide()
