from OCVapp.models import UserProfile, test, Questions, Test_select
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Username.")
    email = forms.CharField(help_text="E-mail.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text="Website.", required=False)
	picture = forms.ImageField(help_text="Profile Image", required=False)
	class Meta:
	    model = UserProfile
        fields = ('website', 'picture')

class TestForm(forms.ModelForm):
	desc = forms.CharField(widget = forms.Textarea())
	class Meta:
		model = test

class QuestionForm(forms.ModelForm):
	statement = forms.CharField(widget = forms.Textarea())
	class Meta:
		model = Questions

class Test(forms.ModelForm):
	class Meta:
		model = Test_select

