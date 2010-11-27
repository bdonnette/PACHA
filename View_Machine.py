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

from PyQt4 import QtCore, QtGui
import Ui_Machine, View_ActionsSupervisions, View_SMBLDAP
import sys


class View_Machine(Ui_Machine.Ui_Machine):

    def __init__(self, conf, machine, view_MainWindow, treeItem):
        self.conf = conf
        self.machine = machine

        self.view_MainWindow = view_MainWindow
        # The TreeItem representing this machine in the TreeView
        self.treeItem = treeItem
        self.widgetMachine = QtGui.QWidget()
        self.setupUi(self.widgetMachine)
        self.setupView()


    def setupView(self):
        self.view_ActionsSupervisions = View_ActionsSupervisions.View_ActionsSupervisions(self.conf, self.machine, self)

        self.toolBox.addItem(self.view_ActionsSupervisions.widgetActionsSupervisions, "Supervisions/Actions")

        if (self.machine.smbldap != None):
            self.view_SMBLDAP = View_SMBLDAP.View_SMBLDAP(self.conf, self.machine)
            self.toolBox.addItem(self.view_SMBLDAP.widgetSMBLDAP, "SMB/LDAP")

        self.reflectStates()


    def reflectStates(self):
        self.view_ActionsSupervisions.reflectStates()
        self.treeItem.setIcon(0, self.conf.val["general"]["icon_levels"][self.machine.state])
        self.machine.group.view.reflectStates()


    def show(self):
        self.widgetMachine.show()


    def hide(self):
        self.widgetMachine.hide()
            

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
