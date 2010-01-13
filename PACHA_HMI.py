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

class HMIapp(object):
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)

        self.grid = QtGui.QGridLayout()
        self.grid2 = QtGui.QGridLayout()
        for ligne in range(1,2):
            for colonne in range(1,3):
                self.grid.addWidget(QtGui.QPushButton(
                               "%d,%d"%(ligne,colonne)),
                               ligne, colonne)
        self.title = QtGui.QPushButton("Titre")

        QtCore.QObject.connect(
                               self.title, QtCore.SIGNAL('clicked()'),
                               self.extend)
        self.grid.addWidget(self.title, 0, 1, 1, 2)

        for ligne in range(1,4):
            for colonne in range(1,4):
                self.grid2.addWidget(QtGui.QPushButton(
                               "%d,%d"%(ligne,colonne)),
                               ligne, colonne)

        self.wr = QtGui.QWidget()
        self.wf = QtGui.QWidget()
        self.wr.setLayout(self.grid)
        self.wf.setLayout(self.grid2)

    def show(self):
        self.wr.show()

    def extend(self):
        self.wf.show()

	QtCore.QObject.disconnect(
                                  self.title, QtCore.SIGNAL('clicked()'),
                                  self.extend)

        QtCore.QObject.connect(
                               self.title, QtCore.SIGNAL('clicked()'),
                               self.reduce)


    def reduce(self):
        self.wf.hide()

	QtCore.QObject.disconnect(
                                  self.title, QtCore.SIGNAL('clicked()'),
                                  self.reduce)

        QtCore.QObject.connect(
                               self.title, QtCore.SIGNAL('clicked()'),
                               self.extend)


hmi = HMIapp()
hmi.show()
sys.exit(hmi.app.exec_())

