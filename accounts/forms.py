from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required = True,label='First Name', widget= forms.TextInput(
        attrs={'class': 'input','id' :'', 'placeholder':'First Name'}
    ))
   
    last_name = forms.CharField(required = True,label='Last Name', widget= forms.TextInput(
        attrs={'class': 'input','id' :'', 'placeholder':'Last Name'}
    ))

    username = forms.CharField(required = True,label='First Name', widget= forms.TextInput(
        attrs={'class': 'input', 'id' :'','placeholder':'Username'}
    )) 
  
    email= forms.EmailField(required=True,label='Email',widget=forms.EmailInput(
        attrs={'class': 'input','id' :'','placeholder':'youremail@email.com'}) )

    password1 = forms.CharField(required = True,
        label='New Password1', widget=forms.PasswordInput(
            attrs={'class': 'input','id' :'','placeholder':'********'}
        )
    )
    password2 = forms.CharField(required=True,
        label='New Password2', widget=forms.PasswordInput(
            attrs={'class': 'input','id' :'','placeholder':'********'}
        )
    )
    # last_name = forms.CharField()

    # class Meta:
    #     model= User
    #     fields=['username','email','password1','password2', 'first_name', 'last_name']


class PwdChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder':'Old Password','id': 'form-oldPassword'}
        )
    )

    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder':'New Password','id': 'form-NewPassword'}
        )
    )

    new_password2 = forms.CharField(
        label='New Password 2', widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder':'Repeat new password','id': 'form-New2Password'}
        )
    )

class ContactForm(forms.Form):
    """this is a form for users to cntact us on what they need from our site"""
    first_name = forms.CharField(max_length = 300,required = True,label='',
         widget= forms.TextInput(
            attrs={'class': '', 'id' :'contact_fname','placeholder':'FIRST NAME'}
    )) 
    last_name = forms.CharField(max_length = 300,required = True,label='',widget= forms.TextInput(
        attrs={'class': '', 'contact_lname' :'','placeholder':'LAST NAME'}
    )) 
    email = forms.EmailField(required = True,label='',widget= forms.EmailInput(
        attrs={'class': '', 'id' :'contact_email','placeholder':'email@email.com'}
    )) 
    message_ = forms.CharField(max_length = 5000,label='',required = True, widget= forms.Textarea(
        attrs={'rows':10, 'cols':30,'class': '', 'id' :'contact_message','placeholder':'Your Message'}
    )) 

