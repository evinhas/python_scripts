#! /usr/bin/python
import csv
import sys, getopt

inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'Arguments were not included. \nUsage: csv_remove_commas.py -i <inputfile> -o <outputfile>'
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print 'Usage: csv_remove_commas.py -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

with open(inputfile, "rb") as infile, open(outputfile, "wb") as outfile:
	reader = csv.reader(infile)
	writer = csv.writer(outfile)
	for row in reader:
		row1 = []
		value1 = ""
		for value in row:
			value1 = value.replace(",","")
			row1.append(value.replace(",",""))
		#print(row1)
		writer.writerow(row1)

