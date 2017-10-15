#!/usr/bin/env python3
import webbrowser
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s[%(levelname)s]: %(message)s')

def get_lookup_cmd():
	if len(sys.argv) > 1:
		#get command from command line.
		cmd = ''.join(sys.argv[1])
		logging.debug('cmd = ' + str(cmd))
		return cmd
	else:
		print("Usage: webcmd your_linux_commad! Like this:")
		print("./webcmd find")

url = 'http://man.linuxde.net/' + get_lookup_cmd()
webbrowser.open(url)
