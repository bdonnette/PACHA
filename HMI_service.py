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

services = {
    "Apache"	: "httpd",
    "ssh"	: "sshd",
    "ntp"	: "ntpd"
}

class HMI_service(HMI_line):
    ''' This class aims at facilitating the interaction with services
    so as to show start, stop and restart service buttons
    which act accordingly, using rc scripts.'''
    def __init__(self,
                 remote_machine = "localhost",
                 service = "ntp"):
        ''' Additions from HMI_action :
        - Buttons : start, stop, restart
        - Corresponding action as a shell command
        '''
        HMI_line.__init__(self, remote_machine, 0)

        self.remote_machine = remote_machine
        self.user = "root"
        self.password = "toto"
        self.base = "/etc/rc.d/init.d/" + services[service]
        label_base = services[service]
        self.start_button = QtGui.QPushButton(service + " start")
        self.stop_button = QtGui.QPushButton(service + " stop")
        self.restart_button = QtGui.QPushButton(service + " restart")
        self.layout.addWidget(self.start_button, 1, 3, 1, 1)
        self.layout.addWidget(self.stop_button, 1, 4, 1, 1)
        self.layout.addWidget(self.restart_button, 1, 5, 1, 1)
        # geo = self.wForm.geometry()
        # geo.setWidth(450)
        # geo.setHeight(50)
        # self.wForm.setGeometry(geo)
        
        # next : bind action and button
        QtCore.QObject.connect(
            self.start_button,
            QtCore.SIGNAL('clicked()'),
            self.start_command)
        
        QtCore.QObject.connect(
            self.stop_button,
            QtCore.SIGNAL('clicked()'),
            self.stop_command)
        
        QtCore.QObject.connect(
            self.restart_button,
            QtCore.SIGNAL('clicked()'),
            self.restart_command)

    def do_command(self, action):
        if action in ["start", "stop", "restart"]:
            command = self.base + " %s" % action
            # ssh = ssh_agent(self.remote_machine,
            #                 self.user,
            #                 self.password)
            # ssh.action(command)
            print ("Command : %s") % command

    def start_command(self):
        self.do_command("start")

    def stop_command(self):
        self.do_command("stop")

    def restart_command(self):
        self.do_command("restart")

if (__name__ == "__main__"):
    # unit test
    app = QtGui.QApplication(sys.argv)
    service = HMI_service("192.168.122.14",
                        "ntp")
    service.wForm.show()
    sys.exit(app.exec_())
