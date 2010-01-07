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
# Generic client and server
# Ought to be protocol-agnostic, should be specialized

import socket
import sys

class SocketProcess(object):
    def __init__(self, s_type = "TCP", debug = 0, port = "1025"):
        if (s_type == "TCP"):
            self.stype = (socket.AF_INET, socket.SOCK_STREAM)
        elif (s_type == "UDP"):
            self.stype = (socket.AF_INET, socket.SOCK_DGRAM)
        elif (s_type == "TCP6"):
            self.stype = (socket.AF_INET6, socket.SOCK_STREAM)
        elif (s_type == "UDP6"):
            self.stype = (socket.AF_INET6, socket.SOCK_DGRAM)
        else:
            # Unsupportable...
            raise TypeError

        # Other elements
        self.port = port
        self.debug = debug

        if (0 < self.debug):
            print "SocketProcess init %s" % s_type

        self.sock = socket.socket(self.stype[0], self.stype[1])

    def __log__(self, level, message):
        if (self.debug < level):
            return
        print "NA : %s" % message
