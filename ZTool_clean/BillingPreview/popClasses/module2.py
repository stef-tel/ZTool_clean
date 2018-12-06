from module1 import connectionDetails, ZToken, ZFile

myConnectionDetails = connectionDetails("c2bfc320-bb04-413d-8ce6-91886f7b4d9b","xnAH1Foi03IxaybnuBL1")
myZToken = ZToken()
myZToken.generate(myConnectionDetails)
print("Token is : " + myZToken.value)

myZbillingPreviewRun = ZFile("BillingPreviewRun")
myZbillingPreviewRun.generate(myConnectionDetails, myZToken)
if myZbillingPreviewRun.value == "SUCCESS" :
    print("Billing Run Id : " + myZbillingPreviewRun.runId)
    myZbillingPreviewRun.value == "Started"
    myZbillingPreviewRun.retrieve(myConnectionDetails, myZbillingPreviewRun.runId, myZToken, 100)
    
    if myZbillingPreviewRun.value == "Completed" :
        print("Billing Preview FileURL : " + myZbillingPreviewRun.fileUrl )
        myZbillingPreviewRun.download(myConnectionDetails,myZbillingPreviewRun.fileUrl,"download")
        if myZbillingPreviewRun.value == "DOWNLOADED" :
            myZbillingPreviewRun.unzip("download")

myZDataExport1 = ZFile("Export")
myZbillingPreviewRun.generate(myConnectionDetails, myZToken)
