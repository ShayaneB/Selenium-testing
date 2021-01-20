from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://localhost:8080/share")
driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-username").send_keys("admin")
driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-password").send_keys("admin")
driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-submit-button").click()
time.sleep(10)

driver.find_element_by_id("HEADER_USER_MENU_POPUP_text").click()
driver.find_element_by_id("HEADER_USER_MENU_PROFILE_text").click()
time.sleep(5)

driver.find_element_by_id("template_x002e_user-profile_x002e_user-profile_x0023_default-button-edit-button").click()
time.sleep(5)

driver.find_element_by_id("template_x002e_user-profile_x002e_user-profile_x0023_default-sign-upload").click()
driver.find_element_by_xpath("//*[@id='template_x002e_dnd-upload_x002e_user-profile_x0023_default-file-selection-button-overlay']/span/input").send_keys("/home/shayane/Pictures/testScreenshot.png")