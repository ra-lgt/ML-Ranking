from django import forms


class Register(forms.Form):
    email_id = forms.EmailField(max_length=100)
    passwd = forms.CharField(max_length=100)
    re_password = forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)

class Login(forms.Form):
    email_id=forms.EmailField(max_length=100)
    passwd=forms.CharField(max_length=100)



class contact(forms.Form):
    name=forms.CharField(max_length=100)
    emails = forms.EmailField(max_length=100)
    message=forms.CharField(max_length=100)
    subject=forms.CharField(max_length=100)
    number=forms.CharField(max_length=100)
