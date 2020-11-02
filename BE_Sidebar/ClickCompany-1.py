import unittest, time, sys, os, path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from settings import *

"""
Scenario:
1. Login from last newly created user test with English language setting (refer to BE_Signup-ValidInput-1)
2. click OK button from tutorial
3. Click company button

Expected Result:
1. Redirect to https://bebasakuntansi.com
"""
class SidebarCompany(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_LOCATION)
        self.base_url = BASE_URL

    def test_signup_properly(self):
        driver = self.driver
        db = connection()
        cursor = db.cursor()
        cursor.execute("SELECT * from tb_cmpy_account WHERE language_id=2 ORDER BY id DESC LIMIT 1")
        user=cursor.fetchone()
        db.close()

        #login
        driver.get(self.base_url + '/login')
        driver.find_element_by_id("inputEmail").send_keys(user[4])
        driver.find_element_by_id("inputPassword").send_keys('Test1234')
        driver.find_element_by_css_selector(".btn-primary").click()
        time.sleep(1)

        driver.find_element_by_css_selector(".bnmst_submitbtn").click()
        time.sleep(1)
        current_url = driver.current_url
        driver.find_element_by_xpath("//*[@id='gronavfoot']/li[1]").click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        self.assertEqual(driver.current_url.rstrip('/'), 'https://bebasakuntansi.com')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
