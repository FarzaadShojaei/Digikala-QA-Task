from selenium.webdriver.common.by import By
from time import sleep
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.PhoneNumber_Textbox_name = "username"
        self.Submit_Button_Xpath = " //button[@type='submit']"

    def enter_PhoneNumber(self, UserPhoneNumber):
        self.driver.find_element(By.NAME, self.PhoneNumber_Textbox_name).send_keys(UserPhoneNumber)

    def Click_On_Login_Button(self):
        self.driver.find_element(By.XPATH, self.Submit_Button_Xpath).click()
        sleep(3)