from django import forms
from . import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        return super(SignUpForm, self).save()


class StudentForm(forms.ModelForm):

    class Meta:
        model = models.Student
        exclude = ('id',)


class GroupForm(forms.ModelForm):

    class Meta:
        model = models.Group
        exclude = ('id',)


class TeacherForm(forms.ModelForm):

    class Meta:
        model = models.Teacher
        exclude = ('id',)

    
class SubjectForm(forms.ModelForm):

    class Meta:
        model = models.Subject
        exclude = ('id',)


class GradeForm(forms.ModelForm):

    class Meta:
        model = models.Grade
        exclude = ('id', 'student')