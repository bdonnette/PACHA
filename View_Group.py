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

""" GUI for Pacha's Group
"""
class View_Group(object):


    """ Update GUI regarding internal Group's state
    """
    def reflectStates(self):
        self.treeItem.setIcon(0, self.conf.val["general"]["icon_levels"][self.group.state])


    """ Init method
            conf    : Pacha global conf
            group   : the group this GUI is bound to
    """
    def __init__(self, conf, group):
        self.conf = conf
        self.group = group

        self.treeItem = QtGui.QTreeWidgetItem()
        self.treeItem.setText(0, self.group.name)

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
