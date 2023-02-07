from django import forms
from django.contrib.auth.forms import UserCreationForm

from adminFCT.models import Profesor, User, Contacto, Empleado, Empresa

class ProfesorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user
class registro(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        '''fields = [
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            "password1",
            "password2",
        ]'''



'''
class ContactoForm(forms.Form):
    empresa = forms.ModelChoiceField(label='empresa',queryset=Empresa.objects.all())
    empleado = forms.ModelChoiceField(label='empleado',queryset=Empleado.objects.all())
    #nombre = forms.CharField(max_length=100)
    mailCon = forms.EmailField()


'''
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['empresa','empleado','mailCon']

class ContactoForm2(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nomEmp']
