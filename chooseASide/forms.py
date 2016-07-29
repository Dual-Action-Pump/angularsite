__author__ = 'davidaxelrod'
from django import forms


class ThoughtForm(forms.Form):
    PRO_OR_CON = ((True, 'Pro'), (False, 'Con'), )
    opinion = forms.CharField(widget=forms.Textarea)
    pro_or_con = forms.ChoiceField(choices=PRO_OR_CON)

class CreateTopic(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(max_length=100,help_text="A description of the topic")
