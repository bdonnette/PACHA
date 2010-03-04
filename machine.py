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
''' a Machine is here to instantiate from config files
so as to be further requested from outer (HMI) classes.
'''
import HMI_ssh as ssh
import ConfigParser

class Machine(object):
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

        i = 0
        self.actions = []
        while (True):
            i += 1
            section = self.hostname + "_action"
            lbl = "action%d" % i
            try :
                m_action = {"name" : config.get(section, lbl+"_lbl", 0)}
                m_action["command"] =  config.get(section, lbl+"_cmd", 0)
            except (ConfigParser.NoOptionError,
                    ConfigParser.NoSectionError) :
                break
            self.actions.append(m_action)

        # SNMP does need more only if cyphered
        self.supervisions = []
        i = 0
        while (True):
            i += 1
            section = self.hostname+"_supervision"
            lbl = ("svc%d" % i)+"_%s"
            try :
                m_supervision = {"name" : config.get(section, lbl % "name", 0),
                                 "param": config.get(section, lbl % "param", 0),
                                 "method": config.get(section, lbl % "method", 0)
                                 }
                if (m_supervision["method"] == "ssh"):
                    m_supervision["command"] = config.get(
                        section, lbl % "command", 0)
                
            except (ConfigParser.NoOptionError, 
                    ConfigParser.NoSectionError) :
                break
            self.supervisions.append(m_supervision)

        self.services = []
        while (True):
            i += 1
            section = self.hostname+"_service"
            lbl = "service%d" % i
            try :
                m_service = {"name" : config.get(section, lbl, 0)}
            except (ConfigParser.NoOptionError,
                    ConfigParser.NoSectionError) :
                break
            self.services.append(m_service)

if (__name__ == "__main__"):
    # unit test
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read('config/example.cfg')
    try:
        N_MACHINES = CONFIG.get("Machines", "number", 1)
    except ConfigParser.NoSectionError:
        N_MACHINES = 0
    M_DICT = {}
    for i in range(int(N_MACHINES)):
        label = CONFIG.get("Machines", "hostname%d" % (i+1), 1)
        M_DICT[label] = Machine(CONFIG, label)
    print M_DICT
    N_MACHINES = (M_DICT.keys()).__len__()

    print N_MACHINES
        
