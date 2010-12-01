# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ActionsSupervisions.ui'
#
# Created: Tue Nov 30 14:40:26 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ActionsSupervisions(object):
    def setupUi(self, ActionsSupervisions):
        ActionsSupervisions.setObjectName(_fromUtf8("ActionsSupervisions"))
        ActionsSupervisions.resize(571, 429)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ActionsSupervisions)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(ActionsSupervisions)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ActionsSupervisions)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.buttonsLayout = QtGui.QVBoxLayout()
        self.buttonsLayout.setObjectName(_fromUtf8("buttonsLayout"))
        self.verticalLayout_2.addLayout(self.buttonsLayout)
        self.resultEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.resultEdit.setEnabled(True)
        self.resultEdit.setReadOnly(True)
        self.resultEdit.setPlainText(_fromUtf8(""))
        self.resultEdit.setObjectName(_fromUtf8("resultEdit"))
        self.verticalLayout_2.addWidget(self.resultEdit)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ActionsSupervisions)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.resultEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(ActionsSupervisions)

    def retranslateUi(self, ActionsSupervisions):
        ActionsSupervisions.setWindowTitle(QtGui.QApplication.translate("ActionsSupervisions", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ActionsSupervisions", "Supervisions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ActionsSupervisions", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ActionsSupervisions", "Clear", None, QtGui.QApplication.UnicodeUTF8))

