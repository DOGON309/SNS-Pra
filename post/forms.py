from django import forms

class PostForm(forms.Form):
    content = forms.CharField(label = 'ツイート', max_length =500, widget=forms.Textarea(attrs={'class': 'form-control'}))

class CommentForm(forms.Form):
    content = forms.CharField(label = 'コメント', max_length =250, widget=forms.TextInput(attrs={'class': 'form-control'}))