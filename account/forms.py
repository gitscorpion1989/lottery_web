from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from models import Lo_bet

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fileds = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()

        return user

class Lo_betForm(ModelForm):
    
    class Meta:
        model = Lo_bet
        fields = ['re1', 're2','re3', 're4','re5', 're6']
        exclude = ['phase', 'bet_date' , 'owner']
