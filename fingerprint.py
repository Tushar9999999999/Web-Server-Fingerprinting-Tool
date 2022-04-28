import os
import requests

print("\nWelcome to Webserver fingerprinting tool collection")
print("Where you can get all info about web servers used by website from various tools to provide more accuracy in indetification")
print("Developed by Tushar, Sahith and Vidip\n")

server = input("Enter server name: ")

req = requests.get('http://www.' + server)
print("\nBanner Grab")
print(req.headers)
print()

some_headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'ETag']
for header in some_headers:
    try:
        result = req.headers[header]
        print(header + " : " + result)
    except:
        print(header + " : Not found")

try:
    print("\nProbable Server Type")
    data = list(req.headers)
    for i in range(len(data)):
        if(data[i]=='Date' or data[i]=='date'):
            d=i
        if(data[i]=='Server' or data[i]=='server'):
            s=i

    if(d>s):
        print("Might be Apache\n")
    else:
        print("Might be IIS/Netscape\n")
except:
    print("Could not find probable server type\n")

try:
    print("WhatWeb")
    os.system("whatweb " + server)
except:
    print("whatweb error")

try:
    print("\nMalformed Request")
    os.system("nc " + server + " 80")
except:
    print("netcat error")