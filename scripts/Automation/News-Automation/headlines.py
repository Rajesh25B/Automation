import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Automate the headlines in a headless mode:
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

# non-headless mode
# driver = webdriver.Chrome()
path = '//*[@id="news-list"]/div/div/h2/a'

driver.get('https://www.cricbuzz.com/cricket-news/latest-news')
vals = driver.find_elements(by=By.XPATH, value=path)
time.sleep(5)

# Automate the latest-news: Export them into a .csv file

headlines = []
links = []
for item in vals:
    headlines.append(item.text)
    links.append(item.get_attribute('href'))

my_data = {'headlines': headlines, 'links': links}

data = pd.DataFrame(my_data)
# data.to_csv('headlines.csv')
data.to_csv('headlines-headless-1.csv')

driver.quit()
