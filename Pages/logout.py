class LogOut():
    def __init__(self,driver):
        self.driver = driver
        
        self.adminProfile_id = "HEADER_USER_MENU_POPUP_text"
        self.logout_id = "HEADER_USER_MENU_LOGOUT_text"
        
    def AdminProfile(self):
        self.driver.find_element_by_id(self.adminProfile_id).click()
        
    def Logout(self):
        self.driver.find_element_by_id(self.logout_id).click()