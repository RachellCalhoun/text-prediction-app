from django import forms



class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40}))
