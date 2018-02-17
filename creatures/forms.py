from django import forms


class StandardEncounterForm(forms.Form):
    pass

    
class QuantityEncounterForm(forms.Form):
    quantity = forms.IntegerField(
        required = True,
        label = 'Number',
        min_value = 1,
        max_value = 10000
    )
