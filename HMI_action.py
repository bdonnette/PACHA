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
    def __init__(self,
                 remote_machine = "localhost",
                 user = "root", password = "",
                 do_label = "do", command = "echo toto",
                 feedback_command = "ping %s"):
        ''' Additions from HMI_line :
        - "Do it" button
        - Corresponding action as a shell command
        '''
        HMI_line.__init__(self, remote_machine, 0)
        self.set_width(4)
        width = self.width
        self.remote_machine = remote_machine
        self.user = user
        self.password = password
        self.command = command
        self.do_button = QtGui.QPushButton(do_label)
        self.layout.addWidget(self.do_button, 1, 2, 1, width*3)
        self.feedback_command = feedback_command % remote_machine

        # next : bind action and button
        QtCore.QObject.connect(
            self.do_button,
            QtCore.SIGNAL('clicked()'),
            self.do_command)

    def do_command(self):
        ssh = ssh_agent(self.remote_machine,
                        self.user,
                        self.password)
        ssh.action(self.command)

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
