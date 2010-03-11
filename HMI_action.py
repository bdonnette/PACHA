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
from HMI_ssh import *

class HMI_action(HMI_line):
    ''' This class defines an HMI element (on which a line is to be based)
    so as to define a generic active HMI element object
    to be derived into whatever element will have to be'''

    def __init__(self, agent, command, label,
                 feedback_command, feedback_line = None, dbg = None):
        ''' Init through an ssh agent instead of host and co
        passed by through the config file'''
        #first init inside
        self.agent = agent
        HMI_line.__init__(self, agent.host, 0)
        self.set_width(2)
        width = self.width
        self.command = command
        self.do_button = QtGui.QPushButton(label)
        self.layout.addWidget(self.do_button, 1, 2, 1, width*3)
        self.feedback_command = feedback_command % agent.host
        self.feedback_line = feedback_line
        self.dbg = dbg
        # next : bind action and button
        QtCore.QObject.connect(
            self.do_button,
            QtCore.SIGNAL('clicked()'),
            self.do_command)
  
    def do_command(self):
        ''' Does the command as issued '''
        rtn = self.agent.action(self.command)
        if (self.feedback_line != None):
            self.feedback_line.setPlainText(QtCore.QString(rtn))
        else:
            if (self.dbg):
                self.dbg.dprint("Feedback : %s" %rtn, 0)

    # Feedback : TBD (ssh / local ?)
    def feedback(self):
        pass

if (__name__ == "__main__"):
    # unit test
    app = QtGui.QApplication(sys.argv)
    action = HMI_action("localhost",
                        "test", "",
                        "echo toto", "echo",
                        "ping %s")
