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


"""
"""
class Group(object):

    """
    """
    def __init__(self, conf, groupName):
        self.conf = conf
        self.name = groupName
        self.state = self.conf.STATE_UNKNOWN
        self.machines = []


    """
    """
    def updateState(self):

        all_available       = True
        all_hb_up           = True
        all_mach_straight   = True


        for machine in self.machines:
            all_available     = all_available & (machine.hb_state != self.conf.HB_UNKNOWN)
            all_hb_up         = all_hb_up & (machine.hb_state == self.conf.HB_UP)
            all_mach_straight = all_mach_straight & (machine.hb_state == self.conf.HB_STRAIGHT)

        state = self.conf.STATE_UNKNOWN

        if (all_available & all_hb_up & all_mach_straight):
            state = self.conf.STATE_GREEN
        elif (all_available & all_hb_up & (not all_mach_straight)):
            state = self.conf.STATE_YELLOW
        elif (not all_available | (not all_hb_up)):
            state = self.conf.STATE_RED
            
        self.state = state


    """
    """
    def printTty(self):
        print "|"
        print "|\\================================"
        print "| |Group"
        print "| |-name\t: %s" % self.name
        print "| |-state\t: %s" % self.state
        for machine in self.machines:
            machine.printTty()


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
