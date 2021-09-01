from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://psd.bits-pilani.ac.in/Login.aspx")

soup = BeautifulSoup(driver.page_source, "html.parser")

USERNAME_FIELD = "TxtEmail"
username = "YOUR_EMAIL"
PASSWORD_FIELD = "txtPass"
password = "YOUR_PASSWORD"
SUBMIT = "Button1"

username_field = driver.find_element_by_id(USERNAME_FIELD)
password_field = driver.find_element_by_id(PASSWORD_FIELD)
submit = driver.find_element_by_id(SUBMIT)

username_field.send_keys(username)
password_field.send_keys(password)

submit.click()

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.find_element_by_link_text("Fill Station Preference").click()
soup = BeautifulSoup(driver.page_source, "html.parser")

lst = soup.find_all('span', {"class": "spanclass uiicon ui-icon-arrowthick-2-n-s"})
from pprint import pprint
stations = []
for span in lst:
    stations.append(span.text)

driver.quit()
