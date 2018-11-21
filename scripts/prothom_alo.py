import requests
import re
from bs4 import BeautifulSoup

url = input()
data = requests.get(url )
soup = BeautifulSoup(data.text,'html.parser')

title = soup.find_all('title') 

f = open('helloworld.html','w', encoding="utf-8")

message = """<html>
<head>
<meta charset="UTF-8">
</head>
<body> """

headline =  """  <h1>  """ + str (title[0].text ) + """</h1> """


# for i in soup.find_all('noscript',{'id':'ari-noscript'} )[0]:
# 	message+=str(i)

image = ""

for i in soup.find_all('noscript',{'id':'ari-noscript'} )[0].find_all('img'):
	image+=str(i)


body=str(soup.find_all('noscript',{'id':'ari-noscript'} )[0].text  ) + "<br>"

message+=headline
message+=body
message+=image
message+=image


message+= """</body>
</html>"""

f.write(message)
f.close()


