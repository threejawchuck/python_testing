import Widget 

import unittest

# this is a class that has a bunch of tests 
class TestWidget (unittest.TestCase):
	def setUp (self):
		self.w = Widget.Widget()
		pass

	def tearDown (self):
		del self.w

	def test_getNumAccount (self):
		#default better be zero
		self.assertEqual(0, self.w.getNumAccount())
		pass

	def test_addAccount (self):
		# check that there's nothing there
		self.assertEqual(0, self.w.getNumAccount())

		# now add an account
		id, account = self.w.addAccount()

		# better be 1
		self.assertEqual(1, self.w.getNumAccount())

		pass

	def test_getAccount (self):
		# check that there's nothing there
		self.assertEqual(0, self.w.getNumAccount())

		# now add an account
		actual_id, actual_account = self.w.addAccount()

		# now use that id to get the account back
		self.assertEqual(actual_account, self.w.getAccount(actual_id))

		# now check all the error conditions
		# first arg is the exceptino your looking for, second is the function, and everything after that is passed to arg 2
		self.assertRaises(RuntimeError, self.w.getAccount, -1)
		self.assertRaises(RuntimeError, self.w.getAccount, actual_id+1)





# take every test in this class and use it to define a suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestWidget)

# now register this test suite with the test runner
unittest.TextTestRunner(verbosity=2).run(suite)