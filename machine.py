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
import ConfigParser

class machine(object):
    ''' This class represents a machine, with both its SNMP and ssh
    accesses (any can be left blank though)
    '''
    def __init__(self, config, label):
        ''' IN : config, a ConfigParser object
        Initializes the object from the config file
        by parsing the "label" section
        '''
        self.hostname = label
        ssh_user = config.get(label, "user", 0)
        ssh_pass = config.get(label, "password", 0)
        self.agent = ssh.ssh_agent(self.hostname, ssh_user, ssh_pass)

        # SNMP does need more only if cyphered



if (__name__ == "__main__"):
    # unit test
    config = ConfigParser.ConfigParser()
    config.read('example.cfg')
    try:
        n_machines = config.get("Machines", "number", 1)
    except ConfigParser.NoSectionError:
        n_machines = 0

    m_dict = {}
    for i in range(int(n_machines)):
        label = config.get("Machines", "hostname%d" % (i+1), 1)
        m_dict[label] = machine(config, label)
        
    print m_dict
    n_machines = (m_dict.keys()).__len__()

    print n_machines
        
