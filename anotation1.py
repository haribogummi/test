# coding: UTF-8

import re
import sys
import csv

def position():
	dic1={}
	dic2={}
	f=open("snp_test.csv","rb")	
	datareader = csv.reader(f)

	for row in datareader:
		dic2={row[1]:row[2]}
		dic1.update(dic2)
	return dic1
	f.close()


def search():
	dic1=position()
	c=0
	print "Position,Nuc,n_p,Start,End,Type"
	for k,v in dic1.iteritems():
		f=open("gfftest.gff","r")
		lines = f.readlines()

		for line in lines:
			if re.match("#",line) == None:
				line=line.rstrip("\n")
				line=line.split("\t")
				result=()
				if int(k) >= int(line[3]) and int(k) <= int(line[4]):
					print k+","+v+","+line[5]+","+line[3]+","+line[4]+","+line[2]

##問題点　+-がででこない(表記の問題?)　chromeson を書き出さない条件分布ないしgene,sRNAなどのTypeをまとめる方法が必要
#	f.close()



##---------------------------------##

if __name__ == '__main__':
	position()
	search()
