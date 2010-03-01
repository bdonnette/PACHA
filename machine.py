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

import HMI_ssh as ssh

class machine(object):
    ''' This class represents a machine, with both its SNMP and ssh
    accesses (any can be left blank though)
    '''

    def __init__(self,
                 name,
                 ssh_user, ssh_pass = ""):
        self.hostname = name
        self.agent = ssh.ssh_agent(self.hostname, ssh_user, ssh_pass)

        # SNMP does need more only if cyphered


        
