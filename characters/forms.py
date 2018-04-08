from django import forms

class ImportForm(forms.Form):
    name = forms.CharField()
    
    class_role = forms.ChoiceField(
        required = True,
        choices = [
            ('F', 'Fighter'),
            ('R', 'Ranger'),
            ('P', 'Paladin'),
            ('C', 'Cleric'),
            ('D', 'Druid'),
            ('T', 'Thief'),
            ('A', 'Assassin'),
            ('MU', 'Magic-User'),
            ('I', 'Illusionist'),
            ('MO', 'Monk'),
            ('B', 'Bard'),
            ('CF', 'Cleric/Fighter'),
            ('CFM','Cleric/Fighter/Magic-User'),
            ('CR','Cleric/Ranger'),
            ('CM','Cleric/Magic-User'),
            ('CT','Cleric/Thief'),
            ('CA','Cleric/Assassin'),
            ('FM','Fighter/Magic-User'),
            ('FI','Fighter/Illusionist'),
            ('FT','Fighter/Thief'),
            ('FA','Fighter/Assassin'),
            ('FMT','Fighter/Magic-User/Thief'),
            ('MT','Magic-User/Thief'),
            ('IT','Illusionist/Thief'),
        ]
    )
    
    level = forms.IntegerField(
        required=True,
        min_value = 0,
        max_value = 50
    )
    
    hit_points = forms.IntegerField(
        required = True,
        min_value = 1,
        max_value = 5000
    )
    
    strength = forms.IntegerField(
        required=True,
        min_value = 1,
        max_value = 30
    )
    
    dexterity = forms.IntegerField(
        required=True,
        min_value = 1,
        max_value = 30
    )
    
    constitution = forms.IntegerField(
        required=True,
        min_value = 1,
        max_value = 30
    )
    
    intelligence = forms.IntegerField(
        required=True,
        min_value = 1,
        max_value = 30
    )
    
    wisdom =  forms.IntegerField(
        required=True,
        min_value = 1,
        max_value = 30
    )
    
    charisma = forms.IntegerField(
        required=True,
        min_value = 1,
        max_value = 30
    )
    
class CreateForm(forms.Form):
    name = forms.CharField()
    
class AttributesForm(forms.Form):
    str = forms.IntegerField()
    dex = forms.IntegerField()
    con = forms.IntegerField()
    int = forms.IntegerField()
    wis = forms.IntegerField()
    chr = forms.IntegerField()
    com = forms.IntegerField()
