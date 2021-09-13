from django import forms
from student.models import student





class NameForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    citizenid = forms.CharField(label='Citizen ID', max_length=100)
    CHOICES = [('M','Male'),('F','Female')]
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=['1980','1981','1982','1983','1984','1985','1986']))
    email = forms.CharField(label='Email Address', max_length=100)
    mobilenum = forms.CharField(label='Mobile number', max_length=100)
    age = forms.CharField(label='Age', max_length=100)
    address = forms.CharField(label='Address',widget=forms.Textarea)