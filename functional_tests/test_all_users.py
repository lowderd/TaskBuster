from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        # Basic setup for test case
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Basic teardown for test case
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        # Check that django install worked
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_elements_by_tag_name("h1")
        # Second h1 tag is the one that changed color, so index into list of elements
        self.assertEqual(h1[1].value_of_css_property("color"), "rgba(200, 50, 255, 1)")
