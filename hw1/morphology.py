import fst

class Parser():

	def __init__(self):
		pass

	def generate(self, analysis):
		output = ['p','a','n','i','c','k','e','d']
		return ''.join(output)

	def parse(self, word):
		output = ['p','a','n','i','c','+past form']
		return ''.join(output)


if __name__ == '__main__':
	user_input = raw_input()
	p = Parser()
	if user_input:
		print user_input, '-->',
		print p.parse(user_input)
