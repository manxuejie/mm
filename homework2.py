from urllib import request
url='http://www.17k.com/chapter/2933095/36699279.html'
wp = request.urlopen(url)
contene = wp.read()
fp = open("test.txt","w+b")
fp.write(content)
fp.close()