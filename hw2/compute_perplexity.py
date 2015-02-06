import sys
import math
import json

def eval(model_file, data_file):
	sum_log_prob = 0.0
	f = open(data_file)
	lm = json.loads(open(model_file).read())
	N = 0.0
	for s in f:
		tokens = s.split(' ')
		for t in tokens:
			N += 1
			if t in lm['']:
				sum_log_prob += lm[''][t]
			else:
				sum_log_prob += lm['']['UNK']
	print 'Te Rutherford %s' % math.exp(- sum_log_prob / N)

if __name__ == '__main__':
	eval('my_unigram_model.json', sys.argv[1])
