__author__ = 'davidaxelrod'
from django import forms


class ThoughtForm(forms.Form):
    PRO_OR_CON = ((True, 'Pro'), (False, 'Con'),)
    opinion = forms.CharField(widget=forms.Textarea)
    pro_or_con = forms.ChoiceField(choices=PRO_OR_CON)


class CreateTopicForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(max_length=100, help_text="A description of the topic")

    def clean(self):
        cleaned_data = super(CreateTopicForm, self).clean()
        for item in cleaned_data:
            item = item.decode('utf-8', 'ignore').encode("utf-8")
        return cleaned_data
