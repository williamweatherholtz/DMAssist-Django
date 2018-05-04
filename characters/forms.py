from django import forms

from .models import ClassRole

class ImportForm(forms.Form):
    name = forms.CharField(required=True)
    
    hp = forms.IntegerField(required=True,min_value=1, max_value=32767)
    
    str = forms.IntegerField(required=True,min_value=1,max_value=30)
    dex = forms.IntegerField(required=True,min_value=1,max_value=30)
    con = forms.IntegerField(required=True,min_value=1,max_value=30)
    int = forms.IntegerField(required=True,min_value=1,max_value=30)
    wis = forms.IntegerField(required=True,min_value=1,max_value=30)
    chr = forms.IntegerField(required=True,min_value=1,max_value=30)
    com = forms.IntegerField(required=True,min_value=1,max_value=30)
    
    level = forms.IntegerField(
        min_value = 0, max_value = 500
    )
    
    class_role = forms.ChoiceField(
        required = True,
        choices = [
            (ClassRole.FIGHTER.value, 'Fighter'),
            (ClassRole.RANGER.value, 'Ranger'),
            (ClassRole.PALADIN.value, 'Paladin'),
            (ClassRole.CLERIC.value, 'Cleric'),
            (ClassRole.DRUID.value, 'Druid'),
            (ClassRole.THIEF.value, 'Thief'),
            (ClassRole.ASSASSIN.value, 'Assassin'),
            (ClassRole.MAGIC_USER.value, 'Magic-User'),
            (ClassRole.ILLUSIONIST.value, 'Illusionist'),
            (ClassRole.MONK.value, 'Monk'),
            (ClassRole.BARD.value, 'Bard'),
            (ClassRole.ACROBAT.value, 'Acrobat'),
            (ClassRole.CAVALIER.value, 'Cavalier'),
            (ClassRole.BARBARIAN.value, 'Barbarian'),
        ]
    )
    
class CreateForm(forms.Form):
    name = forms.CharField()
