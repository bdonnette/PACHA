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

        master_is_all = False
        master_is_none = False
        all_slaves_are_none = True
        one_in_transition = False
        one_slave_is_all = False
        # These fall in the default RED case
#        one_error_or_unknown = False

        for machine in self.machines:
            if (machine.is_master):
                #FIXME If more than one machine is configured as master we won't see it here
                master_is_all = (machine.hb_state == self.conf.HB_ALL)
                master_is_none = (machine.hb_state == self.conf.HB_NONE)
            else:
                all_slaves_are_none = all_slaves_are_none & (machine.hb_state == self.conf.HB_NONE)
                one_slave_is_all = one_slave_is_all | (machine.hb_state == self.conf.HB_ALL)

            one_in_transition = one_in_transition | (machine.hb_state == self.conf.HB_TRANSITION)
#            one_error_or_unknown = one_error_or_unknown | (machine.hb_state == self.conf.HB_ERROR) | (machine.hb_state == self.conf.HB_UNKNOWN)

        # Default: all cases are RED
        state = self.conf.STATE_RED

        # GREEN if master is "all" and all slaves are "none"
        if (master_is_all & all_slaves_are_none):
            state = self.conf.STATE_GREEN
        else:
            # If one machine is in transition then YELLOW
            if (one_in_transition):
                state = self.conf.STATE_YELLOW
            elif(master_is_none & one_slave_is_all):
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
