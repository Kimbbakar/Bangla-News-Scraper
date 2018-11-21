import os,sys
from django.shortcuts import render
SCRIPT_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.join(SCRIPT_DIR, 'script'); 
sys.path.append(SCRIPT_DIR)


def home(request):
	return render(request,'home.html')