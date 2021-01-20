from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import os.path
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from Pages.loginPage import LoginPage
from Pages.dashboard import Dashboard
from Pages.createFolder import NewFolder
from Pages.testingOCR import OCR
from Pages.NewUser import NewUser
from Pages.SearchGroups import Groups
from Pages.setUsersRole import users_role
from Pages.DefineWorkflow import defineWorkflow
from Pages.UploadInFolder import FolderUpload
from Pages.unsubscribe import UnSubscribe
from Pages.logout import LogOut
from Pages.Esignature import E_sign
from Pages.DeleteVersion import VersionDelete
from Pages.folderOCR import OCROfFolder
from Pages.userDeletion import UserDelete
from Pages.UploaderPlus import uploaderPlus

class LoginLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        cls.driver.implicitly_wait(10)
        
    def test_login(self):
        driver = self.driver
        
        driver.get("http://localhost:8080/share")
        # driver.maximize_window()

        #Login
    
        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()
        time.sleep(5)  
              
        # # #Dept. Creation.     
        department = Dashboard(driver)
        # department.department_creation()
        # department.department_name("ABC")
        # department.department_details("For Testing")
        # department.click_deptCreate()
        # time.sleep(5)  
        
        # #New Folder Creation      
        folder = NewFolder(driver)
        # folder.dashboardOfDept()
        # time.sleep(5)

        # folder.dropDownofFolder()
        # folder.folderBtn()
        # folder.nameOfFolder("Testing")
        # folder.folderCreated()
        # time.sleep(5)

        # #Running OCR
        runOCR = OCR(driver)
        # runOCR.UploadFile()
        # time.sleep(10)
        
        # runOCR.openFile()
        # time.sleep(5)
        
        # runOCR.clickEngOCR()
        # time.sleep(30)
    
        # #Create New User
        userCreation = NewUser(driver)
        # userCreation.adminConsol()
        # time.sleep(5)

        # userCreation.createNewUser()
        # userCreation.userBtn()
        # time.sleep(5)

        # userCreation.NewUserDetails("Test")
        # userCreation.emailID("shayane.basu@eisenvault.com")
        # userCreation.User_name("Tester")
        # userCreation.userCreateBtn()
        # time.sleep(5)
        
        # #Search New User.
        # userCreation.searchBox("Tester")
        # userCreation.btnForSearch()
        # time.sleep(3)
        
        # userCreation.clickUser1()
        # time.sleep(3)
        
        # #Edit User Password.
        # userCreation.editBtn()
        # time.sleep(3)
        
        # userCreation.updatePswd("Test@123")
        # userCreation.confirmNewPswd("Test@123")
        # userCreation.clickSaveBtn()
        # time.sleep(5)
        # userCreation.adminConsol()
        # time.sleep(5)

        # userCreation.createNewUser()
        # userCreation.userBtn()
        # time.sleep(5)
        
        # #User Details.
        # userCreation.NewUserDetails("Test01")
        # userCreation.emailID("shayane.basu@eisenvault.com")
        # userCreation.User_name("Viewer")
        # userCreation.userCreateBtn()
        # time.sleep(6)
        
        # #Search New User.
        # userCreation.searchBox("Viewer")
        # userCreation.btnForSearch()
        # time.sleep(5)
        # userCreation.clickUser2()
        # time.sleep(5)
        
        # #Edit User Password.
        # userCreation.editBtn()
        # time.sleep(5)
        
        # userCreation.updatePswd("Viewer@123")
        # userCreation.confirmNewPswd("Viewer@123")
        # userCreation.clickSaveBtn()
        # time.sleep(5)

        # #List of all groups.
        groupsCreation = Groups(driver)
        # groupsCreation.group_tab()
        # time.sleep(5)
        # groupsCreation.all_groups()
        # time.sleep(7)
        
        # #Create new group.
        # groupsCreation.create_newGroup()
        # groupsCreation.group_ID("Unique")
        # groupsCreation.group_name("Test Group01")
        # groupsCreation.create_button()
        # time.sleep(7)
        
        # #Search New group.
        # groupsCreation.search_newGroup("Test Group01")
        # time.sleep(3)
        # groupsCreation.click_newGroup()
        # time.sleep(5)
        
        # #Set User role in the department.
        setRoles = users_role(driver)
        # setRoles.homeTab()
        # time.sleep(5)
        # setRoles.deptName()
        # time.sleep(3)
        # setRoles.deptMembers()
        # time.sleep(3)
        # setRoles.addUsers()
        # time.sleep(3)
        # setRoles.searchUser("Test")
        # time.sleep(3)
        # setRoles.searchBtn()
        # time.sleep(3)
        # setRoles.selectUser()
        # time.sleep(3)
        # setRoles.selectRole()
        # time.sleep(3)
        # setRoles.assignManagerRole()
        # time.sleep(3)
        # setRoles.addUserBtn()
        # time.sleep(3)
        
        # #Set Viewer role in the department.
        # setRoles.searchUser("Viewer")
        # time.sleep(5)
        # setRoles.searchBtn()
        # time.sleep(5)
        # setRoles.selectUser()
        # time.sleep(5)
        # setRoles.selectRole()
        # time.sleep(5)
        # setRoles.assignViewerRole()
        # time.sleep(5)
        # setRoles.addUserBtn()
        # time.sleep(5)
        
        # #Define Workflow.
        defineWrkFlw = defineWorkflow(driver)
        # setRoles.homeTab()
        # time.sleep(5)
        # setRoles.deptName()
        # time.sleep(3)
        # folder.dashboardOfDept()
        # time.sleep(5)
        # defineWrkFlw.makeTheOptionsActive()
        # defineWrkFlw.TestFolder_moreOption()
        # time.sleep(5)
        # defineWrkFlw.DefinWorkflwBtn()
        # time.sleep(5)
        # defineWrkFlw.SelectApproverBtn()
        # time.sleep(5)
        
        # #Adding 2 approvers: Admin and Tester.
        # defineWrkFlw.SearchApprover("Administrator")
        # time.sleep(3)
        # defineWrkFlw.SearchBtn()
        # time.sleep(3)
        # defineWrkFlw.AddApprover()
        # time.sleep(3)
        # defineWrkFlw.SearchApprover("Tester")
        # time.sleep(3)
        # defineWrkFlw.SearchBtn()
        # time.sleep(3)
        # defineWrkFlw.AddApprover()
        # time.sleep(3)
        # defineWrkFlw.SelectBtn()
        # time.sleep(5)
        # defineWrkFlw.ApplyToSubFolders()
        # time.sleep(3)
        # defineWrkFlw.OkBtn()
        # time.sleep(5)
               
        # #Uploading in folder to check define workflow.
        folder_upload = FolderUpload(driver)
        # setRoles.deptName()
        # time.sleep(3)
        # folder.dashboardOfDept()
        # time.sleep(5)
        # folder_upload.Click_Folder()
        # time.sleep(5)
        # folder_upload.UploadFileInFolder()
        # time.sleep(5)
        
        # #Go to my task and do approval.
        # folder_upload.goToTask()
        # time.sleep(5)
        # folder_upload.myTask()
        # time.sleep(3)
        # folder_upload.makeEditingActive()
        # folder_upload.Edit_Task()
        # time.sleep(3)
        # folder_upload.Approve_Task()
        # time.sleep(3)
        
        # # Unsubscribe
        unNotify = UnSubscribe(driver)
        # setRoles.homeTab()
        # time.sleep(5)
        # setRoles.deptName()
        # time.sleep(5)
        # folder.dashboardOfDept()
        # time.sleep(3)
        # unNotify.ClickDoc()
        # time.sleep(5)
        # unNotify.ClickUnotify()
        # time.sleep(5)
        
        # #QR code Testing.
        # unNotify.QRcode()
        # time.sleep(5)
        # unNotify.PageNo("1")
        # time.sleep(3)
        # unNotify.OKBtn()
        # time.sleep(5)
         
        # #Add e-sign to the profile.
        log_out = LogOut(driver)
        # log_out.AdminProfile()
        # time.sleep(3)
        
        e_sign = E_sign(driver)
        # e_sign.myProfile()
        # time.sleep(3)
        # e_sign.editProfile()
        # time.sleep(3)
        # e_sign.uploadBtn()
        # e_sign.fileTo_UploadBtn("/home/shayane/Pictures/testScreenshot.png")
        # time.sleep(3)
        # e_sign.SaveChangesBtn()
        # time.sleep(5)

        # #Go to the department from the top bar.
        # e_sign.GoToDepts()
        # time.sleep(3)
        # e_sign.ClickDept()
        # time.sleep(3)
        # e_sign.DocLib()
        # time.sleep(3)
        
        # #Open file and run e-sign.
        # runOCR.openFile()
        # time.sleep(5)
        # e_sign.RunESign()
        # time.sleep(5)
        
        # # Version delete.
        versionDlt = VersionDelete(driver)
        # versionDlt.VrsnDlt_btn()
        # time.sleep(5)
        # versionDlt.VersionSelectBtn()
        # time.sleep(3)
        # versionDlt.okBtn()
        # time.sleep(3)
        
        #Logout.
        log_out.AdminProfile()
        time.sleep(5)
        log_out.Logout()
        driver.implicitly_wait(7)
        
        #Login as Manager user. 
        login.enter_username("Tester")
        login.enter_password("Test@123")
        login.click_login()
        time.sleep(5)
        
        # #Go to the department.
        # setRoles.deptName()
        # time.sleep(5)
        # folder.dashboardOfDept()
        # time.sleep(5)
        
        # # Click FolderOCR.
        # defineWrkFlw.makeTheOptionsActive()
        # defineWrkFlw.TestFolder_moreOption()
        # time.sleep(5)
        # FldrOCR = OCROfFolder(driver)
        # FldrOCR.runEngOCR()
        # time.sleep(30)
        
        #Logout.
        log_out.AdminProfile()
        time.sleep(5)
        log_out.Logout()
        time.sleep(5)        
        #Login as viewer user. 
        login.enter_username("Viewer")
        login.enter_password("Viewer@123")
        login.click_login()
        time.sleep(5)
        
        #Go to the department.
        setRoles.deptName()
        time.sleep(5)
        folder.dashboardOfDept()
        time.sleep(5)
        runOCR.openFile()
        time.sleep(10)
        
        #Logout.
        log_out.AdminProfile()
        time.sleep(5)
        log_out.Logout()
        time.sleep(5)
        
        #Login
        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()
        driver.implicitly_wait(7) 
        
        #Search the user to be deleted.
        userCreation.adminConsol()
        time.sleep(5)
        userCreation.createNewUser()
        time.sleep(5)
        userCreation.searchBox("Tester")
        userCreation.btnForSearch()
        time.sleep(3)
        userCreation.clickUser1()
        time.sleep(3)
        
        # Delete new user that we created.
        Deletion = UserDelete(driver)
        Deletion.DeletionBtn()
        time.sleep(5)
        Deletion.ConfirmBtn()
        time.sleep(5)
        userCreation.searchBox("Tester")
        userCreation.btnForSearch()
        time.sleep(3)
        
        #Uploader Plus.
        userCreation.adminConsol()
        time.sleep(5)
        UploadPlus = uploaderPlus(driver)
        UploadPlus.ApplyUploaderPlus()
        time.sleep(3)
        UploadPlus.SelectDept()
        time.sleep(5)
        # UploadPlus.deptName()
        UploadPlus.OKBtn()
        time.sleep(3)
        UploadPlus.DocType()
        time.sleep(3)
        UploadPlus.SaveBtn()
        time.sleep(3)
        e_sign.GoToDepts()
        time.sleep(3)
        e_sign.ClickDept()
        time.sleep(3)
        e_sign.DocLib()
        time.sleep(5)
        UploadPlus.uploadFile()
        time.sleep(5)
        UploadPlus.EmplName('Test')
        time.sleep(3)
        UploadPlus.emplID('12345')
        time.sleep(3)
        UploadPlus.emplStatus()
        time.sleep(3)
        UploadPlus.empDocType()
        time.sleep(3)
        UploadPlus.okBtn()
        time.sleep(10)
        
    @classmethod    
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed.")
       
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/shayane/Desktop/Systest_Testing/Reports/ReportsofPerformActions'))