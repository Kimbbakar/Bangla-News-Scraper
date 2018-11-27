import os,sys
from django.shortcuts import render
from .models import news
from django.http import HttpResponse , JsonResponse
SCRIPT_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.join(SCRIPT_DIR, 'scripts'); 
sys.path.append(SCRIPT_DIR)
 
import prothom_alo,kaler_kantho


def home(request):
	return render(request,'home.html')


def scrap(request):
	data = {}

	if request.POST['portal']=='pa':
		data = prothom_alo.news(request.POST['url'] )
	elif request.POST['portal']=='kk':
		data = kaler_kantho.news(request.POST['url'] )

	return JsonResponse(data)

def postnews(request): 
	data = {}

	if news.objects.filter(url =request.POST['url'] ).exists()==False:
		new_news = news(
			url 		= request.POST['url'],
			portal_name = request.POST['portal'],
			headline 	= request.POST['headline'], 
			body	 	= request.POST['body'],
			img	 		= request.POST['image'],
			email	 	= request.POST['email']
			)
		#new_news.save()

		data ['message'] = "Thanks for your contribution!"

	else:
		data ['message'] = "This news already in our database. We appreciate your contribution!"

	return JsonResponse(data)