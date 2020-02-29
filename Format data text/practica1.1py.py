#! /usr/bin/env python
import re

regex = re.compile('[A-Z][a-z][a-z] [1-2][0-9] [0-1][0-9]:[0-5][0-9]:[0-5][0-9]')
regex1 = re.compile('[A-Z][a-z][a-z] [1-2][0-9] [2][0-4]:[0-5][0-9]:[0-5][0-9]')
regex11 = re.compile('[A-Z][a-z][a-z]  [1-9] [0-1][0-9]:[0-5][0-9]:[0-5][0-9]')
regex111 = re.compile('[A-Z][a-z][a-z] [1-9] [2][0-4]:[0-5][0-9]:[0-5][0-9]')
regex1111 = re.compile('[A-Z][a-z][a-z] [3][0-1] [0-1][0-9]:[0-5][0-9]:[0-5][0-9]')
regex11111 = re.compile('[A-Z][a-z][a-z] [3][0-1] [2][0-4]:[0-5][0-9]:[0-5][0-9]')
regex2 = re.compile('[A-Z][a-z][a-z]  \d \d\d:\d\d:\d\d')
regErr= re.compile('[F][e][b] [3][0-9] [0-1][0-9]:[0-5][0-9]:[0-5][0-9]')
regErr1= re.compile('[A][p][r] [3][1-9] ')
regErr2= re.compile('[J][u][n] [3][1-9] ')
regErr3= re.compile('[S][e][t] [3][1-9] ')
regErr4= re.compile('[N][o][v] [3][1-9] ')

with open('dates.txt','r') as f:
	for line in f:
		print(line)
		if regErr.match(line) or regErr1.match(line) or regErr2.match(line) or regErr3.match(line) or regErr4.match(line):
			print("incorrect")
		elif regex.match(line) or regex1.match(line) or regex11.match(line) or regex111.match(line) or regex1111.match(line) or regex11111.match(line):
			print("correcto")
	
		else:
			print("incorrecto")

