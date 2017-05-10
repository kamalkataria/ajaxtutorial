from django import forms
from ajaxit.models import Employees

# from ajaxdemo import settings
DATE_INPUT_FORMATS = ['%d-%m-%Y']
# formats=DATE_INPUT_FORMATS
class EmployeeForm(forms.ModelForm):
    emp_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control play', 'placeholder': 'Employee Name','required':'true'}),
        label='')

    emp_email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control play', 'placeholder': 'Email Address','required':'true'}),
        label='')
    emp_dob = forms.DateField(
        widget=forms.DateInput(format="%d-%m-%Y",attrs={'class': 'form-control play', 'placeholder': 'Date of Birth(yyyy-mm-dd)','required':'true'}),
        label='')
    emp_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control play', 'placeholder': 'Password','required':'true'}),
        label='')

    class Meta:
        model = Employees
        fields = ['emp_name', 'emp_email', 'emp_dob', 'emp_pass']
