class NewUser():
    def __init__(self,driver):
        self.driver = driver
        
        self.adminTools = "HEADER_ADMIN_CONSOLE_text"
        self.userOption = "Users"
        self.newUserBtn = "page_x002e_ctool_x002e_admin-console_x0023_default-newuser-button-button"
        self.firstName = "page_x002e_ctool_x002e_admin-console_x0023_default-create-firstname"
        self.email = "page_x002e_ctool_x002e_admin-console_x0023_default-create-email"
        self.username = "page_x002e_ctool_x002e_admin-console_x0023_default-create-username"
        self.createUserBtn = "page_x002e_ctool_x002e_admin-console_x0023_default-createuser-ok-button-button"
        self.userSearch = "page_x002e_ctool_x002e_admin-console_x0023_default-search-text"
        self.userSearchBtn = "page_x002e_ctool_x002e_admin-console_x0023_default-search-button-button"
        self.searchname1 = "Test"
        self.searchname2 = "Test01"
        self.searchname3 = "test02"
        self.editUser = "page_x002e_ctool_x002e_admin-console_x0023_default-edituser-button-button"
        self.newPswd = "page_x002e_ctool_x002e_admin-console_x0023_default-update-password"
        self.confirmPswd = "page_x002e_ctool_x002e_admin-console_x0023_default-update-verifypassword"
        self.saveBtn = "page_x002e_ctool_x002e_admin-console_x0023_default-updateuser-save-button-button"
    
    def adminConsol(self):
        self.driver.find_element_by_id(self.adminTools).click()
        
    def createNewUser(self):
        self.driver.find_element_by_link_text(self.userOption).click()
        
    def userBtn(self):
        self.driver.find_element_by_id(self.newUserBtn).click()
        
    def NewUserDetails(self, first_name):
        self.driver.find_element_by_id(self.firstName).send_keys(first_name)

    def emailID(self, email_add):
        self.driver.find_element_by_id(self.email).send_keys(email_add)

    def User_name(self,nameofuser):
        self.driver.find_element_by_id(self.username).send_keys(nameofuser)

    def userCreateBtn(self):
        self.driver.find_element_by_id(self.createUserBtn).click()
        
    def searchBox(self, usernm):
        self.driver.find_element_by_id(self.userSearch).clear()
        self.driver.find_element_by_id(self.userSearch).send_keys(usernm)
        
    def btnForSearch(self):
        self.driver.find_element_by_id(self.userSearchBtn).click()

    def clickUser1(self):
        self.driver.find_element_by_link_text(self.searchname1).click()
        
    def clickUser2(self):
        self.driver.find_element_by_link_text(self.searchname2).click()
        
    def clickUser3(self):
        self.driver.find_element_by_link_text(self.searchname3).click()

    def editBtn(self):
        self.driver.find_element_by_id(self.editUser).click()

    def updatePswd(self, pswd):
        self.driver.find_element_by_id(self.newPswd).send_keys(pswd)

    def confirmNewPswd(self, newpswd):
        self.driver.find_element_by_id(self.confirmPswd).send_keys(newpswd)
        
    def clickSaveBtn(self):
        self.driver.find_element_by_id(self.saveBtn).click()