from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/')
page = driver.page_source