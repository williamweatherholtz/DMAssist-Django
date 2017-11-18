from django import forms

class ItemCountForm(forms.Form):
    item_count = forms.IntegerField(
        required = True, label='Count',
        min_value=1, max_value=10000
    )

class TreasureTypeForm(forms.Form):
    #regex matches at least one alphabetic character with possible numbers in front
    types_str = forms.RegexField(
        required = True, label='Treasure Types',
        strip = True, regex = r'(([0-9]*)?[a-zA-Z]+)+'
    )
