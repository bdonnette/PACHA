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
import os

""" GUI for Pacha's Action
"""
class View_Action(object):


    """ Ask internal business object to perform action
    """
    def issue_action(self):
        error, stdout = self.action.issue()
        self.viewActionsSupervisions.displayResult(os.linesep.join(stdout))
        if (error):
            QtGui.QMessageBox.critical(self.pushButton,
    			                          'Erreur',
                                          "La commande s'est terminee avec l'erreur %i : %s%s" % (error, os.linesep, os.linesep.join(stdout)))


    """ Initial method to set dynamic elements up
    """
    def setupView(self):
        self.pushButton.setText(self.action.label)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.issue_action)

            
    """ Init method
            action                  : internal business object this view is bound to
            viewActionsSupervisions : the GUI panel this object belongs to
    """
    def __init__(self, action, viewActionsSupervisions):
        self.action = action
        self.viewActionsSupervisions = viewActionsSupervisions

        self.pushButton = QtGui.QPushButton()
        self.setupView()

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
