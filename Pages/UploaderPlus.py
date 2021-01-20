from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
import os.path

class uploaderPlus():
    def __init__(self,driver):
        self.driver = driver
        
        self.uploaderPlus_Option_linktext = "Uploader Plus"
        self.select_dept_id = "page_x002e_ctool_x002e_admin-console_x0023_default-new-upload-folder-button"
        self.deptName_linkText = "Documents"
        self.OkBtn_id = "page_x002e_ctool_x002e_admin-console_x0023_default-new-form-ok-button"
        self.docType_id = "page_x002e_ctool_x002e_admin-console_x0023_default-edit-form_prop_up_allowedTypes-entry"
        self.saveBtn_id = "page_x002e_ctool_x002e_admin-console_x0023_default-edit-form-form-submit-button"
        self.EmplName_id = "template_x002e_dnd-upload_x002e_documentlibrary_x0023_default-metadata-form_prop_ev-hr_employeeName"
        self.EmplyID_id = "template_x002e_dnd-upload_x002e_documentlibrary_x0023_default-metadata-form_prop_ev-hr_employeeID"
        self.EmplStatus_id = "template_x002e_dnd-upload_x002e_documentlibrary_x0023_default-metadata-form_prop_ev-hr_employeeStatus"
        self.EmplDocType_id = "template_x002e_dnd-upload_x002e_documentlibrary_x0023_default-metadata-form_prop_ev-hr_performance"
        self.Ok_btn_id = "template_x002e_dnd-upload_x002e_documentlibrary_x0023_default-metadata-form-form-submit-button"
        self.dropZone = "template_x002e_documentlist_v2_x002e_documentlibrary_x0023_default-dl-body"
        
    def ApplyUploaderPlus(self):
        self.driver.find_element_by_link_text(self.uploaderPlus_Option_linktext).click()
        
    def SelectDept(self):
        self.driver.find_element_by_id(self.select_dept_id).click()
        
    def deptName(self):
        self.driver.find_element_by_link_text(self.deptName_linkText).click()
        
    def OKBtn(self):
        self.driver.find_element_by_id(self.OkBtn_id).click()
        
    def DocType(self):
        documentType = Select(self.driver.find_element_by_id(self.docType_id))
        documentType.select_by_value("ev-hr:eisenvaultHRPerformanceDoc")
        
    def SaveBtn(self):
        self.driver.find_element_by_id(self.saveBtn_id).click()
        
    def uploadFile(self):
        JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"

        def drop_files(element, files, offsetX=0, offsetY=0):
            driver = element.parent
            isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
            paths = []
            
            # ensure files are present, and upload to the remote server if session is remote
            for file in (files if isinstance(files, list) else [files]) :
                if not os.path.isfile(file) :
                    raise FileNotFoundError(file)
                paths.append(file if isLocal else element._upload(file))
            
            value = '\n'.join(paths)
            elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
            elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

        WebElement.drop_files = drop_files

        dropzone = self.driver.find_element_by_id(self.dropZone)
        # drop a single file
        dropzone.drop_files("/home/shayane/Desktop/easychair.docx")
        
    def EmplName(self,nameOfEmployee):
        self.driver.find_element_by_id(self.EmplName_id).send_keys(nameOfEmployee)
        
    def emplID(self,ID):
        self.driver.find_element_by_id(self.EmplyID_id).send_keys(ID)
        
    def emplStatus(self):
        EmpStatus = Select(self.driver.find_element_by_id(self.EmplStatus_id))
        EmpStatus.select_by_value('Currently Employed')
        
    def empDocType(self):
        EmpDoctype = Select(self.driver.find_element_by_id(self.EmplDocType_id))
        EmpDoctype.select_by_value('Promotion Letter')
        
    def okBtn(self):
        self.driver.find_element_by_id(self.Ok_btn_id).click()