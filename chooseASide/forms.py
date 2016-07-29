__author__ = 'davidaxelrod'
from django import forms
import re

from django.core.exceptions import ValidationError


class ThoughtForm(forms.Form):
    PRO_OR_CON = ((1, 'Pro'), (0, 'Con'),)
    opinion = forms.CharField(widget=forms.Textarea)
    pro_or_con = forms.ChoiceField(choices=PRO_OR_CON)


class CreateTopicForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(max_length=100, help_text="A description of the topic")

    def clean(self):
        cleaned_data = super(CreateTopicForm, self).clean()
        standardChars = re.compile('[\w\d\'.,/%#@]+')
        for item in cleaned_data:
            if not standardChars.match(item):
                raise ValidationError(_('Invalid Special Character.'))
        return cleaned_data
