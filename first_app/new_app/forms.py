from django import forms
from .models import chaiVariety

#class bnti hai hamesha
class ChaiVarityForm(forms.Form):    
    chai_varity = forms.ModelChoiceField(queryset=chaiVariety.objects.all(), label="Select chai variety")