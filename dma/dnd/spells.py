from random import sample,choice

from .roll import roll
from .time import TimePeriod, TimeUnit
from .sourcebook import SourceBook

#aliases for the lazy
S = TimeUnit.segment
R = TimeUnit.round
T = TimeUnit.turn
H = TimeUnit.hour
D = TimeUnit.day
Y = TimeUnit.year
VA = TimeUnit.variable
P = TimeUnit.permanent
tp = TimePeriod

V = SourceBook.v
U = SourceBook.ua

#contains minimal info on spells (name, class and level)
class Spell():
    def __init__(self, name, spell_class, level,
            cast=None, duration=TimePeriod(0,R), duration_lvl=TimePeriod(0,S),
            sourcebook=None):
        self.name = name
        self.role = spell_class
        self.level = level

        #additional information (not yet defined for most spells
        self.cast_time = cast
        self.duration = duration
        self.duration_per_level = duration_lvl
        self.sourcebook = sourcebook

    def __str__(self):
        spell_class = ''
        if self.role == 'M':
            spell_class = 'Magic-User'
        elif self.role == 'I':
            spell_class = 'Illusionist'
        elif self.role == 'C':
            spell_class = 'Cleric'
        elif self.role == 'D':
            spell_class = 'Druid'


        ret = '{} ({} Lvl {})'.format(self.name,spell_class,self.level)
        return ret

    def __lt__(self,other):
        if self.level < other.level:
            return True
        elif self.level > other.level:
            return False
        else:
            if self.name.lower() < other.name.lower():
                return True
            else:
                return False

    def __eq__(self,other):
        if (self.name == other.name and
            self.level == other.level and
            self.role == other.role):
            return True
        else: return False

def randomSpellScroll(num,mu_min,mu_max,cl_min=0,cl_max=0):
    #Set cleric range to mu_range if cl_min/max are not given
    if (not cl_min): cl_min = mu_min
    if (not cl_max): cl_max = mu_max

    spells = ''

    r = roll(100)
    if r > 70:
        r = roll(100)
        if r > 75:
            spells = [s for s in druid_spells
                if s.level >= cl_min and s.level <= cl_max]
        else:
            spells = [s for s in cleric_spells
                if s.level >= cl_min and s.level <= cl_max]
    else:
        r = roll(100)
        if r > 90:
            spells = [s for s in illusionist_spells
                if s.level >= mu_min and s.level <= mu_max]
        else:
            spells = [s for s in mu_spells
                if s.level >= mu_min and s.level <= mu_max]

    spells = sample(spells, num)
    spells = sorted(spells, key=lambda spell: spell.level)
    spells = [str(s) for s in spells]
    return spells

