from django.shortcuts import render,redirect
from FirstApp.models import *
from FirstApp.forms import *
from django.core.mail import send_mail
from GOU import settings 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.



def register(request):
	if request.method=='POST':
		#form=UserSignUpForm(request.POST)
		user=User.objects.create_user(first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],email=request.POST['email'],
			username=request.POST['username'],password=request.POST['password1'])
		desig=request.POST['desig']
		Desig.objects.create(desig=desig,user=user)
		messages.success(request,request.POST['username']+' is Succefully Registered')
	pform=user_desig()
	form = UserSignUpForm()
	return render(request,'Register.html',{'form':form,'pform':pform})

@login_required
def welcome(request):

	return render(request,'welcome.html')

@login_required
def dashboard(request):
	n=documentuserdata.objects.last()

	return render(request,'welcome.html')




@login_required
def document(request):
	form=typeoffile()
	return render(request,'document.html',{'form':form})

def tofile(request):
	if request.method=='POST':
		data=documentuserdata(typeoffiles=request.POST['filetype'])
		data.save()
		return redirect('/selectafile')

def userrecived(request,username):
	data=documentuserdata.objects.filter(u_name=username)
	return render(request,'userrecived.html',{'data':data})

@login_required
def selectafile(request):
	if request.method=='POST':
		u_name=request.POST['towhom']
		u_file=request.FILES['file']
		u_description=request.POST['description']
		data=documentuserdata.objects.last()
	
		data.u_name=u_name
		data.u_file=u_file
		data.u_description=u_description
		#userdata=Desig.objects.get(user_id=user.id)
		"""print(User.id)
								if data.notify==0:
									data.notify=data.notify+1
								else:
									data.notify=0"""

		
		#data=documentuserdata(u_name=u_name,u_file=u_file,u_description=u_description)
		data.save()
		
		return HttpResponse('File Transfered Succefully...!')
		#messages.success(request,request.POST['towhom']+' File transfered Succefully')
	

	form=selectfileForm()
	return render(request, 'selectafile.html',{'form':form})

def forgotpwd(request):
	if request.method=='POST':
		data=User.objects.get(email=request.POST['email'])
		sub="Reg to Your Login details...!"
		body="Username is: "+data.username+" password is: "+data.password
		sender=settings.EMAIL_HOST_USER
		reciver=request.POST['email']
		send_mail(sub,body,sender,[reciver])
		return HttpResponse('<h1>Check Your Eamil for login details</h1>')
	return render(request,"forgotpwd.html")

def notification(request):
	global n
	n=0
	return redirect('/userrecived')
	