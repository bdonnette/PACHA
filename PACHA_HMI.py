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

''' This module is the main HMI window of the PACHA project.
It invokes machine.py to parse config and builds its HMI elements.
'''

import sys
from PyQt4 import QtCore, QtGui
import HMI_Machine as HM
import machine as M
import ConfigParser
import debug_print as dp

class Hmi_app(object):
    ''' Main app class. Reads config via the machine object.
    ''' 
# New
    def __init__(self, config_file = "config.example.cfg", debug = 2):
        ''' App initialization throuh HMI usuals first
        Initialization of the HMI through config file then.'''
        # HMI initialization
        self.app = QtGui.QApplication(sys.argv)
        self.grid = QtGui.QGridLayout()
        self.main_widget = QtGui.QWidget()
        # Close event overloaded
        self.main_widget.closeEvent = self.quit_main
        # Config
        self.dbg = dp.debug_print(debug)
        self.all_machines = []
        self.machine_viewed = 0
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        i = 0
        
        while (True):
            i += 1
            try :
                label = config.get("Machines", "hostname%d" % i, 1)
            except (ConfigParser.NoOptionError, 
                    ConfigParser.NoSectionError) :
                break
            a_machine = M.Machine(config, label)
            a_hmi_machine = HM.HMI_Machine(i, label, self.dbg)
            a_hmi_machine.configure(a_machine)
            self.all_machines.append({"machine": a_machine,
                                      "HMI": a_hmi_machine})
            self.grid.addWidget(a_hmi_machine.synthex.Form,
                                0, i, 1, 1)
            QtCore.QObject.connect(a_hmi_machine.synthex.button,
                                   QtCore.SIGNAL("ToggleMachineView(int)"),
                                   self.toggle)
            QtCore.QObject.connect(a_hmi_machine.widget,
                                   QtCore.SIGNAL("CloseMachineView()"),
                                   self.quit_bt)
        self.main_widget.setLayout(self.grid)
        self.main_widget.setGeometry(0, 12, 640, 50)
        self.has_shown = False
        self.n_machines = i-1

    # After the creation, let's have a few true methods
    def show(self):
        ''' Widget show for the first time display '''
        self.main_widget.show()
        if (not self.has_shown):
            self.has_shown = True
            self.pos = self.main_widget.pos()
            self.hgt = self.main_widget.height()
            self.height = self.main_widget.frameGeometry().height()
            for i in range(0, self.n_machines):
                self.all_machines[i]["HMI"].move(
                    self.pos.x(), 
                    self.pos.y() + self.height + 24)
            self.pos_w = self.all_machines[0]["HMI"].pos()

    def toggle(self, numitem):
        ''' Intelligent display of 1 machine at a time
        '''
        if (self.machine_viewed) :
            pos = self.all_machines[self.machine_viewed - 1]["HMI"].hide()
            if (numitem == self.machine_viewed) :
                machine_viewed = 0
                self.pos_w = pos
            else :
                machine_viewed = numitem
                self.all_machines[machine_viewed - 1]["HMI"].show(pos)
        else:
            machine_viewed = numitem
            self.all_machines[machine_viewed - 1]["HMI"].show(self.pos_w)

        self.machine_viewed = machine_viewed

    def quit_main(self, event):
        ''' Overload the main QUIT event to make both quits effective'''
        if (self.machine_viewed):
            self.quit_bt()

    def quit_bt(self):
        ''' To overload the QUIT event so as to do the same as button
        re-press'''
        self.pos_w = self.all_machines[self.machine_viewed - 1]["HMI"].hide()
        self.machine_viewed = 0


#HMI = Hmi_app(3)
# to become :
HMI = Hmi_app(config_file = "config/default.cfg", debug = 0)
HMI.show()
sys.exit(HMI.app.exec_())