cleric_spells = [
    Spell(
        name='Bless',
        spell_class='C',
        level=1,
        cast=tp(1,R),
        duration=tp(6,R),
        sourcebook=V
    ),
    Spell('Ceremony','C',1,
        cast=tp(1,H),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Combine','C',1,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Command','C',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Create Water','C',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Cure Light Wounds','C',1,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Detect Evil','C',1,
        cast=tp(1,R),
        duration=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Detect Magic','C',1,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Endure Cold/Heat','C',1,
        cast=tp(1,R),
        duration_lvl=tp(9,T),
        sourcebook=U
    ),
    Spell('Invisibility to Undead','C',1,
        cast=tp(4,S),
        duration=tp(6,R),
        sourcebook=U
    ),
    Spell('Light','C',1,
        cast=tp(4,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Magic Stone','C',1,
        cast=tp(1,R),
        duration=tp(6,R),
        sourcebook=U
    ),
    Spell('Penetrate Disguise','C',1,
        cast=tp(2,R),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Portent','C',1,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Precipitation','C',1,
        cast=tp(3,S),
        duration_lvl=tp(1,S),
        sourcebook=U
    ),
    Spell('Protection From Evil','C',1,
        cast=tp(4,S),
        duration=tp(0,R),
        duration_lvl=tp(3,R),
        sourcebook=V
    ),
    Spell('Purify Food & Drink','C',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Remove Fear','C',1,
        cast=tp(4,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Resist Cold','C',1,
        cast=tp(1,R),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Sanctuary','C',1,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Aid','C',2,
        cast=tp(4,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Augury','C',2,
        cast=tp(2,R),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Chant','C',2,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Detect Charm','C',2,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Detect Life','C',2,
        cast=tp(1,R),
        duration=tp(5,R),
        sourcebook=U
    ),
    Spell('Dust Devil','C',2,
        cast=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Enthrall','C',2,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Find Traps','C',2,
        cast=tp(5,S),
        duration=tp(3,T),
        sourcebook=V
    ),
    Spell('Hold Person','C',2,
        cast=tp(5,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Holy Symbol','C',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Know Allignment','C',2,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Messenger','C',2,
        cast=tp(1,R),
        duration_lvl=tp(1,H),
        sourcebook=U
    ),
    Spell('Resist Fire','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Silence 15\' Radius','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Slow Poison','C',2,
        cast=tp(1,S),
        duration=tp(0),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Snake Charm','C',2,
        cast=tp(5,S),
        duration=tp(VA),
        sourcebook=V
    ),
    Spell('Speak With Animals','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Spiritual Hammer','C',2,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Withdraw','C',2,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Wyvern Watch','C',2,
        cast=tp(5,S),
        duration=tp(8,H),
        sourcebook=U
    ),
    Spell('Animate Dead','C',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Cloudburst','C',3,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Continual Light','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Create Food & Water','C',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Cure Blindness','C',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Cure Disease','C',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Death\'s Door','C',3,
        cast=tp(5,S),
        duration_lvl=tp(1,H),
        sourcebook=U
    ),
    Spell('Dispel Magic','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Feign Death','C',3,
        cast=tp(2,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Flame Walk','C',3,
        cast=tp(5,S),
        duration=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Glyph of Warding','C',3,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Locate Object','C',3,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Magical Vestment','C',3,
        cast=tp(1,R),
        duration_lvl=tp(6,R),
        sourcebook=U
    ),
    Spell('Meld Into Stone','C',3,
        cast=tp(7,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Negative Plane Protection','C',3,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Prayer','C',3,
        cast=tp(6,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Remove Curse','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Remove Paralysis','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        duration_lvl=tp(0),
        sourcebook=U
    ),
    Spell('Speak With Dead','C',3,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Water Walk','C',3,
        cast=tp(7,S),
        duration=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Abjure','C',4,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Cloak of Fear','C',4,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Cure Serious Wounds','C',4,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Detect Lie','C',4,
        cast=tp(7,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Divination','C',4,
        cast=tp(1,T),
        duration=tp(0,R),
        sourcebook=V
    ),
    Spell('Exorcise','C',4,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Giant Insect','C',4,
        cast=tp(1,VA),
        duration_lvl=tp(2,R),
        sourcebook=U
    ),
    Spell('Imbue With Spell Ability','C',4,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Lower Water','C',4,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Neutralize Poison','C',4,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Protection From Evil 10\' Radius','C',4,
        cast=tp(7,S),
        duration=tp(0,R),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Speak With Plants','C',4,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Spell Immunity','C',4,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Spike Growth','C',4,
        cast=tp(7,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Sticks to Snakes','C',4,
        cast=tp(7,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Tongues','C',4,
        cast=tp(7,S),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Air Walk','C',5,
        cast=tp(1,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Animate Dead Monsters','C',5,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Atonement','C',5,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Commune','C',5,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Cure Critical Wounds','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Dispel Evil','C',5,
        cast=tp(8,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Flame Strike','C',5,
        cast=tp(8,S),
        duration=tp(1,S),
        sourcebook=V
    ),
    Spell('Golem','C',5,
        cast=tp(8,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Insect Plague','C',5,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Magic Font','C',5,
        cast=tp(5,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Plane Shift','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Quest','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Rainbow','C',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Raise Dead','C',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Spike Stones','C',5,
        cast=tp(6,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('True Seeing','C',5,
        cast=tp(8,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Aerial Servant','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,D),
        sourcebook=V
    ),
    Spell('Animate Object','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Blade Barrier','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(3,R),
        sourcebook=V
    ),
    Spell('Conjure Animal','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Find The Path','C',6,
        cast=tp(3,R),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Forbiddance','C',6,
        cast=tp(6,R),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Heal','C',6,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Heroes\' Feast','C',6,
        cast=tp(1,T),
        duration=tp(1,H),
        sourcebook=U
    ),
    Spell('Part Water','C',6,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Speak With Monsters','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Stone Tell','C',6,
        cast=tp(1,T),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Word of Recall','C',6,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Astral Spell','C',7,
        cast=tp(3,T),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Control Weather','C',7,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Earthquake','C',7,
        cast=tp(1,T),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Exaction','C',7,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Gate','C',7,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Holy (Unholy) Word','C',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Regenerate','C',7,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Restoration','C',7,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Resurrection','C',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Succor','C',7,
        cast=tp(1,D),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Symbol','C',7,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Wind Walk','C',7,
        cast=tp(1,R),
        duration_lvl=tp(6,T),
        sourcebook=V
    )
]

druid_spells = [
    Spell('Animal Friendship','D',1,
        cast=tp(6,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Ceremony','D',1,
        cast=tp(1,H),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Detect Balance','D',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Detect Magic','D',1,
        cast=tp(3,S),
        duration=tp(12,R),
        sourcebook=V
    ),
    Spell('Detect Poison','D',1,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Detect Snares & Pits','D',1,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(4,R),
        sourcebook=V
    ),
    Spell('Entangle','D',1,
        cast=tp(3,S),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Faerie Fire','D',1,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(4,R),
        sourcebook=V
    ),
    Spell('Invisibility to Animals','D',1,
        cast=tp(4,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Locate Animals','D',1,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Pass Without Trace','D',1,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Precipitation','D',1,
        cast=tp(3,S),
        duration_lvl=tp(1,S),
        sourcebook=U
    ),
    Spell('Predict Weather','D',1,
        cast=tp(1,R),
        duration_lvl=tp(2,H),
        sourcebook=V
    ),
    Spell('Purify Water','D',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Shillelagh','D',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Speak With Animals','D',1,
        cast=tp(3,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Barkskin','D',2,
        cast=tp(3,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Charm Person Or Mammal','D',2,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Create Water','D',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Cure Light Wounds','D',2,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Feign Death','D',2,
        cast=tp(3,S),
        duration=tp(4,R),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Fire Trap','D',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Flame Blade','D',2,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Goodberry','D',2,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Heat Metal','D',2,
        cast=tp(4,S),
        duration=tp(7,R),
        sourcebook=V
    ),
    Spell('Locate Plants','D',2,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Obscurement','D',2,
        cast=tp(4,S),
        duration_lvl=tp(4,R),
        sourcebook=V
    ),
    Spell('Produce Flame','D',2,
        cast=tp(4,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Reflecting Pool','D',2,
        cast=tp(2,H),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Slow Poison','D',2
        cast=tp(0),
        duration=tp(0),
        duration_lvl=tp(0),
        sourcebook=U
    ),
    Spell('Trip','D',2,
        cast=tp(4,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Warp Wood','D',2,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Call Lightning','D',3,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Cloudburst','D',3,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U,
    ),
    Spell('Cure Disease','D',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Hold Animal','D',3,
        cast=tp(5,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Know Alignment','D',3,
        cast=tp(5,S),
        duration=tp(5,R),
        sourcebook=U,
    ),
    Spell('Neutralize Poison','D',3,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Plant Growth','D',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Protection From Fire','D',3,
        cast=tp(5,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Pyrotechnics','D',3,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Snare','D',3,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Spike Growth','D',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U,
    ),
    Spell('Starshine','D',3,
        cast=tp(5,S),
        duration_lvl=tp(1,T),
        sourcebook=U,
    ),
    Spell('Stone Shape','D',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Summon Insects','D',3,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Tree','D',3,
        cast=tp(5,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Water Breathing','D',3,
        cast=tp(5,S),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Animal Summoning I','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Call Woodland Beings','D',4,
        cast=tp(2,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Control Temperature','D',4,
        cast=tp(6,S),
        duration=tp(4,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Cure Serious Wounds','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Dispel Magic','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Hallucinatory Forest','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Hold Plant','D',4,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Plant Door','D',4,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Produce Fire','D',4,
        cast=tp(6,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Protection From Lightning','D',4,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Repel Insects','D',4,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Speak With Plants','D',4,
        cast=tp(1,T),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Animal Growth','D',5,
        cast=tp(7,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Animal Summoning II','D',5,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Anti-Plant Shell','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Commune With Nature','D',5,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Control Winds','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Insect Plague','D',5,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Moonbeam','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
    ),
    Spell('Pass Plant','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Spike Stones','D',5,
        cast=tp(6,S),
        duration=(1,VA),
        duration_lvl=tp(1,R),
        sourcebook=U,
    ),
    Spell('Sticks To Snakes','D',5,
        cast=tp(7,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Transmute Rock To Mud','D',5,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Wall of Fire','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Animal Summoning III','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Anti-Animal Shell','D',6,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Conjure Fire Elemental','D',6,
        cast=tp(6,R),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Cure Critical Wounds','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Feeblemind','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Fire Seeds','D',6,
        cast=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Liveoak','D',6,
        cast=tp(1,T),
        duration_lvl=tp(1,D),
        sourcebook=U,
    ),
    Spell('Transmute Water To Dust','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=U,
    ),
    Spell('Transport Via Plants','D',6,
        cast=tp(3,S),
        duration=tp(1,D),
        sourcebook=V
    ),
    Spell('Turn Wood','D',6,
        cast=tp(8,S),
        duration_lvl=tp(4,R),
        sourcebook=V
    ),
    Spell('Wall of Thorns','D',6,
        cast=tp(8,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Weather Summoning','D',6,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Animate Rock','D',7,
        cast=tp(9,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Changestaff','D',7,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=U,
    ),
    Spell('Chariot of Sustarre','D',7,
        cast=tp(1,T),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Confusion','D',7,
        cast=tp(9,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Conjure Earth Elemental','D',7,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Control Weather','D',7,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Creeping Doom','D',7,
        cast=tp(9,S),
        duration_lvl=tp(4,R),
        sourcebook=V
    ),
    Spell('Finger of Death','D',7,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Fire Storm','D',7,
        cast=tp(9,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Reincarnate','D',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Sunray','D',7,
        cast=tp(3,S),
        duration=tp(1,R),
        sourcebook=U,
    ),
    Spell('Transmute Metal To Wood','D',7,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=V
    ),
]

mu_spells = [
    Spell('Affect Normal Fires','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Alarm','M',1,
        cast=tp(1,R),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U,
    ),
    Spell('Armor','M',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U,
    ),
    Spell('Burning Hands','M',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Charm Person','M',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Comprehend Languages','M',1,
        cast=tp(1,R),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Dancing Lights','M',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Detect Magic','M',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Enlarge','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Erase','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Feather Fall','M',1,
        cast=tp(0.1,S),
        duration_lvl=tp(1,S),
        sourcebook=V
    ),
    Spell('Find Familiar','M',1,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Firewater','M',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=U,
    ),
    Spell('Friends','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Grease','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=U,
    ),
    Spell('Hold Portal','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Identify','M',1,
        cast=tp(1,T),
        duration_lvl=tp(1,S),
        sourcebook=V
    ),
    Spell('Jump','M',1,
        cast=tp(1,S),
        duration=tp(1,T),
        sourcebook=V
    ),
    Spell('Light','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Magic Missile','M',1,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Melt','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
    ),
    Spell('Mending','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Message','M',1,
        cast=tp(1,S),
        duration=tp(5,S),
        duration_lvl=tp(1,S),
        sourcebook=V
    ),
    Spell('Mount','M',1,
        cast=tp(1,R),
        duration=tp(12,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
    ),
    Spell('Nystul\'s Magic Aura','M',1,
        cast=tp(1,R),
        duration_lvl=tp(1,D),
        sourcebook=V
    ),
    Spell('Precipitation','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,S),
        sourcebook=U,
    ),
    Spell('Protection From Evil','M',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Push','M',1,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Read Magic','M',1,
        cast=tp(1,R),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Run','M',1,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U,
    ),
    Spell('Shield','M',1,
        cast=tp(1,S),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Shocking Grasp','M',1,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Sleep','M',1,
        cast=tp(1,S),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Spider Climb','M',1,
        cast=tp(1,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Taunt','M',1,
        cast=tp(1,R),
        duration=tp(0),
        sourcebook=U,
    ),
    Spell('Tenser\'s Floating Disc','M',1,
        cast=tp(1,S),
        duration=tp(3,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Unseen Servant','M',1,
        cast=tp(1,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Ventriloquism','M',1,
        cast=tp(1,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Wizard Mark','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=U,
    ),
    Spell('Write','M',1,
        cast=tp(1,R),
        duration_lvl=tp(1,H),
        sourcebook=V
    ),
    Spell('Audible Glamer','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Bind','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
    ),
    Spell('Continual Light','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Darkness 15\' Radius','M',2,
        cast=tp(2,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Deeppockets','M',2,
        cast=tp(1,T),
        duration=tp(24,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
    ),
    Spell('Detect Evil','M',2,
        cast=tp(2,S),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Detect Invisibility','M',2,
        cast=tp(2,S),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('ESP','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Flaming Sphere','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
    ),
    Spell('Fools Gold','M',2,
        cast=tp(1,R),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Forget','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Invisibility','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Irritation','M',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=U,
    ),
    Spell('Knock','M',2,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Know Alignment','M',2,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=U,
    ),
    Spell('Leomund\'s Trap','M',2,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Levitate','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Locate Object','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Magic Mouth','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Melf\'s Acid Arrow','M',2,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=U,
    ),
    Spell('Mirror Image','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Preserve','M',2,
        cast=tp(2,R),
        duration=tp(1,P),
        sourcebook=U,
    ),
    Spell('Protection From Cantrips','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,D),
        sourcebook=U
    ),
    Spell('Pyrotechnics','M',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Ray of Enfeeblement','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Rope Trick','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,T),
        sourcebook=V
    ),
    Spell('Scare','M',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Shatter','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Stinking Cloud','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Strength','M',2,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Tasha\'s Uncontrollable Hideous Laughter','M',2,
        cast=tp(2,S),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Vocalize','M',2,
        cast=tp(1,R),
        duration=tp(5,R),
        sourcebook=U
    ),
    Spell('Web','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,T),
        sourcebook=V
    ),
    Spell('Whip','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Wizard Lock','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Zephyr','M',2,
        cast=tp(2,S),
        duration=tp(1,S),
        sourcebook=U
    ),
    Spell('Blink','M',3,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Clairaudience','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Clairvoyance','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Cloudburst','M',3,
        cast=tp(3,S),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Detect Illusion','M',3,
        cast=tp(3,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R)
        sourcebook=U
    ),
    Spell('Dispel Magic','M',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Explosive Runes','M',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Feign Death','M',3,
        cast=tp(1,S),
        duration=tp(6,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Fireball','M',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Flame Arrow','M',3,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(1,S),
        sourcebook=V
    ),
    Spell('Fly','M',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Gust of Wind','M',3,
        cast=tp(3,S),
        duration=tp(1,S),
        sourcebook=V
    ),
    Spell('Haste','M',3,
        cast=tp(3,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Hold Person','M',3,
        cast=tp(3,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Infravision','M',3,
        cast=tp(1,R),
        duration=tp(12,R),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Invisibility 10\' Radius','M',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Item','M',3,
        cast=tp(3,S),
        duration_lvl=tp(6,T),
        sourcebook=U
    ),
    Spell('Leomund\'s Tiny Hut','M',3,
        cast=tp(3,S),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Lightning Bolt','M',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Material','M',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Melf\'s Minute Meteors','M',3,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Monster Summoning I','M',3,
        cast=tp(3,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Phantasmal Force','M',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Protection From Evil 10\' Radius','M',3,
        cast=tp(3,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Protection From Normal Missiles','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Secret Page','M',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Sepia Snake Sigil','M',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Slow','M',3,
        cast=tp(3,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Suggestion','M',3,
        cast=tp(3,S),
        duration=tp(6,T),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Tongues','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Water Breathing','M',3,
        cast=tp(3,S),
        duration_lvl=tp(3,T),
        sourcebook=V
    ),
    Spell('Wind Wall','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Charm Monster','M',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Confusion','M',4,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Dig','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Dimension Door','M',4,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Dispel Illusion','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Enchanted Weapon','M',4,
        cast=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Evard\'s Black Tentacles','M',4,
        cast=tp(8,S),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Extension I','M',4,
        cast=tp(2,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Fear','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Fire Charm','M',4,
        cast=tp(4,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Fire Shield','M',4,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Fire Trap','M',4,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Fumble','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Hallucinatory Terrain','M',4,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Ice Storm','M',4,
        cast=tp(4,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Leomund\'s Secure Shelter','M',4,
        cast=tp(4,T),
        duration_lvl=tp(6,T),
        sourcebook=U
    ),
    Spell('Magic Mirror','M',4,
        cast=tp(1,H),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Massmorph','M',4,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Minor Globe of Invulnerability','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Monster Summoning II','M',4,
        cast=tp(4,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Otiluke\'s Resilient Sphere','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Plant Growth','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Polymorph Other','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Polymorph Self','M',4,
        cast=tp(3,S),
        duration_lvl=tp(2,T),
        sourcebook=V
    ),
    Spell('Rary\'s Mnemonic Enhancer','M',4,
        cast=tp(1,T),
        duration=tp(1,D),
        sourcebook=V
    ),
    Spell('Remove Curse','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Shout','M',4,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Stoneskin','M',4,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Ultravision','M',4,
        cast=tp(4,S),
        duration=tp(6,T),
        duration_lvl=tp(6,T),
        sourcebook=U
    ),
    Spell('Wall of Fire','M',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Wall of Ice','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Wizard Eye','M',4,
        cast=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Airy Water','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Animal Growth','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Animate Dead','M',5,
        cast=tp(5,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Avoidance','M',5,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Bigby\'s Interposing Hand','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Cloudkill','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Conjure Elemental','M',5,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Cone of Cold','M',5,
        cast=tp(5,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Contact Other Plane','M',5,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Dismissal','M',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Distance Distortion','M',5,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Dolor','M',5,
        cast=tp(5,S),
        duration=tp(2,R),
        sourcebook=U
    ),
    Spell('Extension II','M',5,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Fabricate','M',5,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Feeblemind','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Hold Monster','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Leomund\'s Lamentable Belabourment','M',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Leomund\'s Secret Chest','M',5,
        cast=tp(1,T),
        duration=tp(60,D),
        sourcebook=V
    ),
    Spell('Magic Jar','M',5,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Monster Summoning III','M',5,
        cast=tp(5,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Mordenkainen\'s Faithful Hound','M',5,
        cast=tp(5,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Passwall','M',5,
        cast=tp(5,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Sending','M',5,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Stone Shape','M',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Telekinesis','M',5,
        cast=tp(5,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Teleport','M',5,
        cast=tp(2,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Transmute Rock To Mud','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Wall of Force','M',5,
        cast=tp(5,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Wall of Iron','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Wall of Stone','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Anti-Magic Shell','M',6,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Bigby\'s Forceful Hand','M',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Chain Lightning','M',6,
        cast=tp(6,S),
        duration=tp(0),
        sourcebook=U
    ),
    Spell('Contingency','M',6,
        cast=tp(1,T),
        duration_lvl=tp(1,D),
        sourcebook=U
    ),
    Spell('Control Weather','M',6,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Death Spell','M',6,
        cast=tp(6,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Disintegrate','M',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Enchant An Item','M',6,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Ensnarement','M',6,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Extension III','M',6,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Eyebite','M',6,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Geas','M',6,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Glassee','M',6,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Globe of Invulnerability','M',6,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Guards and Wards','M',6,
        cast=tp(3,T),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Invisible Stalker','M',6,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Legend Lore','M',6,
        cast=tp(1,VA),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Lower Water','M',6,
        cast=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Monster Summoning IV','M',6,
        cast=tp(6,S),
        duration=tp(5,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Mordenkainen\'s Lucubration','M',6,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=U
    ),
    Spell('Move Earth','M',6,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Otiluke\'s Freezing Sphere','M',6,
        cast=tp(6,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Part Water','M',6,
        cast=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Project Image','M',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Reincarnation','M',6,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Repulsion','M',6,
        cast=tp(6,S),
        duration_lvl=tp(5,S),
        sourcebook=V
    ),
    Spell('Spiritwrack','M',6,
        cast=tp(3,R),
        duration_lvl=tp(1,Y),
        sourcebook=V
    ),
    Spell('Stone To Flesh','M',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Tenser\'s Transformation','M',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Transmute Water To Dust','M',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Banishment','M',7,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Bigby\'s Grasping Hand','M',7,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Cacodemon','M',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Charm Plants','M',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Delayed Blast Fireball','M',7,
        cast=tp(7,S),
        duration=tp(5,R),
        sourcebook=V
    ),
    Spell('Drawmij\'s Instant Summons','M',7,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Duo-Dimension','M',7,
        cast=tp(7,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Forcecage','M',7,
        cast=tp(1,VA),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Limited Wish','M',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Mass Invisibility','M',7,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Monster Summoning V','M',7,
        cast=tp(6,S),
        duration=tp(6,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Mordenkainen\'s Magnificent Mansion','M',7,
        cast=tp(7,R),
        duration_lvl=tp(1,H),
        sourcebook=U
    ),
    Spell('Mordenkainen\'s Sword','M',7,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Phase Door','M',7,
        cast=tp(7,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Power Word, Stun','M',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Reverse Gravity','M',7,
        cast=tp(7,S),
        duration=tp(1,S),
        sourcebook=V
    ),
    Spell('Sequester','M',7,
        cast=tp(1,R),
        duration=tp(7,D),
        duration_lvl=tp(1,D),
        sourcebook=U
    ),
    Spell('Simulacrum','M',7,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Statue','M',7,
        cast=tp(7,S),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Teleport Without Error','M',7,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=U
    ),
    Spell('Torment','M',7,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Truename','M',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Vanish','M',7,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Volley','M',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Antipathy/Sympathy','M',8,
        cast=tp(6,T),
        duration_lvl=tp(12,T),
        sourcebook=V
    ),
    Spell('Bigby\'s Clenched Fist','M',8,
        cast=tp(8,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Binding','M',8,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Clone','M',8,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Demand','M',8,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Glassteel','M',8,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Incendiary Cloud','M',8,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Mass Charm','M',8,
        cast=tp(8,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Maze','M',8,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Mind Blank','M',8,
        cast=tp(1,S),
        duration=tp(1,D),
        sourcebook=V
    ),
    Spell('Monster Summoning VI','M',8,
        cast=tp(8,S),
        duration=tp(7,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Otiluke\'s Telekinetc Sphere','M',8,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Otto\'s Irresistible Dance','M',8,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Permanency','M',8,
        cast=tp(2,R),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Polymorph Any Object','M',8,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Power Word, Blind','M',8,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Serten\'s Spell Immunity','M',8,
        cast=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Sink','M',8,
        cast=tp(8,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Symbol','M',8,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Trap The Soul','M',8,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Astral Spell','M',9,
        cast=tp(9,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Bigby\'s Crushing Hand','M',9,
        cast=tp(9,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Crystalbrittle','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Energy Drain','M',9,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Gate','M',9,
        cast=tp(9,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Imprisonment','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Meteor Swarm','M',9,
        cast=tp(9,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Monster Summoning VII','M',9,
        cast=tp(9,S),
        duration=tp(8,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Mordenkainen\'s Disjunction','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Power Word, Kill','M',9,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Prismatic Sphere','M',9,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Shape Change','M',9,
        cast=tp(9,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Succor','M',9,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Temporal Stasis','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Time Stop','M',9,
        cast=tp(9,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Wish','M',9,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V
    )
]

illusionist_spells = [
    Spell('Audible Glamer','I',1,
        cast=tp(5,S),
        duration_lvl=tp(3,R),
        sourcebook=V
    ),
    Spell('Change Self','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Chromatic Orb','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Color Spray','I',1,
        cast=tp(1,S),
        duration=tp(1,S),
        sourcebook=V
    ),
    Spell('Dancing Lights','I',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Darkness','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Detect Illusion','I',1,
        cast=tp(1,S),
        duration=tp(3,R),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Detect Invisibility','I',1,
        cast=tp(1,S),
        duration_lvl=tp(5,R),
        sourcebook=V
    ),
    Spell('Gaze Reflection','I',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=V
    ),
    Spell('Hypnotism','I',1,
        cast=tp(1,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Light','I',1,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Phantasmal Force','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Phantom Armor','I',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Read Illusionist Magic','I',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=U
    ),
    Spell('Spook','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Wall of Fog','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Alter Self','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        duration_lvl=(2,R),
        sourcebook=U
    ),
    Spell('Blindness','I',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Blur','I',2,
        cast=tp(2,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Deafness','I',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Detect Magic','I',2,
        cast=tp(2,S),
        duration_lvl=tp(2,R),
        sourcebook=V
    ),
    Spell('Fascinate','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Fog Cloud','I',2,
        cast=tp(2,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Hypnotic Pattern','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Improved Phantasmal Force','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Invisibility','I',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Magic Mouth','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Mirror Image','I',2,
        cast=tp(2,S),
        duration_lvl=tp(3,R),
        sourcebook=V
    ),
    Spell('Misdirection','I',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Ultravision','I',2,
        cast=tp(2,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Ventriloquism','I',2,
        cast=tp(2,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Whispering Wind','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Continual Darkness','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Continual Light','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Delude','I',3,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Dispel Illusion','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Fear','I',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Hallucinatory Terrain','I',3,
        cast=tp(5,R),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Illusionary Script','I',3,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Invisibility 10\' Radius','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Non-detection','I',3,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Paralyzation','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Phantom Steed','I',3,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=U
    ),
    Spell('Phantom Wind','I',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Rope Trick','I',3,
        cast=tp(3,S),
        duration_lvl=tp(2,T),
        sourcebook=V
    ),
    Spell('Spectral Force','I',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Suggestion','I',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Wraithform','I',3,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=U
    ),
    Spell('Confusion','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Dispel Exhaustion','I',4,
        cast=tp(4,S),
        duration_lvl=tp(3,T),
        sourcebook=V
    ),
    Spell('Dispel Magic','I',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Emotion','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Improved Invisibility','I',4,
        cast=tp(4,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Massmorph','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Minor Creation','I',4,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Phantasmal Killer','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Rainbow Pattern','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Shadow Monsters','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Solid Fog','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Vacancy','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,T),
        sourcebook=U
    ),
    Spell('Advanced Illusion','I',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Chaos','I',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Demi-Shadow Monsters','I',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Dream','I',5,
        cast=tp(1,D),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Magic Mirror','I',5,
        cast=tp(1,H),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Major Creation','I',5,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=V
    ),
    Spell('Maze','I',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Projected Image','I',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Shadow Door','I',5,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Shadow Magic','I',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Summon Shadow','I',5,
        cast=tp(5,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Tempus Fugit','I',5,
        cast=tp(5,S),
        duration_lvl=tp(5,T),
        sourcebook=U
    ),
    Spell('Conjure Animals','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Death Fog','I',6,
        cast=tp(6,S),
        duration=tp(1,VA),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Demi-Shadow Magic','I',6,
        cast=tp(6,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Mass Suggestion','I',6,
        cast=tp(6,S),
        duration=tp(4,T),
        duration_lvl=tp(4,T),
        sourcebook=V
    ),
    Spell('Mirage Arcane','I',6,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Mislead','I',6,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Permanent Illusion','I',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V
    ),
    Spell('Phantasmagoria','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Programmed Illusion','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Shades','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('True Sight','I',6,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V
    ),
    Spell('Veil','I',6,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Alter Reality','I',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Astral Spell','I',7,
        cast=tp(3,T),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Prismatic Spray','I',7,
        cast=tp(7,S),
        duration=tp(0),
        sourcebook=V
    ),
    Spell('Prismatic Wall','I',7,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V
    ),
    Spell('Shadow Walk','I',7,
        cast=tp(1,S),
        duration_lvl=tp(6,T),
        sourcebook=U
    ),
    Spell('Vision','I',7,
        cast=tp(7,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Weird','I',7,
        cast=tp(7,S),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('First Level Magic-User Spells','I',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V
    )
]

all_spells = (cleric_spells + druid_spells
            + mu_spells + illusionist_spells)

def randomSpell():
    return choice(all_spells)

def randomIllusionistSpells(num=1,level=None):
    if not level:
        return sample(illusionist_spells, num)
    else:
        spells = [s for s in illusionist_spells if s.level == level]
        return sample(spells, num)


def test_module():
    print(cleric_spells[0].cast_time)
    print(cleric_spells[0].duration)
    print(cleric_spells[0].sourcebook)


if __name__ == '__main__':
    test_module()


