import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse


import simplejson as json
 
def news(url):

	data = requests.get(url )
	data.encoding = "utf-8"
	soup = BeautifulSoup(data.text,'html.parser')
 
	message = """
	<html> 
		<head> 
			<meta charset="UTF-8">
		</head>
	
		<body> 
	"""

	headline =  str (soup.find_all('title')[0].text )  


	image = ""

	if len(soup.find_all('noscript',{'id':'ari-image-1566436'} ) ) :
		for i in soup.find_all('noscript',{'id':'ari-image-1566436'} )[0].find_all('img'):
			tmp = i
			tmp ["height"] ="200" 
			tmp ["width"]  ="250"
			image+=str(tmp)


	if len(soup.find_all('noscript',{'id':'ari-noscript'} ) ) :
		for i in soup.find_all('noscript',{'id':'ari-noscript'} )[0].find_all('img'):
			tmp = i
			tmp["height"] ="200" 
			tmp ["width"] ="250"
			image+=str(tmp)



	body=str(soup.find_all('noscript',{'id':'ari-noscript'} )[0].text  )

	message+="<br>"
	message+="""  <h2>  """ + headline + """</h2> """
	message+="<br>"
	message+=body
	message+="<br>"
	message+="<br>"
	message+=image 


	message+= """
		</body>
	</html>
	"""
	
	data = {}

	data ['headline'] = headline
	data ['body']     = body
	data ['image']    = image 
	data ['message']  = message
	return data

