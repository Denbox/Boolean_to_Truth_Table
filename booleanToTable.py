#!/usr/bin/python
import sys
header = raw_input('Header: ') #describes boolean values and output
inputs = header.split()[:-1] #input nodes
file_name = header.split()[-1] #affected node
expression = raw_input('Expression: ') #boolean to parse
exp = expression.replace('(', ' ( ').replace(')', ' ) ')
#cleaned to separate parenthesis from words (spaces removed later anyway)
#expression is valid if it can be parsed by eval()

output = open(file_name+'.csv', 'w') #file to write to
output.write(header+'\n') #top line of output file
for i in range(2 ** len(inputs)): #all possible input combinations
				b = '{0:b}'.format(i).zfill(len(inputs)) #b = i as binary string
				rep = dict(zip(inputs, b)) #replace input node with binary value
				e = ' '.join([rep[i] if i in rep else i for i in exp.split()])
				#e contains the substituted expression that can be evaluated
				output.write(' '.join(b)+' '+str(int(eval(e)))+'\n')
				#print out values of input nodes and corresponding evaluation
