import urllib.request as urlr
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urlr.urlopen(url)
localFile = open('iris.csv', 'w')
localFile.write(u.read())