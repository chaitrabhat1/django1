from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=10)
    input=forms.IntegerField(min_value=1, max_value=100, label="$3")