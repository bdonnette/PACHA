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
import HMI_Machine as HM

class HMIapp(object):
    def __init__(self, n_machines = 2):
        # Global app init
        self.app = QtGui.QApplication(sys.argv)

        self.grid = QtGui.QGridLayout()
        self.gridlist = []

        # Machines HMI elements
        self.Machines = []
        self.machine_viewed = 0

        for i in range(0, n_machines):
            # read config of machine...
            
            self.Machines.append(HM.HMI_Machine(i+1))
            self.Machines[i].config()
            # Remainder : colored widget to be changed upon signal/slot
            self.grid.addWidget(self.Machines[i].synthex.button,
                                0, i, 1, 1)
            QtCore.QObject.connect(self.Machines[i].synthex.button,
                                   QtCore.SIGNAL("ToggleMachineView(int)"),
                                   self.toggle)


        self.wr = QtGui.QWidget()
        self.wr.setLayout(self.grid)

    def show(self):
        self.wr.show()

    def toggle(self, numitem):
        ''' Intelligent display of 1 machine at a time
        '''
        if (self.machine_viewed) :
            self.Machines[self.machine_viewed - 1].hide()
            if (numitem == self.machine_viewed) :
                machine_viewed = 0
            else :
                machine_viewed = numitem
                self.Machines[machine_viewed - 1].show()

        else:
            machine_viewed = numitem
            self.Machines[machine_viewed - 1].show()

        self.machine_viewed = machine_viewed

hmi = HMIapp()
hmi.show()
sys.exit(hmi.app.exec_())

