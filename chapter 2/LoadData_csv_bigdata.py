import numpy

data = numpy.loadtxt('ch02-data.csv',dtype='|S',delimiter=',')
for datarow in data:
	print(datarow)