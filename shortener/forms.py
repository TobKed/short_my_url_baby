from django import forms
from .models import Link


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url"]
        labels = {
            'url': '',
        }


class LinkInfoForm(forms.Form):
    url = forms.URLField(disabled=True, label=False)
