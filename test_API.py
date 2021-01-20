import requests, json
from requests.auth import HTTPBasicAuth

#In case of file OCR.
response = requests.get("http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/8996e36a-ad4b-4ea1-ba0c-563214c061f3", auth=('admin', 'admin'))
print(response.json())

aspect_OCR = response.json()['entry']['aspectNames']
if "ev:remoteOCR" in aspect_OCR: 
    print("OCR on pdf is successful.")
else:
    print("OCR on pdf is failed.")
   
#In case of folder OCR.
response = requests.get("http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/0296535e-2a08-4671-8d43-951e20686360", auth=('admin', 'admin'))
# print(response.json())

aspect_FolderOCR = response.json()['entry']['aspectNames']
if "ev:remoteOCR" in aspect_FolderOCR: 
    print("OCR on folder is successful.")
else:
    print("OCR on folder is failed.")
    
#To check E-Sign
response = requests.get("http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/ad238515-603f-41aa-9932-5470374319d7", auth=('admin', 'admin'))
# print(response.json())

aspect_Esign = response.json()['entry']['aspectNames']
if "esign:signPosition" in aspect_Esign: 
    print("E-sign successfully applied")
else:
    print("E-sign failed.")