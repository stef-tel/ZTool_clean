import requests
import json
import time
import shutil
#import csv
#from contextlib import closing
import datetime
import zipfile
import os
from pathlib import Path

#**************** CLASS *****************
#            connectionDetails
#****************************************

class connectionDetails:
  def __init__(self, clientId, clientSecret, proxy = 'None',env = 'DEV'):
    
    self.clientId = clientId
    self.clientSecret = clientSecret
    self.userName = "stephane.tellier_DEV@endexar.com"
    self.password = "godigitalR3"

    if env=="PROD":
        self.url= "https://rest.zuora.com"
    else:
        self.url = "https://rest.apisandbox.zuora.com"
          
    if proxy == 'None':
        self.proxyYesNo = input("SE proxy ? (Y/N) : ") 
    else:
        self.proxyYesNo = proxy
        print("SE proxy called with : " + self.proxyYesNo)
    

    if self.proxyYesNo == "Y":
        #self.verify = True
        self.verify = False
        self.proxies = {
          'http': 'gateway.schneider.zscaler.net:80',
          'https': 'gateway.schneider.zscaler.net:80',
        }
    else :
        self.verify = False
        self.proxies = {}



#**************** END CLASS *****************
#            connectionDetails
#****************************************

#**************** CLASS *****************
#            ZToken
#****************************************

class ZToken:
  def __init__(self):
    self.status = "empty"
    self.tenant = "empty"
    self.statusMsg = "empty"
    self.token = "empty"
    

  def generate(self, connectionDetails):

    payload = "client_id=" + connectionDetails.clientId + "&client_secret=" + connectionDetails.clientSecret + "&grant_type=client_credentials"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }
    
    uri = connectionDetails.url + "/oauth/token"   

    try :
        response = requests.request("POST", uri, data=payload, headers=headers, proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify)
    except requests.exceptions.Timeout:
        print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
        self.status = "Failure"
        self.statusMsg = "Connection failed : Time Out. Try with another proxy choice."
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        self.status = "Failure"
        self.statusMsg = e
        return

    self.status = str(response.status_code)
    if response.status_code == 200:
        parsed_json = json.loads(response.text)
        self.token = parsed_json['access_token']
        self.tenant = parsed_json['scope']
        index = self.tenant.find('tenant.')
        if index >= 0:
            self.tenant = self.tenant[index+8 : index+12]
        else:
            self.tenant = "not found"
        self.status = "Success"
        print("tenant : " + self.tenant)
        self.statusMsg = "you're connected to tenant " + self.tenant
    else:
        self.statusMsg = "HTTP ERROR - error code = : " + str(response.status_code) + " while creating auth. token"
        self.status = "Failure"
        print(self.statusMsg)
        return

#**************** END CLASS *****************
#            ZToken
#********************************************



#**************** CLASS *****************
#            ZFile
#****************************************

