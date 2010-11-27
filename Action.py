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
class Action(object):

    ""
    ""
    def __init__(self, conf, machineConfPars, index, machine):
        self.conf = conf
        self.machine = machine

        key = "action"
        section = key + "s"
        option = key + "%i" % index
        try :
            self.label = machineConfPars.get(section, option + "_label", 0)
            self.command = machineConfPars.get(section, option + "_command", 0)
        except (ConfigParser.NoOptionError,
                ConfigParser.NoSectionError) :
            print "--ERROR Parsing config file--"
            pass

    """
    """
    def issue(self):
        return self.machine.sshAgent.query(self.command)

    """
    """
    def printTty(self):
        print "| |"
        print "| |\\"
        print "| | |Action"
        print "| | |-label\t: %s" % self.label
        print "| | |-command\t: %s" % self.command


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
