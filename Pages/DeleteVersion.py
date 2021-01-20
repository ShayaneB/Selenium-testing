from selenium.webdriver.support.ui import Select

class VersionDelete():
    def __init__(self,driver):
        self.driver = driver
        
        self.versionDelete_Btn_link_text = 'Version Delete'
        self.select_version_xpath = '//select[@name="prop_version"]'
        self.Ok_Btn_xpath = '//button[@type="button" and text()="OK"]'
        
    def VrsnDlt_btn(self):
        self.driver.find_element_by_link_text(self.versionDelete_Btn_link_text).click()
        
    def VersionSelectBtn(self):
        version_id = Select(self.driver.find_element_by_xpath(self.select_version_xpath))
        version_id.select_by_value('1.0')
        
    def okBtn(self):
        self.driver.find_element_by_xpath(self.Ok_Btn_xpath).click()