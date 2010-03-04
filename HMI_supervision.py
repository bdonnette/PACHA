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
import random as rnd

class Supervisor(object):
    ''' Global supervisor, to encompass df-like commands and true
    SNMP requests (the latter dependent on the SNMP object) '''
    def __init__(self, supervised_item = {}):
        ''' Input : dictionnary declaring :
        - Method (ssh / SNMP / local (test only))
        - True accessor (command / OID / function)
        - Remote
        - Config elements such as normal, warning, alert
        and error levels '''
        self.method = supervised_item["method"]
        self.accessor = supervised_item["command"]
        if (self.method == "SNMP"):
            print "Not implemented yet"

    def do_supervision(self):
        if (self.method == "SNMP"):
            print "Not implemented yet"

class HMI_supervision(HMI_line):
    ''' This class defines an HMI element (on which a line is to be based)
    so as to define a generic supervision HMI element object
    to be derived into whatever element will have to be'''
    def __init__(self, supervised_item = {}, hostname = "localhost"):
        ''' Adds the following to HMI_object class :
        - "Update" button
        '''
#        supervised_item["remote_machine"] = hostname

        HMI_line.__init__(self, hostname, 0)
        
        self.update_bt = QtGui.QPushButton("Actualiser")
        self.layout.addWidget(self.update_bt, 1, 3)
        self.item = supervised_item
        self.supervision = Supervisor(self.item)
        QtCore.QObject.connect(self.update_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.update,
                               QtCore.Qt.QueuedConnection)

    def update(self):
        ''' Updates the value '''
        if self.item :
            accession = self.item["command"]
            self.value = accession()
            self.pix.changeColor(self.value)

def get_value():
    ''' Test function only'''
    random_val = rnd.randint(0,2)
    return random_val

def test():
    ''' Proceeds the unit test '''
#not finished yet
    app = QtGui.QApplication(sys.argv)
    svc_item = {"method":"local", "command":get_value}
    sup = HMI_supervision(svc_item, "localhost")
    w2 = QtGui.QWidget()
    w2.setLayout(sup.layout)
    w2.setGeometry(0, 12, 480, 32)
    w2.show()
    sys.exit(app.exec_())
        
if (__name__ == "__main__"):
    # unit test
    test()
