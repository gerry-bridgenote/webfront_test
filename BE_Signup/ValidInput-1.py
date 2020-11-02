import unittest, requests, time, sys, os, path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from settings import *

"""
Scenario:
1. Input sign up form with proper input

Expected Result:
1. Redirect to confirm page
2. Click signup
3. Redirect to dashboard page as a new user
"""
class Signup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_LOCATION)
        self.base_url = BASE_URL

    def test_signup_properly(self):
        db = connection()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) from tb_cmpy_account")
        result=cursor.fetchone()
        company_id = int(result[0]) + 1
        db.close()

        driver = self.driver
        driver.get(self.base_url + '/signup/invoice/index')
        driver.execute_script("""var jquery_script = document.createElement('script'); 
        jquery_script.src = 'https://code.jquery.com/jquery-3.1.0js';
        jquery_script.onload = function(){ var $ = window.jQuery;};""")
        time.sleep(1)

        #fill in sign up form & use total record + 1 to distinguish account
        driver.find_element_by_id("email").send_keys('test' + str(company_id) + '@example.com')
        driver.find_element_by_id("password").send_keys('Test1234')
        driver.find_element_by_id("company_name").send_keys('Testing Company')
        driver.find_element_by_id("fiscal_year_ending").send_keys('11')
        Select(driver.find_element_by_id('currency')).select_by_visible_text('USD')
        driver.find_element_by_id("referral_code").send_keys('12345')
        driver.find_element_by_link_text('Terms And Conditions').click()
        time.sleep(1)
        driver.execute_script("document.getElementById('end-terms').scrollIntoView();")
        time.sleep(1)
        driver.find_element_by_id('close_terms').click()
        time.sleep(1)
        driver.find_element_by_id('agreement').click()

        #confirmation page
        current_url = driver.current_url
        driver.find_element_by_xpath("//*[contains(text(), 'Sign Up')]").click()
        WebDriverWait(driver, 5).until(EC.url_changes(current_url))
        current_url = driver.current_url
        self.assertEqual(driver.current_url, self.base_url + '/signup/invoice/confirm')
        time.sleep(1)
        driver.find_element_by_xpath("//*[contains(text(), 'Sign Up')]").click()

        #dashboard page after login
        WebDriverWait(driver, 5).until(EC.url_changes(current_url))
        self.assertEqual(driver.current_url, self.base_url + '/menu/dashboard')
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
