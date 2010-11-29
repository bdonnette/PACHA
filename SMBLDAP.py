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

import ConfigParser


""" Represents the SMB/LDAP part of a Machine as specified by user in conf
"""
class SMBLDAP(object):

    """
    """
    def userAdd(self, newUserName):
        print self.cmd_user_add % newUserName
        return self.machine.sshAgent.query(self.cmd_user_add % newUserName)


    """
    """
    def userDel(self, userNameToDel):
        return self.machine.sshAgent.query(self.cmd_user_del % userNameToDel)


    """
    """
    def usersLs(self):
        return self.machine.sshAgent.query(self.cmd_users_ls)


    """
    """
    def groupAdd(self, newGroupName):
        return self.machine.sshAgent.query(self.cmd_group_add % newGroupName)


    """
    """
    def groupDel(self, groupNameToDel):
        return self.machine.sshAgent.query(self.cmd_group_del % groupNameToDel)

    """
    """
    def groupsLs(self):
        return self.machine.sshAgent.query(self.cmd_groups_ls)


    """    Test function that displays this Machine in TTY
    """
    def printTty(self):
        print "| |"
        print "| |\\"
        print "| | |SMB/LDAP"
        print "| | |-cmd_user_add\t: %s" % self.cmd_user_add
        print "| | |-cmd_user_del\t: %s" % self.cmd_user_del
        print "| | |-cmd_users_ls\t: %s" % self.cmd_users_ls
        print "| | |-cmd_group_add\t: %s" % self.cmd_group_add
        print "| | |-cmd_group_del\t: %s" % self.cmd_group_del
        print "| | |-cmd_groups_ls\t: %s" % self.cmd_groups_ls
        print "| | |-cmd_user_to_group\t: %s" % self.cmd_user_to_group
        print "| | |-cmd_user_off_group\t: %s" % self.cmd_user_off_group


    """ Constructor
    """
    def __init__(self, conf, userConfig, machine):
        self.conf = conf
        self.machine = machine

        section = "smbldap"

        try :
            self.cmd_user_add = self.conf.val[section]["cmd_user_add"]
            self.cmd_user_del = self.conf.val[section]["cmd_user_del"]
            self.cmd_users_ls = self.conf.val[section]["cmd_users_ls"] % userConfig.get(section, "users_searchbase")
            self.cmd_group_add = self.conf.val[section]["cmd_group_add"]
            self.cmd_group_del = self.conf.val[section]["cmd_group_del"]
            self.cmd_groups_ls = self.conf.val[section]["cmd_groups_ls"] % userConfig.get(section, "groups_searchbase")
            self.cmd_user_to_group = self.conf.val[section]["cmd_user_to_group"]
            self.cmd_user_off_group = self.conf.val[section]["cmd_user_off_group"]
        except (ConfigParser.NoOptionError,
                ConfigParser.NoSectionError) :
            print "--ERROR Parsing config file--"
            pass


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
