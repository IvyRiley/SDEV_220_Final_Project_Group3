from django import forms

class EncryptForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    method = forms.ChoiceField(choices=[('basic', 'Hex'), ('caesar', 'Caesar + Hex')])

class DecryptForm(forms.Form):
    encrypted = forms.CharField(widget=forms.Textarea)
    method = forms.ChoiceField(choices=[('basic', 'Hex'), ('caesar', 'Caesar + Hex')])