class Groups():
    def __init__(self,driver):
        self.driver = driver
        
        self.groups_link_text = "Groups"
        self.browse_button_id = "page_x002e_ctool_x002e_admin-console_x0023_default-browse-button-button"
        self.newgroup_class_name = "groups-newgroup-button"
        self.groupID_id = "page_x002e_ctool_x002e_admin-console_x0023_default-create-shortname"
        self.groupname_id = "page_x002e_ctool_x002e_admin-console_x0023_default-create-displayname"
        self.create_group_id = "page_x002e_ctool_x002e_admin-console_x0023_default-creategroup-ok-button-button"
        self.browse_group_id = "page_x002e_ctool_x002e_admin-console_x0023_default-search-text"
        self.click_group_id = "page_x002e_ctool_x002e_admin-console_x0023_default-search-button-button"
        
    def group_tab (self):
        self.driver.find_element_by_link_text(self.groups_link_text).click()
        
    def all_groups(self):
        self.driver.find_element_by_id(self.browse_button_id).click()
        
    def create_newGroup(self):
        self.driver.find_element_by_class_name(self.newgroup_class_name).click()
        
    def group_ID(self, short_name):
        self.driver.find_element_by_id(self.groupID_id).send_keys(short_name)
        
    def group_name(self, groupName):
        self.driver.find_element_by_id(self.groupname_id).send_keys(groupName)
        
    def create_button(self):
        self.driver.find_element_by_id(self.create_group_id).click()
    
    def search_newGroup(self, groupName):
        self.driver.find_element_by_id(self.browse_group_id).send_keys(groupName)
        
    def click_newGroup(self):
        self.driver.find_element_by_id(self.click_group_id).click()    