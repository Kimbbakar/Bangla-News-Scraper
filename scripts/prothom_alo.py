import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse


import simplejson as json
 
def news(url):

	data = requests.get(url )
	soup = BeautifulSoup(data.text,'html.parser')

	title = soup.find_all('title') 

	message = """<html>
	<head>
	<meta charset="UTF-8">
	</head>
	<body> """

	headline =  """  <h2>  """ + str (title[0].text ) + """</h2> """


	# for i in soup.find_all('noscript',{'id':'ari-noscript'} )[0]:
	# 	message+=str(i)

	image = ""

	for i in soup.find_all('noscript',{'id':'ari-noscript'} )[0].find_all('img'):
		tmp = i
		tmp["height"]="200" 
		tmp ["width"]="250"
		image+=str(tmp)


	body=str(soup.find_all('noscript',{'id':'ari-noscript'} )[0].text  )

	message+="<br>"
	message+=headline
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

