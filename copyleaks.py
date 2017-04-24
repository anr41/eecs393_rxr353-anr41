#Ashley Roberson

import requests
import smtplib
import json

url = 'https://api.copyleaks.com'

#Gets API Token
response = requests.post(url + '/v1/account/login-api', data = {"Email": "anr41@case.edu", "ApiKey": "4D169E9D-59EF-40ED-A456-C37C3F731603"})
token = response.json()['access_token']
print(token)

headers = {'Http Request headers': 'copyleaks-sandbox-mode'}
headers['Authorization']= 'Bearer %s' % token

files = {'file': open('assignment.txt', 'rb')}
response = requests.post(url + '/v1/academic/create-by-text', headers=headers, files=files)

print(response.text)

pid = response.json()['ProcessId']

while True:
    response = requests.get(url + '/v1/academic/%s/status' % pid, headers=headers)
    Status = response.json()['Status']
    print(Status)
    if(Status == 'Finished'):
	    break

response = requests.get(url + '/v1/academic/%s/result' % pid, headers=headers)
print(response.headers)
print(json.loads(response.text))
percents = json.loads(response.text)
print('Percents: %d' % percents)
numberOfCopiedWords = json.loads(response.text)['NumberOfCopiedWords']
print('NumberOfCopiedWords: %d' % numberOfCopiedWords)
comparisonReport = json.loads(response.text)['ComparisonReport']
print('ComparisonReport: %s' % comparisonReport)
title = json.loads(response.text)['Title']
print('Title: %s' % title)