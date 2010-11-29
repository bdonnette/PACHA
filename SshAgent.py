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

import os, time
import thread

"""
"""
class SshAgent(object):

    """
    """
    def __init__(self, conf, machineConfPars, machine):
        self.conf = conf
        self.machine = machine
        self.user = machineConfPars.get("sshagent", "user", 0)
        self.password = machineConfPars.get("sshagent", "password", 0)


    """
    """
    def query_from_lame_win32(self, ip, user, password, command):
        import subprocess
        if (password == ""):
            full_cmd = self.conf.val["general"]["ssh_win_cmd_no_pass"] % (
                user, ip, command)
        else:
            full_cmd = self.conf.val["general"]["ssh_win_cmd_pass"] % (
                user, password, ip, command)

        child = subprocess.Popen(full_cmd,
                         shell = True,
                         stdin = subprocess.PIPE,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.STDOUT)

        result = ""
        for line in child.stdout:
                result += line

        if (child.wait() != 0):
            result += str(child.wait()) + "\r\n"

        # If we didn't manage to reach the machine, add the error code to result
        # so that following result handling don't fail
#        if (child.wait() != 0):
#            result += "%i\r\n" % child.wait()

        return result.strip('\r\n')

    """
    """
    def query_from_awesome_linux(self, ip, user, password, command):
        import pexpect

        stdout = ""

        str_password = 'password: '
        str_newkey = 'Are you sure you want to continue connecting'
        str_connection_refused = 'ssh: connect to host %s port 22: Connection refused' % ip
        str_no_route_to_host = 'ssh: connect to host %s port 22: No route to host' % ip

        child = pexpect.spawn(self.conf.val["general"]["ssh_lnx_cmd"] % (user, ip, command))

        i = child.expect([str_password,
                          pexpect.TIMEOUT,
                          str_connection_refused,
                          str_no_route_to_host,
                          str_newkey
                          ])

        if (i == 0):
            child.sendline(password)
            child.expect(pexpect.EOF)
            stdout = child.before
        elif (i == 1 or i == 2 or i == 3 or i == 4):
            stdout = "%s %s\n%i" % (child.before, child.after, i)

        stdout = stdout.strip('\r\n')

        return stdout

    """
    """
    def query(self, command):
        # Add the exit status of the command asked by user
        # TODO put this in conf?
        command += "; echo $?"

        result = ""

        if (os.name == "nt"):
            result = self.query_from_lame_win32(self.machine.ip,
                                                self.user,
                                                self.password,
                                                command)
        else:
            result = self.query_from_awesome_linux(self.machine.ip,
                                                   self.user,
                                                   self.password,
                                                   command)

        stdout, sep, exitStatus = result.rpartition('\n')

        return (int(exitStatus), stdout.strip('\r'))


    def printTty(self):
        print "| |"
        print "| |\\"
        print "| | |SshAgent"
        print "| | |-user\t: %s" % self.user
        print "| | |-password\t: %s" % self.password


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
