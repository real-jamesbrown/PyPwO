#!/usr/bin/env python

def error(msg):
	print("[EE] {0}".format(msg))
	

try:
	import lxml
except ImportError, msg:
	error("You have to install lxml")


