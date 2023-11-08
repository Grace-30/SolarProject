from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserInput2, UserInput, ElectronicDetail



class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
       password=forms.CharField(label='Password', widget=forms.PasswordInput)
       password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)    

       class Meta: 
           model= User
           fields=('username','first_name','last_name','email')

       def clean_password2(self):
            cd=self.cleaned_data
            if cd['password'] != cd['password2']:
                 raise forms.ValidationError('Password don\'t match.')
            return cd['password2'] 

class UserInputForm(forms.ModelForm):
       class Meta: 
           model=UserInput2
           fields= ('loadName','powerOfLoad','noOfLoad','operatingHours','effectiveSunlight')

class UserInputForm1(forms.ModelForm):
     class Meta:
          model= UserInput
          fields= ('load_Name','power_Of_Load','no_Of_Load','operating_Hours','effective_Sunlight')


class ElectronicDetailsForm(forms.ModelForm):
     class Meta:
          model= ElectronicDetail
          fields= ('electronicName','power_Of_Load','no_Of_Load','operating_Hours','effective_Sunlight')


'''class UserInputForm2(forms.ModelForm):
       class Meta: 
           model=UserInput2
           fields= ('loadName','powerOfLoad','noOfLoad','operatingHours','effectiveSunlight')'''
