from django import forms
from django.contrib.auth.forms import UserCreationForm

from adminFCT.models import Profesor, User

class ProfesorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user