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

"""
"""
class View_Supervision(object):

    """
    """
    def __init__(self, conf, supervision, viewActionsSupervisions):
        self.conf = conf
        self.supervision = supervision
        self.viewActionsSupervisions = viewActionsSupervisions

        self.widget = QtGui.QListWidgetItem()
        self.setupView()


    """
    """
    def setupView(self):
        self.widget.setText(self.supervision.label)
        if (self.supervision.vital):
            font = QtGui.QFont()
            font.setBold(True)
            self.widget.setFont(font)
#        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.issue_action)

    def reflectState(self):
        self.widget.setIcon(self.conf.val["general"]["icon_levels"][self.supervision.state])

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
