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

        hb_ok = True
        one_in_transition = False

        for machine in self.machines:
            if (machine.is_master):
                hb_ok = hb_ok & (machine.hb_state == self.conf.HB_ALL)
            else:
                hb_ok = hb_ok & (machine.hb_state == self.conf.HB_NONE)

            one_in_transition = one_in_transition | (machine.hb_state == self.conf.HB_TRANSITION)

        # Default: all cases are RED
        state = self.conf.STATE_RED

        # GREEN if master is "all" and all slaves are "none"
        if (hb_ok):
            state = self.conf.STATE_GREEN
        else:
            # If previous statement is not true: YELLOW
            state = self.conf.STATE_YELLOW

        # If one machine is in transition then YELLOW
        if (one_in_transition):
            state = self.conf.STATE_YELLOW
            
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
