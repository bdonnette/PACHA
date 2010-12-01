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
import Ui_ActionsSupervisions, View_Action, View_Supervision, View_Service
import sys

""" GUI for Pacha's Action and Supervision panel
"""
class View_ActionsSupervisions(Ui_ActionsSupervisions.Ui_ActionsSupervisions):

    """ Update GUI regarding internal Actions and Supervisions' states
    """
    def reflectStates(self):
        for viewSupervision in self.viewSupervisions:
            viewSupervision.reflectState()

        for viewService in self.viewServices:
            viewService.reflectState()


    """ Populate Edit
            text    : output to populate Edit with
    """
    def displayResult(self, text):
        self.resultEdit.setPlainText(text)


    """ Initial method to set dynamic elements up
    """
    def setupView(self):
        # Supervisions
        self.viewSupervisions = []
        for supervision in self.machine.supervisions:
            viewSupervision = View_Supervision.View_Supervision(self.conf,
                                                                supervision,
                                                                self)
            self.listWidget.addItem(viewSupervision.widget)
            self.viewSupervisions.append(viewSupervision)
        
        # Actions
        self.viewActions = []
        for action in self.machine.actions:
            viewAction = View_Action.View_Action(action, self)
            self.buttonsLayout.addWidget(viewAction.pushButton)
            self.viewActions.append(viewAction)

        # Services
        self.viewServices = []
        for service in self.machine.services:
            viewService = View_Service.View_Service(self.conf, service)
            self.buttonsLayout.addWidget(viewService.widget)
            self.viewServices.append(viewService)


    """ Init method
            conf            : Pacha global conf
            machine         : internal business object this view is bound to
            view_machine    : the widget this object belongs to
    """
    def __init__(self, conf, machine, view_machine):
        self.conf = conf
        self.machine = machine
        self.view_machine = view_machine

        self.widgetActionsSupervisions = QtGui.QWidget()
        self.setupUi(self.widgetActionsSupervisions)
        self.setupView()

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
