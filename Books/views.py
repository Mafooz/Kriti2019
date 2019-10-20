from django.shortcuts import render, redirect
from .forms import BookuploadForm, VerifyForm, OtpForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django_otp.oath import totp
from .models import Books
import time
secret_key=b'12345678901234567890'
now=int(time.time())


def books(request):
	book = Books.objects.all()
	return render(request,'book.html',{'books':book})

def otp(request):
	if request.session['otp']==0:
		return redirect('verifyourself')

	if request.method=='POST':
		form=OtpForm(request.POST)
		if form.is_valid():
			var=form.cleaned_data['otp']
			if var==request.session['0'] :
				request.session['otp']=0
				request.session['books']=1
				return redirect('bookupload')
			else:
				form=OtpForm()
	else:
		form=OtpForm()
	return render(request,'otp.html',{'form':form})	

def verifyourself(request):
	if request.method=='POST':
		form=VerifyForm(request.POST)
		if form.is_valid():
			email=form.cleaned_data['Username']
			var=totp(key=secret_key, step=10,digits=6,t0=(now-30))
			otp=var
			send_mail(
				'Otp verification',
				'Your otp is '+ str(var),
				'elearnweb.kriti@gmail.com',
				[email + '@iitg.ac.in'],
				fail_silently=False,
			)
			request.session['0']=var
			request.session['otp']=1
			request.session['books']=0
			return redirect('otp')	
	else:
		form=VerifyForm()
	return render(request,'verify.html',{'form':form})	


def bookupload(request):
	form=BookuploadForm(request.POST,request.FILES)
	if form.is_valid():
		rform=form.save(commit=False)
		rform.save()
		return redirect('home')
	else:
		form=BookuploadForm()
	return render(request,'bookupload.html',{'form':form})