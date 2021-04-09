import time
from selenium import webdriver

wd = webdriver.Chrome("/Volumes/Geozedo60/Python/chromedriver")
wd.get("https://www.google.com")

time.sleep(3)
html = wd.page_source
print(html)

wd.close()
