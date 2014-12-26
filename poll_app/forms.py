from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegisterationForm(UserCreationForm):
	"""Writing Form for User registeration. """

	# defining the fields that we want in our form
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=100, required=True)


	class Meta(object):
		"""docstring for Meta"""
		model = User #The model we are using
		#Fields we gonna to contain
		fields = ('username', 'email', 'password1', 'password2', 'first_name')
	
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']

		if commit:
			user.save()

		return user
