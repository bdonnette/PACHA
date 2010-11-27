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


import ConfigParser

""" 
"""
class Service(object):

    ""
    ""
    def __init__(self, conf, machineConfPars, index, machine):
        self.machine = machine
        self.conf = conf

        key = "service"
        section = key + "s"
        option = key + "%i" % index
        try :
            self.label = machineConfPars.get(section, option + "_label", 0)
            self.command = machineConfPars.get(section, option + "_command", 0)
            self.status_command = machineConfPars.get(section, option + "_status_command", 0)
            self.status = self.conf.STATE_UNKNOWN
        except (ConfigParser.NoOptionError,
                ConfigParser.NoSectionError) :
            print "--ERROR Parsing config file--"
            pass


    """
    """
    def updateState(self):
        error, stdout = self.machine.sshAgent.query(self.status_command)

        if (error):
            self.status = self.conf.STATE_UNKNOWN
        else:
            if (stdout == '0'):
                self.status = self.conf.STATE_RED
            else:
                self.status = self.conf.STATE_GREEN


    """
    """
    def start(self):
        return self.machine.sshAgent.query(self.command + " start")

    """
    """
    def restart(self):
        return self.machine.sshAgent.query(self.command + " restart")


    """
    """
    def printTty(self):
        print "| |"
        print "| |\\"
        print "| | |Service"
        print "| | |-label\t: %s" % self.label
        print "| | |-command\t: %s" % self.command
        print "| | |-status_command\t: %s" % self.status_command
        print "| | |-status\t: %s" % self.status


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
