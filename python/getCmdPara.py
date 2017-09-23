#!/usr/bin/python

import sys 

def isIntNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def getInputPara():
	flag = 0
	for i in range(1, len(sys.argv)):
		if (".xls" in sys.argv[i] or ".xlsx" in sys.argv[i]):
			flag = flag + 1
			print("excel file:" + sys.argv[i])
		if (isIntNumber(sys.argv[i])):
			flag = flag + 1
			print("language index:" + sys.argv[i])
	if (flag == 2):
		print("get you command, please wait translate finish!")
		return True
	else:
		print("you input param error!")


getInputPara()
