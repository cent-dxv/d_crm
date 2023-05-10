from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Records


class signup_form(UserCreationForm):
  email = forms.EmailField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control my-4' , 'placeholder' :'Email addres'}))
  username= forms.CharField( max_length='20' , widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' :'User Name'}))
  # phone = forms.NumberInput(  widget=forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' :'+251'}))

  class Meta:
    model = User
    fields =('email' , 'username','password1' ,  'password2')



  def __init__(self, *args, **kwargs):
    super(signup_form, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span> <br/><br/>'

    self.fields['password1'].widget.attrs['class'] = 'form-control my-3'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = 'password'
    # self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>  Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
    self.fields['password1'].help_text = ''

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



class AddRecord_form(forms.ModelForm):

    firstname =  forms.CharField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control ' , 'placeholder' :'first name'}))
    lastname =   forms.CharField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control ' , 'placeholder' :'first name'}))
    address =  forms.CharField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control ' , 'placeholder' :'last name'}))
    email = forms.EmailField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control my-4' , 'placeholder' :'Email addres'}))
    city =   forms.CharField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control ' , 'placeholder' :'city'}))
    state =  forms.CharField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control ' , 'placeholder' :'state'}))
    zipcode =  forms.CharField(label="" , widget=forms.TextInput(attrs={'class' : 'form-control ' , 'placeholder' : 'zip code'}))

    class Meta:
      model = Records
      exclude = ("user" ,)