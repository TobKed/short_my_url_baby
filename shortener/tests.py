from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def fill_form(elem, value):
        elem.send_keys(value)

    def fill_form_by_id(self, form_element_id, value):
        elem = self.driver.find_element_by_id(form_element_id)
        return self.fill_form(elem, value)

    def navigate(self):
        self.driver.get(self.url)


class HomePage(BasePage):
    url = "http://localhost:8000"

    def fill_url(self, value):
        elem = self.driver.find_element_by_id("id_url")
        elem.clear()
        self.fill_form(elem, value)

    def submit(self):
        self.driver.find_element_by_css_selector(".btn").click()

    def get_url(self):
        elem = self.driver.find_element_by_id("id_url")
        return elem.get_property("value")


def get_final_url(driver, url):
        test_page = BasePage(driver)
        test_page.url = url
        test_page.navigate()
        return driver.current_url


class LogInTest(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_make_short_url(self):
        test_url = "https://www.jmr.pl/"
        homepage = HomePage(self.browser)
        homepage.navigate()
        homepage.fill_url(test_url)
        homepage.submit()
        short_url = homepage.get_url()
        final_url = get_final_url(self.browser, short_url)
        StaticLiveServerTestCase.assertEqual(self, test_url, final_url)

    def tearDown(self):
        self.browser.close()
