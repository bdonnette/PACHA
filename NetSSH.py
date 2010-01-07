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

from NetClient import *
import pyssh as ssh

class NetSSH(NetClient):
    def __init__(self, host_name, user_name, password, prompt):
        """            
        @param host_name: Host name or IP address
        @param user_name: User name 
        @param password: Password
        @param prompt: Command prompt (or partial string matching the end of the prompt)
        """
        debug = 2
        Client.__init__(self, "TCP", '22', debug) 
        self.host_name = host_name
        self.user_name = user_name
        self.password = password
        self.prompt = prompt
        self.port = '22'  #default SSH port
        self.session_ssh = None
        
    def login(self):
        """
        Connect to the remote host and login.    
        """
        self.session_ssh = ssh.Ssh(self.user_name, self.host_name, self.port)
        self.session_ssh.login(self.password)

        
    def run_command(self, command):
        """Run a command on the remote host.
            
        @param command: Unix command
        @return: Command output
        @rtype: String
        """ 
        response = self.ssh.sendcmd(command)
        return self.__strip_output(command, response)
        
    
    def logout(self):
        """Close the connection to the remote host.
            
        """
        self.ssh.logout()
        
        
    def run_atomic_command(self, command):
        """Connect to a remote host, login, run a command, and close the connection.
            
        @param command: Unix command
        @return: Command output
        @rtype: String
        """
        self.login()
        command_output = self.run_command(command)
        self.logout()
        return command_output

        
    def __strip_output(self, command, response):
        """Strip everything from the response except the actual command output.
            
        @param command: Unix command        
        @param response: Command output
        @return: Stripped output
        @rtype: String
        """
        lines = response.splitlines()
        # if our command was echoed back, remove it from the output
        if command in lines[0]:
            lines.pop(0)
        # remove the last element, which is the prompt being displayed again
        lines.pop()
        # append a newline to each line of output
        lines = [item + '\n' for item in lines]
        # join the list back into a string and return it
        return ''.join(lines)

# Test code
    def test():
        my_ssh = NetSSH("192.168.122.14", "root", "toto", "#")
        my_ssh.login
        my_ssh.run_command("ls -ltr")
        my_ssh.logout
    
if (__name__ == "__main__"):
    test
