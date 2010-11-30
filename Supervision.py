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
class Supervision(object):

    ""
    ""
    def __init__(self, conf, userConfig, index, machine):
        self.conf = conf
        self.machine = machine

        key = "supervision"
        section = key + "s"
        option = key + "%i" % index
        try :
            self.label = userConfig.get(section, option + "_label", 0)
            self.vital = (userConfig.get(section, option + "_vital", 0) == "True")
            self.param = userConfig.get(section, option + "_param", 0)
            self.method = userConfig.get(section, option + "_method", 0)
            self.state = self.conf.STATE_UNKNOWN

            if (self.method == "ssh"):
                self.command = userConfig.get(section, option + "_command", 0)
                if (userConfig.has_option(section, option + "_field")):
                    self.field = int(userConfig.get(section, option + "_field", 0)) - 1
                else:
                    self.field = self.conf.STATE_UNKNOWN

                if (userConfig.has_option(section, option + "_sep")):
                    self.sep = userConfig.get(section, option + "_sep", 0)
                else:
                    self.sep = ""

            self.levels = [
                int(userConfig.get(section, option + "_low_green")),
                int(userConfig.get(section, option + "_low_orange")),
                int(userConfig.get(section, option + "_low_red")),
                int(userConfig.get(section, option + "_low_undef"))
            ]

        except (ConfigParser.NoOptionError,
                ConfigParser.NoSectionError) :
            print "--ERROR Parsing config file--"
            pass


    """
    """
    def updateState(self):
        error, stdout = self.machine.sshAgent.query(self.command)

        if (int(error)):
            self.state = self.conf.STATE_UNKNOWN
        else:
            if (self.field != self.conf.STATE_GREEN) :
                if (self.sep):
                    # TODO handle exit status
                    val = int((stdout[0].split(self.sep)[self.field]).strip("%"))
                else:
                    # TODO handle exit status
                    val = int((stdout[0].split()[self.field]).strip("%"))

            level = self.conf.STATE_YELLOW
            levels = self.levels
            for i in range(len(levels)):
                if (val >= int(levels[i])):
                    level = i

            self.state = level


    """
    """
    def printTty(self):
        print "| |"
        print "| |\\"
        print "| | |Supervision"
        print "| | |-label\t: %s" % self.label
        print "| | |-vital\t: %s" % self.vital
        print "| | |-param\t: %s" % self.param
        print "| | |-method\t: %s" % self.method
        print "| | |-state\t: %s" % self.state
        print "| | |-method\t: %s" % self.method

        if (self.method == "ssh"):
            print "| | |-command\t: %s" % self.command
            print "| | |-field\t: %s" % self.field
            print "| | |-sep\t\t: %s" % self.sep

        print "| | |-levels\t: %s" % self.levels


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
