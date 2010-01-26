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

import sys
from PyQt4 import QtCore, QtGui
from HMI_object import *

class HMI_action(HMI_object):
    ''' This class defines an HMI element (on which a line is to be based)
    so as to define a generic active HMI element object
    to be derived into whatever element will have to be'''
    def __init__(self, do_label = "do", command = "echo toto"):
        ''' Additions from HMI_object :
        - "Do it" button
        '''
        self.do_button = QtGui.QPushButton(do_label)
