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


""" Business object thet represents the SMB/LDAP part of a Machine as specified by user in conf
"""
class SMBLDAP(object):

    """ Ask remote server to create new user
            newUserName : the memberUid of new user to create
            return      : (exitStatus, [stdoutLine ...])
    """
    def userAdd(self, newUserName):
        return self.machine.sshAgent.query(self.cmd_user_add % newUserName)


    """ Ask remote server to delete an user
            userNameToDel : the memberUid of user to delete
            return        : (exitStatus, [stdoutLine ...])
    """
    def userDel(self, userNameToDel):
        return self.machine.sshAgent.query(self.cmd_user_del % userNameToDel)


    """ Ask remote server to list all users
            return  : (exitStatus, [stdoutLine ...])
    """
    def usersLs(self):
        return self.machine.sshAgent.query(self.cmd_users_ls)


    """ Ask remote server to create new group
            newGroupName    : the group Uid of new group to create
            return          : (exitStatus, [stdoutLine ...])
    """
    def groupAdd(self, newGroupName):
        return self.machine.sshAgent.query(self.cmd_group_add % newGroupName)


    """ Ask remote server to delete a group
            groupNameToDel  : the groupUid of group to delete
            return          : (exitStatus, [stdoutLine ...])
    """
    def groupDel(self, groupNameToDel):
        return self.machine.sshAgent.query(self.cmd_group_del % groupNameToDel)


    """ Ask remote server to list all groups
            return  : (exitStatus, [stdoutLine ...])
    """
    def groupsLs(self):
        return self.machine.sshAgent.query(self.cmd_groups_ls)


    """ Ask remote server to list all groups of a specified user
            userName    : the memberUid of the user
            return      : (exitStatus, [stdoutLine ...])
    """
    def getGroupsOfUser(self, userName):
        return self.machine.sshAgent.query(self.cmd_ls_groups_of_user % (self.userConf.get("smbldap", "groups_searchbase"), userName))


    """ Return the list of all groups a specified user can be added to.
            Retreived through {groupsLs \ getGroupsOfUser}

            userName    : the memberUid of the user
            return      : (exitStatus, [stdoutLine ...])
    """
    def getGroupsAvailableForUser(self, userName):

        result = ""

        error, all_groups = self.groupsLs()

        if (not error):
            error, groups_of_user = self.getGroupsOfUser(userName)

            if (not error):
                for group in groups_of_user:
                    if (group != ''):
                        all_groups.remove(group)

                result = all_groups

            else:
                result = groups_of_user

        else:
            result = all_groups
    
        return (error, result)


    """ Ask remote server to add a user to a grou
            user    : the UID of the user
            group   : the UID of the group
            return  : (exitStatus, [stdoutLine ...])
    """
    def add_user_to_group(self, user, group):
        return self.machine.sshAgent.query(self.cmd_add_user_to_group % (user, group))


    """ Ask remote server to remove a user from a group
            user    : the UID of the user
            group   : the UID of the group
            return  : (exitStatus, [stdoutLine ...])
    """
    def remove_user_from_group(self, user, group):
        return self.machine.sshAgent.query(self.cmd_remove_user_from_group % (user, group))


    """ Displays this instance in TTY
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
        print "| | |-cmd_groups_ls\t: %s" % self.cmd_ls_groups_of_user
        print "| | |-cmd_add_user_to_group\t: %s" % self.cmd_add_user_from_group
        print "| | |-cmd_remove_user_from_group\t: %s" % self.cmd_remove_user_from_group


    """ Init method
            conf        : Pacha global config
            userConf    : machine specific configuration
            index       : index of Service in the list of Services in conf file
            machine     : machine that owns this Service
    """
    def __init__(self, conf, userConf, machine):
        self.conf = conf
        self.userConf = userConf
        self.machine = machine

        section = "smbldap"

        try :
            self.cmd_user_add = self.conf.val[section]["cmd_user_add"]
            self.cmd_user_del = self.conf.val[section]["cmd_user_del"]
            self.cmd_users_ls = self.conf.val[section]["cmd_users_ls"] % self.userConf.get(section, "users_searchbase")
            self.cmd_group_add = self.conf.val[section]["cmd_group_add"]
            self.cmd_group_del = self.conf.val[section]["cmd_group_del"]
            self.cmd_groups_ls = self.conf.val[section]["cmd_groups_ls"] % self.userConf.get(section, "groups_searchbase")
            self.cmd_ls_groups_of_user = self.conf.val[section]["cmd_ls_groups_of_user"]
            self.cmd_add_user_to_group = self.conf.val[section]["cmd_add_user_to_group"]
            self.cmd_remove_user_from_group = self.conf.val[section]["cmd_remove_user_from_group"]
        except (ConfigParser.NoOptionError,
                ConfigParser.NoSectionError) :
            print "--ERROR Parsing config file--"
            pass


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
