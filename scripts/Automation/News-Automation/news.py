'''
1. Get news headlines by XPATH and store them in a .csv using pandas.
2. Assign a custom name to the csv file that is unique everyday.
3. Convert .py to .exe file, so that we can get breaking news whenever we want.
    * pip install pyinstaller
    * Make sure to be in the same directory in shell and run below cmd.
        pyinstaller --onefile news.py
    * we get two folders [build, dist], in dist folder => news.exe 
    * news.exe => run inside a terminal/shell.
'''

from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import os
import sys
import time

from datetime import datetime

application_path = os.path.dirname(sys.executable)

# utilize datetime module to name the csv files according to that particular
# date
now = datetime.now()
month_day_year = now.strftime('%m%d%Y')  # MMDDYY


# Automate the headlines in a headless mode:
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

path = '//*[@id="app"]/div/div[3]/div[2]/div[4]/div[4]/div[1]/div/div/figure/a/figcaption'  # noqa

driver.get('https://timesofindia.indiatimes.com/')
vals = driver.find_elements(by=By.XPATH, value=path)
time.sleep(5)

# Automate the latest-news: Export them into a .csv file
headlines = []

for item in vals:
    headlines.append(item.text)

my_data = {'headlines': headlines}

data = pd.DataFrame(my_data)
file_name = f'headlines-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
data.to_csv(final_path)

driver.quit()
