class E_sign():
    def __init__(self,driver):
        self.driver = driver
        
        self.my_Profile_id = "HEADER_USER_MENU_PROFILE_text"
        self.edit_Profile_id = "template_x002e_user-profile_x002e_user-profile_x0023_default-button-edit-button"
        self.upload_button_id = "template_x002e_user-profile_x002e_user-profile_x0023_default-sign-upload"
        self.file_to_upload_btn_xpath = "//*[@id='template_x002e_dnd-upload_x002e_user-profile_x0023_default-file-selection-button-overlay']/span/input"
        self.go_to_Depts_id = "HEADER_SITES_MENU"
        self.click_on_deptName_id = "HEADER_SITES_MENU_RECENT_abc"
        self.doc_lib_id = "uniqName_30_1"
        self.run_eSign_id = "onActionAddImagesToPdfFiles"
        self.saveChanges_id = "template_x002e_user-profile_x002e_user-profile_x0023_default-button-save"
             
    def myProfile(self):
        self.driver.find_element_by_id (self.my_Profile_id).click()
        
    def editProfile(self):
        self.driver.find_element_by_id (self.edit_Profile_id).click()
        
    def uploadBtn(self):
        self.driver.find_element_by_id(self.upload_button_id).click()
        
    def fileTo_UploadBtn(self, pathOfFile):
        self.driver.find_element_by_xpath(self.file_to_upload_btn_xpath).send_keys(pathOfFile)
        
    def GoToDepts(self):
        self.driver.find_element_by_id(self.go_to_Depts_id).click()
        
    def ClickDept(self):
        self.driver.find_element_by_id(self.click_on_deptName_id).click()
        
    def DocLib(self):
        self.driver.find_element_by_id(self.doc_lib_id).click()
        
    def RunESign(self):
        self.driver.find_element_by_id(self.run_eSign_id).click()  
        
    def SaveChangesBtn(self):
        self.driver.find_element_by_id(self.saveChanges_id).click()