from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .widgets import DatePickerWidget, TimePickerWidget


class SelectTimeWidget(object):
    pass


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Delete junk files', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

    date = forms.DateField(widget=DatePickerWidget)
    time = forms.TimeField(widget=TimePickerWidget)

    # date = forms.DateField(widget=SelectDateWidget(
    #     empty_label=("Choose Year", "Choose Month", "Choose Day"),
    # ),)
    # time = forms.TimeField()

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']