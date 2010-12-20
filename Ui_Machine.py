# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Machine.ui'
#
# Created: Mon Dec 20 11:48:12 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Machine(object):
    def setupUi(self, Machine):
        Machine.setObjectName(_fromUtf8("Machine"))
        Machine.resize(616, 482)
        self.gridLayout = QtGui.QGridLayout(Machine)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolBox = QtGui.QToolBox(Machine)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.retranslateUi(Machine)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Machine)

    def retranslateUi(self, Machine):
        Machine.setWindowTitle(QtGui.QApplication.translate("Machine", "Form", None, QtGui.QApplication.UnicodeUTF8))

