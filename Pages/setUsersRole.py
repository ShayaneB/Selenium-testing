class users_role():
    def __init__(self,driver):
        self.driver = driver
        
        self.home_id = "HEADER_HOME_text"
        self.dept_link_text = "ABC"
        self.dept_members_id = "HEADER_SITE_MEMBERS_text"
        self.inviteUsers_id = "template_x002e_site-members_x002e_site-members_x0023_default-invitePeople-button"
        self.searchUsers_id = "template_x002e_people-finder_x002e_add-users_x0023_default-search-text"
        self.searchBtn_id = "template_x002e_people-finder_x002e_add-users_x0023_default-search-button-button"
        self.selectBtn_xpath = "//*[@type='button' and text()='Select']"
        self.selectRole_xpath = "//*[@type='button' and text()='Select Role ▾']"
        self.managerRole_xpath = "//*[@class='yuimenuitemlabel' and text()='Manager']"
        self.viewer_xpath = "//*[@class='yuimenuitemlabel' and text()='Viewer']"
        self.addUserBtn_xpath = "template_x002e_invitationlist_x002e_add-users_x0023_default-invite-button-button"
        
    def homeTab(self):
        self.driver.find_element_by_id(self.home_id).click()
        
    def deptName (self):
        self.driver.find_element_by_link_text(self.dept_link_text).click()
        
    def deptMembers(self):
        self.driver.find_element_by_id(self.dept_members_id).click()
        
    def addUsers(self):
        self.driver.find_element_by_id(self.inviteUsers_id).click()
        
    def searchUser(self, usrname):
        self.driver.find_element_by_id(self.searchUsers_id).clear()
        self.driver.find_element_by_id(self.searchUsers_id).send_keys(usrname)
        
    def searchBtn(self):
        self.driver.find_element_by_id(self.searchBtn_id).click()

    def selectUser(self):
        self.driver.find_element_by_xpath(self.selectBtn_xpath).click()
        
    def selectRole(self):
        self.driver.find_element_by_xpath(self.selectRole_xpath).click()
        
    def assignManagerRole(self):
        self.driver.find_element_by_xpath(self.managerRole_xpath).click()
        
    def assignViewerRole(self):
        self.driver.find_element_by_xpath(self.viewer_xpath).click()
        
    def addUserBtn(self):
        self.driver.find_element_by_id(self.addUserBtn_xpath).click()