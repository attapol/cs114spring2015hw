import unittest
from recognizer import is_phone_number, is_email_address
from soundex import letters_to_numbers, truncate_to_three_digits, add_zero_padding, soundex_convert
from morphology import Parser

class TestHW1(unittest.TestCase):

	def setUp(self):
		self.f1 = letters_to_numbers()
		self.f2 = truncate_to_three_digits()
		self.f3 = add_zero_padding()
		self.mparser = Parser()

	def is_phone_number(self):
		self.assertTrue(is_phone_number('153-523-1295'))
		self.assertFalse(is_phone_number('15E-523-1295'))

	def is_email_address(self):
		self.assertTrue(is_email_address('tet@brandeis.edu'))
		self.assertFalse(is_email_address('tet@brandeis'))
		self.assertFalse(is_email_address('brandeis.edu'))

	def test_letters(self):
		self.assertEqual("".join(self.f1.transduce(x for x in "washington")), "w25235")
		self.assertEqual("".join(self.f1.transduce(x for x in "jefferson")), "j1625")
		self.assertEqual("".join(self.f1.transduce(x for x in "adams")), "a352")
		self.assertEqual("".join(self.f1.transduce(x for x in "bush")), "b2")

	def test_truncation(self):
		self.assertEqual("".join(self.f2.transduce(x for x in "a33333")), "a333")
		self.assertEqual("".join(self.f2.transduce(x for x in "123456")), "123")
		self.assertEqual("".join(self.f2.transduce(x for x in "11")), "11")
		self.assertEqual("".join(self.f2.transduce(x for x in "5")), "5")

	def test_padding(self):
		self.assertEqual("".join(self.f3.transduce(x for x in "3")), "300")
		self.assertEqual("".join(self.f3.transduce(x for x in "b56")), "b560")
		self.assertEqual("".join(self.f3.transduce(x for x in "c111")), "c111")

	def test_soundex(self):
		self.assertEqual(soundex_convert("Jurafsky"), "j612")

	def test_morphology(self):
		self.assertEqual(self.mparser.parse("lilac+ing"), "lilacking")
		self.assertEqual(generate("lick+ed"), "licked")
		self.assertEqual(generate("sync+ing"), "syncing")

if __name__ == '__main__':
	unittest.main()
