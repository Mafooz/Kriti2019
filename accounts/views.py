from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SelectForm
from Clubs.models import Clubs

def home(request):
	return render(request,'home.html')

def select(request):
	form=SelectForm(request.POST)
	if form.is_valid():
		clubname=form.cleaned_data['select']
		club=get_object_or_404(Clubs,name=clubname)
		src=club.source
		if src=='EX':
			return redirect('external',clubname)
		else:
			return redirect('courses',clubname)

	form=SelectForm()
	return render(request,'select.html',{'form':form})