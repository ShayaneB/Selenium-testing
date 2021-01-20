from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import os.path
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

class LoginLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        
    def test_login(self):
        self.driver.get("http://localhost:8080/share")
        self.driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-username").send_keys("admin")
        self.driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-password").send_keys("admin")
        self.driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-submit-button").click()
        time.sleep(10)
        
        #Create Department.
        self.driver.find_element_by_link_text("Create Department").click()
        time.sleep(5)
        self.driver.find_element_by_id("alfresco-createSite-instance-title").send_keys("ABC")
        self.driver.find_element_by_name("description").send_keys("Testing Purpose")
        self.driver.find_element_by_id("alfresco-createSite-instance-ok-button-button").click()
        time.sleep(10)
        self.driver.find_element_by_id("HEADER_SITE_DOCUMENTLIBRARY_text").click()
        
    #Create Folder "Test".
        self.driver.find_element_by_id("template_x002e_documentlist_v2_x002e_documentlibrary_x0023_default-createContent-button-button").click()
        self.driver.find_element_by_class_name("folder-file").click()
        time.sleep(5)
        self.driver.find_element_by_name("prop_cm_name").send_keys("Test")
        self.driver.find_element_by_id("template_x002e_documentlist_v2_x002e_documentlibrary_x0023_default-createFolder-form-submit-button").click()
        time.sleep(10)
        
    #Upload File.
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

        dropzone = self.driver.find_element_by_id("template_x002e_documentlist_v2_x002e_documentlibrary")
        # drop a single file
        dropzone.drop_files("/home/shayane/Desktop/CAH_PoliciesGroup.ods")
        time.sleep(10)

        # drop multiple files inside folder.
        self.driver.find_element_by_class_name("filter-change").click()
        time.sleep(5)
        JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"

        def drop_files_insideFolder(element, files, offsetX=0, offsetY=0):
            self.driver = element.parent
            isLocal = not self.driver._is_remote or '127.0.0.1' in self.driver.command_executor._url
            paths = []
                
                # ensure files are present, and upload to the remote server if session is remote
            for file in (files if isinstance(files, list) else [files]) :
                if not os.path.isfile(file) :
                    raise FileNotFoundError(file)
                paths.append(file if isLocal else element._upload(file))
                
            value = '\n'.join(paths)
            elm_input = self.driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
            elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

        WebElement.drop_files_insideFolder = drop_files_insideFolder

        dropzone = self.driver.find_element_by_id("template_x002e_documentlist_v2_x002e_documentlibrary_x0023_default-documents")
            # drop multiple files
        dropzone.drop_files_insideFolder(["/home/shayane/Desktop/TestingNewInstance.xlsx", "/home/shayane/Desktop/CAH/Doctors Contract Malaysia UserList.docx", "/home/shayane/Documents/EisenVaultTicketReport.pdf"])
        time.sleep(10)
        
    #Create New User.
        self.driver.find_element_by_id("HEADER_ADMIN_CONSOLE_text").click()
        time.sleep(10)
        self.driver.find_element_by_link_text("Users").click()
        time.sleep(10)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-newuser-button-button").click()
        time.sleep(10)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-create-firstname").send_keys("Test")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-create-email").send_keys("shayane.basu@eisenvault.com")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-create-username").send_keys("tester")
        time.sleep(5)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-createuser-ok-button-button").click()
        time.sleep(10)

        #Search the user and edit the password. 
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-search-text").send_keys("tester")
        time.sleep(5)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-search-button-button").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("Test").click()
        time.sleep(5)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-edituser-button-button").click()
        time.sleep(3)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-update-password").send_keys("Tester@123")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-update-verifypassword").send_keys("Tester@123")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-updateuser-save-button-button").click()
        time.sleep(5)

        #Create Groups.
        self.driver.find_element_by_link_text("Groups").click()
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-browse-button-button").click()
        time.sleep(5)
        self.driver.find_element_by_class_name("groups-newgroup-button").click()
        time.sleep(5)
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-create-shortname").send_keys("Unique")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-create-displayname").send_keys("Test Group01")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-creategroup-ok-button-button").click()
        time.sleep(5)

        #Search Group.
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-search-text").send_keys("Test Group01")
        self.driver.find_element_by_id("page_x002e_ctool_x002e_admin-console_x0023_default-browse-button-button").click()
        time.sleep(5)

        #Go to the home page and go to department members.
        self.driver.find_element_by_id("HEADER_HOME_text").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("ABC").click()
        time.sleep(10)
        self.driver.find_element_by_id("HEADER_SITE_MEMBERS_text").click()
        time.sleep(5)

        #Add New User with role 
        self.driver.find_element_by_id("template_x002e_site-members_x002e_site-members_x0023_default-invitePeople-button").click()
        time.sleep(5)
        self.driver.find_element_by_id("template_x002e_people-finder_x002e_add-users_x0023_default-search-text").send_keys("tester")
        self.driver.find_element_by_id("template_x002e_people-finder_x002e_add-users_x0023_default-search-button-button").click()
        time.sleep(5)
        
        #Manager of department.
        self.driver.find_element_by_xpath("//*[@type='button' and text()='Select']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@type='button' and text()='Select Role ▾']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@class='yuimenuitemlabel' and text()='Manager']").click()
        time.sleep(3)
        self.driver.find_element_by_id("template_x002e_invitationlist_x002e_add-users_x0023_default-invite-button-button").click()
        time.sleep(10)
        
        #Logout
        self.driver.find_element_by_id("HEADER_USER_MENU_POPUP_text").click()
        self.driver.find_element_by_id("HEADER_USER_MENU_LOGOUT_text").click()
        time.sleep(5)
        
        #Login in DMS with new user. 
        self.driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-username").send_keys("tester")
        self.driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-password").send_keys("Tester@123")
        self.driver.find_element_by_id("page_x002e_components_x002e_slingshot-login_x0023_default-submit-button").click()
        time.sleep(10)
        self.driver.find_element_by_link_text("ABC").click()
        time.sleep(10)
        self.driver.find_element_by_id("HEADER_SITE_DOCUMENTLIBRARY_text").click()
        time.sleep(10)

        #Upload a scanned file. 
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

        dropzone = self.driver.find_element_by_id("template_x002e_documentlist_v2_x002e_documentlibrary")
        # drop a single file
        dropzone.drop_files("/home/shayane/Desktop/scansmpl.pdf")
        time.sleep(10)
        self.driver.find_element_by_link_text("scansmpl.pdf").click()

        #Logout
        self.driver.find_element_by_id("HEADER_USER_MENU_POPUP_text").click()
        self.driver.find_element_by_id("HEADER_USER_MENU_LOGOUT_text").click()
        
    @classmethod    
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")
        
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/shayane/Desktop/Testing/Reports/ReportsofNewDepartments'))