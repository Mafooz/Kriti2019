from django import forms
from Courses.models import CoursesE

class RecommendForm(forms.ModelForm):

	class Meta:
		model = CoursesE
		fields = ('name','link','uploaded_by')


