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

import getpass, os
import subprocess as sp

class ssh_agent (object):
    ''' This class handles ssh. Use password='' to go through
    secret key auth. '''
    def __init__(self,
                 host,
                 user, password = ""):
        self.user = user
        self.password = password
        self.host = host
        self.is_win32 = (os.name == "nt")

    def action(self, command="df"):
        user = self.user
        host = self.host
        password = self.password

        if (self.is_win32):
            if (password == ""):
                full_cmd = "c:\Python26\plink.exe -l %s %s %s" % (
                    user, host, command)
            else:
                full_cmd = "c:\Python26\plink.exe -l %s -pw %s %s %s" % (
                    user, password, host, command)
            child = sp.Popen(full_cmd, shell = True, 
                             stdin = sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            l = ""
            if (child.wait == 0):
                self.stdout = l.join(child.stdout.readlines()).strip('\n')
            else:
                self.stdout = l.join(child.stderr.readlines()).strip('\n')
        else:
            import pexpect

            ssh_newkey = 'Are you sure you want to continue connecting'
            child = pexpect.spawn('ssh -l %s %s %s'%(user, host, command))

            if (password != ""):
                i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
                if i == 0: # Timeout
                    print 'ERROR!'
                    print 'SSH could not login. Here is what SSH said:'
                    print child.before, child.after
                    return None
                if i == 1: # SSH does not have the public key. Just accept it.
                    child.sendline ('yes')
                    child.expect ('password: ')
                    i = child.expect([pexpect.TIMEOUT, 'password: '])
                    if i == 0: # Timeout
                        print 'ERROR!'
                        print 'SSH could not login. Here is what SSH said:'
                        print child.before, child.after
                        return None       
                    child.sendline(password)

            child.expect(pexpect.EOF)        
            self.stdout = child.before

        return self.stdout

if (__name__ == "__main__"):
    # unit test
    ssh = ssh_agent("192.168.122.14", "root", "toto")
    print ("Issuing `uname -a` on remote")
    print ssh.action("uname -a")
