from selenium import webdriver
from getpass import getpass

username = input("Enter Username/Email: ")
password = getpass("Enter Password: ")

driver = webdriver.Chrome('/Users/wreckit/Downloads/WebDriver/chromedriver 2')
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id('email')
username_textbox.send_keys(username)

password_text = driver.find_element_by_id('pass')
password_text.send_keys(password)

login = driver.find_element_by_name('login')
login.submit()