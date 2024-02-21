import urllib.request

var = urllib.request.urlopen("https://www.w3.org/Summary.txt")
for x in var:
    print(x.decode().strip())