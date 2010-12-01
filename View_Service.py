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
import Ui_Service

""" GUI for Pacha's Service
"""
class View_Service(Ui_Service.Ui_Service):


    """ Ask business object to start the remote daemon
    """
    def issue_start(self):
        error, stdout = self.service.start()

        if (error):
            QtGui.QMessageBox.critical(self.widgetService,
    			                          'Error',
                                          "La machine a retourne le message suivant : %s" % stdout)
        else:
            message = "La commande de demarrage a ete executee"
            if (stdout != ""):
                message += os.linesep + "et a retourne le message suivant :" + os.linesep + os.linesep.join(stdout)

            QtGui.QMessageBox.information(self.widgetService,
    			                          'Information',
                                          message)


    """ Ask business object to restart the remote daemon
    """
    def issue_restart(self):
        error, stdout = self.service.restart()

        if (error):
            QtGui.QMessageBox.critical(self.widgetService,
    			                          'Error',
                                          "La machine a retourne le message suivant : %s" % os.linesep.join(stdout))
        else:
            message = "La commande de redemarrage a ete executee"
            if (stdout != ""):
                message += os.linesep + "et a retourne le message suivant :" + os.linesep + os.linesep.join(stdout)

            QtGui.QMessageBox.information(self.widgetService,
    			                          'Information',
                                          message)


    """ Update GUI regarding internal Service's state
    """
    def reflectState(self):
        self.buttonIcon.setIcon(self.conf.val["general"]["icon_levels"][self.service.status])


    """ Initial method to set dynamic elements up
    """
    def setupView(self):
        self.labelText.setText(self.service.label)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL("clicked()"), self.issue_start)
        QtCore.QObject.connect(self.restartButton, QtCore.SIGNAL("clicked()"), self.issue_restart)


    """ Init method
            conf            : Pacha global conf
            service         : internal business object this view is bound to
    """
    def __init__(self, conf, service):
        self.conf = conf
        self.service = service
        self.widgetService = QtGui.QWidget()
        self.setupUi(self.widgetService)
        self.setupView()

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
