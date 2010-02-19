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
from HMI_line import *

class Supervisor(object):
    ''' Global supervisor, to encompass df-like commands and true
    SNMP requests (the latter dependent on the SNMP object) '''
    def __init__(self, supervised_item = {}):
        ''' Input : dictionnary declaring :
        - Method (ssh / SNMP)
        - True accessor (command / OID)
        - Remote
        - Config elements such as normal, warning, alert
        and error levels '''
        method = supervised_item["method"]
        accessor = supervised_item["accessor"]

class HMI_supervision(HMI_line):
    ''' This class defines an HMI element (on which a line is to be based)
    so as to define a generic supervision HMI element object
    to be derived into whatever element will have to be'''
    def __init__(self, supervised_item = {}):
        ''' Adds the following to HMI_object class :
        - "Update" button
        '''
        HMI_line.__init__(self, supervised_item["remote_machine"], 0)
        
        self.update_bt = QtGui.QPushButton("Actualiser")
        self.grid.addWidget(self.update_bt, 1, 3)
        self.item = supervised_item
        self.supervision = Supervisor(self.item)
        QtCore.QObject.connect(self.update_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.update,
                               Qt.QueuedConnection)

    def update(self):
        ''' Updates the value '''
        if self.item :
            self.value = self.item.get_value()

        
