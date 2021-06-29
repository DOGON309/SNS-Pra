from django import forms

class PostForm(forms.Form):
    content = forms.CharField(label = 'ツイート', max_length =500, widget=forms.Textarea(attrs={'class': 'form-control'}))