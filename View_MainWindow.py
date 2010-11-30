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
import Ui_MainWindow, View_Group, View_Machine, View_ActionsSupervisions, View_SMBLDAP

"""
"""
class View_MainWindow(Ui_MainWindow.Ui_MainWindow):

    """
    """
    def __init__(self, pachaApp, conf, groups):
        self.pachaApp = pachaApp
        self.conf = conf
        self.groups = groups

        self.widgetMainWindow = QtGui.QMainWindow()
        self.setupUi(self.widgetMainWindow)
        self.setupView()

        self.widgetMainWindow.closeEvent = self.quit_main


    """
    """
    def setupView(self):
        self.groupViews = {}
        self.machineViews = {}

        # Groups
        for group in self.groups:
            viewGroup = View_Group.View_Group(self.conf, group)
            self.treeWidget.addTopLevelItem(viewGroup.treeItem)
            self.groupViews[group.name] = viewGroup
            group.view = viewGroup

            # Machines
            for machine in group.machines:
                # Add an item on the treeWidget
                treeItem = QtGui.QTreeWidgetItem(self.groupViews[machine.group.name].treeItem)
                treeItem.setText(0, machine.hostname)
    
                # Create the View_Machine
                view_Machine = View_Machine.View_Machine(self.conf, machine, self, treeItem)
                # Each instance of Machine keeps a pointer on its view
                machine.view = view_Machine
    
                self.horizontalLayout.addWidget(view_Machine.widgetMachine)
                view_Machine.hide()
                self.machineViews[machine.hostname] = view_Machine

        QtCore.QObject.connect(self.treeWidget,
                               QtCore.SIGNAL("itemSelectionChanged()"),
                               self.treeWidgetItemSelChanged)

        # Show ToolBox of first machine
        self.treeWidget.expandAll()
        self.machineViews.values()[0].show()
        self.showedViewMachine = self.machineViews.values()[0]


    """
    """
    def treeWidgetItemSelChanged(self):
        # This TreeWidget allows only one item to be selected at a time
        # So the first item is the only one on the list
        selectedLabel = str(self.treeWidget.selectedItems()[0].text(0))

        # If user has selected a machine
        if (selectedLabel in self.machineViews.keys()):
            self.showedViewMachine.hide()
            self.machineViews[selectedLabel].show()
            self.showedViewMachine = self.machineViews[selectedLabel]


    """
    """
    def show(self):
        self.widgetMainWindow.show()


    """
    """
    def quit_main(self, event):
        #TODO add an quit event and display a nice message dialog while bluring this window
        print "Please wait while all agents exit..."
        self.pachaApp.quit_main()

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
