## Django Packages
from django import forms
from django_select2 import forms as s2forms

## App packages
from .models import *
from datetime import datetime
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

############################################################################
############################################################################

class TourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-validation': 'required'}),
                           required=False)

        self.fields['description'] = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'data-validation': 'required'}),
        required=False)

        self.fields['tag'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.SelectMultiple(attrs={'class': 'form-control', 'data-validation': 'required'}),
            choices=getAllTourTags()
        )

    class Meta:
        model = Tour
        fields = (
            'name',
            'description',
            'tag'
        )

class TourSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'] = forms.CharField(
            label='Username',
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=False
        )

        self.fields['name'] = forms.CharField(
            label='Tour Name',
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=False
        )

        self.fields['tag'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
            choices=getAllTourTags()
        )
