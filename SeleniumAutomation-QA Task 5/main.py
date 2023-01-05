from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from Login import Login

# driver=webdriver.chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=driver_service)


# Browser Action 1 > Open Web
driver.get("https://www.digikala.com/profile/orders/?activeTab=in_progress")



# Browser Action  1 > Title
window_title = driver.title
print(window_title)

# Browser Action 1 > Tabs

Current_element = driver.find_element(By.CLASS_NAME, "text-subtitle")
Current_element.click()
driver.back()



Delivered_element = driver.find_element(By.XPATH, "//div[contains(text(),'تحویل شده')]")
Delivered_element.click()

Reject_element = driver.find_element("xpath", "//div[contains(text(),'مرجوع شده')]")
Reject_element.click()

Sent_element = driver.find_element("class", "text-subtitle")
Sent_element.click()

Inprogress_element=driver.find_element("id","profile-history-menu")
Inprogress_element.click()
driver.forward()
driver.get("https://www.digikala.com/profile/orders/181257859/")
Cancel_Element=driver.find_element("id","profile-cancel-order")
Cancel_Element.click()
driver.forward()
driver.get("https://www.digikala.com/profile/orders/cancel/178040629")
Radio_element = driver.find_element("name","cancelType")
Radio_element.click()
driver.forward()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='انتخاب کنید']").click()



