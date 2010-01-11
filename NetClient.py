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


from NetArthur import *

class Client(object):
    def __init__(self,
                 host_name = "127.0.0.1", s_type = "TCP",
                 port = "", debug = 0):
        """            
        @param host_name: Host name or IP address
        """
        self.host_name = host_name
        self.level = debug
        self.__log__ (self.level,
                      "init raw Client host = %s" % 
                      self.host_name)

    def __log__(self, level, message):
        if (self.level < level):
            return
        print "CL : %s" % message


class NetClient(SocketProcess, Client):
    def __init__(self,
                 host_name = "127.0.0.1", s_type = "TCP",
                 port = "", debug = 0):
        """            
        @param host_name: Host name or IP address
        """
        SocketProcess.__init__(self, s_type, debug, port)
        Client.__init__(self, host_name, s_type, port, debug)

        self.__log__ (self.level,
                      "init Client host = %s, son of SocketProcess" % 
                      self.host_name)

