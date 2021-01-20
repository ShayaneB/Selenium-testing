class UnSubscribe():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.openDocument_link_text = "scansmpl.pdf"
        self.clickUnsubscribe_id = "notifyAction"
        self.generateQRCode_id = "onActionFormDialog"
        self.enterPageno_id = "alf-id1_prop_page-no"
        self.okBtn_id = "alf-id1-form-submit-button"
        
    def ClickDoc(self):
        self.driver.find_element_by_link_text(self.openDocument_link_text).click()
        
    def ClickUnotify(self):
        self.driver.find_element_by_id(self.clickUnsubscribe_id).click()
        
    def QRcode(self):
        self.driver.find_element_by_id(self.generateQRCode_id).click()
        
    def PageNo(self, pageNo):
        self.driver.find_element_by_id(self.enterPageno_id).send_keys(pageNo)
        
    def OKBtn(self):
        self.driver.find_element_by_id(self.okBtn_id).click()