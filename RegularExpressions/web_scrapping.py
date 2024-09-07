import re
import urllib.request

sites = ['google.com', 'bharaththippireddy.com']

for s in sites:
    print("Searching", s)
    response = urllib.request.urlopen("http://"+s)
    text = str(response.read())
    title = re.findall("<title>.*</title>", text, re.I)
    print(title[0])