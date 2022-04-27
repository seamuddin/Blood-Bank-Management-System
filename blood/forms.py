from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit','mail']


class DRequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodDonorRequest
        fields=['patient_name','patient_age','reason','bloodgroup','mail']
