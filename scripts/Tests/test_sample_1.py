import unittest
import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SeleniumBasedTests(unittest.TestCase):
    def setUp(self):
        # for individual drivers
        # driver_path = r'C:\Users\RAJESH\Desktop\win-env\chromedriver.exe'
        # service = Service(executable_path=driver_path)
        # self.driver = webdriver.Chrome(service=service)

        # driver with global env PATH setting, without headless-mode
        # self.driver = webdriver.Chrome()

        # with headless-mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        self.driver = webdriver.Chrome(options=options)

    def test_h1_tag(self):
        self.driver.get('http://127.0.0.1:5500/app/index.html')
        h1 = self.driver.find_element(by=By.TAG_NAME, value='h1')
        self.assertEqual(h1.text, 'H1 HEADING')
        # time.sleep(5)

    def test_radio_button_click(self):
        self.driver.get('http://127.0.0.1:5500/app/index.html')
        self.driver.find_element(By.ID, 'radio').click()
        # time.sleep(5)

    def test_get_all_links(self):
        self.driver.get('https://www.google.co.in/')
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        a = [link.text for link in links]
        print(a)
        # time.sleep(5)

    def test_confirm_alerts(self):
        self.driver.get('http://127.0.0.1:5500/app/index.html')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(5)
        Alert(self.driver).accept()  # Confirm a alert dialog.
        time.sleep(8)

    def test_alert_text(self):
        self.driver.get('http://127.0.0.1:5500/app/index.html')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        alert_text = Alert(self.driver).text
        self.assertEqual('Hey there...', alert_text)
        time.sleep(5)
        Alert(self.driver).dismiss()
        time.sleep(5)

    def test_maximize_tab(self):
        self.driver.get('http://127.0.0.1:5500/app/index.html')
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.minimize_window()
        time.sleep(5)

    def test_file_upload(self):
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get('http://127.0.0.1:5500/app/index.html')
        self.driver.find_element(By.ID, 'file').send_keys(
            r'C:\Users\RAJESH\Pictures\Screenshots\Screenshot (975).png'
        )
        time.sleep(8)

    def test_get_top_trending_links(self):
        self.driver.get('https://www.google.co.in/')
        self.driver.find_element(
            By.XPATH,
            '//*[@id="APjFqb"]'
        ).send_keys('Top 5 trending topics', Keys.ENTER)
        # scroll down the window
        self.driver.execute_script('window.scroll(0, 600)')
        time.sleep(8)

    def test_get_cookies(self):
        self.driver.get('https://www.google.co.in/')
        cookies = self.driver.get_cookies()
        print([cookie for cookie in cookies], end='\n')
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
