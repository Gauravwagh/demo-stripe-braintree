__author__ = 'gaurav'


from django import forms

class PlanForm(forms.Form):
    plan = forms.CharField()
    token = forms.CharField()