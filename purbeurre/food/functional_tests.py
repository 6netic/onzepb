
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
	""" Testing if ..."""

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_user_can_access_homepage_when_clicking_on_logo(self):
		pass



	def test_user_can_look_for_product(self):
		pass


	def test_user_can_authenticate(self):
		pass


	def test_can_start_a_list_and_retrieve_it_later(self):#to be changed
		# Didier wants to access the homepage
		self.browser.get('http://localhost:8000') 
		
		# He notices the page title
		self.assertIn('Pur Beurre', self.browser.title)
		self.fail('Test of the title is OK !')

		#He notices the name of the website


		#He notices a logo on which he can click to get back to homepage
		#self.
		
		# She is invited to enter a to-do item straight away 
		#[...rest of comments as before] 
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')



