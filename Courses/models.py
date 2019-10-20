from django.db import models
from django.contrib.auth.models import User
from Clubs import models as Clubs_Model
import os

def UploadedConfigPath(instance, filename):
	return os.path.join(filename)


class Shared_notes(models.Model):
	name=models.CharField(max_length=200)
	uploaded_by=models.CharField(max_length=200)
	uploaded_at=models.DateTimeField(auto_now_add=True)


class CoursesC(models.Model):
	name=models.CharField(max_length=200)
	shared_notes=models.ManyToManyField(Shared_notes,related_name='courses')
	clubs=models.ManyToManyField(Clubs_Model.Clubs,related_name='courses')
	class Meta:
		verbose_name_plural='Courses for Clubs and Departments'


class Videos(models.Model):
	name=models.CharField(max_length=200)
	uploaded_by=models.CharField(max_length=200)
	uploaded_at=models.DateTimeField(auto_now_add=True)	
	courses=models.ForeignKey(CoursesC,null=True,related_name='videos',on_delete=models.CASCADE)
	videos=models.FileField(null=True,upload_to=UploadedConfigPath)
	def __str__(self):
		return self.name


class CoursesE(models.Model):
	name=models.CharField(max_length=200)
	link=models.CharField(max_length=500,null=True)
	hosted_by=models.ManyToManyField(Clubs_Model.Clubs,related_name='courseE')	
	is_recommended=models.BooleanField(default=False)
	uploaded_by=models.CharField(max_length=200)
	class Meta:
		verbose_name_plural='External Courses'


	def __str__(self):
		return self.name