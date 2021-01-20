class UserDelete():
    def __init__(self,driver):
        self.driver = driver

        self.deleteUser_Btn_id = "page_x002e_ctool_x002e_admin-console_x0023_default-deleteuser-button-button"
        self.confirmationBtn_xpath = "//button[@type = 'button' and text() = 'Delete']"
        
    def DeletionBtn(self):
        self.driver.find_element_by_id(self.deleteUser_Btn_id).click()
        
    def ConfirmBtn(self):
        self.driver.find_element_by_xpath(self.confirmationBtn_xpath).click()