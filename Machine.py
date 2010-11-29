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

import string, ConfigParser, time
from threading import Thread
import SshAgent, Supervision, Action, Service, SMBLDAP
from PyQt4 import QtCore, QtGui


""" Represents a Machine as specified by user in conf
"""
class Machine(Thread):

    """ ###################################################
            Init
    """

    """ Init
            conf             : Pacha general config dictionary
            machineConfPars  : where to read user configuration
            label            : identifier of the machine (the hostname)
    """
    def __init__(self, conf, machineConfPars, myGroup):
        Thread.__init__(self)
        self.running = False

        self.conf = conf

        # General connection
        self.hostname = machineConfPars.get("general", "hostname", 0)
        self.ip = machineConfPars.get("general", "ip", 0)
        self.group = myGroup
        self.is_master = (machineConfPars.get("general", "is_master", 0) == 'True')
        self.hb_state = self.conf.HB_UNKNOWN

        self.sshAgent = SshAgent.SshAgent(self.conf, machineConfPars, self)
        self.state = self.conf.STATE_UNKNOWN

        # Load user configuration
        self.load_actions(machineConfPars)
        self.load_supervisions(machineConfPars)
        self.load_services(machineConfPars)

        self.smbldap = None
        if (machineConfPars.has_section("smbldap")):
            self.smbldap = SMBLDAP.SMBLDAP(self.conf, machineConfPars, self)


    """ Loads Actions from user config file
    """
    def load_actions(self, machineConfPars):
        self.actions = []
        key = "action"
        i = 1
        option = key + "%i_%s"
        while (machineConfPars.has_option(key + "s", option % (i, "label"))):
            self.actions.append(Action.Action(self.conf, machineConfPars, i, self))
            i += 1


    """ Loads Supervisions from user config file
    """
    def load_supervisions(self, machineConfPars):
        self.supervisions = []
        key = "supervision"
        i = 1
        option = key + "%i_%s"
        while (machineConfPars.has_option(key + "s", option % (i, "label"))):
            self.supervisions.append(Supervision.Supervision(self.conf, machineConfPars, i, self))
            i += 1


    """ Loads Services from user config file
    """
    def load_services(self, machineConfPars):
        self.services = []
        key = "service"
        i = 1
        option = key + "%i_%s"
        while (machineConfPars.has_option(key + "s", option % (i, "label"))):
            self.services.append(Service.Service(self.conf, machineConfPars, i, self))
            i += 1


    """ ###################################################
            Thread
    """

    """
    """
    def updateMachineState(self):
        state = 0
        all_green = True
        one_red = False
        all_vital_green = True
        one_vital_red = False
        for supervision in self.supervisions:
            all_green = all_green & (supervision.state == self.conf.STATE_GREEN)
            one_red = one_red | (supervision.state == self.conf.STATE_RED)

            if (supervision.vital):
                all_vital_green = all_vital_green & (supervision.state == self.conf.STATE_GREEN)

            one_vital_red = one_vital_red | ( (supervision.vital) & (supervision.state == self.conf.STATE_RED) )

        state = self.conf.STATE_UNKNOWN

        if (all_green):
            state = self.conf.STATE_GREEN
        elif (one_red & all_vital_green):
            state = self.conf.STATE_YELLOW
        elif (one_vital_red) :
            state = self.conf.STATE_RED

        self.state = state

#        print "___"
#        print "%s / %s" % (self.hostname, supervision.label)
#        print "all_green\t: %s" % all_green
#        print "one_red\t: %s" % one_red
#        print "one_vital_red\t: %s" % one_vital_red
#        print "all_vital_green\t: %s" % all_vital_green


    """
    """
    def run(self):
        self.running = True
        while(self.running):
            # Update Supervisions states
            for supervision in self.supervisions:
                supervision.updateState()

            for service in self.services:
                service.updateState()

            self.update_hb_state()

            # Compute Machine state based on previous updates
            self.updateMachineState()

            self.group.updateState()

            self.view.reflectStates()

            time.sleep(int(self.conf.val["general"]["ui_refresh_interval"]))


    """
    """
    def exit(self):
        self.running = False


    """ ###################################################
            Methods
    """

    def update_hb_state(self):
        error, stdout = self.sshAgent.query(self.conf.val["general"]["hb_status_command"])

        hb_state = self.conf.HB_UNKNOWN

        if (error):
            hb_state = self.conf.HB_ERROR
        else:
            if (stdout in [self.conf.HB_LOCAL,
                           self.conf.HB_FOREIGN,
                           self.conf.HB_ALL,
                           self.conf.HB_NONE,
                           self.conf.HB_TRANSITION]):
                hb_state = stdout

        self.hb_state = hb_state 


    """    Test function that displays this Machine in TTY
    """
    def printTty(self):
        print "|"
        print "|\\_______________________________"
        print "| |Machine"
        print "| |-hostname\t: %s" % self.hostname
        print "| |-ip\t\t: %s" % self.ip
        print "| |-Group\t: %s" % self.group.name
        print "| |-Master\t: %s" % self.is_master
        print "| |-HB State\t: %s" % self.hb_state

        self.sshAgent.printTty()

        for action in self.actions:
            action.printTty()

        for supervision in self.supervisions:
            supervision.printTty()

        for service in self.services:
            service.printTty()

        if (self.smbldap):
            self.smbldap.printTty()


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
