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
import Ui_SMBLDAP, View_SMBLDAP_dialog

"""
"""
class View_SMBLDAP(Ui_SMBLDAP.Ui_SMBLDAP):

    """
    """
    def __init__(self, conf, machine):
        self.conf = conf
        self.machine = machine

        self.widgetSMBLDAP = QtGui.QWidget()
        self.setupUi(self.widgetSMBLDAP)
        self.setupView()


    """
    """
    def setupView(self):
        QtCore.QObject.connect(self.btnUserAdd, QtCore.SIGNAL("clicked()"), self.addUser)
        QtCore.QObject.connect(self.btnUserDel, QtCore.SIGNAL("clicked()"), self.delUser)
        QtCore.QObject.connect(self.btnUsersRefresh, QtCore.SIGNAL("clicked()"), self.refreshUsersList)
        QtCore.QObject.connect(self.btnGroupAdd, QtCore.SIGNAL("clicked()"), self.addGroup)
        QtCore.QObject.connect(self.btnGroupDel, QtCore.SIGNAL("clicked()"), self.delGroup)
        QtCore.QObject.connect(self.btnGroupsRefresh, QtCore.SIGNAL("clicked()"), self.refreshGroupsList)

        QtCore.QObject.connect(self.listUsers, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.show_dialog)

        # Populate SMBLDAP lists
        self.refreshUsersList()
        self.refreshGroupsList()


    """
    """
    def show_dialog(self, item):
        self.SMBLDAP_dialog = View_SMBLDAP_dialog.View_SMBLDAP_dialog(self.conf, self.machine)
        self.SMBLDAP_dialog.show(item.text())


    """
    """
    def addUser(self):
        newUserName = self.editUser.text()
        if (newUserName == ""):
            # TODO Add a "new username" validation
            QtGui.QMessageBox.warning(self.widgetSMBLDAP,
			                          'Attention',
                                      "Merci de renseigner le champ 'Utilisateur'")
        else:
            error, cmd_res = self.machine.smbldap.userAdd(newUserName)
            if (error):
                # TODO Handle internationalization
                QtGui.QMessageBox.critical(self.widgetSMBLDAP,
    			                          'Erreur',
                                          "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
            else:
                QtGui.QMessageBox.information(self.widgetSMBLDAP,
    			                          'Information',
                                          "Utilisateur '%s' ajoute" % newUserName)

                self.editUser.clear()
                self.refreshUsersList()


    """
    """
    def delUser(self):
        userNameToDel = ""
        if (len(self.listUsers.selectedItems()) != 0):
            userNameToDel = self.listUsers.selectedItems()[0].text()

        if (userNameToDel == ""):
            QtGui.QMessageBox.warning(self.widgetSMBLDAP,
                                      'Attention',
                                      "Merci de selectionner l'utilisateur a supprimer dans la liste.")
        else:
            error, cmd_res = self.machine.smbldap.userDel(userNameToDel)
            if (error):
                QtGui.QMessageBox.critical(self.widgetSMBLDAP,
                                           'Erreur',
                                           "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
            else:
                QtGui.QMessageBox.information(self.widgetSMBLDAP,
        		                              'Information',
                                              "Utilisateur '%s' supprime" % userNameToDel)

            self.refreshUsersList()


    """
    """
    def refreshUsersList(self):
        error, cmd_res = self.machine.smbldap.usersLs()
        if (error):
            QtGui.QMessageBox.critical(self.widgetSMBLDAP,
			                          'Erreur',
                                      "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
        else:
            # TODO put \r in conf
            self.listUsers.clear()
            for stri in cmd_res:
                self.listUsers.addItem(QtCore.QString(stri))


    """
    """
    def addGroup(self):
        newGroupName = self.editGroup.text()
        if (newGroupName == ""):
            # TODO Add a "newGroupName" validation
            QtGui.QMessageBox.warning(self.widgetSMBLDAP,
			                          'Attention',
                                      "Merci de renseigner le champ 'Groupe'")
        else:
            error, cmd_res = self.machine.smbldap.groupAdd(newGroupName)
            if (error):
                QtGui.QMessageBox.critical(self.widgetSMBLDAP,
    			                          'Erreur',
                                          "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
            else:
                QtGui.QMessageBox.information(self.widgetSMBLDAP,
    			                          'Information',
                                          "Groupe '%s' ajoute" % newGroupName)

                self.editGroup.clear()
                self.refreshGroupsList()


    """
    """
    def delGroup(self):
        groupNameToDel = ""
        if (len(self.listGroups.selectedItems()) != 0):
            groupNameToDel = self.listGroups.selectedItems()[0].text()

        if (groupNameToDel == ""):
            QtGui.QMessageBox.warning(self.widgetSMBLDAP,
                                      'Attention',
                                      "Merci de selectionner le groupe a supprimer dans la liste.")
        else:
            error, cmd_res = self.machine.smbldap.groupDel(groupNameToDel)
            if (error):
                QtGui.QMessageBox.critical(self.widgetSMBLDAP,
                                           'Erreur',
                                           "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
            else:
                QtGui.QMessageBox.information(self.widgetSMBLDAP,
                                              'Information',
                                              "Groupe '%s' supprime" % groupNameToDel)

            self.refreshGroupsList()


    """
    """
    def refreshGroupsList(self):
        error, cmd_res = self.machine.smbldap.groupsLs()
        if (error):
            QtGui.QMessageBox.critical(self.widgetSMBLDAP,
			                          'Attention',
                                      "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
        else:
            self.listGroups.clear()
            # TODO put \r in conf
            for stri in cmd_res:
                self.listGroups.addItem(stri)

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
