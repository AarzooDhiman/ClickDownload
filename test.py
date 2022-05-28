from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


op = webdriver.ChromeOptions()
op.add_argument = {'user-data-dir':'/Users/aarzoodhiman/Library/Application Support/Google/Chrome/Default'}


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
##driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=op)

driver.get("https://pair-code.github.io/covid19_symptom_dataset/?country=GBm")


element = driver.find_element_by_class_name("download").click()
element = driver.find_element_by_xpath("//div[contains(text(), 2017)]").click()
element = driver.find_element_by_xpath("//div[contains(@span, Subregions)]").click()
element = driver.find_element_by_xpath("//div[contains(text(), 'Sign in')]").click()
element = driver.find_element_by_xpath("//input[contains(@type, email)]").send_keys("aarzoodhiman@hotmail.com")
element = driver.find_element_by_xpath("//span[contains(text(), 'Next')]").click()
#element = driver.find_element_by_class_name("VfPpkd-vQzf8d").click()





