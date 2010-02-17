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
import HMI_ssh as ssh

class HMI_dictate(object):
    ''' This class defines an HMI element to host command line typing
    and feedback, for ssh commands issued upon sysadmins call '''
    def __init__(self, 
                 host,
                 user, password = ""):
        ''' HMI elemens in place here :
        - "shell" text input line
        - text feedback
        '''
        self.Form = QtGui.QWidget()
        self.Form.resize(480, 300)
        font = QtGui.QFont()

        self.input = QtGui.QLineEdit(self.Form)
        self.input.setGeometry(QtCore.QRect(0, 272, 480, 24))
        self.input.setObjectName("Input")
        self.input.setReadOnly(False)
        self.input.setFont(font)
        self.input.setAlignment(QtCore.Qt.AlignLeft)
        self.input.setEchoMode(0)
        self.input.setMaxLength(80)

        self.feedback = QtGui.QTextEdit(self.Form)
        self.feedback.setGeometry(QtCore.QRect(0, 0, 480, 270))
        self.feedback.setReadOnly(True)
        self.feedback.setObjectName("Feedback")
        self.agent = ssh.ssh_agent(host, user, password)

        QtCore.QMetaObject.connectSlotsByName(self.Form)
        QtCore.QObject.connect(
            self.input,
            QtCore.SIGNAL('returnPressed()'),
            self.do_input)

    def do_input(self):
        command = self.input.text()
        self.output = QtCore.QString(self.agent.action(command))
        self.feedback.setPlainText(self.output)
        self.input.setText("")
                 

if (__name__ == "__main__"):
    # test
    app = QtGui.QApplication(sys.argv)
    hd = HMI_dictate("192.168.122.14", "root", "toto")
    hd.Form.show()
    sys.exit(app.exec_())
