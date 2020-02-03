# This script filters the raw contig file based on 
# a certain threshold of the coverage

input_file = 'raw.txt'
output_file = 'process.txt'

f = open(input_file)
p = open(output_file, 'w')

thres = 10
line = f.readline()
count = 0

while(line):
	if len(line) == 0:
		break
	# When the new line is a header
	if line[0] == '>':
		count += 1
		# Get the coverage value
		cov = line.split('_')[5]
		# Convert string to a float number
		cov = float(cov)
		# When coverage is larger than threshold
		if cov >= thres:
			# Write the header into the new file
			p.write(line)
			line = f.readline()
			while(line[0] != '>'):
				p.write(line)
				line = f.readline()
				if len(line) == 0:
					break
		# When coverage is less than threshold
		else:
			line = f.readline()
			while(line[0] != '>'):
				line = f.readline()
				if len(line) == 0:
					break
print(count)
print('Edit success!')
