import os.path
from selenium.webdriver.remote.webelement import WebElement

class OCR():
    def __init__(self,driver):
        self.driver = driver
        
        self.dropZone = "template_x002e_documentlist_v2_x002e_documentlibrary"
        self.fileToOCR = "scansmpl.pdf"
        self.runOCR = "remote-ocr-english"
    
    def UploadFile(self):    
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

        dropzone = self.driver.find_element_by_id(self.dropZone)
        # drop a single file
        dropzone.drop_files("/home/shayane/Desktop/scansmpl.pdf")

    def openFile(self):
        self.driver.find_element_by_link_text(self.fileToOCR).click()
        
    def clickEngOCR(self):    
        element = self.driver.find_element_by_class_name(self.runOCR)
        element.location_once_scrolled_into_view
        element.click()