from django import forms
from Books.models import Books

class BookuploadForm(forms.ModelForm):

	class Meta:
		model = Books
		fields = ('name','file','courses','uploaded_by')

class VerifyForm(forms.Form):
	Username=forms.CharField(max_length=200)	
	class Meta:
		fields=('Username')

		
class OtpForm(forms.Form):
	otp=forms.IntegerField()	
	class Meta:
		fields=('otp')