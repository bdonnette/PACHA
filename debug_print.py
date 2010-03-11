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

class debug_print(object):
    ''' Prints upon debug level '''
    def __init__(self, level):
        ''' level is instantiated as the app debug level'''
        self.level = level

    def dprint(self, string, level):
        ''' prints if level < self.level, meaning that
        initing with level = 0 means silent '''
        if (level < self.level):
            print string

