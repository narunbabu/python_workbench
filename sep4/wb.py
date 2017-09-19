import numpy as np
import urllib.request as ur

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = ur.urlopen(url)

##localFile = open('iris.csv', 'w')
##localFile.write(u.read().decode('utf-8'))
##localFile.write(u.read().decode(u.headers.get_content_charset()))
##localFile.close()

with open('iris.csv', 'wb') as f:
    f.write(u.read())
##try:
##    url = 'https://www.google.com/search?q=python'
##
##    # now, with the below headers, we defined ourselves as a simpleton who is
##    # still using internet explorer.
##    headers = {}
##    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
##    req = ur(url, headers = headers)
##    resp = ur.urlopen(req)
##    respData = resp.read()
##
##    saveFile = open('withHeaders.txt','w')
##    saveFile.write(str(respData))
##    saveFile.close()
##except Exception as e:
##    print(str(e))
