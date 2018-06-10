from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()    
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User can go to page
        self.browser.get('http://localhost:8000')

        # sees the title and header mentions to-dos
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('To-Do', header_text)
        self.fail('Finish test later')

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

        # User sees "1: Get a haircut" in a todos table
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Get a haircut' for row in rows)
        )

        self.fail('Finish the test!')
        # User can come back to page and see todos
        


if __name__ == '__main__':
    unittest.main()