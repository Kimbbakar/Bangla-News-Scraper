from django.db import models

class news(models.Model):
    portal_name  = models.CharField(max_length=20)	
    headline 	 = models.CharField(max_length=100)
    body 		 = models.CharField(max_length=5000)
    img			 = models.CharField(max_length=1000)
    ok		     = models.IntegerField();    