class OCROfFolder():
    def __init__(self,driver):
        self.driver = driver
        
        self.click_EngOCR_id = "onActionSimpleRepoAction"
        
    def runEngOCR(self):
        self.driver.find_element_by_id(self.click_EngOCR_id).click()    