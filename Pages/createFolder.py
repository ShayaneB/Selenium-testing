class NewFolder():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.deptDashboard = "HEADER_SITE_DOCUMENTLIBRARY_text"
        self.createDropDown = "template_x002e_documentlist_v2_x002e_documentlibrary_x0023_default-createContent-button-button"
        self.createFolderBtn = "folder-file"
        self.folderName = "prop_cm_name"
        self.folderokBtn = "template_x002e_documentlist_v2_x002e_documentlibrary_x0023_default-createFolder-form-submit-button"
        
    def dashboardOfDept (self):
        self.driver.find_element_by_id(self.deptDashboard).click()
        
    def dropDownofFolder (self):
        self.driver.find_element_by_id(self.createDropDown).click()
        
    def folderBtn (self):
        self.driver.find_element_by_class_name(self.createFolderBtn).click()
        
    def nameOfFolder (self, Fname):
        self.driver.find_element_by_name(self.folderName).send_keys(Fname)
        
    def folderCreated (self):
        self.driver.find_element_by_id(self.folderokBtn).click()
        