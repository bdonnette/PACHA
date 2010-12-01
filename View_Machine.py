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

""" GUI for Pacha's Machine
"""
class View_Machine(Ui_Machine.Ui_Machine):

    """ Update GUI regarding internal Machine's state
    """
    def reflectStates(self):
        self.view_ActionsSupervisions.reflectStates()
        self.treeItem.setIcon(0, self.conf.val["general"]["icon_levels"][self.machine.state])
        self.machine.group.view.reflectStates()


    """ Show this widget
    """
    def show(self):
        self.widgetMachine.show()


    """ Hide this widget
    """
    def hide(self):
        self.widgetMachine.hide()


    """ Initial method to set dynamic elements up
    """
    def setupView(self):
        self.view_ActionsSupervisions = View_ActionsSupervisions.View_ActionsSupervisions(self.conf, self.machine, self)

        self.toolBox.addItem(self.view_ActionsSupervisions.widgetActionsSupervisions, "Supervisions/Actions")

        if (self.machine.smbldap != None):
            self.view_SMBLDAP = View_SMBLDAP.View_SMBLDAP(self.conf, self.machine)
            self.toolBox.addItem(self.view_SMBLDAP.widgetSMBLDAP, "SMB/LDAP")

        self.reflectStates()


    """ Init method
            conf            : Pacha global conf
            machine         : the machine this GUI is bound to
            view_MainWindow : Pacha's main window
            treeItem        : the group this GUI is bound to
    """
    def __init__(self, conf, machine, view_MainWindow, treeItem):
        self.conf = conf
        self.machine = machine

        self.view_MainWindow = view_MainWindow
        # The TreeItem representing this machine in the TreeView
        self.treeItem = treeItem
        self.widgetMachine = QtGui.QWidget()
        self.setupUi(self.widgetMachine)
        self.setupView()

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
