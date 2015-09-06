#!C:\Python34\python.exe
# Change line at top to fit your environment

import re
import collections
api_call = re.compile("\/api\/")
fileName='elblogs.txt'


f = open(fileName,'r');
apiCallDict = dict()

#
# Returns the api call type so that it can be used as a key
#
def rtnApiCallType(apiString):
    apiStringSections = apiString.split('/')
    version = apiStringSections.pop(4)
    apiCallTmp = apiStringSections.pop(4)
    apiCallSections = apiCallTmp.split(' ')
    apiCall = apiCallSections.pop(0)
    return "api/"+version + "/"+apiCall

#
# Returns the updated API call dict
#
def updateApiCallDict(apiDict,logEntry):
    apiString = rtnApiCallType(logEntry)
    apiCallCount=0
    if apiString in apiDict:
        apiCallCount = apiDict[apiString]
    apiCallCount +=1
    apiDict[apiString] = apiCallCount
    return apiDict

#
# Prints the API Call dict
#
def printApiDict(apiDict):
    #Sets Total Number of Calls so percentage can be calculated
    total=0
    for apiCall in apiDict:
        total += apiDict[apiCall]

    #Iterates through ordered dict
    newDict = collections.OrderedDict(sorted(apiDict.items(), key=lambda t: t[1],reverse=True))
    for apiCall in iter(newDict):
        count = newDict[apiCall]        

        percentageAsStr = '{:.2%}'.format(count/total)
        if len(percentageAsStr) < 6:
               percentageAsStr = '{: .2%}'.format(count/total)
        countAsStr = '{:5}'.format(count)
        result = percentageAsStr + countAsStr+" "+apiCall
        print(result)
    summary = ("%3d Total API Requests")%(total)
    print(summary)

#
# Main
#
for line in f:
    if api_call.search(line) is not None:
        apiCallDict = updateApiCallDict(apiCallDict, line)

           
printApiDict(apiCallDict)


