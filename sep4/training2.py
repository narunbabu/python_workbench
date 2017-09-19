import urllib.request
 

req = urllib.request.Request('https://arstechnica.com')
html = urllib.request.urlopen(req).read()
print(html)
