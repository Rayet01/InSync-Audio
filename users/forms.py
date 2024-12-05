from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Add the email field to the form

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'email', 'location']  # Include the email field here

    def __init__(self, *args, **kwargs):
        # Pop the user from kwargs
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Prepopulate the email field if the user is provided
        if user:
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        # Save the email change to the User model
        profile = super().save(commit=False)
        user = profile.user
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile