from selenium import webdriver


#firefoxOptions = webdriver.FirefoxOptions()
#firefoxOptions.headless=True
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert 'worked successfully' in browser.title
