from Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=driver_service)
driver.get("https://www.digikala.com/users/login/")
driver.implicitly_wait(4)

login=Login(driver=driver)

login.enter_PhoneNumber('09371434110')
login.Click_On_Login_Button()
driver.implicitly_wait(3)




