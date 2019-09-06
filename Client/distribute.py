from distributing import *
from sending import configure_distribute

#
# Copyright (c) Carlos Tojal (carlostojal)
# distribute.py
# PyChat
# github.com/carlostojal/PyChat
#

s = configure_distributor()
configure_distribute()
configure_client(s)
upload()
