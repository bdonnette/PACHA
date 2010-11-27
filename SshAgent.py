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
        stdout = ""
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
                         stderr = subprocess.PIPE)

        l = ""
        stdout = ""
        exitStatus = 1
        if (child.wait() == 0):
            result = l.join(child.stdout.readlines()).strip('\n')

            # TODO put this in conf
            # stdout can be surrounded by "\r\n" so remove them
            # Remove exit status from answer and store it appart
            stdout, sep, exitStatus = result.rpartition('\n')
        else:
            result = l.join(child.stderr.readlines()).strip('\n')

        return exitStatus, stdout

    """
    """
    def query_from_awesome_linux(self, ip, user, password, command):
        import pexpect

        stdout = ""

        str_newkey = 'Are you sure you want to continue connecting'
        str_connection_refused = 'ssh: connect to host %s port 22: Connection refused' % ip
        str_no_route_to_host = 'ssh: connect to host %s port 22: No route to host' % ip
        str_password = 'password: '
        child = pexpect.spawn(self.conf.val["general"]["ssh_lnx_cmd"] % (user, ip, command))

        exitStatus = 1
        end = False
        i = 0
        while (not end):
            i = child.expect([pexpect.TIMEOUT,
                              str_connection_refused,
                              str_no_route_to_host,
                              str_newkey,
                              str_password])

            if (i == 0):
                stdout = "SSH could not login. Here is what SSH said: %s %s" % (child.before, child.after)
                end = True
            elif (i == 1):
                stdout = "Connection refused: %s %s" % (child.before, child.after)
                end = True
            elif (i == 2):
                stdout = "Unable to find host: %s %s" % (child.before, child.after)
                end = True
            elif (i == 3):
                child.sendline('yes')
            elif (i == 4):
                child.sendline(password)
                child.expect(pexpect.EOF)
                stdout = child.before
                end = True

        stdout = stdout.strip('\r\n')

        if (i == 4):
            # TODO put this in conf
            # stdout can be surrounded by "\r\n" so remove them
            # Remove exit status from answer and store it appart
            stdout, sep, exitStatus = stdout.rpartition('\r\n')

        return exitStatus, stdout

    """
    """
    def query(self, command):
        # Add the exit status of the command asked by user
        # TODO put this in conf?
        command += "; echo $?"

        error = False
        stdout = ""

        if (os.name == "nt"):
            error, stdout = self.query_from_lame_win32(self.machine.ip,
                                                self.user,
                                                self.password,
                                                command)
        else:
            error, stdout = self.query_from_awesome_linux(self.machine.ip,
                                                   self.user,
                                                   self.password,
                                                   command)

        return (int(error), stdout)


    def printTty(self):
        print "| |"
        print "| |\\"
        print "| | |SshAgent"
        print "| | |-user\t: %s" % self.user
        print "| | |-password\t: %s" % self.password


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
