# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SMBLDAP_dialog.ui'
#
# Created: Tue Nov 30 14:40:27 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SMBLDAP_dialog(object):
    def setupUi(self, SMBLDAP_dialog):
        SMBLDAP_dialog.setObjectName(_fromUtf8("SMBLDAP_dialog"))
        SMBLDAP_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SMBLDAP_dialog.resize(769, 526)
        self.horizontalLayout = QtGui.QHBoxLayout(SMBLDAP_dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_3 = QtGui.QLabel(SMBLDAP_dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_6.addWidget(self.label_3)
        self.listGroupsAvailable = QtGui.QListWidget(SMBLDAP_dialog)
        self.listGroupsAvailable.setObjectName(_fromUtf8("listGroupsAvailable"))
        self.verticalLayout_6.addWidget(self.listGroupsAvailable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.btnAddUserToGroup = QtGui.QPushButton(SMBLDAP_dialog)
        self.btnAddUserToGroup.setObjectName(_fromUtf8("btnAddUserToGroup"))
        self.verticalLayout_7.addWidget(self.btnAddUserToGroup)
        self.btnRemoveUserFromGroup = QtGui.QPushButton(SMBLDAP_dialog)
        self.btnRemoveUserFromGroup.setObjectName(_fromUtf8("btnRemoveUserFromGroup"))
        self.verticalLayout_7.addWidget(self.btnRemoveUserFromGroup)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_4 = QtGui.QLabel(SMBLDAP_dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_8.addWidget(self.label_4)
        self.listGroupsOfUser = QtGui.QListWidget(SMBLDAP_dialog)
        self.listGroupsOfUser.setObjectName(_fromUtf8("listGroupsOfUser"))
        self.verticalLayout_8.addWidget(self.listGroupsOfUser)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnClose = QtGui.QPushButton(SMBLDAP_dialog)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.horizontalLayout_4.addWidget(self.btnClose)
        self.btnRefresh = QtGui.QPushButton(SMBLDAP_dialog)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.horizontalLayout_4.addWidget(self.btnRefresh)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(SMBLDAP_dialog)
        QtCore.QMetaObject.connectSlotsByName(SMBLDAP_dialog)

    def retranslateUi(self, SMBLDAP_dialog):
        SMBLDAP_dialog.setWindowTitle(QtGui.QApplication.translate("SMBLDAP_dialog", "Add user to groups", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Available groups:", None, QtGui.QApplication.UnicodeUTF8))
        self.listGroupsAvailable.setSortingEnabled(True)
        self.btnAddUserToGroup.setText(QtGui.QApplication.translate("SMBLDAP_dialog", ">>>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemoveUserFromGroup.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "<<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Groups user belongs to:", None, QtGui.QApplication.UnicodeUTF8))
        self.listGroupsOfUser.setSortingEnabled(True)
        self.btnClose.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("SMBLDAP_dialog", "Refresh", None, QtGui.QApplication.UnicodeUTF8))

