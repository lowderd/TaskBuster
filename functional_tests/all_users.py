from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # Basic setup for test case
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Basic teardown for test case
        self.browser.quit()

    def test_it_worked(self):
        # Check that django install worked
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)


if __name__ == "__main__":
    unittest.main(warnings='ignore')