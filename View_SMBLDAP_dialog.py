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

""" Dialog box for SMB/LDAP to add/remove users to groups
"""
class View_SMBLDAP_dialog(Ui_SMBLDAP_dialog.Ui_SMBLDAP_dialog):


    """ Refresh lists whether we are editing a user or a group
    """
    def refresh_lists(self):
        if (self.group_user):
            self.refresh_groups_lists_of_user()
        else:
            self.refresh_users_lists_of_group()


    """ Ask internal business object to refresh the groups list
    """
    def refresh_groups_lists_of_user(self):
        error, groups_of_user = self.machine.smbldap.getGroupsOfUser(self.displayed_uid)

        if (error):
            QtGui.QMessageBox.critical(self.widget,
                                      'Erreur',
                                      "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(error)))
        else:
            error, groups_available_for_user = self.machine.smbldap.getGroupsAvailableForUser(self.displayed_uid)
            if (error):
                QtGui.QMessageBox.critical(self.widget,
                                          'Erreur',
                                          "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(error)))
            else:
                self.listRight.clear()
                for stri in groups_of_user:
                    self.listRight.addItem(QtCore.QString(stri))

                self.listLeft.clear()
                for stri in groups_available_for_user:
                    self.listLeft.addItem(QtCore.QString(stri))


    """ Ask internal business object to refresh the users list
    """
    def refresh_users_lists_of_group(self):
        error, users_of_group = self.machine.smbldap.getUsersOfGroup(self.displayed_uid)

        if (error):
            QtGui.QMessageBox.critical(self.widget,
                                      'Erreur',
                                      "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(error)))
        else:
            error, users_available_for_group = self.machine.smbldap.getUsersAvailableForGroup(self.displayed_uid)
            if (error):
                QtGui.QMessageBox.critical(self.widget,
                                          'Erreur',
                                          "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(error)))
            else:
                # TODO put \r in conf
                self.listRight.clear()
                for stri in users_of_group:
                    self.listRight.addItem(QtCore.QString(stri))

                self.listLeft.clear()
                for stri in users_available_for_group:
                    self.listLeft.addItem(QtCore.QString(stri))


    """ Ask internal business object to add user to group
    """
    def add_user_to_group(self):
        selected_item = ""
        if (len(self.listLeft.selectedItems()) != 0):
            selected_item = self.listLeft.selectedItems()[0].text()

        if (selected_item == ""):
            QtGui.QMessageBox.warning(self.widget,
                                      'Attention',
                                      "Merci de selectionner un element dans la liste de gauche")
        else:
            if (self.group_user):
                group = selected_item
                user = self.displayed_uid
            else:
                group = self.displayed_uid
                user = selected_item

            error, cmd_res = self.machine.smbldap.add_user_to_group(user, group)

            if (error):
                QtGui.QMessageBox.critical(self.widget,
                                           'Erreur',
                                           "La machine '%s' a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
            else:
                QtGui.QMessageBox.information(self.widget,
                                              'Information',
                                              "L'utilisateur '%s' a ete ajoute au groupe '%s'." % (user, group))

            self.refresh_lists()


    """ Ask internal business object to remove user from group
    """
    def remove_user_from_group(self):
        selected_item = ""
        if (len(self.listRight.selectedItems()) != 0):
            selected_item = self.listRight.selectedItems()[0].text()

        if (selected_item == ""):
            QtGui.QMessageBox.warning(self.widget,
                                      'Attention',
                                      "Merci de selectionner un element dans la liste de droite")
        else:
            if (self.group_user):
                group = selected_item
                user = self.displayed_uid
            else:
                group = self.displayed_uid
                user = selected_item

            error, cmd_res = self.machine.smbldap.remove_user_from_group(user, group)

            if (error):
                QtGui.QMessageBox.critical(self.widget,
                                           'Erreur',
                                           "La machine %s a retourne l'erreur suivante :%s" % (self.machine.hostname, os.linesep + os.linesep.join(cmd_res)))
            else:
                QtGui.QMessageBox.information(self.widget,
                                              'Information',
                                              "L'utilisateur '%s' a ete supprime du groupe '%s'." % (user, group))

            self.refresh_lists()


    """ Show this dialog
            group_user  : Are we editing a group or a user?
            uid         : UID of group or user we are editing
    """
    def show(self, group_user, uid):
        self.group_user = group_user
        self.displayed_uid = uid
        if (self.group_user):
            self.label_left.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Available groups:", None, QtGui.QApplication.UnicodeUTF8))
            self.label_right.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Groups user belongs to:", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.label_left.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Available users:", None, QtGui.QApplication.UnicodeUTF8))
            self.label_right.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Users already in group:", None, QtGui.QApplication.UnicodeUTF8))

        self.refresh_lists()
        self.widget.show()


    """ Destroy/hide this widget
    """
    def close_dialog(self):
        self.widget.close()


    """ Initial method to set dynamic elements up
    """
    def setupView(self):
        # Keep track of the UID on which we are working
        self.displayed_uid = ""

        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), self.close_dialog)
        QtCore.QObject.connect(self.btnRefresh, QtCore.SIGNAL("clicked()"), self.refresh_lists)
        QtCore.QObject.connect(self.btnAddUserToGroup, QtCore.SIGNAL("clicked()"), self.add_user_to_group)
        QtCore.QObject.connect(self.btnRemoveUserFromGroup, QtCore.SIGNAL("clicked()"), self.remove_user_from_group)

        QtCore.QObject.connect(self.listLeft, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.add_user_to_group)
        QtCore.QObject.connect(self.listRight, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.remove_user_from_group)


    """ Init method
            conf            : Pacha global conf
            machine         : the machine that owns the business object of this widget
    """
    def __init__(self, conf, machine):
        self.conf = conf
        self.machine = machine

        self.widget = QtGui.QWidget()
        self.setupUi(self.widget)
        self.setupView()

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
