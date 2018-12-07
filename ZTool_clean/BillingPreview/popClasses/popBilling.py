import requests
import json
import time
import shutil
#import csv
#from contextlib import closing
import datetime
import zipfile
import os

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
    self.errorMsg = "empty"
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
        self.errorMsg = "Connection failed : Time Out. Try with another proxy choice."
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        self.status = "Failure"
        self.errorMsg = e
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
    else:
        self.errorMsg = "HTTP ERROR - error code = : " + str(response.status_code) + " while creating auth. token"
        self.status = "Failure"
        print(self.errorMsg)
        return

#**************** END CLASS *****************
#            ZToken
#********************************************



#**************** CLASS *****************
#            ZFile
#****************************************

class ZFile:
  def __init__(self, Type):
    self.status = "empty"
    self.fileUrl = "empty"
    self.type = Type
    self.value = "empty"
    self.runId = "emtpy"
    self.path = "empty"
    self.fileName = "empty"

    if self.type == "BillingPreviewRun":
        self.success = "success"
        self.idName = "billingPreviewRunId"
        self.status = "status"
    else:
        self.success = "Success"
        self.idName = "Id"
        self.status = "Status"

  def generate(self, connectionDetails, myZToken):
    #launch Zuora job. There are 2 types for the moment : BillingPreviewRun and DataSourceExport
    
    if self.type == "BillingPreviewRun":
        payload = "{\r\n\"assumeRenewal\": \"None\",\r\n\"batch\": \"\",\r\n\"chargeTypeToExclude\": \"\",\r\n\"includingEvergreenSubscription\": \"true\",\r\n\"targetDate\": \"2019-05-1\"\r\n}"
        uri = connectionDetails.url + "/v1/billing-preview-runs"
    else:
        payload = "{\r\n\"Format\": \"csv\",\r\n\"Name\": \"test_Export_1476935164445\",\r\n\"Query\": \"select Subscription.Id, Subscription.Name, Subscription.CostType__c, Subscription.CostTypeValue__c, Subscription.Entity__c, Subscription.Status, Subscription.SubscriptionEndDate, Subscription.TermType, Account.AccountNumber, Account.BillCycleDay, Account.Batch, Account.CompanyCode__c, Account.Currency, Account.CustomerCompanyName__c, Account.FreeTextAttribute1__c, Account.FreeTextAttribute1__c, Account.SEAccountID__c, Account.Status, BillToContact.City, BillToContact.Country from subscription where Subscription.Entity__c = 'EBA' and Subscription.Status = 'Active'\",\r\n\"Zip\": false\r\n}"
        uri = connectionDetails.url + "/v1/object/export"

    headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + myZToken.value,
                'cache-control': "no-cache"
                }

    try :
        response = requests.request("POST", uri, data=payload, headers=headers, proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify)
    except requests.exceptions.Timeout:
        print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
        self.value = "ERROR"
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        self.value = "ERROR"
        return

    if response.status_code == 200:
        parsed_json = json.loads(response.text)
        
        #if self.type == "BillingPreviewRun":
        #    success = "success"
        #    idName = "billingPreviewRunId"
        #    status = "Status"
        #else:
        #    success = "Success"
        #    idName = "Id"
        #    status = "status"

        if parsed_json[self.success] == True:
            self.runId = parsed_json[self.idName]
            self.value = "SUCCESS"
        else :
            self.value = parsed_json['reasons.message']

    else:
        self.value = response.status_code
        print("something went wrong : " + self.value)
        return

  def retrieve(self, connectionDetails, runId, myZToken, maxTry):
        
        self.runId = runId
        if self.type == "BillingPreviewRun":
            uri = connectionDetails.url + "/v1/billing-preview-runs/" + self.runId
        else :
            uri = connectionDetails.url + "/v1/object/export/" + self.runId

        headers = {
                    'Content-Type': "application/json",
                    'Authorization': "Bearer " + myZToken.value,
                    'cache-control': "no-cache"
                    }    
        
        retry = True
        numberTry = 0
        while retry == True and numberTry <= maxTry :
            numberTry += 1
            try :
                response = requests.request("GET", uri, headers=headers, proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify)
            except requests.exceptions.Timeout:
                print("Connection failed : Time Out. Try with another proxy choice (Y/N).")
                self.value = "ERROR"
                return
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)
                self.value = "ERROR"
                return
        
            if response.status_code == 200:
                parsed_json = json.loads(response.text)
                
                if parsed_json[self.status] == "Completed":
                    
                    if self.type == "BillingPreviewRun":    
                        self.fileUrl = parsed_json['resultFileUrl']
                    else :
                        self.fileUrl = connectionDetails.url + "/v1/files/" + parsed_json['FileId']

                    self.value = parsed_json[self.status]
                    retry = False
                    return

                elif parsed_json[self.status] == "Error":
                    self.value = parsed_json[self.status]
                    print("something went wrong during integrate: " + str(self.value))
                    retry = False
                    return
                else :
                    self.value = parsed_json[self.status]
                    print("Status : " + self.value + " - Number Try : " + str(numberTry) + "   ", end="", flush=True)
                    for x in range(3):    
                        time.sleep(1)
                        print("____", end="", flush=True)
                    print("____")
            else:
                self.value = response.status_code
                print()
                print("something went wrong during integrate: " + str(self.value))
                retry = False
                return

  def download(self, connectionDetails, fileUrl,dirPath):
    
    try :
        response = requests.get(fileUrl, auth=(connectionDetails.userName, connectionDetails.password), proxies=connectionDetails.proxies, timeout=5, verify=connectionDetails.verify, stream=True)
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
    zip_ref.extractall(targetPath)
    zip_ref.close()
    if os.path.exists(targetPath + '/' + self.fileName ):
        os.remove(targetPath + '/' + self.fileName)
        self.status = "ZIP_EXTRACTED"
    else:
        print("The file " + targetPath + "/" + self.fileName + " does not exist")
        self.status = "ZIP_FAILED"
    print(self.status)

#**************** END CLASS *****************
#            ZFile
#****************************************


