from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.utils import timezone
from .models import news

import datetime

import os,sys
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
	request.session.set_expiry(300)
	data = {}

	if news.objects.filter(url =request.POST['url'] ).exists()==False:
		new_news = news(
			url 		= request.POST['url'],
			portal_name = request.POST['portal'],
			headline 	= request.POST['headline'], 
			body	 	= request.POST['body'],
			img	 		= request.POST['image'],
			email	 	= request.session['email']
			)
		new_news.save()

		data ['message'] = "Thanks for your contribution!"
		data ['success'] = True

	else:
		data ['message'] = "This news already in our database. We appreciate your contribution!"
		data ['success'] = False

	return JsonResponse(data)



def contribution(request):
	request.session.set_expiry(300)
	data = {}
	today = datetime.date.today()
	if 'email' not in request.session:
		request.session['email'] = request.POST['email']


	data[ "contribution1" ] = news.objects.filter(email=request.session['email']).count()
	data[ "contribution2" ] = news.objects.filter(email=request.session['email'],date__year = today.year,date__month=today.month,date__day=today.day ).count()
	data[ 'email' ]  = request.session['email']

	return JsonResponse(data)
