from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Clubs.models import Clubs


class SelectForm(forms.Form):
	cl1=Clubs.objects.filter(source='CL')
	cl2=Clubs.objects.filter(source='DE')
	cl3=Clubs.objects.filter(source='EX')

	li1=[]
	li2=[]
	li3=[]
	for clubs in cl1:
		li1.append((clubs.name,clubs.name))
	for clubs in cl2:
		li2.append((clubs.name,clubs.name))
	for clubs in cl3:
		li3.append((clubs.name,clubs.name))

	tu1=['CLUB',tuple(li1)]
	tu2=['DEPARTMENT',tuple(li2)]
	tu3=['EXTERNAL_COURSES',tuple(li3)]
	li=[tu1,tu2,tu3]
	CHOICES=tuple(li)
	select=forms.ChoiceField(choices=CHOICES)