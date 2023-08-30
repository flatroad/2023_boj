import sys
readline = sys.stdin.readline

while(True):
	try:
			str = readline()
			if (str.__len__() == 0):
				break
			print(str, end='')
	except:
		break
  