class ZFile:
  def __init__(self, Type):
    self.statusName = "empty"
    self.fileUrl = "empty"
    self.type = Type
    self.value = "empty"
    self.runId = "emtpy"
    self.path = "empty"
    self.fileName = "empty"
    self.statusMsg = "empty"
    self.status = "empty"
    self.retry = True

    if self.type == "BillingPreviewRun":
        self.successName = "success"
        self.idName = "billingPreviewRunId"
        self.statusName = "status"
    else:
        self.successName = "Success"
        self.idName = "Id"
        self.statusName = "Status"

  def generate(self, connectionDetails, ZToken, chargeTypeToExclude, batch, targetDate, invoiceDate):
    #launch Zuora job. There are 2 types for the moment : BillingPreviewRun and DataSourceExport
    if self.type == "BillingPreviewRun":
        payload = "{\r\n\"assumeRenewal\": \"None\",\r\n\"batch\": \"" + batch + "\",\r\n\"chargeTypeToExclude\": \"" + chargeTypeToExclude + "\",\r\n\"includingEvergreenSubscription\": \"true\",\r\n\"targetDate\": \"2019-05-1\"\r\n}"
        payload = "{\r\n\"assumeRenewal\": \"None\",\r\n\"batch\": \"" + batch + "\",\r\n\"chargeTypeToExclude\": \"" + chargeTypeToExclude + "\",\r\n\"includingEvergreenSubscription\": \"true\",\r\n\"targetDate\": \"" + targetDate + "\"\r\n}"
        #payload = "{\r\n\"assumeRenewal\": \"None\",\r\n\"batch\": \"Batch 3\",\r\n\"chargeTypeToExclude\": \"OneTime,Usage\",\r\n\"includingEvergreenSubscription\": \"true\",\r\n\"targetDate\": \"2017-01-10\"\r\n\"invoiceDate\":\"2017-01-10\"\r\n}"
        #payload = "{\r\n\"assumeRenewal\": \"None\",\r\n\"batch\": \"Batch 3\",\r\n\"chargeTypeToExclude\": \"OneTime,Usage\",\r\n\"includingEvergreenSubscription\": \"true\",\r\n\"targetDate\": \"2017-01-10\"\r\n\"invoiceDate\":\"2017-01-10\"\r\n}"       
        uri = connectionDetails.url + "/v1/billing-preview-runs"
    else:
        payload = "{\r\n\"Format\": \"csv\",\r\n\"Name\": \"test_Export_1476935164445\",\r\n\"Query\": \"select Subscription.Id, Subscription.Name, Subscription.CostType__c, Subscription.CostTypeValue__c, Subscription.Entity__c, Subscription.Status, Subscription.SubscriptionEndDate, Subscription.TermType, Account.AccountNumber, Account.BillCycleDay, Account.Batch, Account.CompanyCode__c, Account.Currency, Account.CustomerCompanyName__c, Account.FreeTextAttribute1__c, Account.FreeTextAttribute1__c, Account.SEAccountID__c, Account.Status, BillToContact.City, BillToContact.Country from subscription where Subscription.Entity__c = 'EBA' and Subscription.Status = 'Active'\",\r\n\"Zip\": false\r\n}"
        uri = connectionDetails.url + "/v1/object/export"

    headers = {
                 "Content-Type": "application/json",
                 "Authorization": "Bearer " + str(ZToken.token),
                "cache-control": "no-cache"
                }
    #headers["Authorization"] = " Bearer " + str(ZToken.token)

    try :
        response = requests.request("POST", uri, data=payload, headers=headers, proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify)
    except requests.exceptions.Timeout:
        print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
        self.status = "ERROR"
        self.statusMsg = "Connection failed : Time Out. Try with another proxy choice (Y/N)."
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        self.status = "ERROR"
        self.statusMsg = str(e)
        return

    if response.status_code == 200:
        parsed_json = json.loads(response.text)

        if parsed_json[self.successName] == True:
            self.runId = parsed_json[self.idName]
            self.status = "SUCCESS"
            self.statusMsg = "Billing Run Preview Id = " + parsed_json[self.idName]
        else :
            self.statusMsg = parsed_json['reasons'][0]['message']
            self.status = "Failure"

    else:
        self.statusMsg = response.status_code
        self.status = "Failure"
        print("something went wrong : " + str(self.value))
        #return

  def retrieve(self, connectionDetails, runId, myZToken, maxTry):
        
        self.runId = runId
        if self.type == "BillingPreviewRun":
            uri = connectionDetails.url + "/v1/billing-preview-runs/" + self.runId
        else :
            uri = connectionDetails.url + "/v1/object/export/" + self.runId

        headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + str(myZToken.token),
                    "cache-control": "no-cache"
                    }
        
        self.retry = True
        numberTry = 1
        while self.retry == True and numberTry <= maxTry :
            numberTry += 1
            try :
                response = requests.request("GET", uri, headers=headers, proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify)
            except requests.exceptions.Timeout:
                print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
                self.status = "ERROR"
                self.retry = False
                return
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)
                self.status = "ERROR"
                self.retry = False
                return
        
            if response.status_code == 200:
                parsed_json = json.loads(response.text)
                
                if parsed_json[self.statusName] == "Completed":
                    
                    if self.type == "BillingPreviewRun":    
                        self.fileUrl = parsed_json['resultFileUrl']
                    else :
                        self.fileUrl = connectionDetails.url + "/v1/files/" + parsed_json['FileId']

                    self.status = parsed_json[self.statusName]
                    self.statusMsg = "Result File Url : " + self.fileUrl
                    self.retry = False
                    return

                elif parsed_json[self.statusName] == "Error":
                    self.status = parsed_json[self.statusName]
                    print("something went wrong during integrate: " + str(self.status))
                    self.retry = False
                    return
                else :
                    self.status = parsed_json[self.statusName]
                    print("Status : " + self.value + " - Number Try : " + str(numberTry) + "   ", end="", flush=True)
                    for x in range(3):    
                        time.sleep(1)
                        print("____", end="", flush=True)
                    print("____")
            else:
                self.status = response.status_code
                print()
                print("something went wrong during integrate: " + str(self.value))
                self.retry = False
                return

  def download(self, connectionDetails, fileUrl,dirPath):
    
    try :
        response = requests.get(fileUrl, auth=(connectionDetails.userName, connectionDetails.password), proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify, stream=True)
    except requests.exceptions.Timeout:
        print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
        self.status = "ERROR"
        self.statusMsg = "Error while downlaoding file"  + fileUrl + " - time Out"
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        self.status = "ERROR"
        self.statusMsg = "Error while downlaoding file"  + fileUrl + " - " + e
        return

    if response.status_code == 200:
        ts = time.time()
        myTimeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
        
        with open(dirPath + '/test_' + myTimeStamp + '.zip', 'wb') as outFile:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, outFile)
            self.path = dirPath
            self.fileName = 'test_' + myTimeStamp + '.zip'
            self.status = "DOWNLOADED"
            self.statusMsg = "Temp File Name : " + self.fileName
    else:
        self.status = response.status_code
        self.statusMsg = "something went wrong : " + self.status
        print("something went wrong : " + self.status)
        return

  def downloadCsv(self, connectionDetails, myZToken, fileUrl,dirPath):
    
    headers = {
                    'Accept': "application/pdf",
                    'Authorization': "Bearer " + myZToken.value,
                    'cache-control': "no-cache"
                    }    

    try :
        response = requests.request("GET", fileUrl, headers=headers, proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify, stream=True)
    except requests.exceptions.Timeout:
        print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
        self.value = "ERROR"
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        self.value = "ERROR"
        return

    if response.status_code == 200:
        ts = time.time()
        myTimeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
        
        with open(dirPath + '/test_' + myTimeStamp + '.zip', 'wb') as outFile:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, outFile)
            self.path = dirPath
            self.fileName = 'test_' + myTimeStamp + '.zip'
            self.value = "DOWNLOADED"
    else:
        self.value = response.status_code
        print("something went wrong : " + self.value)
        return

  def unzip(self, targetPath):
    zip_ref = zipfile.ZipFile(self.path + '/' + self.fileName, 'r')
    
    for name in zip_ref.namelist():
        zip_ref.extract(name, targetPath)
        self.csvName = name
    
    #zip_ref.extractall(targetPath)
    zip_ref.close()
    if os.path.exists(targetPath + '/' + self.fileName ):
        os.remove(targetPath + '/' + self.fileName)
        self.status = "ZIP_EXTRACTED"
        self.statusMsg = "ZIP content successfully extracted : " + self.fileName
    else:
        print("The file " + targetPath + "/" + self.fileName + " does not exist")
        self.status = "ZIP_FAILED"
        self.statusMsg = "something went wrong during unzip"
    print(self.status)

#**************** END CLASS *****************
#            ZFile
#****************************************


#**************** CLASS *****************
#            pz Settings
#****************************************



#**************** END CLASS *****************
#            pz Settings
#********************************************

class pzSettings:
  def __init__(self):
    self.checkOK = False
    self.load()

  def load(self):
    data_folder = Path("BillingPreview/settings/")
    file_to_open = data_folder / "settings.json"
  
    try:
        with open(file_to_open) as json_file:  
            data = json.load(json_file)            
            self.tempFolderPath =  data['settings']['tempFolderPath']
            print('tempFolderPath: ' + data['settings']['tempFolderPath'])
            self.resultsFolderPath =  data['settings']['resultsFolderPath']
            print('resultsFolderPath: ' + data['settings']['resultsFolderPath'])
        self.checkOK = True
    except:
        print(os.getcwd())
        self.checkOK = False