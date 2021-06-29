from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))