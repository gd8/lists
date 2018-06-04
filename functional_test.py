from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()    
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User can go to page
        self.browser.get('http://localhost:8000')

        # sees the title mentions to-dos
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish test later')

        # User can enter new todos
        # User can come back to page and see todos


if __name__ == '__main__':
    unittest.main()