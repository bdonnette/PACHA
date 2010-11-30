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


"""
"""
class Pacha_config(object):

    """
    """
    def __init__(self, conf_parser):

        ## Values in conf_parser file ################
        # [general]
        key_general = "general"
        values_general = {
            # These filenames will be overidden for their PixMap values in View_MainWindow
            "icon_levels"           : conf_parser.get(key_general, "icon_levels").split(),

            "ssh_win_cmd_no_pass"   : conf_parser.get(key_general, "ssh_win_cmd_no_pass"),
            "ssh_win_cmd_pass"      : conf_parser.get(key_general, "ssh_win_cmd_pass"),
            "ssh_lnx_cmd"           : conf_parser.get(key_general, "ssh_lnx_cmd"),
            "ui_refresh_interval"   : conf_parser.get(key_general, "ui_refresh_interval"),
            "hb_status_command"     : conf_parser.get(key_general, "hb_status_command")
        }

        # [smbldap]
        key_smbldap = "smbldap"
        values_smbldap = {
            "cmd_user_add"          : conf_parser.get(key_smbldap, "cmd_user_add"),
            "cmd_user_del"          : conf_parser.get(key_smbldap, "cmd_user_del"),
            "cmd_users_ls"          : conf_parser.get(key_smbldap, "cmd_users_ls"),
            "cmd_group_add"         : conf_parser.get(key_smbldap, "cmd_group_add"),
            "cmd_group_del"         : conf_parser.get(key_smbldap, "cmd_group_del"),
            "cmd_groups_ls"         : conf_parser.get(key_smbldap, "cmd_groups_ls"),
            "cmd_ls_groups_of_user" : conf_parser.get(key_smbldap, "cmd_ls_groups_of_user"),
            "cmd_add_user_to_group"     : conf_parser.get(key_smbldap, "cmd_add_user_to_group"),
            "cmd_remove_user_from_group"    : conf_parser.get(key_smbldap, "cmd_remove_user_from_group")
        }

        self.val = {key_general     : values_general,
                    key_smbldap     : values_smbldap}


        ## Constants ############################
        # Levels (these values must reflect the icon_levels conf values)
        self.STATE_GREEN    = 0
        self.STATE_YELLOW   = 1
        self.STATE_RED      = 2
        self.STATE_UNKNOWN  = 3

        # Heartbeat
        self.HB_UNKNOWN     = "Unknown"
        self.HB_ERROR       = "Error"
        # These are answers expected from HB
        self.HB_LOCAL       = "local"
        self.HB_FOREIGN     = "foreign"
        self.HB_ALL         = "all"
        self.HB_NONE        = "none"
        self.HB_TRANSITION  = "transition"


# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
