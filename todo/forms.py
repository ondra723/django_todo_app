from django import forms
from django.forms import SelectDateWidget


class SelectTimeWidget(object):
    pass


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Delete junk files', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

    date = forms.DateField()
    time = forms.TimeField()

    # date = forms.DateField(widget=SelectDateWidget(
    #     empty_label=("Choose Year", "Choose Month", "Choose Day"),
    # ),)
    # time = forms.TimeField()