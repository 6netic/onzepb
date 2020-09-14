
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
	""" Testing if ..."""

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Didier wants to access the homepage
		self.browser.get('http://localhost:8000') 
		
		# He notices the page title
		self.assertIn('Pur Beurre', self.browser.title)
		self.fail('Test is finished !')
		
		# She is invited to enter a to-do item straight away 
		#[...rest of comments as before] 
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')



