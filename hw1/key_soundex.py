from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
	"""
	Returns an FST that converts letters to numbers as specified by
	the soundex algorithm
	"""

	# Let's define our first FST
	f1 = FST('soundex-generate')

	# Indicate that '1' is the initial state
	f1.add_state('start')
	f1.initial_state = 'start'

	f1.add_state('non-first letter')
	f1.set_final('non-first letter')

	# Add the rest of the arcs
	for letter in string.ascii_letters:
		f1.add_arc('start', 'non-first letter', (letter), (letter))
		f1.add_arc('non-first letter', 'non-first letter', (letter), ('0'))
	return f1

def truncate_to_three_digits():
	"""
	Create an FST that will truncate a soundex string to three digits
	"""

	# Ok so now let's do the second FST, the one that will truncate
	# the number of digits to 3
	f2 = FST('soundex-truncate')

	# Indicate initial and final states
	f2.add_state('1')
	f2.initial_state = '1'
	f2.set_final('1')

	# Add the arcs
	for letter in string.letters:
		f2.add_arc('1', '1', (letter), (letter))

	for n in range(10):
		f2.add_arc('1', '1', str(n), str(n))

	return f2

def add_zero_padding():
	# Now, the third fst - the zero-padding fst
	f3 = FST('soundex-padzero')

	f3.add_state('1')
	f3.add_state('2')
	
	f3.initial_state = '1'
	f3.set_final('2')

	for letter in string.letters:
		f3.add_arc('1', '1', letter, letter)
	for number in xrange(10):
		f3.add_arc('1', '1', str(number), str(number))
	
	for n in range(10):
		f3.add_arc('1', '2', (), '000')
	return f3

if __name__ == '__main__':
	user_input = raw_input().strip()
	f1 = letters_to_numbers()
	f2 = truncate_to_three_digits()
	f3 = add_zero_padding()

	if user_input:
		print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
