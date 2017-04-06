import csv

filename = 'ch02-data.csv'

data = []
try:
	with open(filename,'r',encoding = 'utf-8') as f:
		reader = csv.reader(f)
		header = reader.__next__()#python 3.x要用__next__()
		data = [row for row in reader]
except csv.Error as e:
	print("Error reading CSV file at line %s: %s"%(reader.line_num, e))
	sys.exit(-1)

if header:
	print(header)
	print('==================================')

for datarow in data:
	print(datarow)