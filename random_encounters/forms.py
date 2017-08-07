from django import forms

class TravelForm(forms.Form):
    days = forms.IntegerField(
        required = True,
        label = 'Days',
        min_value = 1,
        max_value = 10000
    )

    temperature = forms.ChoiceField(
        required = True,
        choices = [
            ('Temperate', 'Temperate'),
            ('Tropical','Tropical'),
            ('Cold', 'Cold')
        ]
    )
    
    population = forms.ChoiceField(
        required = True,
        choices = [
            ('Wilderness', 'Wilderness'),
            ('Rural', 'Rural'),
            ('Urban', 'Urban')
        ]
    )
    
    terrain = forms.ChoiceField(
        required = True,
        choices = [
            ('Plains', 'Plains'),
            ('Forest', 'Forest'),
            ('Hills', 'Hills'),
            ('Mountains', 'Mountains'),
            ('Desert', 'Desert'),
            ('Swamp', 'Swamp')
        ]
    )
