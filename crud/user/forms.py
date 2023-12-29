from django import forms


class AddForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=50)
    age = forms.IntegerField()
    gender = forms.BooleanField()
    birthDay = forms.DateField()
