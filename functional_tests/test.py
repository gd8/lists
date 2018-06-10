from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()    
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User can go to page
        self.browser.get(self.live_server_url)

        # sees the title and header mentions to-dos
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('To-Do', header_text)

        # User can enter new todos with a input that has a placeholder
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User enters Get a haircut as a to do
        inputbox.send_keys('Get a haircut')

        # User hits enter
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)

        # User enters Read a book as a to do
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Read a book')

        # User hits enter
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)

        # User sees "1: Get a haircut" in a todos table
        self.check_for_row_in_list_table('1: Get a haircut')
        # User sees "2: Read a book" in a todos table
        self.check_for_row_in_list_table('2: Read a book')

        self.fail('Finish the test!')
        # User can come back to page and see todos
        
