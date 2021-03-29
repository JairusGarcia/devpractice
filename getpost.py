import requests

URL = 'http://search.msboc.us/ConsolidatedResults.cfm?ContractorType=&VarDatasource=BOC&Advanced=1'
myobj = {'Co_Name': '315 FIRE PROTECTION'}

r = requests.post(URL, data = myobj)
print(r.text)
