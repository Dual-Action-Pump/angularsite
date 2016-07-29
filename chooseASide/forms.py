__author__ = 'davidaxelrod'
from django import forms
import re


from django.core.exceptions import ValidationError



class ThoughtForm(forms.Form):
    PRO_OR_CON = ((1, 'Pro'), (0, 'Con'),)
    opinion = forms.CharField(widget=forms.Textarea, max_length=6000)
    pro_or_con = forms.ChoiceField(choices=PRO_OR_CON)


class CreateTopicForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(max_length=100, help_text="A description of the topic")

    def remove_non_ascii(self,text):
        stripped = text.rstrip()
        if re.match(r'^[a-zA-Z0-9][ \'A-Za-z0-9_.?"!,-]*$', stripped):
            return stripped
        else:
            raise ValidationError("Please pick standard characters")

    def clean(self):
        cleaned_data = super(CreateTopicForm, self).clean()
        standardChars = re.compile('[\w\d\'.,/%#@]+')
        for k,item in cleaned_data.items():
            print(item)
            print("prior :" + item)
            item = self.remove_non_ascii(item)
            print("post : " + item)
        return cleaned_data
