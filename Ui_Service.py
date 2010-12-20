# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Service.ui'
#
# Created: Mon Dec 20 11:48:13 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Service(object):
    def setupUi(self, Service):
        Service.setObjectName(_fromUtf8("Service"))
        Service.resize(546, 445)
        self.widget = QtGui.QWidget(Service)
        self.widget.setGeometry(QtCore.QRect(50, 20, 315, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonIcon = QtGui.QPushButton(self.widget)
        self.buttonIcon.setEnabled(True)
        self.buttonIcon.setText(_fromUtf8(""))
        self.buttonIcon.setFlat(False)
        self.buttonIcon.setObjectName(_fromUtf8("buttonIcon"))
        self.horizontalLayout.addWidget(self.buttonIcon)
        self.labelText = QtGui.QLabel(self.widget)
        self.labelText.setObjectName(_fromUtf8("labelText"))
        self.horizontalLayout.addWidget(self.labelText)
        self.startButton = QtGui.QPushButton(self.widget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        self.restartButton = QtGui.QPushButton(self.widget)
        self.restartButton.setObjectName(_fromUtf8("restartButton"))
        self.horizontalLayout.addWidget(self.restartButton)

        self.retranslateUi(Service)
        QtCore.QMetaObject.connectSlotsByName(Service)

    def retranslateUi(self, Service):
        Service.setWindowTitle(QtGui.QApplication.translate("Service", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelText.setText(QtGui.QApplication.translate("Service", "RAS", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("Service", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.restartButton.setText(QtGui.QApplication.translate("Service", "Restart", None, QtGui.QApplication.UnicodeUTF8))

