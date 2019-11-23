#Input Boxes

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?153770259640")

#How to find numbe rof input boxes

inputboxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(inputboxes)) # 8


# Status of the textboxes
status = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print("Displayed or not: ", status)
enable = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print("Enabled or not: ",enable)

#How to provide values to the text

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Hasan")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Mahmud")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("01938123456")
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("Bangladesh")
driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Chittagong")
driver.find_element(By.ID, "RESULT_TextField-6").send_keys("hasan.mahmud@gmail.com")


# Status of the textboxes
#driver.quit()

# driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()




# #Explicit wait
# wait = WebDriverWait(driver,10)


# element = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//*[@id='1-stop-flights-checkbox']")))

# element.click()

# time.sleep(2)
# driver.quit()




