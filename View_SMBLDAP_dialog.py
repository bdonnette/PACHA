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
import Ui_SMBLDAP_dialog

"""
"""
class View_SMBLDAP_dialog(Ui_SMBLDAP_dialog.Ui_SMBLDAP_dialog):

    """
    """
    def __init__(self, conf, machine):
        self.conf = conf
        self.machine = machine

        self.widget = QtGui.QWidget()
        self.setupUi(self.widget)
        self.setupView()


    """
    """
    def setupView(self):
        # Keep track of the memberUid on which we are working
        self.displayedUser = ""

        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), self.closeDialog)
        QtCore.QObject.connect(self.btnRefresh, QtCore.SIGNAL("clicked()"), self.refreshGroupsLists)
        QtCore.QObject.connect(self.btnAddUserToGroup, QtCore.SIGNAL("clicked()"), self.add_user_to_group)
        QtCore.QObject.connect(self.btnRemoveUserFromGroup, QtCore.SIGNAL("clicked()"), self.remove_user_from_group)

        self.refreshGroupsLists()


    """
    """
    def closeDialog(self):
        self.widget.close()


    """
    """
    def refreshGroupsLists(self):
        error, groups_of_user = self.machine.smbldap.getGroupsOfUser(self.displayedUser)

        if (error):
            QtGui.QMessageBox.critical(self.widget,
			                          'Erreur',
                                      "La machine %s a retourne l'erreur suivante :\n%s" % (self.machine.hostname, error))
        else:
            error, groups_available_for_user = self.machine.smbldap.getGroupsAvailableForUser(self.displayedUser)
            if (error):
                QtGui.QMessageBox.critical(self.widget,
    			                          'Erreur',
                                          "La machine %s a retourne l'erreur suivante :\n%s" % (self.machine.hostname, error))
            else:
                # TODO put \r in conf
                self.listGroupsOfUser.clear()
                for stri in groups_of_user.split('\r\n'):
                    self.listGroupsOfUser.addItem(stri)

                self.listGroupsAvailable.clear()
                for stri in groups_available_for_user:
                    self.listGroupsAvailable.addItem(stri)


    """
    """
    def add_user_to_group(self):
        group = ""
        if (len(self.listGroupsAvailable.selectedItems()) != 0):
            group = self.listGroupsAvailable.selectedItems()[0].text()

        if (group == ""):
            QtGui.QMessageBox.warning(self.widget,
                                      'Attention',
                                      "Merci de selectionner dans la liste de gauche, le groupe auquel ajouter l'utilisateur '%s'." % self.displayedUser)
        else:
            error, cmd_res = self.machine.smbldap.add_user_to_group(self.displayedUser, group)

            if (error):
                QtGui.QMessageBox.critical(self.widget,
                                           'Erreur',
                                           "La machine %s a retourne l'erreur suivante :\n%s" % (self.machine.hostname, cmd_res))
            else:
                QtGui.QMessageBox.information(self.widget,
                                              'Information',
                                              "L'utilisateur '%s' a ete ajoute au groupe '%s'." % (self.displayedUser, group))

            self.refreshGroupsLists()


    """
    """
    def remove_user_from_group(self):
        group = ""
        if (len(self.listGroupsOfUser.selectedItems()) != 0):
            group = self.listGroupsOfUser.selectedItems()[0].text()

        if (group == ""):
            QtGui.QMessageBox.warning(self.widget,
                                      'Attention',
                                      "Merci de selectionner dans la liste de droite, le groupe dont vous souhaitez supprimer l'utilisateur '%s'." % self.displayedUser)
        else:
            error, cmd_res = self.machine.smbldap.remove_user_from_group(self.displayedUser, group)

            if (error):
                QtGui.QMessageBox.critical(self.widget,
                                           'Erreur',
                                           "La machine %s a retourne l'erreur suivante :\n%s" % (self.machine.hostname, cmd_res))
            else:
                QtGui.QMessageBox.information(self.widget,
                                              'Information',
                                              "L'utilisateur '%s' a ete supprime du groupe '%s'." % (self.displayedUser, group))

            self.refreshGroupsLists()


    """
    """
    def show(self, memberUid):
        self.displayedUser = memberUid
        self.refreshGroupsLists()
        self.widget.show()


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
