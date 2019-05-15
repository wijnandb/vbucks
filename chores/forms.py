from django import forms

class Nameform(forms.Form):
    your_name = forms.CharField(label='Jouw naam', max_length=100)