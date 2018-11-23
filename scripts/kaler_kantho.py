import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse


import simplejson as json
 
def news(url):

	data = requests.get(url )
	data.encoding = "utf-8"
	soup = BeautifulSoup(data.text,'html.parser') 

	message = """<html>
	<head>
	<meta charset="UTF-8">
	</head>
	<body> """

	headline =  str (soup.find_all('h2')[0] .text ) 

	image = ""

	if len(soup.find_all('img',{'class':'img'} )):
		for i in soup.find_all('img',{'class':'img'} ) :
			tmp = i
			tmp["height"]="200" 
			tmp ["width"]="250" 
			image+=str(tmp)
	body = ""

	for i in soup.find_all('div',{'class':'some-class-name2'} )[0].find_all('p'):
		body+=str(i.text )
 

	message+="<br>"
	message+="""  <h2>  """ + headline + """</h2> """
	message+="<br>"
	message+=body
	message+="<br>"
	message+="<br>"
	message+=image 


	message+= """</body>
	</html>"""
	
	data = {}

	data ['headline'] = headline
	data ['body'] = body
	data ['image'] = image 
	data['message'] = message
	return data

