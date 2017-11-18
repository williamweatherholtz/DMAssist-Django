from django import forms

class SpellForm(forms.Form):
    spell_class = forms.ChoiceField()
    level = forms.IntegerField()
