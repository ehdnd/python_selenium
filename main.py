# selenium 4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://google.com")

search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys("hello")
search_bar.send_keys(Keys.ENTER)

search_results = WebDriverWait(browser, 10).until(
EC.presence_of_all_elements_located((By.CLASS_NAME, "g")))

print(search_results)

input()

browser.quit()