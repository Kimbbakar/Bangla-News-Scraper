from django.db import models

class news(models.Model):
    portal_name  = models.CharField(max_length=20)	
    url			 = models.CharField(primary_key=True ,max_length=300,null = False )
    headline 	 = models.CharField(max_length=100)
    body 		 = models.CharField(max_length=5000)
    img			 = models.CharField(max_length=1000)
    email		 = models.CharField(max_length=50,default = "Unknown" ) 