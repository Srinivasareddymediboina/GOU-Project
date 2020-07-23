import datetime
from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Desig(models.Model):
	options=[(1,'CLERK'),(2,'JTO'),(3,'AD'),(4,'ADET'),(5,'ADG'),(6,'DIR'),(7,'DDG'),(8,'OTHER DDGS'),(9,'SRDDG')]
	desig=models.CharField(max_length=50,null=True,choices=options)
	role=models.IntegerField(null=True)
	user=models.OneToOneField(User,on_delete=models.CASCADE)

class documentuserdata(models.Model):
	u_name=models.CharField(max_length=100,null=True)
	u_file=models.FileField(upload_to='documentuser/',null=True)
	u_description=models.TextField(max_length=500,null=True)
	typeoffiles=models.CharField(max_length=50, null=True)




userdata=User.objects.all()
class typeoffile(models.Model):

	vals=[('adminfile','Adminfile'),('aplsafile','Aplsafile'),
	('compliancefile','Compliancefile'),('itfile','Itfile'),
	('ruralfile','Ruralfile'),('srfile','Srfile'),
	('securityfile','Securityfile'),('technologyfile','Technologyfile')]
	
	filetype=models.CharField(max_length=50, choices=vals)


# Create your models here.

class selectfile(models.Model):
	#v=[('vro','VRO'),('vra','VRA'),('ai','AI'),('mro','MRO')]
	v=[('clerk','CLERK'),("jto",'JTO'),("ad",'AD'),("adet",'ADET'),('adg','ADG'),('dir','DIR'),('ddg','DDG'),('other ddgs','OTHER DDGS'),('srddg','SRDDG')]
	"""for i in userdata:
			 		v.append((i.username,i.username))"""

	towhom = models.CharField(max_length = 100,choices=v, null=True)
	#als=[('adminfile','Adminfile'),('aplsafile','Aplsafile'),('compliancefile','Compliancefile'),('itfile','Itfile'),('ruralfile','Ruralfile'),('srfile','Srfile'),('securityfile','Securityfile'),('technologyfile','Technologyfile')]
	file=models.FileField(null=True)
	description = models.TextField(null=True)
	date_added = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.filename
	def added(self):
		return self.date_added >= timezone.now() - datetime.timedelta(days=1)
	class Meta:
		verbose_name = 'Admin File'
		verbose_name_plural = 'Admin Files'



 

