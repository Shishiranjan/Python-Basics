#Lecture: internet with python

import urllib.request
# Here to connect or to request the data from server u have to import url library along with request. So urllib is going to request for data on
# port 80 by default which is also the default port for HTTP. This is exactly what ur browser does when u type url in your address bar.It makes request for the data
#available at that address which is actually an ip address. If u know the ipaddress of ur favourite website then u can type that instead of whole url in most of the
#cases.

req = urllib.request.urlopen('https://www.google.com')

print(req.read())
