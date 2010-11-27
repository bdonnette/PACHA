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
import Ui_SMBLDAP

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
                                          "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, cmd_res))
            else:
                QtGui.QMessageBox.information(self.widgetSMBLDAP,
    			                          'Information',
                                          "Utilisateur '%s' ajoute" % newUserName)

                self.editUser.clear()
                self.refreshUsersList()


    """
    """
    def delUser(self):
        if (len(self.listUsers.selectedItems()) != 0):
            userNameToDel = self.listUsers.selectedItems()[0].text()
            if (userNameToDel == ""):
                QtGui.QMessageBox.warning(self.widgetSMBLDAP,
    			                          'Attention',
                                          "Merci de selectionner dans la liste l'utilisateur a supprimer")
            else:
                error, cmd_res = self.machine.smbldap.userDel(userNameToDel)
                if (error):
                    QtGui.QMessageBox.critical(self.widgetSMBLDAP,
        			                          'Erreur',
                                              "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, cmd_res))
                else:
                    QtGui.QMessageBox.information(self.widgetSMBLDAP,
        			                          'Information',
                                              "Utilisateur '%s' supprime" % newUserName)

                    self.refreshUsersList()


    """
    """
    def refreshUsersList(self):
        error, cmd_res = self.machine.smbldap.usersLs()
        if (error):
            QtGui.QMessageBox.critical(self.widgetSMBLDAP,
			                          'Erreur',
                                      "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, cmd_res))
        else:
            # TODO put \r in conf
            for stri in cmd_res.split('\r\n'):
                self.listUsers.addItem(stri)


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
                                          "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, cmd_res))
            else:
                QtGui.QMessageBox.information(self.widgetSMBLDAP,
    			                          'Information',
                                          "Groupe '%s' ajoute" % newGroupName)

                self.editGroup.clear()
                self.refreshGroupList()


    """
    """
    def delGroup(self):
        if (len(self.listGroups.selectedItems()) != 0):
            groupNameToDel = self.listGroups.selectedItems()[0].text()
            if (groupNameToDel == ""):
                QtGui.QMessageBox.warning(self.widgetSMBLDAP,
    			                          'Attention',
                                          "Merci de selectionner dans la liste le groupe a supprimer")
            else:
                error, cmd_res = self.machine.smbldap.groupDel(groupNameToDel)
                if (error):
                    QtGui.QMessageBox.critical(self.widgetSMBLDAP,
        			                          'Erreur',
                                              "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, cmd_res))
                else:
                    QtGui.QMessageBox.information(self.widgetSMBLDAP,
        			                          'Information',
                                              "Groupe '%s' supprime" % newUserName)

                    self.refreshGroupsList()


    """
    """
    def refreshGroupsList(self):
        error, cmd_res = self.machine.smbldap.groupsLs()
        if (error):
            QtGui.QMessageBox.critical(self.widgetSMBLDAP,
			                          'Attention',
                                      "La machine %s a retourne l'erreur suivante : %s" % (self.machine.hostname, cmd_res))
        else:
            # TODO put \r in conf
            for stri in cmd_res.split('\r\n'):
                self.listGroups.addItem(stri)

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
