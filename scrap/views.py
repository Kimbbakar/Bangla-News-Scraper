import os,sys
from django.shortcuts import render
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