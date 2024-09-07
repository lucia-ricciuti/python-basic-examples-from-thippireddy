import urllib.request

try:
    url = urllib.request.urlopen("http://www.python.org")
    content = url.read()
except urllib.error.HTTPError:
    print("The the web page is not found")
    exit()
    
f = open("python.html", "wb")
f.write(content)
f.close()