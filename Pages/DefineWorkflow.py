from selenium.webdriver.common.action_chains import ActionChains

class defineWorkflow():
    def __init__(self,driver):
        self.driver = driver
        
        #Locate the folder and hover to get the option of more. 
        self.locate_folder_link_text = "Testing"
        # element = self.locate_folder_link_text
        # element.location_once_scrolled_into_view
        # hov = ActionChains(self.driver).move_to_element(self.locate_folder_link_text)
        # hov.perform()
        
        self.click_more_option_id = "onActionShowMore"
        self.define_wrkflw_Btn_class_name = "alfresco.doclib.action.WorkflowUserActionExecuter"
        self.select_approverBtn_xpath = "//*[@type='button' and text()='Select']"
        self.search_approver_id = "alf-id14_assoc_selectedUser-cntrl-picker-searchText"
        self.searchBtn_id = "alf-id14_assoc_selectedUser-cntrl-picker-searchButton-button"
        self.add_approver_className = "addIcon"
        self.okBtn_id = "alf-id14_assoc_selectedUser-cntrl-ok-button"
        self.applyToSubFolders_id = "alf-id14_prop_applySubfolders-entry"
        self.ok_btn_id = "alf-id14-form-submit-button"
        
    def makeTheOptionsActive(self):    
        element = self.driver.find_element_by_link_text(self.locate_folder_link_text)
        element.location_once_scrolled_into_view
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()
        
    def TestFolder_moreOption(self):
        self.driver.find_element_by_id(self.click_more_option_id).click()
        
    def DefinWorkflwBtn(self):
        self.driver.find_element_by_class_name(self.define_wrkflw_Btn_class_name).click()

    def SelectApproverBtn(self):
        self.driver.find_element_by_xpath(self.select_approverBtn_xpath).click()
        
    def SearchApprover(self, ApproverName):
        self.driver.find_element_by_id(self.search_approver_id).clear()
        self.driver.find_element_by_id(self.search_approver_id).send_keys(ApproverName)
        
    def SearchBtn(self):
        self.driver.find_element_by_id(self.searchBtn_id).click()
    
    def AddApprover(self):
        self.driver.find_element_by_class_name(self.add_approver_className).click()

    def SelectBtn(self):
        self.driver.find_element_by_id(self.okBtn_id).click()

    def ApplyToSubFolders(self):
        self.driver.find_element_by_id(self.applyToSubFolders_id).click()

    def OkBtn(self):
        self.driver.find_element_by_id(self.ok_btn_id).click()