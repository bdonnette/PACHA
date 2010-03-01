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
from HMI_supervision import *

class dfDiskSupervision(HMI_supervision):
    ''' Disk usage supervision via ssh using the df command 
    '''
    
    def __init__(self, server, disk, steps):
        ''' This init takes the following :
        server : a "machine" type is expected here
        disk : "/dev/sda1" for example
        steps : [0, 70, 90, 100] : steps for green, orange, red, KO
        '''
        self.agent = server.agent
        self.command = "df -k | grep %s" % disk
        self.steps = steps
        print self.command

        self.item = {"method":"ssh", "accessor":self.do_dfSupervision}

    def do_dfSupervision(self):
        outputs = (self.agent.action(self.command)).splitlines()
        output = (int)(outputs[1].split()[4].strip('%'))
        return output, self.steps

                     
        

if (__name__ == "__main__"):
    # unit test
    import machine as m
    server = m.machine("192.168.122.14", "root", "toto")
    df = dfDiskSupervision(server, "wd0", [0, 8, 60, 100])
    print df.do_dfSupervision()
