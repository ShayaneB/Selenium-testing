class Dashboard():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.create_department = "Create Department"
        self.enter_name = "alfresco-createSite-instance-title"
        self.enter_details = "description"
        self.ok_btn = "alfresco-createSite-instance-ok-button-button"
        
    def department_creation(self):
        self.driver.find_element_by_link_text(self.create_department).click()
        
    def department_name(self, DeptName):
        self.driver.find_element_by_id(self.enter_name).send_keys(DeptName)
        
    def department_details(self,description):
        self.driver.find_element_by_name(self.enter_details).send_keys(description)
        
    def click_deptCreate(self):
        self.driver.find_element_by_id(self.ok_btn).click()