from django.shortcuts import render, redirect , get_object_or_404
from .forms import RecommendForm
from .models import CoursesC , Videos , CoursesE
from django.conf import settings
from Clubs.models import Clubs

def recommend(request):
	form=RecommendForm(request.POST)
	if form.is_valid():
		rform=form.save(commit=False)
		rform.save()
		return redirect('home')
	else:
		form=RecommendForm()
	return render(request,'recommend.html',{'form':form})



def playcourse(request,clubname,pk,videoname):
	course=get_object_or_404(CoursesC,pk=pk)
	videos=Videos.objects.filter(courses=course)
	if videoname=='#':
		pvideo=videos[0]
	else:
		pvideo=get_object_or_404(videos,name=videoname)
	return render(request,'course.html',{'videos':videos,'pvideo':pvideo,'course':course,'clubname':clubname})


def courses(request,clubname):
	club=get_object_or_404(Clubs,name=clubname)
	course=CoursesC.objects.filter(clubs=club)
	return render(request,'courses.html',{'course':course,'clubname':clubname})


def external(request,clubname):
	club=get_object_or_404(Clubs,name=clubname)
	courses = CoursesE.objects.filter(hosted_by=club)
	return render(request,'externalcourses.html',{'courses':courses})



