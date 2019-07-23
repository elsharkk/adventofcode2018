import sys

# quick summary of problem
#	puzzle input is a series of changes in frequency
#	it is a list of + and -
#	add them all up 
# test cases
#	+1, +1, +1 = 3
#	+1, +1, -2 = 0
#	-1, -2, -3 = 6

def parse_string(line):
	return int(line)

total = 0
with open(r'..\data\d1p1.txt', 'r') as data:
	for line in data.readlines():
		total = total + parse_string(line)

print('Total of all numbers:',total)

