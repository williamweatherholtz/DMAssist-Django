from .sourcebook import SourceBook
from .time import TimePeriod, TimeUnit

from enum import Enum

class MagicItemCategory(Enum):
    POTION = 0
    SCROLL = 1
    RING = 2
    ROD = 3
    STAVE = 4
    WAND = 5
    MISC = 6


class MagicItem():
    def __init__(self, name, category, source, desc, activation_time=None):
        self.name = name
        self.category = category
        self.activation_time = activation_time
        self.source = source
        self.desc = desc

#merge these classes, changing read_time to activation_time and adding a category attribute (pot, ring, scroll, etc.)
class Potion():
    def __init__(self, name, desc, source):
        self.name = name
        self.description = desc
        self.source = source

class Scroll():
    def __init__(self, name, read_time, desc, source):
        self.name = name
        self.read_time = read_time
        self.description = desc
        self.source = source

class Ring():
    def __init__(self, name, desc):
        self.name = name,
        self.desc = desc
        self.source = source



potions = [
Potion(name = 'Potion of Animal Control',
    desc = ('This potion enables the imbiber to empathize with and control the emotions of animals of 1 type, i.e. cats, dogs, horses, etc. The number of animals so controlled depends upon size: 5-20 animals of the size of <a href="/creatures/giant-rat">giant rats</a>, 3-12 animals of about man-size, or 1-4 animals of about ½ ton or more in weight. The sort of animal which can be controlled depends upon the particular potion as indicated by die roll (d20):\n\n'
    '<table>'
    '<tr><th>Roll</th><th>Animal Type(s)</th></tr>'
    '<tr><td>1-4</td><td>mammal/marsupial</td></tr>'
    '<tr><td>5-8</td><td>avian</td></tr>'
    '<tr><td>9-12</td><td>reptile/amphibian</td></tr>'
    '<tr><td>13-15</td><td>fish</td></tr>'
    '<tr><td>16-17</td><td>mammal/marsupial/avian</td></tr>'
    '<tr><td>18-19</td><td>reptile/amphibian/fish</td></tr>'
    '<tr><td>20</td><td>all of the above</td></tr>'
    '</table>/n/n'
    'Animals with intelligence of 5 (low intelligence) or better are entitled to a saving throw versus magic. Control is limited to emotions or drives unless some form of communication is possible. Note that many monsters cannot be controlled by the use of this potion, nor can humans, demi-humans, or humanoids. (Cf. <i>Ring of Mammal Control</i>.)'
   ),
   source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Clairaudience',
    desc = 'This potion empowers the creature drinking it to hear as the third level magic-user <a href="/spells/clairaudience-magic-user-lvl-3">spell</a> of the same name. It can be used, however, to <i>clairaudit</i> unknown areas within 3". Its effects last for 2 turns only.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Clairvoyance',
    desc = 'This potion empowers the individual to see as the third level magic-user spell, <a href="/spells/clairvoyance-magic-user-lvl-3"><i>clairvoyance</i></a>. It differs from the spell in that unknown areas up to 3" distant can be seen. Its effects last for 1 turn only.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Climbing',
    desc = ('Imbibing this potion enables the individual to climb as a thief, up or down vertical surfaces, with only a base 1% chance of slipping and falling. (Check at the halfway point, d%, 01 equals a fall.) A climbing potion is effective for 1 turn plus 5 to 20 rounds. For every 1,000 g.p. weight equivalent carried by the character, there is an additional 1% added to chance of slipping. If the climber wears armor, there are the following additions to the slipping/falling chance:\n\n'
        '<table>'
        '<tr><th>Armor</th><th>Extra Fall Chance</th></tr>'
        '<tr><td>studded leather</td><td>1%</td></tr>'
        '<tr><td>ring mail</td><td>2%</td></tr>'
        '<tr><td>scale mail</td><td>4%</td></tr>'
        '<tr><td>chainmail</td><td>7%</td></tr>'
        '<tr><td>banded or splinted armor</td><td>8%</td></tr>'
        '<tr><td>plate mail</td><td>10%</td></tr>'
        '<tr><td>magic armor, any type</td><td>1%</td></tr>'
        '</table>'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Delusion',
    desc = 'This potion affects the mind of the character so that he or she believes the liquid is some other potion (<i>healing</i>, for example, is a good choice - damage is "restored" by drinking it, and only death or rest after an adventure will reveal that the potion only caused the imbiber to believe that he or she was aided). If several individuals taste this potion, it is still 90% probable that they will all agree it is the same potion (or whatever type the DM announces or hints at).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Diminution',
    desc = 'When this potion is quaffed, the individual, and all he or she carries and wears, will diminish in size to as small as 5% of normal size. If half of the contents are swallowed, the person shrinks to 50% of normal size. The effects of this potion last for 6 turns plus 2-5 turns (d4 + 1).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Dragon Control',
    desc = ('This potion enables the individual drinking it to cast what is in effect a <a href="/spells/charm-monster-magic-user-lvl-4"><i>charm monster</i></a> spell upon any dragon within 6". The dragon is entitled to a saving throw versus magic, but it is made at -2 on the die. There are various sorts of <i>dragon control</i> potions, as shown below (d20):\n\n'
        '<table><tr><th>Roll</th><th><Dragon Type</th></tr>'
        '<tr><td>1-2</td><td>white dragon</td></tr>'
        '<tr><td>3-4</td><td>black dragon</td></tr>'
        '<tr><td>5-7</td><td>green dragon</td></tr>'
        '<tr><td>8-9</td><td>blue dragon</td></tr>'
        '<tr><td>10</td><td>red dragon</td></tr>'
        '<tr><td>11-12</td><td>brass dragon</td></tr>'
        '<tr><td>13-14</td><td>copper dragon</td></tr>'
        '<tr><td>15</td><td>bronze dragon</td></tr>'
        '<tr><td>17</td><td>silver dragon</td></tr>'
        '<tr><td>17</td><td>gold dragon</td></tr>'
        '<tr><td>18-19</td>evil dragon*<td></td></tr>'
        '<tr><td>20</td><td>good dragon**</td></tr>'
        '</table>\n\n'
        '* Black, blue, green, red, white.\n'
        '** Brass, bronze, copper, gold, silver\n\n'
        'Control lasts for from 5-20 (5d4) rounds.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of ESP',
    desc = 'The <i>ESP</i> potion bestows an ability which is the same as the second level <a href="/spells/esp-magic-user-lvl-2">magic-user spell</a> of the same name, except that its effects last for 5-40 (5d8) rounds, i.e. 5 to 40 minutes.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Extra-Healing',
    desc = 'This potion restores 6-27 (3d8 + 3) hit points of damage when wholly consumed, or 1-8 hit points of damage for each one-third potion.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Fire Resistance',
    desc = 'This potion bestows magical invulnerability to all forms of normal fire (such as bonfires, burning oil, or even huge pyres of flaming wood) upon the person drinking it. It furthermore gives resistance to such fires as generated by molten lava, a <a href="/spells/wall-of-fire-druid-lvl-5/"><i>wall of fire</i></a>, a <a href="/spells/fireball-magic-user-lvl-3/"><i>fireball</i></a>, fiery dragon breath and similar intense flame/heat. All damage from such fires is reduced by -2 from each die of damage, and if a saving throw is applicable, it is made at +4. Note: If but one-half of the potion is consumed it confers invulnerability to normal fires and half the benefits noted above (-1, +2). The potion lasts 1 turn, or 5 rounds for half doses.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Flying',
    desc = 'A flying potion enables the individual drinking it to fly in the same manner as the third level magic-user spell, <a href="/spells/fly-magic-user-lvl-3"><i>fly</i></a>.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Gaseous Form',
    desc = 'By imbibing this magical liquid, the individual causes his or her body, as well as what it carries and wears, to become gaseous in form and able to flow accordingly at a base speed of 3"/round. (A <a href="/spells/gust-of-wind-magic-user-lvl-3/"><i>gust of wind</i></a> spell, or even normal strong air currents, will blow the gaseous form backwards at air speed.) The gaseous form is transparent and insubstantial. It wavers and shifts. It cannot be harmed except by magical fires or lightnings, in which case damage is normal. A whirlwind will inflict double damage upon any creature in <i>gaseous form</i>. When in such condition the individual is able to enter any space which is not airtight, i.e., a small crack or hole which allows air to penetrate also allows entry by a creature in gaseous form. The entire potion must be consumed to achieve this result, and the effects last the entire duration.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Giant Control',
    desc = ('A full potion of this draught must be drunk in order to make its effects be felt. It will influence 1 or 2 giants as if a <a href="/spells/charm-monster-magic-user-lvl-4"><i>charm monster</i></a> spell were affecting them. If only 1 giant is so influenced, it is entitled to a saving throw versus magic at -4 on the die roll; if 2 are influenced the die rolls are at +2. The type of giant subject to a particular potion is randomly determined as follows:\n\n'
        '<table><tr><th>Roll</th><th>Giant Type</th></tr>'
        '<tr><td>1-5</td><td><a href="/creautres/hill-giant">hill giant</a></td></tr>'
        '<tr><td>6-9</td><td><a href="/creatures/stone-giant">stone giant</a></td></tr>'
        '<tr><td>10-13</td><td><a href="/creatures/frost-giant">frost giant</a></td></tr>'
        '<tr><td>14-17</td><td><a href="/creatures/fire-giant">fire giant</a></td></tr>'
        '<tr><td>18-19</td><td><a href="/creatures/cloud-giant">cloud giant</a></td></tr>'
        '<tr><td>20</td><td><a href="/creatures/storm-giant">storm giant</a></td></tr>'
        '</table>\n\n'
        'Control lasts for only 5-30 (5d6) rounds.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Giant Strength',
    desc = ('When a <i>giant strength</i> potion is consumed the individual gains great strength and bonuses to damage when he or she scores a hit with any hand-held or thrown weapon. It is also possible for the person to hurl rocks as shown on the table below. Note that the type of <i>giant strength</i> gained by drinking the potion is randomly determined on the same table:\n\n'
        '<table>'
        '<tr><th rowspan="2">Die Score</th><th rowspan="2">Strength Equivalent</th><th rowspan="2">Weight Allowance</th><th rowspan="2">Damage Bonus</th><th colspan="2">Rock Hurling</th><th rowspan="2">Bend Bars/Lift Gates</th></tr>'
        '<tr><th>Range</th><th>Base Damage</th></tr>'
        '<tr><td>1-6</td><td><a href="/creatures/hill-giant">Hill Giant</a></td><td>+4,500</td><td>+7</td><td>8"</td><td>1-6</td><td>50%</td></tr>'
        '<tr><td>7-10</td><td><a href="/creatures/stone-giant">Stone Giant</a></td><td>+5,000</td><td>+8</td><td>16"</td><td>1-12</td><td>60%</td></tr>'
        '<tr><td>11-14</td><td><a href="/creatures/frost-giant">Frost Giant</a></td><td>+6,000</td><td>+9</td><td>10"</td><td>1-8</td><td>70%</td></tr>'
        '<tr><td>15-17</td><td><a href="/creatures/fire-giant">Fire Giant</a></td><td>+7,500</td><td>+10</td><td>12"</td><td>1-8</td><td>80%</td></tr>'
        '<tr><td>18-19</td><td><a href="/creatures/cloud-giant">Cloud Giant</a></td><td>+9,000</td><td>+11</td><td>14"</td><td>1-10</td><td>90%</td></tr>'
        '<tr><td>20</td><td><a href="/creatures/storm-giant">Storm Giant</a></td><td>+12,0000</td><td>+12</td><td>16"</td><td>1-12</td><td>100%</td></tr>'
        '</table>\n\n'
        'Compare these abilities to the character <i>strength<i> ability and to the <i>girdle of giant strength</i>. The potion can be used only by fighters. Note this does not give the same powers as a <i>girdle</i>.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Growth',
    desc = 'This potion causes the person consuming it to enlarge in both height and weight, his or her garments and other worn and carried gear likewise growing in size. Strength is increased sufficiently to allow bearing normal armor and weapons, but does not add to combat. Movement increases to that of a giant of approximately equal size. Each quarter of the potion consumed causes 6\' height growth, i.e. a full potion increases height by 24\'.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Healing',
    desc = 'An entire potion must be consumed in a single drinking (round) in order for this liquor to restore 4-10 (2d4 + 2) hit points of damage. (Cf. <i>extra-healing</i>.)',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Heroism',
    desc = ('This potion gives the imbiber a temporary increase in life energy levels if he or she has fewer than 10 levels of experience. This is shown below:\n\n'
        '<table><tr><th>Level of Consumer</th><th>Number of Energy Levels Bestowed</th><th>10-sided Dice for Accumulated Damage Bestowed</th></tr>'
        '<tr><td>0</td><td>4</td><td>4</td></tr>'
        '<tr><td>1st-3rd</td><td>3</td><td>3+1</td></tr>'
        '<tr><td>4th-6th</td><td>2</td><td>2+2</td></tr>'
        '<tr><td>7th-9th</td><td>1</td><td>1+3</td></tr>'
        '</table>\n\n'
        'When the potion is quaffed, the individual fights as if he or she were at the experience level bestowed by the magic of the elixir. Damage sustained is taken first from magically gained hit dice and bonus points. This potion is restricted to use by men-at-arms and fighters.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Human Control',
    desc = ('A potion of <i>human control</i> allows the imbiber to control up to 32 levels/hit dice of humans/humanoids/demi-humans as if a <a href="/spells/charm-person-magic-user-lvl-1"><i>charm person</i></a> spell had been cast, and the human types to be controlled are entitled to saving throws versus magic. Any pluses on hit dice are rounded <i>down</i> to the lowest whole die, i.e. 1+2 = 1, 2+6 = 2. The type of human(s) which can be controlled is randomly determined on the table below:\n\n'
        '<table><tr><th>Die Score</th><th>Type Controlled</th></tr>'
        '<tr><td>1-2</td><td>Dwarves</td></tr>'
        '<tr><td>3-4</td><td>Elves/Half-Elves</td></tr>'
        '<tr><td>5-6</td><td>Gnomes</td></tr>'
        '<tr><td>7-8</td><td>Halflings</td></tr>'
        '<tr><td>9-10</td><td>Half-Orcs</td></tr>'
        '<tr><td>11-16</td><td>Humans</td></tr>'
        '<tr><td>17-19</td><td>Humanoids (gnolls, orcs, goblins, etc.)</td></tr>'
        '<tr><td>20</td><td>Elves, Half-Elves, and Humans</td></tr>'
        '</table>\n\n'
        'This potion lasts for from 5-30 rounds.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Invisibility',
    desc = 'When this potion is consumed it confers <i>invisibility</i> similar to the <a href="/spells/invisibility-magic-user-lvl-2/">spell</a> of the same name. As actions involving combat cause termination of the non-visible state, the individual possessing the potion can quaff a single gulp - equal to 1/8 the contents of the container - to bestow <i>invisibility</i> for 3-6 turns.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Invulnerability',
    desc = 'This potion confers immunity to non-magical weapons and attacks from creatures with no magical properties (see <b>CREATURES STRUCK ONLY BY MAGICAL WEAPONS</b> in the Dungeon Master\'s Guide) or with fewer than 4 hit dice. Thus, an 8th level character without a magical weapon could not harm the imbiber of an <i>invulnerability</i> potion. It further improves armor class rating by 2 classes and gives a bonus of +2 to the individual on his or her saving throws versus all forms of attack. Its effects are realized only when the entire potion is consumed, and they last for 5-20 rounds. Only fighters can use this potion.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Levitation',
    desc = 'A <i>levitation</i> potion enables the consumer to <i>levitate</i> in much the same manner as the second level <a href="/spells/levitate-magic-user-lvl-2">magic-user spell</a> of the same name. The potion allows levitation of the individual only, subject to a maximum weight of 6,000 g.p. equivalent, so it is possible that the individual drinking the potion could carry another person.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Longevity',
    desc = 'The <i>longevity</i> potion reduces the character\'s game age by from 1-12 years when it is imbibed, but each time one is drunk there is a 1% cumulative chance that it will have the effect of reversing all age removal from previously consumed <i>longevity</i> potions. The potion otherwise restores youth and vigor. It is also useful to counter magical or monster-based aging attacks. The entire potion must be consumed to achieve the results.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Oil of Etherealness',
    desc = 'This potion is actually a light oil which is applied externally to the dress and exposed flesh. It then confers <i>etherealness</i>. In the ethereal state the individual can pass through solid objects - sideways, upwards, downwards - or to different <i>planes</i>. Naturally, the individual cannot touch non-ethereal objects. The oil takes effect 3 rounds after application and it lasts for 4 + 1-4 turns unless removed with a weak acidic solution prior to the expiration of its normal effective duration. It can be applied to objects as well as creatures; one potion is sufficient to anoint a normal human and such gear as he or she typically carries (2 or 3 weapons, garments, armor, shield, and the usual miscellaneous gear carried). Ethereal individuals are invisible. (Cf. <a href="/spells/phase-door-magic-user-lvl-7"><i>phase door</i></a> spell, and <b>TRAVEL IN THE KNOWN PLANES OF EXISTENCE</b> in the Dungeon Master\'s Guide.)',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Oil of Slipperiness',
    desc = 'Similar to the <i>oil of etherealness</i>, this liquid is to be applied externally. This application makes it impossible for the individual to be grabbed or grasped/hugged by any opponent or constricted by snakes or tentacles. (Note that a roper could still inflict weakness, but that the monster\'s tentacles could not entwine the opponent coated with <i>oil of slipperiness</i>.) In addition, such obstructions as webs, magical or otherwise, will not affect an anointed individual; and bonds such as ropes, manacles, and chains can be slipped free. Magical ropes and the like are not effective against this oil. If poured on a floor or on steps there is a 95% chance/round that creatures standing on the surface will slip and fall. The oil lasts 8 hours to wear off normally, or it can be wiped off with an alcohol solution (such as wine).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Philter of Love',
    desc = 'This potion is such as to cause the individual drinking it to become <i>charmed</i> (cf. <a href="/spells/charm-person-magic-user-lvl-1"><i>charm</i></a> spells) with the first creature seen after consuming the draught, or actually become enamored and <i>charmed</i> if the creature is of similar race and of the opposite sex. Charming effects wear off in 4 + 1-4 turns, but the enamoring effects last until a <a href="/spells/dispel-magic-cleric-lvl-3"><i>dispel magic</i></a> spell is cast upon the individual.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Philter of Persuasiveness',
    desc = 'When this potion is imbibed the individual becomes more charismatic. Thus, he or she gains a bonus of 25% on reaction dice rolls. The individual is also able to <i>suggest</i> (cf. the magic-user <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a> spell) once per turn to as many creatures as are within a range of 3" of him or her.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Plant Control',
    desc = 'A <i>plant control</i> potion enables the individual who consumed it to influence the behavior or vegetable life forms - including normal plants, fungi, and even molds and <a href="/creatures/shambling-mound">shambling mounds</a> - within the parameters of their normal abilities. The imbiber can cause the vegetable forms to remain still/silent, move, entwine, etc. according to their limits. Vegetable monsters with intelligence of 5 or higher are entitled to a saving throw versus magic. Plants within a 2" x 2" square can be controlled subject to the limitations set forth above, for from 5-20 rounds. Self-destructive control is not directly possible if the plants are intelligent. (Cf. <a href="/spells/charm-plants-magic-user-lvl-7"><i>charm plants</i></a> spell.) Control range is 9".',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Poison',
    desc = 'A <i>poison</i> potion is simply a highly toxic liquid in a potion flask. Typically, <i>poison</i> potions are odorless and of any color. Ingestion, introduction of the poison through a break in the skin, or possibly just skin contact, will cause death. Poison can be weak (+4 to +1 on saving throw), average, or deadly (-1 to -4 or more on saving throw). Some poison can be such that a <a href="/spells/neutralize-poison-cleric-lvl-4"><i>neutralize poison</i></a> spell will simply lower the toxicity level by 40% - say from a -4 to a +4 on saving throw potion. You might wish to allow characters to hurl poison flasks (see <b>COMBAT</b> in the Dungeon Master\'s Guide).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Polymorph Self',
    desc = 'This potion duplicates the effects of the fourth level <a href="/spells/polymorph-self-magic-user-lvl-4">magic-user spell</a> of the same name in most respects.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Speed',
    desc = 'A potion of <i>speed</i> increases movement and combat capabilities of the imbiber by 100%. Thus, a movement rate of 9" becomes 18", and a character normally able to attack but once per round would gain double attacks in a round. Note that this does not reduce spell casting time, however (cf. <a href="/spells/haste-magic-user-lvl-3"><i>haste</i></a> spell). Use of a <i>speed</i> potion ages the individual by 1 year. The other effects last from 5-20 rounds, the aging is permanent.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Super-Heroism',
    desc = ('This potion gives the individual a temporary increase in life energy levels (cf. <i>heroism</i> potion) if he or she has fewer than 13 levels of experience:\n\n'
        '<table><tr><th>Level of Consumer</th><th>Number of Energy Level Bestowed</th><th>10-sided Dice for Accumulated Damage Bestowed</th></tr>'
        '<tr><td>0</td><td>6</td><td>5</td></tr>'
        '<tr><td>1st-3rd</td><td>5</td><td>4 + 1</td></tr>'
        '<tr><td>4th-6th</td><td>4</td><td>3 + 2</td></tr>'
        '<tr><td>7th-9th</td><td>3</td><td>2 + 3</td></tr>'
        '<tr><td>10th-12th</td><td>2</td><td>1 + 4</td></tr>'
        '</table>\n\n'
        'It is otherwise the same as a <i>heroism</i> potion, but its effects last from but 5 to 30 melee rounds.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Sweet Water',
    desc = 'This liquid is not actually a potion to be drunk (though if it is drunk it will taste good), but it is to be added to other liquids in order to change them to pure, drinkable water. It will neutralize poison and ruin magic potions (no saving throw). The contents of the container will change up to 100,000 cubic feet of polluted or salt or alkaline water to fresh water. It will turn up to 1,000 cubic feet of acid into pure water. The effects of the potion are permanent, but subject to later contamination or infusion after an initial period of 5-20 rounds.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Treasure Finding',
    desc = 'A potion of <i>treasure finding</i> empowers the drinker with a location sense, so that he or she can point to the direction of the nearest mass of treasure. The treasure must be within 24" or less, and its mass must equal metal of at least 10,000 copper pieces or 100 gems or any combination thereof. Note that only valuable metals (copper, silver, electrum, gold, platinum, etc.) and gems (and jewelry, of course) are located; worthless metals or magic without precious metals/gems are not found. The consumer of the potion can "feel" the direction in which treasure lies, but not its distance. Intervening substances other than special magical words or lead-lined walls will not withstand the powers which the liquor bestows upon the individual. The effects of the potion last for from 5-20 rounds. (Clever players will attempt triangulation.)',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Undead Control',
    desc = ('This potion in effect gives the imbiber the ability to <i>charm</i> certain undead (ghasts, ghosts, ghouls, shadows, skeletons, spectres, wights, wraiths, vampires, and zombies). The <i>charming</i> ability is similar to the magic-user spell, <a href="/spells/charm-person-magic-user-lvl-1"><i>charm person</i></a>. It affects a maximum of 16 hit dice of undead, rounding down any hit point additions to hit dice to the lowest die, i.e. 4 + 1 equals 4 hit dice. The undead are entitled to saving throws versus magic only if they have intelligence. Saving throws are made at -2 due to the power of the potion, but the effect wears off in from 5-20 rounds. To determine type of undead affected by a particular potion, roll d10 and consult the following table:\n\n'
        '<table><tr><th>D10 Roll</th><th>Undead Type</th></tr>'
        '<tr><td>1</td><td><a href="/creatures/ghast">Ghasts</a></td></tr>'
        '<tr><td>2</td><td><a href="/creatures/ghost">Ghosts</a></td></tr>'
        '<tr><td>3</td><td><a href="/creatures/ghoul">Ghouls</a></td></tr>'
        '<tr><td>4</td><td><a href="/creatures/shadow">Shadows</a></td></tr>'
        '<tr><td>5</td><td><a href="/creatures/skeleton">Skeletons</a></td></tr>'
        '<tr><td>6</td><td><a href="/creatures/spectre">Spectres</a></td></tr>'
        '<tr><td>7</td><td><a href="/creatures/wight">Wights</a></td></tr>'
        '<tr><td>8</td><td><a href="/creatures/wraith">Wraiths</a></td></tr>'
        '<tr><td>9</td><td><a href="/creatures/vampire">Vampires</a></td></tr>'
        '<tr><td>0</td><td><a href="/creatures/zombie">Zombies</a></td></tr>'
        '</table>'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Potion(name = 'Potion of Water Breathing',
    desc = 'It is 75% likely that a <i>water breathing</i> potion will contain two doses, 25% probable that there will be four in the container. The elixir allows the character drinking it to breathe normally in liquids which contain oxygen suspended within them. This ability lasts for one full hour per dose of potion quaffed, with an additional 1-10 rounds (minutes) variable. Thus, a character who has consumed a <i>water breathing</i> potion could enter the depths of a river, lake, or even the ocean and not drown while the magical effects of the potion persisted.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),

#UNEARTHED POTIONS
Potion( name = 'Elixir of Health',
    desc = 'This special potion cures blindness, deafness, disease, feeblemindedness, insanity, infection, infestation, poisoning, and rot. It will not heal wounds or restore hit points lost through any of the above causes. Half a flask will cure any one or two of the listed problems. Imbibing the whole potion will cure any and all of the above afflictions that the drinker may be suffering.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Elixir of Life',
    desc = 'This potent draught will restore life to any creature, even if at a negative hit point level equal to up to 20% of total hit points. (Thus, it will benefit even a creature at -10 hit points, so long as that creature has a full-strength hit point total of 50 or more.) The power of the elixir will function only if administered internally within 5 rounds of the occurence of death. One turn later, the recipient will be unconscious but at 1 hit point strength. For each negative hit point neutralized in this fashion, the recipient must rest for one day or else receive a <a href="/spells/cure-light-wounds-cleric-lvl-1"><i>cure light wounds</i></a> spell to offset the need for that one day of rest. A <a href="/spells/cure-serious-wounds-cleric-lvl-4"><i>cure serious wounds</i></a> spell will count for two days of rest, a <a href="/spells/cure-critical-wounds-cleric-lvl-5"><i>cure critical wounds</i></a> spell for three, and a <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> spell for seven days. Demi-humans are affected by this elixir.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Elixir of Madness',
    desc = 'A single sip of this stuff will cause the imbiber to go mad, as if he or she were affected by a <a href="/spells/symbol-magic-user-lvl-8"><i>symbol</a> of insanity</i>. Once any creature is affected by the elixir, the dweomer from the entire flask instantly disappears, and the remaining draught is merely foul-tasting liquid.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Elixir of Youth',
    desc = 'Quaffing this rare and highly dweomered elixir will reverse aging. The entire contents of the flask must be consumed; sipping from it initially will reduce the potency of the liquid. Taking the full-potency dose reduces the imbiber\'s age by 2-5 years, and drinking the lower-potency liquid reduces age by only 1-3 years.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Potion of Fire Breath',
    desc = 'This magical draught allows the imbiber to retain the dweomer of the fluid for up to six turns before belching forth a tongue of flame. After the expiration of this time limit, however, the potion becomes impotent, and there is a 10% chance that the flames will erupt in the imbiber\'s own system, inflicting double damage upon him or her, with no saving throw allowed. Each potion container holds enough liquid for four small draughts. If a small draught only is quaffed, then the imbiber is able to breathe forth a 1" wide cone of fire up to 2" long which inflicts 3-12 points of damage. If a double draught is taken, range and damage are doubled; and if a triple draught is quaffed, then ranged and damage are tripled. If the entire contents are taken at once, then the width of the breath of flame is 2" and the length is 8", and damage inflicted is 5-50 points. Saving throws versus <i>breath weapon</i> apply, for half damage, in all cases.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Acid Resistance',
    desc = 'When this oil is applied to skin, cloth, or any other material, it confers virtual invulnerability to acid. The oil will not wear off quickly; an application lasts for one full day before becoming impotent. However, each time material or flesh is exposed to acid, the potency of the oil is diminished by as many minutes as the acid would have caused points of damage to exposed flesh. Thus, if a <a href="/creatures/black-dragon"><i>black dragon</i></a> of largest size and greatest age breathed upon a person protected by this oil, each breath would lower the oil\'s remaining protection time by 64 minutes, or 32 minutes if a successful saving throw versus <i>breath weapon</i> is made. Each flask contains sufficient oil for one man-sized creature (and accoutrements) for 24 hours. Or, 24 such man-sized creatures could each by coated for one hour\'s time; any combination of number of creatures and duration of potency between these extremes is also possible. (A horse is equivalent to eight man-sized creatures.)',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Disenchantment',
    desc = 'This special oil allows the removal of all <i>enchantment/charm</i> dweomers placed upon living things. If the contents of a flask of this substance are rubbed on a creature, all enchantments and charms placed upon it are removed. If the oil is rubbed onto objects which bear a dweomer of the <i>enchantment/charm</i> sort, this magic will be lost for 21 to 30 turns (d10 +20); after that time has elapsed, the oil will have lost its potency, and the item will regain its former dweomer. The oil does not radiate any magical qualities once it is applied, and masks the dweomer of whatever it coats, so that an item so coated will not show any dweomer if magic is detected for as long as the oil remains effective.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Elemental Invulnerability',
    desc = 'This precious substance has equal chances for being of any of the four basic sorts - air, earth, fire, or water. (Roll d4 to determine which sort is discovered.) This oil gives total invulnerability to normal elemental forces on the Prime Material Plane: normal wind storms, fire, earth slides, floods, and so forth. Additionally, there is a 10% chance that any container of this oil which is discovered will be usable on any of the Elemental or Paraelemental Planes. The oil allows the person(s) treated to operate freely and without danger of harm by elemental forces. Of course, monsters do other sorts of damage, and such attacks by elemental creatures will still be effective, but at -1 per die of damage. The oil comes in sufficient quantity to coat one individual for eight days duration, or eight individuals for one day.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Fiery Burning',
    desc = 'When this substance is subjected to air, it bursts into flame, the fire being so hot that it will inflict 5-30 points (5d6) of damage to any creature coated with the oil (saving throw vs. spell applicable for half damage). If hurled, a flask containing this oil will always break. Any creature within 1" of the place of impact of the oil flask is subject to the effects, but a maximum of six such creatures can be affected. (The oil can, for instance, be used to consume the bodies of as many as six regenerating creatures such as <a href="/creatures/troll">trolls</a>.) If the flask is opened, the creature holding it will immediately suffer 1-4 points of damage. Unless that creature then proceeds to roll equal to or less than its dexterity on 2d10, the flask will not be re-stoppered in time to prevent the oil from exploding, with effects as described above.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Fumbling',
    desc = 'This viscous substance will initially seem to be of a useful sort - <i>acid resistance</i>, <i>elemental invulnerability</i>, or <i>slipperiness</i>, for instance - until the wearer is under stress in a melee combat situation. At that point, he or she will have a 50% chance each round of fumbling and dropping whatever he or she holds - weapon, shield, spell components, and so forth. Only a thorough bath of solvent (alcohol, turpentine, etc.) will remove the substance before its potency wears off.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Impact',
    desc = 'This magical substance is charged with a powerful dweomer which has beneficial effects upon blunt weapons and missiles of all sorts, magical and non-magical. When applied to a blunt weapon such as a club, hammer, or mace, it causes the weapon to both be magical and deliver extra damage. When the oil is applied to a missile, its effect is to make it both magical and very deadly upon impact. Missiles upon which the <i>oil of impact</i> will properly function are hurled hammers, hurled clubs, sling stones, and sling bullets. A flask of this substance will contain from 3-5 applications. Each application will last for 9-12 rounds on a hand-held weapon, but when applied to a missile weapon the substance has but a single "charge." With respect to missiles, however, only a small amount need to be used, so that 4-5 sling missiles or 2 larger weapons can be treated with a single application. If the oil is used on a hand-held weapon, its dweomer will bestow +3 status to the weapon\'s hit probability and cause +6 damage on a successful hit. Missiles will be +3 both "to hit" and to damage.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Sharpness',
    desc = ('This magical substance resembles the fine oil used to clean and protect metal armor and weapons. If it is carefully rubbed on the blade of any edged or pointed weapon, the oil will have the effect of making it equivalent to a magic weapon. One such application will last for 9-12 rounds. A flask of the substance will contain from 3-5 applications. The dweomer of the <i>oil of sharpness</i> is determined by die roll:\n\n',
        '<table>'
        '<tr><th>d20 Result</th><th>+ To Hit and Damage</th></tr>'
        '<tr><td>1-2</td><td>1</td></tr>'
        '<tr><td>3-5</td><td>2</td></tr>'
        '<tr><td>6-11</td><td>3</td></tr>'
        '<tr><td>12-16</td><td>4</td></tr>'
        '<tr><td>17-19</td><td>5</td></tr>'
        '<tr><td>20</td><td>6</td></tr>'
        '</table>'
    ),
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Oil of Timelessness',
    desc = 'This smooth liquid appears to be an oil of any sort - even possibly of poisonous nature. When applied to any matter which was formerly alive (leather, leaves, paper, wood, dead flesh, etc.), it enables that substance to resist the passage of time, each year of actual time affecting the object as if only a day had passed. The substance never wears off, though it can be magically removed. The object coated with the oil also gains a +1 bonus on any saving throws which must be made for it. There is sufficient oil within one flask to coat one horse, eight humans, or an equivalent area/volume of some other eligible object or substance.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Philter of Beauty',
    desc = 'When this substance is consumed, the individual gains +1 on charisma (18 maximum) and +1 to +4 on his or her comeliness score for the duration of the liquid\'s effect. All reactions pertaining to charisma and comeliness apply, but if the effects wear off within sight of any creature that was influenced by the enhanced charisma and comeliness, then the creature(s) will certainly have a hostile reaction to this turn of events and attack the individual.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Philter of Glibness',
    desc = 'This magical draught allows the imbiber to fluently speak - even tell lies - smoothly, believably, and undetectably. Magical investigation (such as <a href="/spells/detect-lie-cleric-lvl-4"><i>detect lie</i></a>) will not give the usual results, but will reveal that some minor "stretching of the truth" might be occuring.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Philter of Stammering and Stuttering',
    desc = 'When this liquid is consumed, it will seem to be a beneficial draught - one of <i>glibness</i> or <i>persuasiveness</i>, for instance. But whenever something meaningful must be spoken (the verbal component of a spell, the text of a scroll, conversation with a monster, etc.), the beverage\'s true effect will be revealed - nothing can be said properly, and reactions of all creatures hearing such nonsense will be at -25% penalty.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Potion of Rainbow Hues',
    desc = 'This rather syrupy draught must be stored in a metallic container. A full flask holds sufficient liquid for seven hours\' effect. The imbiber only has to concentrate on some color or colors and he or she will turn that very hue in less than one segment. Any color or combination of colors is possible, if the user of the magical drink simply holds the thought in his mind for the space of time required for the hue(s) to be effected. If the potion is quaffed sparingly, it is possible to get seven draughts of one hour duration apiece.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Potion of Ventriloquism',
    desc = 'When it is imbibed, this potion enables the drinker to duplicate the effects of a <a href="/spells/ventriloquism-magic-user-lvl-1"><i>ventriloquism</i></a> spell as if he or she were a magic-user. The potion lasts for six such uses, or until its effects fade due to expiration of time.',
    source = SourceBook.UNEARTHED_ARCANA
),
Potion( name = 'Potion of Vitality',
    desc = 'This potion enables the consumer to be refreshed and full of vitality despite exertion, lack of sleep, and going without food and drink for as long as seven days. If the potion is consumed after one or more days of such exertion or deprivation, it will nullify the adverse effects and still bestow vitality for the remaining number of days up to seven. In addition, the potion is proof against poisons and diseases for the indicated period - and while the potion is in effect, the beneficiary will recover lost hit points at the rate of 1 every 4 hours.',
    source = SourceBook.UNEARTHED_ARCANA
)
]


scrolls = [
Scroll( name = 'Protection from Demons',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = ('This scroll requires 1 full round to read if it is to protect against all sorts of demons, including demon princes, 7 segments to protect against demons of <a href="/creatures/type-6-demon">type VI</a> or lower, and only 3 segments to protect against <a href="/creatures/type-3-demon">type III</a> or lower. The circle of protection generated springs outwards from the scroll reader in a 10\' radius. No demon protected against can penetrate the circle physically or magically or in any way, but the person(s) within can launch attacks, if otherwise possible, upon demons. The protection moves with the reader of the scroll. Its effect lasts for 5-20 (5d4) rounds.\n\n'
        'Note that the protection radius is not an actual physical globe, and if the user forces a demon into a place from which further retreat is impossible (e.g., a corner), and then continues forward until the demon would be within the radius of the circle, the demon is not harmed, and the protection is considered voluntarily broken and disappears. There is no way in which this can be used as an offensive weapon.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Devils',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'This scroll is nearly identical to the <i>protection from demons</i> scroll. It requires 1 round to read if it is to protect against all kinds of devils, including arch-devils, 7 segments to protect against greater devils or lower, and 3 segments to protect against lesser devils or lower.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Elementals',
    read_time = (6, TimeUnit.segment),
    desc = ('There are 5 varieties of this scroll:\n\n'
        '01-15: <i>Protection from Air Elementals</i> (including <a href="/creatures/aerial-servant">aerial servants</a>, <a href="/creatures/djinni">djinn</a>, <a href="creatures/invisible-stalker">invisible stalkers</a>, and <a href="/creatures/wind-walker">wind walkers</a>)\n'
        '16-30: <i>Protection from Earth Elementals</i> (including <a href="/creatures/xorn">xorn</a>)\n'
        '31-45: <i>Protection from Fire Elementals</i> (including <a href="/creatures/efreeti">efreet</a> and <a href="/creatures/salamander">salamanders</a>)\n'
        '46-60: <i>Protection from Water Elementals</i> (including <a href="/creatures/triton">tritons</a> and <a href="/creatures/water-weird">water weirds</a>)\n'
        '61-00: <i>Protection from All Elementals</i>\n\n'
        'The magic protects the reader and all within 10\' of him or her from the kind of elemental noted, as well as elemental creatures of the same, or all, planes. The circle of protection affects a maximum of 24 hit dice of elemental creatures if the scroll is of a <i>specific</i> elemental type, 16 hit dice if it is against <i>all</i> sorts of elementals. The spell lasts for 5-40 (5d8) rounds. Attack out of the circle is possible, as is attack into it by any elemental creature with more hit dice than are protected against or by several elemental creatures - those in excess of the protected number of hit dice being able to enter and attack.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Lycanthropes',
    read_time = TimePeriod(4, TimeUnit.segment),
    desc = ('There are 7 types of this scroll:\n\n'
        '01-05: <i>Protection from <a href="/creatures/werebear">Werebears</a></i>\n'
        '06-10: <i>Protection from <a href="/creatures/wereboar">Wereboars</a></i>\n'
        '11-20: <i>Protection from <a href="/creatures/wererat">Wererats</a></i>\n'
        '21-25: <i>Protection from <a href="/creatures/weretiger">Weretigers</a></i>\n'
        '25-40: <i>Protection from <a href="/creatures/werewolf">Werewolves</a></i>\n'
        '41-98: <i>Protection from all Lycanthropes</i>\n'
        '99-00: <i>Protection from Shape-Changers</i>\n\n'
        'The magic circle from the reading of the scroll extends in a 10\' radius. It moves with the person who read the scroll. Each scroll protects against 49 hit dice of lycanthrope(s), rounds all hit point pluses downwards unless they exceed +2. The protection is otherwise similar to that against elementals. The <i>protection from shape-changers</i> scroll protects against monsters (except gods and god-like creatures) able to change their form to that of man; i.e. <a href="/creatures/doppleganger">dopplegangers</a>, certain dragons, druids, <a href="/creatures/jackalwere">jackalwere</a>, and those under the influence of polymorph spells, as well as all actual lycanthropes. The magic lasts for 5-30 rounds.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Magic',
    read_time = TimePeriod(8, TimeUnit.segment),
    desc = ('This scroll invokes a very powerful and invisible globe of anti-magic in a 5\' radius from the reader. It prevents any form of magic from passing into or out of its confines, but normal things are not restricted by it. As with other protections, the globe of anti-magic moves with its invoker. Any magical item which touches the globe must be saved for with a 50% likelihood of the object being drained of all magic from the power of the globe, i.e. save equals 11 or better with d20. The protection lasts for 5-30 (5d6) rounds.\n\n'
        'If multiple magic items encounter the globe simultaneously, the leading item (a magic sword held in advance of its holder, for instance) is the first affected, then the others are checked in order of decreasing power until the first item fails its save, at which time the globe is cancelled and the item is drained of its magic.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Petrification',
    read_time = TimePeriod(5, TimeUnit.segment),
    desc = 'A 10\' radius circle of protection extends from, and moves with, the reader of this scroll. All within its confines are absolutely immune to any attack forms, magical or otherwise, which cause flesh to turn to stone. The protection lasts for 5-20 (5d4) rounds.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Possession',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'This scroll generates a magic circle of 10\' radius which extends from, and moves with, the reader. All creatures within its confines are protected from possession by magical spell attacks such as <a href="/spells/magic-jar-magic-user-lvl-5"><i>magic jar</i></a>; attack forms aimed at possession or mental control or psychic energy drain which are psionically based or magically based, or demon, devil, <a href="/creatures/night-hag">night hag</a>, or similar creature possession (obsession). This protects even dead bodies if they are within the magic circle. The protection lasts for 10 to 60 rounds in 90% of these scrolls; 10% have power which lasts 10 to 60 turns, but the protection is <i>stationary</i>.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
Scroll( name = 'Protection from Undead',
    read_time = TimePeriod(4, TimeUnit.segment),
    desc = ('When this scroll is read a 5\' radius circle of protection extends from, and moves with, the reader. It protects all within its circumference from all physical attacks from undead (<a href="/creatures/ghast">ghasts</a>, <a href="/creatures/ghost">ghosts</a>, <a href="/creatures/ghoul">ghouls</a>, <a href="/creatures/shadow">shadows</a>, <a href="/creatures/skeleton">skeletons</a>, <a href="/creatures/spectre">spectres</a>, <a href="/creatures/wight">wights</a>, <a href="/creatures/wraith">wraiths</a>, <a href="/creatures/vampire">vampires</a>, <a href="/creatures/zombie">zombies</a>) but not magic spells or other attack forms. If a creature leaves the protected area it is then subject to physical attack as well. The protection will restrain up to 35 hit dice/levels of undead; excess hit dice/levels can pass through the circle. It remains in effect for 10-80 (10d8) rounds. Note: some <i>protection</i> scrolls of this nature will protect only against certain types of undead (one or more) rather than all undead, at the DM\'s option. The following table from <b>POTIONS, <i>Undead Control</i></b> may be used to determine a specific type of undead.\n\n'
        '<table><tr><th>Die Roll</th><th>Undead Type</th></tr>'
        '<tr><td>1</td><td><a href="/creatures/ghast">Ghasts</a></td></tr>'
        '<tr><td>2</td><td><a href="/creatures/ghost">Ghosts</a></td></tr>'
        '<tr><td>3</td><td><a href="/creatures/ghoul">Ghouls</a></td></tr>'
        '<tr><td>4</td><td><a href="/creatures/shadow">Shadows</a></td></tr>'
        '<tr><td>5</td><td><a href="/creatures/skeleton">Skeletons</a></td></tr>'
        '<tr><td>6</td><td><a href="/creatures/spectre">Spectres</a></td></tr>'
        '<tr><td>7</td><td><a href="/creatures/wight">Wights</a></td></tr>'
        '<tr><td>8</td><td><a href="/creatures/wraith">Wraiths</a></td></tr>'
        '<tr><td>9</td><td><a href="/creatures/vampire">Vampires</a></td></tr>'
        '<tr><td>0</td><td><a href="/creatures/zombie">Zombies</a></td></tr>'
        '</table>'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
#Unearthed scrolls
Scroll( name = 'Protection from Acid',
    read_time = TimePeriod(5, TimeUnit.segment),
    desc = 'The reader of the scroll is protected from all forms of acid, up to a damage limit of 20 hit dice or a time limit of 9-12 turns (d4 +8), whichever comes first. Thus, the scroll would provide safety from three separate breath-weapon attacks be a <a href="/creatures/black dragon</a> of smallest size (normally 6 HD of damage per attack), with a small amount of protection yet unused - assuming that the attacks all take place before the time limit expires.',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Breath Weapons, Dragon',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'Only the individual reading this scroll is protected. Protection is not limited by alignment type or type of breath; it extends to all forms of dragon breath, and lasts for 6-12 rounds (2d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Cold',
    read_time = TimePeriod(3, TimeUnit.segment),
    desc = 'Protection extends outward from the reader within a 3" diameter sphere. All within this area are protected from the effects of normal cold as low as absolute zero. Against magical cold, the liquid acts as the clerical spelll <a href="/spells/resist-cold-cleric-lvl-1"><i>resist cold</i></a>, but with enhanced benefits (+6 on saving throw, damage one-quarter normal or one-eighth if save is made). The duration of the effect is 5-8 turns (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Electricity',
    read_time = TimePeriod(5, TimeUnit.segment),
    desc = 'Protection is provided in a 2" diameter sphere centered on the reader. All protected are immune to any electrical attacks and associated effects. Protection lasts for 3-12 rounds (3d4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Fire',
    read_time = TimePeriod(8, TimeUnit.segment),
    desc = 'Protection extends to a 3" diameter sphere centered on the reader. All within this area are able to withstand flame and heat of the hottest sort, even of magical or elemental nature. Protection lasts for 5-8 turns (d4  +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Gas',
    read_time = TimePeriod(3, TimeUnit.segment),
    desc = 'The scroll generates a 1" diameter sphere of protection centered on the reader, and all within this area are immune to the effects of any form of gas - poison gas, breath weapons which are gaseous in nature, spells which generate gas clouds such as <a href="/spells/stinking-cloud-magic-user-lvl-2"><i>stinking cloud</i></a> and <a href="/spells/cloudkill-magic-user-lvl-5"><i>cloudkill</i></a>, and all similar forms of noxious, toxic vapors. The scroll\'s protection lasts for 5-8 rounds (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Illusions',
    read_time = TimePeriod(7, TimeUnit.segment),
    desc = 'Only the individual reading the scroll is protected, and the benefit extends to any form of <i>illusion/phantasm</i> magic witnessed by the individual. Protection lasts for 5-30 rounds (5d6).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Paralyzation',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'Only the reader is affected by the dweomer of this scroll. The protection extends to all forms of paralyzation, muscle and nerve paralysis included. A <a href="/spells/hold-monster-magic-user-lvl-5"><i>hold</i></a> spell will not work upon the protected individual, nor will any sort of paralysis brought about by gas. Protection lasts for 2-5 turns (d4 +1).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Plants',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'Protection extends to a 1" diameter sphere centered on the reader. All forms of vegetable life, including fungi, slimes, molds, and the like are unable to penetrate the protective sphere. If it is moved toward such plant life which is capable of movement, the plant will be pushed away. If the protective sphere is pushed up against an immobile, firmly fixed form of plant life (such as a well-rooted shrub, bush, or tree), the sphere will not be able to be moved farther in that direction unless the reader of the scroll has enough strength and mass to be able to uproot the plant under normal circumstances. Protection lasts for 5-8 turns (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Poison',
    read_time = TimePeriod(3, TimeUnit.segment),
    desc = 'Protection afforded by the scroll extends only to the reader. No form of poison - ingested, insinuated, contacted, breathed, etc. - will affect the protected individual, and any such poison in the reader\'s system is permanently neutralized by the dweomer of the scroll. Protection lasts for 3-12 rounds (d10 +2).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Traps',
    read_time = TimePeriod(0, TimeUnit.variable),
    desc = ('There are three forms of this scroll - those that protect from mechanical traps (50%), magical traps (30%), and those that protect from any form of trap (20%).\n\n'
        '<b>Mechanical</b>: Reading time: 4 segments. Protection extends only to the reader. Traps of mechanical nature do not function against the reader, but neither are they revealed. Protection lasts for 5-20 rounds (5d4).\n\n'
        '<b>Magical</b>: Reading time: 8 segments. Protection extends in a 1" diameter sphere centered on the reader. Magical traps do not function against those in the area of protection, but neither are they revealed. Protection lasts for 3-12 rounds (d10 +2).\n\n'
        '<b>Any trap</b>: Reading time: 1 round. Protection extends in a 1" diameter sphere centered on the reader. The dweomer prevents the functioning of any trap, but does not reveal any that may exist within the protective sphere. Protection lasts for 2-8 rounds (2d4).'
    ),
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Water',
    read_time = TimePeriod(6, TimeUnit.segment),
    desc = 'Protection extends in a 1" diameter sphere centered on the reader. All forms of water - liquid, solid, and vapor, ice, hail, snow, sleet, steam, and so forth - are unable to penetrate the sphere of protection. If those being protected come upon a form of water, the substance simply will not touch them; thus, they will not slip on ice, sink into a body of water, etc. Protection lasts for 5-8 turns (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Weapons, Magical',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'Protection extends only to the reader. The form of magic weapon indicated is prevented from touching/harming the protected individual - but note that missile protection does not extends to missiles created by spell casting (such as <a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a>) or the use of spell-like power. Protection lasts for 5-8 rounds (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
Scroll( name = 'Protection from Weapons, Non-magic',
    read_time = TimePeriod(1, TimeUnit.round),
    desc = 'Protection extends in a 1" diameter sphere centered on the reader. The form of non-magical weapon indicated is prevented from touching/harming the protected individual - but note that missile protection does not extend to normal missiles of large size, such as projectiles from a catapult or objects hurled by giants. Protection lasts for 5-8 rounds (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
)
]

rings = [
Ring( name = 'Ring of Contrariness',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This magic ring is cursed so as to make its wearer unable to agree with any idea or statement or action. Once put on, the ring can be removed only after a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell is cast upon the individual wearing it. Because of the curse, the wearer will resist any attempts to cast such a spell. Furthermore, the <i>contrariness</i> ring will have one of the following additional magical properties:\n\n'
        '01-20: <a href="/spells/fly-magic-user-lvl-3"><i>Flying</i></a>\n'
        '21-40: <a href="/spells/invisibility-magic-user-lvl-2"><i>Invisibility</i></a>\n'
        '41-60: <a href="/spells/levitate-magic-user-lvl-2"><i>Levitation</i></a>\n'
        '61-70: <a href="/spells/shocking-grasp-magic-user-lvl-1"><i>Shocking Grasp</i></a> (once per round)\n'
        '71-80: <i>Spell Turning</i>\n'
        '81-00: <a href="/spells/strength-magic-user-lvl-2"><i>Strength</i></a> (18/00)\n\n'
        'Note that <i>contrariness</i> can <i>never</i> be removed from the ring. The wearer will use his or her own powers, plus those of the ring, to retain it on his or her finger. The wearer of the ring will never damage him or herself. If, for example, other characters suggest that the wearer should make certain that attacks upon him or her are well-defended against, or that he or she should not strike his or her own head, the ring wearer will agree - possibly attacking or striking at the speaker\'s head - because obviously the <i>result</i> must be contrary in this case. If a <i>ring of contrariness</i> turns spells, the cumulative <i>remove curse</i> cast upon the individual wearing it must equal or exceed 00 (100%).'
    )
),
Ring( name = 'Ring of Delusion',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>delusion ring</i> will convince the wearer that it is some other sort of ring, a ring of whatever sort the wearer really desires. As the wearer will be completely convinced that the ring is actually one with other magical properties, he or she will unconsciously use his or her abilities of any sort (including those of other magical items available) to actually produce a result commensurate with the supposed properties of the <i>delusion ring</i>. As referee, you will have to be most judicious in determining how successful the self-delusion can be, as well as how observers can be affected and what they will observe. The ring can be removed at any time.'
),
Ring( name = 'Ring of Djinni Summoning',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'One of the fabled rings of fantasy legend, the "genie" ring is most useful indeed, for it a special "gate" by means of which a certain <a href="/creatures/djinni">djinni</a> can be summoned from the Elemental Plane of Air. When the ring is rubbed the summons is served, and the djinni will appear on the next round. The djinni will faithfully obey and serve the wearer of the ring, but if the servant of the ring is ever killed, the ring becomes non-magical and worthless.'
),
Ring( name = 'Ring of Elemental Command',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The 4 types of <i>elemental command</i> rings are very powerful. Each appears to be nothing more than a lesser ring (detailed below), but each has certain other powers as well as the following common properties:\n\n'
        '1. Elementals of the plane to which the ring is attuned cannot approach within 5\' of or attack the wearer; or, if the wearer desires, he or she may forego this protection and instead attempt to <a href="/spells/charm-monster-magic-user-lvl-4"><i>charm</i></a> the elemental (saving throw applicable at -2 on the die). If the latter fails, however, total protection is lost and no further attemp at charming can be made, but the secondary properties given below will then function with respect to the elemental.\n\n'
        '2. Creatures, other than normal elementals, from the plane to which the ring is attuned attack at -1 on their "to hit" dice, the ring wearer takes damage at -1 on each hit die, makes applicable saving throws from the creature\'s attacks at +2, all attacks are made by the wearer of the ring at +4 "to hit" (or -4 on the elemental creature\'s saving throw), and the wearer does +6 damage (total, not per die) adjusted by any other applicable bonuses and/or penalties. Any weapon used by the ring wearer can hit elementals or elemental creatures even if it is not magical.\n\n'
        '3. The wearer of the ring is able to converse with the elementals or elemental creatures of the plane to which the ring is attuned, and they will recognize that he or she wears the ring, so they are at least going to show a healthy respect to the wearer. If alignment is opposed, this respect will be <i>fear</i> if the wearer is strong, <i>hatred</i> and a <i>desire to slay</i> if the wearer is weak.\n\n'
        '4. In addition, the possessor of a <i>ring of elemental command</i> will suffer a saving throw penalty as follows:\n\n'
        'Air: -2 vs. fire\n'
        'Earth: -2 vs. petrification\n'
        'Fire -2 vs. water or cold\n'
        'Water -2 vs. lightning/electricity\n\n'
        '5. Only one power (whether major or minor) or a <i>ring of elemental command</i> can be in use at one time.\n\n'
        '<b>Air</b>: The wearer can at will produce the following magical effects:\n\n'
        '<a href="/spells/gust-of-wind-magic-user-lvl-3"><i>gust of wind</i></a> (once per round)\n'
        '<a href="/spells/fly-magic-user-lvl-3"><i>fly</i></a>\n'
        '<a href="/spells/wall-of-force-magic-user-lvl-5"><i>wall of force</i></a> (once per day)\n'
        '<a href="/spells/control-winds-druid-lvl-5"><i>control winds</i></a> (once per week)\n'
        '<a href="/spells/invisibility-magic-user-lvl-2"><i>invisibility</i></a>\n\n'
        'The ring will appear to be nothing other than an <i>invisibility ring</i> until a certain condition is met (such as having the ring <a href="/spells/bless-cleric-lvl-1"><i>blessed</i></a>, slaying an <a href="/creatures/air-elemental">air elemental</a>, or whatever you determine as necessary to activate its full potential).\n\n'
        '<b>Earth</b>: The wearer can at will produce the following magical effects:\n\n'
        '<a href="/spells/stone-tell-cleric-lvl-6"><i>stone tell</i></a> (once per day)\n'
        '<a href="/spells/passwall-magic-user-lvl-5"><i>passwall</i></a> (twice per day)\n'
        '<a href="/spells/wall-of-stone-magic-user-lvl-5"><i>wall of stone</i></a> (once per day)\n'
        '<a href="/spells/stone-to-flesh-magic-user-lvl-6"><i>stone to flesh</i></a> (twice per week)\n'
        '<a href="/spells/move-earth-magic-user-lvl-6"><i>move earth</i></a> (once per week)\n'
        '<a href="/spells/feather-fall-magic-user-lvl-1"><i>feather fall</i></a>\n\n'
        'The ring will appear to be nothing other than a <i>ring of feather falling</i> until the condition you establish is met.\n\n'
        '<b>Fire</b>: The wearer can at will produce the following magical effects:\n\n'
        '<a href="/spells/burning-hands-magic-user-lvl-1"><i>burning hands</i></a> (once per turn)\n'
        '<a href="/spells/pyrotechnics-druid-lvl-3"><i>pyrotechnics</i></a> (twice per day)\n'
        '<a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a> (once per day)\n'
        '<a href="/spells/flame-strike-cleric-lvl-5"><i>flame strike</i></a> (twice per week)\n'
        '<i>fire resistance</i>\n\n'
        'The ring will appear to be nothing other than a <i>ring of fire resistance</i> until the condition you establish is met.\n\n'
        '<b>Water</b>: The wearer can at will produce the following magical effects:\n\n'
        '<a href="/spells/purify-water-druid-lvl-1"><i>purify water</i></a>\n'
        '<a href="/spells/create-water-cleric-lvl-1"><i>create water</i></a> (once per day)\n'
        '<a href="/spells/water-breathing-druid-lvl-3"><i>water breathing</i></a> (5\' radius)\n'
        '<a href="/spells/wall-of-ice-magic-user-lvl-4"><i>wall of ice</i></a> (once per day)\n'
        '<a href="/spells/airy-water-magic-user-lvl-5"><i>airy water</i></a>\n'
        '<a href="/spells/lower-water-cleric-lvl-4"><i>lower water</i></a> (twice per week)\n'
        '<a href="/spells/part-water-cleric-lvl-6"><i>part water</i></a> (twice per week)\n'
        '<i>water walking</i>\n\n'
        'The ring will appear to be nothing other than a <i>ring of water walking</i> until the condition you establish is met.\n\n'
        'Rings operate at 12th level of experience, or the minimum level needed to perform the equivalent magic spell, if greater, with respect to range, duration, or area of effect determinations which might apply. The additional powers take only 5 segments to bring forth.'
    )
),
Ring( name = 'Ring of Feather Falling',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring protects its wearer by automatic activation of a <a href="/spells/feather-fall-magic-user-lvl-1"><i>feather fall</i></a> if the individual falls 5\' or more. (Cf. <a href="/spells/feather-fall-magic-user-lvl-1"><i>feather fall</i></a> spell.)'
),
Ring( name = 'Ring of Fire Resistance',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The wearer of this ring is totally immune to the effects of normal fires - torches, flaming oil, bonfires, etc. Very large and hot fires, molten lava, demon immolation, <a href="/creatures/hell-hound">hell hound</a> breath, or a <a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a> spell will cause 10 hit points of damage per round (1 per segment) if the wearer is directly within such conflagration. Exceptionally hot fires such as <a href="/creatures/red-dragon">red dragon</a> breath, <a href="/creatures/pyrohydra">pyrohydra</a> breath, <a href="/spells/fireball-magic-user-lvl-3"><i>fireballs</i></a>, <a href="/spells/flame-strike-cleric-lvl-5"><i>flame strike</i></a>, <a href="/spells/fire-storm-druid-lvl-7"><i>fire storm</i></a>, etc. are saved against at +4 on the die roll, and all damage dice are calculated at -2 per die, but each die is never less than 1 in any event. (As a rule of thumb, consider very hot fires as those which have a maximum initial exposure of up to 24 hit points, those of exceptional heat 25 or more hit points.)'
),
Ring( name = 'Ring of Free Action',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring enables the wearer to move and attack freely and normally whether attacked by a <a href="/spells/web-magic-user-lvl-2"><i>web</i></a>, <a href="/spells/hold-monster-magic-user-lvl-5"><i>hold</i></a>, or <a href="/spells/slow-magic-user-lvl-3"><i>slow</i></a> spell, or even while under water. In the former case the spells have no effect, while in the latter the individual moves at normal (surface) speed and does full damage even with such cutting weapons as axes and scimitars and with such smashing weapons as flails, hammers, and maces, insofar as the weapon used is held rather than hurled. Thus will not, however, enables <i>water breathing</i> without the further appropriate magic.'
),
Ring( name = 'Ring of Human Influence',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring has the effect of raising the wearer\'s charisma to 18 with respect to encounter reactions with humans/humanoids. The wearer can make a <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a> to any human or humanoid conversed with (saving throw applies). The wearer can also <i>charm</i> up to 21 levels/hit dice of human/humanoids (saving throws apply) just as if he or she were using the magic-user spell, <a href="/spells/charm-person-magic-user-lvl-1"><i>charm person</i></a> The two latter uses of the ring are applicable but once per day. <i>Suggestion</i> or <i>charm</i> requires 3 segments of casting time.'
),
Ring( name = 'Ring of Invisibility',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The wearer of an <i>invisibility ring</i> is able to become invisible at will, instantly. This non-visible state is exactly the same as the magic-user <a href="/spells/invisibility-magic-user-lvl-2"><i>invisibility</i></a> spell, except that 10% of these rings also have <i>inaudibility</i> as well, making the wearer absolutely silent. If the wearer wishes to speak, he or she breaks all silence features in order to do so.'
),
Ring( name = 'Ring of Mammal Control',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This ring enables its wearer to exercise complete control over mammals with intelligence of 4 or less (<i>animal</i> or <i>semi</i>-intelligent mammals). Up to 30 hit dice of mammals can be controlled. Control extends to such limits as to enable the wearer to have the creatures controlled actually kill themselves, but complete concentration is required. (Note: the ring does not affect bird-mammal combinations, humans, semi-humans, and monsters such as <a href="/creatures/lammasu">lammasu</a>, <a href="/creatures/shedu">shedu</a>, <a href="/creatures/manticore">manticores</a>, etc.) If you are in doubt about any monster, it is NOT a mammal.\n\n'
        'Obviously, rats, weasels, herd animals, dolphins, and even <a href="/creatures/unicorn">unicorns</a> are mammals, but intelligence will preclude control of the better ones. Control time is 3 segments.'
    )
),
Ring( name = 'Ring of Multiple Wishes',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring contains 2-8 (2d4) <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spells. As with any <i>wish</i>, you must be very judicious in how you handle the request. If players are greedy and grasping, be sure to "crock" them. Interpret their wording exactly, twist the wording, or simply rule the request is beyond the power of the magic. In any case, the <i>wish</i> is used up, whether or not (or how) the <i>wish</i> was granted. Note that no <i>wish</i> is able to cancel the decrees of god-like beings, unless it comes from another such creature.'
),
Ring( name = 'Ring of Protection',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>ring of protection</i> increases the wearer\'s armor class value and saving throws versus all forms of attack. A +1 ring raises AC by 1, say from 10 to 9 and gives a bonus of +1 on saving throw die rolls. The magical properties of a <i>ring of protection</i> are cumulative with all other magical items of protection except as follows:\n\n'
        '1. The ring does not add to armor value if magical armor is worn, although it does add to saving throw die rolls.\n\n'
        '2. More than 1 <i>ring of protection</i> operating on the same person, or in the same area, do not combine protection; only one - the strongest, if applicable - will function, so a pair of +2 <i>protection</i> rings are still only +2.\n\n'
        'To determine the value of the protection ring use the table below:\n\n'
        '<table>'
        '<tr><th>Percentile Result</th><th>Protection Value</th></tr>'
        '<tr><td>01-70</td><td>+1</td></tr>'
        '<tr><td>71-82</td><td>+2</td></tr>'
        '<tr><td>83</td><td>+2, 5\' radius protection</td></tr>'
        '<tr><td>84-90</td><td>+3</td></tr>'
        '<tr><td>91</td><td>+3, 5\' radius protection</td></tr>'
        '<tr><td>92-97</td><td>+4 on AC, +2 on saving throws</td></tr>'
        '<tr><td>98-00</td><td>+6 on AC, +1 on saving throws</td></tr>'
        '</table\n\n'
        'The <i>radius</i> bonus of 5\' extends to all creatures within its circle, but applies only to their saving throws, i.e. only the ring wearer gains armor class additions.'

    )
),
Ring( name = 'Ring of Regeneration',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'There are 2 forms of this ring: The standard <i>regeneration ring</i> restores 1 hit point of damage (and will replace lost limbs or organs eventually also) per turn. It will bring its wearer back from death (but if poison is the cause, the saving throw must be made or else the wearer dies again from the poison still in his or her system). Only total destruction of all living tissue by fire or acid or similar means will prevent <i>regeneration</i>. Of course the ring must be worn, and its removal stops regeneration processes. The rare form is the <i>vampiric regeneration ring</i>. This ring bestows one-half of the value of hit points of damage the wearer inflicts upon opponents in hand-to-hand (melee, non-missile, non-spell) combat immediately upon its wearer (fractions dropped). It does not otherwise cause regeneration or restore life, limb or organ. To determine which type of ring is discovered roll percentile dice: 01-90 = <i>ring of regeneration</i>, 91-00 = <i>vampiric regeneration ring</i>. In no case can the wearer\'s hit point total exceed that initially generated.'
),
Ring( name = 'Ring of Shooting Stars',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This ring has 2 modes of operation, both working only in relative darkness. During night hours, under the open sky, the <i>shooting stars ring</i> will perform the following functions:\n\n'
        '<a href="/spells/dancing-lights-magic-user-lvl-1"><i>dancing lights</i></a> (once per hour) - as the spell\n'
        '<a href="/spells/light-magic-user-lvl-1"><i>light</i></a> (twice per night), 12" range - as the spell\n'
        '<i>ball lightning</i> (once per night) - see below\n'
        '<i>shooting stars</i> (special) - see below\n\n'
        'The <i>ball lightning</i> function releases 1 to 4 balls of lightning at the wearer\'s option. These glowing globes exactly resemble <i>dancing lights</i>, and the ring wearer controls them as he or she would control <i>dancing lights</i>. These spheres have a 12" range and a 4 round duration. They can be moved at 4" per round. Each sphere is about 3\' in diameter, and any creature it touches or comes near to dissipates its charge (save versus magic equals one-half damage as the contact was across an air gap). The charge values are:\n\n'
        '<table>'
        '<tr><th>Number of Balls</th><th>Lightning Damage</th></tr>'
        '<tr><td>4</td><td>2-8 hit points each</td></tr>'
        '<tr><td>3</td><td>2-12 hit points each</td></tr>'
        '<tr><td>2</td><td>5-20 hit points each</td></tr>'
        '<tr><td>1</td><td>4-48 hit points</td></tr>'
        '</table>\n\n'
        'Release can be simultaneous or singular, during the course of 1 round or as needed throughout the night.\n\n'
        'The <i>shooting stars</i> are glowing missiles with fiery trails, much like a <a href="/spells/meteor-swarm-magic-user-lvl-9"><i>meteor swarm</i></a>. 3 <i>shooting stars</i> can be released from the ring each week, simultaneously or one at a time. They impact for 12 hit points of damage and burst (as a <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a>) in a 1" diameter sphere for 24 hit points of damage. Any creature struck will take full damage from impact plus full damage from the <i>shooting star</i> burst. Creatures within the burst radius must save versus magic to take only one-half damage, i.e. 12 hit points of damage, otherwise they too take the full 24 hit points of damage. Range is 7", at the end of which the burst will occur, unless an object or creature is struck before that. The <i>shooting stars</i> follow a straight line path. A creature in the path must save versus magic or be impacted upon by the missile, and saving throw rolls are at -3 within 2" of the ring wearer, -1 within 2" to 4", normal beyond 4".\n\n'
        'Indoors at night, or underground, the ring has the following properties:\n\n'
        '<a href="/spells/faerie-fire-druid-lvl-1"><i>faerie fire</i></a> (twice per day) - as the spell\n'
        '<i>spark shower</i> (once per day) - see below\n\n'
        'The <i>spark shower</i> is a flying cloud of sizzling purple sparks, which fan out from the ring for 20\' to a breadth of 10\'. Creatures within this area take from 2-8 hit points of damage each if no metallic armor is worn or no metallic weapon is held, 4-16 otherwise.\n\n'
        'Range, duration, and area of effect of functions are the minimum for the comparable spell unless otherwise stated. Casting time is 5 segments.'
    )
),
Ring( name = 'Ring of Spell Storing',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>ring of spell storing</i> will contain 2-5 (d4 +1) spells which the wearer can employ just as if he or she were a spell user of the level appropriate to use the spell in question. The class of spells contained within the ring is determined in the same fashion as the spells on scrolls. The level of each spell is determined as follows:\n\n'
        'cleric: d6, if 6 is rolled roll d4 instead\n'
        'druid: as cleric\n'
        'magic-user: d8, if 8 is rolled roll d6 instead\n'
        'illusionist: as cleric\n\n'
        'Which spell type of any given level is contained by the ring is also randomly determined. The ring has the empathic ability to impart to the wearer the names of its spells. Once class, level, and type are determined, the properties of the ring are <i>fixed</i> and <i>unchangeable</i>. Once a spell is cast from the ring, it can only be restored by a character of appropriate class and level of experience, i.e. a 12th level magic-user is needed to restore a 6th level magic-user spell to the ring. Spells stores require 5 segments each to cast.'
    )
),
Ring( name = 'Ring of Spell Turning',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This ring distorts the three normal dimensions with respect to magic spells directed at its wearer. Any spell cast at an individual will usually rebound, in part or perhaps in whole, upon the spell caster. The distance between, and area occupied by, the victim (the ring wearer) and the spell caster are not as they seem when the magic activates the <i>spell turning</i> ring. Three important exceptions must be noted:\n\n'
        '1. Spells which affect an area, and which are not cast directly at the ring wearer, are not turned by the ring.\n\n'
        '2. Spells which are delivered by touch are not turned.\n\n'
        '3. Magic contained in devices (rods, staves, wands, rings, and other items) which are triggered without spell casting are not turned. Note: a scroll spell is <i>not</i> considered a device.\n\n'
        'When a spell is cast at an individual wearing a <i>ring of spell turning</i> percentile dice are rolled and rounded to the nearest decimal, i.e. 1-5 is dropped, 6-9 adds 10, so 05 equals 0%, but 96 equals 100%. The score of the percentile dice indicates what portion of the spell has been turned back upon its caster.\n\n'
        'Damage is determined and awarded proportionally. Saving throws (for both opponents) are adjusted upwards by +1 for each 10% below 100%, i.e. 80% = +2, 70% = +3, ... 10% = +9. Even with such adjustments in saving throw it is possible that both target individual and spell caster will end up polymorphed into bullfrogs!\n\n'
        '<b>Note Regarding Ring of Spell Turning</b>: Unless the percentile dice score for the <i>turning</i> effect is 09 or less or 91 or more, this ring will allow a saving throw against spells which normally have none. The effect of the save will be to negate or inflict half normal damage as appropriate to the spell in question. For each 10% of the spell <i>turned</i>, allow a 5% chance (1 in 20) to save. Thus, if 11-19 is rolled, a roll of 20 saves, 20-29 allows a 19-20 to save, 30-39 allows 18-20, and so on. Example: An illusionist casts a <a href="/spells/maze-illusionist-lvl-5"><i>maze</i></a> spell upon a fighter wearing a <i>ring of spell turning</i>. The <i>maze</i> spell normally allows no saving throw, but the ring turns 34% of the spell effect. The fighter has a 15% chance to save against the spell (34% on the <i>turning</i>); otherwise it will take full normal effect. The illusionist mmust also save (100% - 34% = 66%, or 6 10% increments, which converts to a 30% chance to save) by rolling a 15-20 or be <i>mazed</i> also. Saving in this case will negate spell effect. This special saving throw is NOT modified by race, magic items, or any other condition, including existing spells.\n\n'
        'Spells which affect a certain number of levels which are aimed at the ring wearer must be able to affect as many levels as the wearer and the spell caster combined. If this condition is fulfilled, then the procedure above applies to ultimate effect determination.\n\n'
        'In the case of the ring wearer desiring to receive a spell, he or she must remove the <i>spell turning</i> ring to be able to do so.\n\n'
        'Psionic attacks are not considered as spell casting.\n\n'
        'If the spell caster and spell recipient both wear <i>spell turning</i> rings a resonating field is set up, and one of the following results will take place:\n\n'
        '01-70: spell drains away without effect\n'
        '71-80: spell affects both equally at full effect\n'
        '81-97: both rings are drained permanently\n'
        '98-00: both individuals go through a rift into the <i>Positive Material Plane</i>'
    )
),
Ring( name = 'Ring of Swimming',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>ring of swimming</i> bestows the ability to swim at a full 21" base speed upon the wearer, assuming, of course, he or she is clad only in garments appropriate for such activity. It further enables the wearer to dive up to 50\' into water without injury, providing the depth of the water is at least 1½\' per 10\' of diving elevation; and the wearer can stay underwater for up to 4 rounds before a 1 hour (floating) rest is needed. The ring confers the ability to stay afloat under all but typhoon-like conditions.'
),
Ring( name = 'Ring of Telekinesis',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This ring enables the wearer to telekinese objects in the same manner as the fifth level magic-user spell, <a href="/spells/telekinesis-magic-user-lvl-5"><i>telekinesis</i></a>. The amount of weight which can be so moved, however, is variable. Roll percentile dice to find the strength of the ring:\n\n'
        '01-25: 250 g.p. maximum\n'
        '26-50: 500 g.p. maximum\n'
        '51-89: 1,000 g.p maximum\n'
        '90-99: 2,000 g.p. maximum\n'
        '00: 4,000 g.p. maximum\n\n'
        'Telekinesis time is only 1 segment to begin the effect.'
    )
),
Ring( name = 'Ring of Three Wishes',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Although the ring contains 3 <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spells instead of a variable number, it is otherwise the same as a <i>multiple wish</i> ring except that 25% (01-25) contain 3 <a href="/spells/limited-wish-magic-user-lvl-7"><i>limited wish</i></a> spells.'
),
Ring( name = 'Ring of Warmth',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>warmth</i> ring provides its wearer with body heat even in conditions of extreme cold where the wearer has no clothing whatsoever. It also provides restoration of cold-sustained damage at the rate of 1 hit point of damage per turn. It increases saving throws versus cold-based attacks by +2 and reduces damage sustained by -1 per die.'
),
Ring( name = 'Ring of Water Walking',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring enables the wearer to walk upon any liquid without sinking into it; this includes mud, quicksand, oil, running water, and even snow. The ring wearer\'s feet do not actually contact the surface he or she is walking upon when liquid or water is being walked upon (but oval depressions about 1½\' long and 1 inch deep per 100 pounds of weight of the walker will be observed in hardening mud or set snow). Rate of movement is standard movement for the individual wearing this ring. Up to 1,200 pounds weight can be supported by a <i>water walking</i> ring.'
),
Ring( name = 'Ring of Weakness',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This cursed ring causes the wearer to lose 1 point of strength and 1 point of constitution per turn until the individual reaches 3 in each ability area. This loss is not noticeable until the individual actually observes his or her weakened state due to some exertion (such as combat or heavy lifting), for the ring will also make the wearer <i>invisible</i> at will (and also cause the rate of strength and constitution point loss to double). Note that when full weakness is attained the wearer will be unable to function in his or her class. The <i>weakness</i> ring can be removed only if a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell, followed by a <a href="/spells/dispel-magic-magic-user-lvl-3"><i>dispel magic</i></a> spell, is cast upon the ring. There is a 5% chance that the ring is reversed, being a <i>ring of berserk strength</i>. This form gradually increases strength and constitution to 18 each (roll percentile dice for bonus strength if the wearer is a fighter). Increase is 1 point per ability per turn. However, once 18s in both abilities are reached, the wearer will always melee with any opponent he or she meets, immediately, regardless of circumstances. Points lost from the ring are restored by rest on a 1 day for 1 point basis, with 1 point of each ability lost being restored in 1 day of rest. Berserk strength is lost when the ring is removed, as are constitution points gained.'
),
Ring( name = 'Ring of Wizardry',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Only magic-users can benefit from this type of ring. Other classes, even those with spell ability, can neither use nor understand the working of a <i>ring of wizardry</i>. The ring <i>doubles</i> spell ability (i.e. the number of spells a magic-user may prepare each day) in one or more spell levels. To determine the properties of a given ring use the table below:\n\n'
        '<table>'
        '<tr><th>Percentile Roll</th><th>Doubled Spell Level(s)</th></tr>'
        '<tr><td>01-50</td><td>First level spells</td></tr>'
        '<tr><td>51-75</td><td>Second level spells</td></tr>'
        '<tr><td>76-82</td><td>Third level spells</td></tr>'
        '<tr><td>83-88</td><td>First and second level spells</td></tr>'
        '<tr><td>89-92</td><td>Fourth level spells</td></tr>'
        '<tr><td>93-95</td><td>Fifth level spells</td></tr>'
        '<tr><td>96-99</td><td>First through third level spells</td></tr>'
        '<tr><td>00</td><td>Fourth and fifth level spells</td></tr>'
        '</table>'
    )
),
Ring( name = 'Ring of X-Ray Vision',
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>ring of X-Ray vision</i> empowers its possessor with the ability to see into and/or through substances which are impenetrable to normal sight. Vision range is 20\', with the viewer seeing as if it were normal light due to expanded vision capability. <i>X-Ray vision</i> will penetrate 20\' of cloth, wood, or similar animal or vegetable material, up to 10\' of stone or 10 inches of many metals:\n\n'
        '<table>'
        '<tr><th>Substance Scanned</th><th>Thickness Penetrated per Round of X-Raying</th><th>Maximum Thickness</th></tr>'
        '<tr><td>Animal matter</td><td>4\'</td><td>20\'</td></tr>'
        '<tr><td>Vegetable matter</td><td>2½\'</td><td>20\'</td></tr>'
        '<tr><td>Stone</td><td>1\'</td><td>10\'</td></tr>'
        '<tr><td>Iron, Steel, etc.</td><td>1 inch</td><td>10 inches</td></tr>'
        '<tr><td>Lead, Gold, Platinum</td><td>nil</td><td>nil</td></tr>'
        '</table>\n\n'
        'It is possible to scan 100 square feet of area during 1 round; thus during 1 turn the wearer of the ring could scan a full area of stone 10\' wide, 10\' high and 1\' thick. Secret compartments, drawers, recesses, and doors are 90% likely to be located by X-ray vision scanning. Even though this ring enables its wearer to scan secret doors, traps, hidden items, and the like, it also limits his or her use of the power, for it drains 1 point of constitution if used more frequently than once every 6 turns. If it is used 3 turns in 1 hour the user loses 2 points from his or her total constitution score, 3 if used 4 turns, etc. Constitution loss is recovered at the rate of 2 points per day of rest. Constitution of 2 means the wearer is exhausted and <i>must</i> rest immediately. No activity, not even walking, can be performed until constitution of 3 or better is restored.'

    )
),
#UNEARTHED RINGS
Ring( name = 'Ring of Animal Friendship',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'When the wearer of this ring approaches within 1" of any animal(s) of <i>neutral</i> alignment and <i>animal</i> intelligence, the creature(s) must save versus spell. If they succeed, they will then move rapidly away from the ring wearer. If the saving throw fails, then the creature(s) will become docile and follow the ring wearer around. The dweomer of the item functions at 6th level, so up to 12 hit dice of animals can be affected by this ring. Those feeling friendship for the wearer will actually guard and protect the individual if he or she expends a charge from the ring to cause such behavior. A ring of this sort typically has 27 charges when discovered, and it cannot be recharged. A druid wearing this ring can influence twice the prescribed hit dice worth of animals (24 rather than 12), and a ranger is able to influence 18 hit dice worth of animals.'
),
Ring( name = 'Anything Ring',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This ring will initially appear to be a standard <i>ring of warmth</i>. However, the wearer may command three other functions from the ring, choosing from among the other standard sorts of magical rings. The period of such functioning will be one operation in the case of a ring which has such a function type (<i>djinni summoning</i>, <i>wishes</i>, etc.). Otherwise the effect will last for 1 day (24 hours). Any ring function so commanded will never be usable again; for example, the ring cannot be made to give more than one <a href="/spells/wish-magic-user-lvl-9">wish</a>. After three singular uses of this sort, the ring will turn into a non-magical piece of jewelry worth from 100 to 600 gp.'
),
Ring( name = 'Ring of Blinking',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'When the wearer of this ring issues the proper verbal command, the dweomer of the item activates, and he or she is then affected exactly as if a <a href="/spells/blink-magic-user-lvl-3"><i>blink</i></a> spell were operating upon his or her person. The effect always lasts for 6 rounds. The ring then ceases to function for 6 turns (1 hour) while it replenishes itself. The command word is usually engraved somewhere on the ring. The ring will activate whenever this word is spoken, even though the command might be given by someone other than the wearer, provided that the word is spoken within 10 feet of the ring.'
),
Ring( name = 'Ring of Boccob',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This ornate piece of jewelry initially appears to be a valuable but non-magical ring. Even magical <i>detection</i> of the most powerful sort will not reveal the dweomer of the item. The function of the ring comes into play whenever the wearer is assailed by some magical device which actually contacts his or her person - the magical device will malfunction, failing to affect its intended target, and if it does not save versus the power of the ring, it will furthermore be turned into a non-magical item. Whenever the ring cancels the power of an item in this fashion, it will cease to function for 1-4 hours thereafter. After this period of quiescence, it will operate normally again. Note that single-use magic items, such as a magic arrow or crossbow bolt or a <i>javelin of lightning</i>, will not have their function cancelled by the ring, but will merely give the wearer protection from their magical effects. This immunity from magical effect does not prevent normal damage from being administered by such an item. Saving throws for items against the cancellation power of the ring are as follows:\n\n'
        '1: Automatic failure for any item\n'
        '2: Saving throw for relics\n'
        '3: Saving throw for artifacts\n'
        '4: Saving throw for hand-held weapons\n'
        '5: Saving throw for rods and staves\n'
        '6: Saving throw for all other items\n'
        '7-20: Any item saves on a roll in this range'
    )
),
Ring( name = 'Ring of Chameleon Power',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'Whenever the wearer of this ring desires, he or she is able to magically blend in with the surroundings. This enables 90% invisibility in foliage, against walls, and so forth. If the wearer is associating with creatures with intelligence of 4 or greater at a distance of 6" or less, the dweomer of the ring enables the wearer to seem to be one of those creatures, but each turn of such association carries a 5% cumulative chance that the creatures will detect the ring wearer for what he or she actually is. Thus, such an association can never persist for more than 20 turns without the wearer being detected, because at the end of that time the chance of detection has risen to 100%. In addition, creatures with 16 or greater intelligence use their intelligence score as an addition to the base chance of detection - i.e., 21% at the end of turn 1, 26% at the end of turn 2, and so forth, if a creature of 16 intelligence is involved. Creatures with 3 or lower intelligence will instinctively and automatically detect the wearer if they come within a 1" radius of him or her.'
),
Ring( name = 'Ring of Clumsiness',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This cursed ring typically radiates another dweomer to disguise its baneful nature. The possible secondary powers are:\n'
        '01-10: <i>Free action</i>\n'
        '11-20: <i>Feather falling</i>\n'
        '21-35: <i>Invisibility</i>\n'
        '36-50: <i>Jumping</i>\n'
        '51-60: <i>Swimming</i>\n'
        '61-80: <i>Warmth</i>\n'
        '81-00: <i>Water walking</i>\n\n'
        'The secondary power works normally, except when the wearer is under stress - combat, stealth, delicate activity - at which time the <i>clumsiness</i> dweomer takes effect. Dexterity is lowered to half normal, rounded down. Chances for stealth and precise actions are also lowered by one-half, rounded down. Any attempt at spell casting that requires the handling of a material component or the accomplishment of a somatic component will only succeed if the wearer makes a saving throw versus spell; otherwise, the spell is botched and annuled. The ring can only be taken off by a successfully cast <a href="/spells/dispel-magic-magic-user-lvl-3"><i>dispel magic</i></a> spell (vs. 12th-level magic). Success destroys both the primary and secondary dweomer of the ring.'
    )
),
Ring( name = 'Ring of Faerie',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This specially dweomered ring is given by the gray elves to their closest associates and allies only. Each ring is aligned either toward evil (5%), good (75%), or neutrality (20%). It enables the wearer to perform certain functions as if he or she were an <a href="/creatures/elf">elf</a>:\n\n'
        '<i>Concealment in woodlands</i> is such that the wearer can be detected only by those creatures able to detect invisible objects.\n\n'
        'If alone and not in metal armor, the wearer can <i>move silently</i> with a 66.6% chance of success, enabling him or her to achieve surprise on a roll of 1-4 on a d6. An attempt to <i>move silently</i> will succeed on a roll of 01-67; if the number rolled is 68 or higher, then noise generated by the wearer\'s movement will be discernible up to that number of feet away from the individual.\n\n'
        '<i>Infravision</i> to a range of 60 feet is bestowed by the ring.\n\n'
        '<i>Concealed doors</i> are noted 16.6% of the time (roll of 1 on d6) when going past them, 50% of the time when actively searched for.\n\n'
        '<i>Secret doors</i> are found 33.3% of the time (1-2 on d6) when actively searched for.\n\n'
        'Rings of alignment not corresponding to that of the wearer will not function.'
    )
),
Ring( name = 'Ring of Jumping',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'In a single segment the wearer of this ring is able to call forth its power so as to be able to leap 30 feet ahead, or 10 feet backwards or straight up, with an arc of about 2 feet for every 10 feet traveled (cf. 1st-level magic-user spell, <a href="/spells/jump-magic-user-lvl-1"><i>jump</i></a>). The wearer must use the ring\'s power carefully, for it can perform only four times per day.'
),
Ring( name = 'Ring of Mind Shielding',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This form of magic ring is usually of fine workmanship and wrought from heavy gold. The wearer is so shielded as to be completely immune to <a href="/spells/esp-magic-user-lvl-2"><i>ESP</i></a>, <a href="/spells/detect-lie-cleric-lvl-4"><i>detect lie</i></a>, <a href="/spells/know-alignment-cleric-lvl-2"><i>know alignment</i></a>, and telepathic reading of the mind. If the wearer is also possessed of psionic power, he or she has the benefit of a <i>thought shield</i> defense at no point cost, all all psionic attack damage suffered by the wearer is at -2 points while the ring is worn. Furthermore, the wearer is more capable of dealing with a <i>psionic blast</i> attack, gaining +1 on saving throws versus such attacks if the wearer is not psionically endowed, or -3 on damage if the wearer does possess psionics.'
),
Ring( name = 'Ring of the Ram',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This ornate ring can be of any hard metal, usually a silver alloy or iron. It has the head of a ram (or possibly a buck goat) as its device. When magic is detected for, it will reveal an <i>evocation</i> dweomer upon the ring. The wearer is able to cause the ring to give forth a ram-like force, manifested by a vaguely discernible shape which resembles the head of a ram (or goat). This force strikes one target for 1-6 points of damage if 1 charge is expended, 2-12 points if 2 charges are used, or 3-18 points if 3 charges (the maximum) are used. The ring is quite useful, for instance, for knocking opponents off of walls or ladders, or over ledges; the force of the blow is considerable, and if a victim fails to save versus spell, it is knocked free - or down. The range of this power is 3". The target of the blow must take any applicable adjustments to its saving throw from the following list:\n\n'
        'Smaller than man-sized: -1\n'
        'Larger than man-sized: +2\n\n'
        'Strength under 12: -1\n'
        'Strength of 18-20: +3\n'
        'Strength over 20: +6\n\n'
        '4 or more legs: +4\n\n'
        'Over 1,000 lbs. weight: +2\n\n'
        '2 charges expended: -1\n'
        '3 charges expended -2\n\n'
        'The DM should note that circumstantial adjustments must be made according to need. For instance, a <a href="/creatures/fire-giant">fire giant</a> balanced on a narrow ledge should <i>not</i> gain any benefit from strength and weight unless he knows that he is about to be struck by the force of the ring. This is also a case where common sense will serve best.\n\n'
        'In addition to its attack mode, the <i>ring of the ram</i> also has the power to open doors as if a person of 18/00 strength were doing so. If 2 charges are expended, the effect is as for a character of 19 strength, and if 3 charges are expended, the effect is as if a 20 strength were used. Magically held or locked portals can be opened in this manner. Structural damage from the ramlike force is identical to an actual battering ram (see Dungeon Masters Guide) if the ring is used in this mode, with double or triple damage accruing for applications of 2 or 3 charges. Magic items struck by the ramlike force must save versus <i>crushing blow</i> if 3 charges are used; otherwise the force will not affect them. Other (non-magical) items which are the target of the force will always have to save versus <i>crushing blow</i> from the impact.\n\n'
        'A ring of this sort will have from 6-60 charges when discovered. It can be recharged by a magic-user employing <a href="/spells/enchant-an-item-magic-user-lvl-6"><i>enchant an item</i></a> and <a href="/spells/bigbys-clenched-fist-magic-user-lvl-8"><i>Bigby\'s Clenched Fist</i></a> in combination. The orginal ring of this sort was created by the renowned magic-user Lythargyrhum.'
    )
),
Ring( name = 'Ring of Shocking Grasp',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This ordinary-seeming ring will radiate only a faint, unidentifiable aura of magic when examined, but it contains a strong dweomer when used to inflict damage upon an opponent. If the wearer attacks an enemy, attempting to touch that individual with the hand upon which the ring is worn, a successful "to hit" roll indicates that the touch has taken place, and from 7-14 points of damge (d8 +6) are delivered to the target creature. After three discharges of this nature, regardless of the time elapsed betweeen them, the ring will be inert for 1 turn. It is of note that when actually functioning, this ring causes a circular, charged extrusion to appear on the palm of the wearer\'s hand.'
),
Ring( name = 'Ring of Sustenance',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This magical ring provides its wearer with life-sustaining nourishment even though he or she might go for days without food or drink. The ring also refreshes the body and mind, so that its wearer needs to sleep only two hours per day to gain the benefit of eight hours of sleep. The ring must be worn for a full week in order to function properly, and if it is removed it immediately loses its benefits and must again be worn for a week to reattune itself to the wearer. After functioning (in either or both capacities) for any period of seven consecutive days, a <i>ring of sustenance</i> will cease to function for a week while it replenishes its dweomer.'
),
Ring( name = 'Ring of Truth',
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'There is little doubt that wearing a ring of this nature is a mixed blessing. While any lie told to the wearer is detectable as such by him or her, by the same token he or she is unable to tell any sort of falsehood. Any attempt to lie results in speaking the literal truth, but in turn the wearer is able to discern the last prevarication on the part of another. In fact, the voice of the liar rises to a falsetto due to the power of the ring. If the wearer of the ring encounters some magic which enables falsehoods to otherwise be spoken without detection (such as someone under the effects of an <a href="/spells/detect-lie-cleric-lvl-4"><i>undetectable lie</i></a> spell or a <i>philter of glibness</i>, no lie is noticed, but the ring wearer will not hear the voice of the person so dweomered, whether or not he or she is trying to listen.'
)
]

rods = [
MagicItem( name = 'Rod of Absorption',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This rod acts as a magnet and draws magic spells of any nature (cleric, druid, magic-user, or illusionist) into itself, nullifying their effects but storing their <i>potential</i> within until the wielder chooses to release this energy in the form of spells of his or her own casting. The magic absorbed must have been directed at the character possessing the rod. (Cf. <i>ring of spell turning</i>). The wielder can instantly detect the spell level and decide on whether to react or not when the rod absorbs it. The wielder can use the energy to cast any spell he or she has memorized, in but 1 segment, without loss of spell memory, as long as the spell so cast is of equal or lesser level than the one absorbed. Excess levels are stored as potential, and can be cast in like manner (in 1 segment with no spell memory loss) as any level spell so long as the wielder knows the spell and has it memorized.\n\n'
        'The <i>rod of absorbption</i> can never be recharged. It absorbs 50 spell levels and can thereafter only discharge any remaining potential it might have within. The wielder will know this upon grasping the item. If it has charges used, this indicates that it has already absorbed that many spell levels and they have been used.\n\n'
        'Example: a cleric has a <i>rod of absorption</i> and uses it to nullify the effect of a <a href="/spells/hold-person-magic-user-lvl-3"><i>hold person</i></a> spell cast at him by a magic-user. The rod has now absorbed 3 spell levels, can absorb 47 more, and the cleric can, in 1 segment, cast any first, second, or third level spell he or she has memorized, <i>without</i> memory loss of that spell, by using the stored potential of the rod. Assume the cleric casts a <a href="/spells/hold-person-cleric-lvl-2"><i>hold person</i></a> back. This spell is only second level to him or her, so the rod then holds 1 spell level of potential, and can absorb 47 more still, with 2 charges permanently disposed of.'
    )
),
MagicItem( name = 'Rod of Beguiling',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This rod enables its possessor to radiate an emotional and mental wave of fellow-feeling to all creatures with any intelligence whatsoever (1 or higher intelligence). The effect is to cause all such creatures within a 2" radius of the device to be virtually charmed by the individual and beguiled into regarding him or her as their comrade, friend, and/or mentor (no saving throw). The beguiled creatures will love and respect the rod wielder. They will trustingly listen and obey insofar as communication is possible, and the instruction seems plausible and does not outwardly consign the beguiled to needless injury or destruction or go against their nature or alignment. Each charge of the rod beguiles for 1 turn. It can be recharged.'
),
MagicItem( name = 'Rod of Cancellation',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This dreaded rod is a bane to all classes, for its touch will drain any item of <i>all</i> magical properties unless a saving throw versus the cancellation is made. Contact is made by scoring a normal "to hit" score in melee combat.\n\n'
        '<table>'
        '<tr><th>Saving Throw</th><th>Item</th></tr>'
        '<tr><td>20</td><td>potion</td></tr>'
        '<tr><td>19</td><td>scroll</td></tr>'
        '<tr><td>17</td><td>ring</td></tr>'
        '<tr><td>14</td><td>rod</td></tr>'
        '<tr><td>13</td><td>staff</td></tr>'
        '<tr><td>15</td><td>wand</td></tr>'
        '<tr><td>12</td><td>miscellaneous magic item</td></tr>'
        '<tr><td>3</td><td>artifact or relic</td></tr>'
        '<tr><td>11(8)</td><td>armor or shield (if +5)</td></tr>'
        '<tr><td>9(7)</td><td>sword (holy sword)</td></tr>'
        '<tr><td>10</td><td>miscellaneous weapon*</td></tr>'
        '</table>\n\n'
        '* Several small items, such as magic arrows or bolts, together in one container will be drained simultaneously.\n\n'
        'If the score indicated, or higher, is not rolled (d20), the item is drained. Upon the item\'s draining, the rod itself becomes brittle and is no longer potent. Drained items are not restorable, even by <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>.'
    )
),
MagicItem( name = 'Rod of Lordly Might',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This rod has functions which are spell-like as well as uses as a magic weapon of different sorts. It also has several more mundane workings. The <i>rod of lordly might</i> is metal, thicker than other rods, with a flanged ball at one end and various studs along its length. It weighs 10 pounds, thus requiring 16 or greater strength to wield properly (-1 on "to hit" rolls for each point of strength below 16).\n\n'
        'The spell-like functions of the rod are:\n\n'
        '1. <i>Paralyzation</i> upon touch if the wielder so commands\n\n'
        '2. <i>Fear</i> upon all enemies viewing it if the wielder so desires (6" maximum range)\n\n'
        '3. <i>Drain</i> 2-8 hit points from the opponent touched and bestow them upon the rod wielder (up to the rod wielder\'s normal maximum; cf. <i>ring of regeneration</i>)\n\n'
        'Each such function draws off 1 charge from the rod. The functions entitle victims to saving throws versus magic, with the exception of function 3 above which requires a successful "hit" during melee combat.\n\n'
        'The weapon uses of the rod are:\n\n'
        '1. +2 mace as is\n\n'
        '2. +1 <i>sword of flame</i> when button #1 is pushed - a blade spring forth from the ball, which becomes the hilt, while the handle shortens the weapon to an overall length of 3\'\n\n'
        '3. +4 battle axe when button #2 is pushed - blade springs forth at the ball, and the whole lengthens to a 4\' length\n\n'
        '4. +3 spear when button #3 is pushed - the sword blade springs forth, and the handle can be lengthened up to 12\', for an overall length of from 6\' minimum to 15\' maximum (the latter length highly suitable for lance employment)\n\n'
        'These functions do not use charges.\n\n'
        'The mundane uses of the rod are:\n\n'
        '1. Climbing pole - when button #4 is pushed a spike which can anchor in granite is extruded from the butt, while the tip sprouts 3 sharp hooks; the rod lengthens 5\' per segment until button #4 is pushed again or until 50\' is reached. In either case, horizontal bars of 3 inch length then fold out from the sides, 1\' apart, in staggered progression. The rod is firmly held by spike and hooks and will bear up to 4,000 pounds (40,000 g.p. equivalent) weight. It retracts by pushing button #5.\n\n'
        '2. The same function will force open doors if the rod\'s base is planted 30\' or less from the portal to be forced and is in line with it. The force exerted is equal to <a href="/creatures/storm-giant">storm giant</a> strength.\n\n'
        '3. When button #6 is pushed the rod will indicate magnetic north and give the possessor a knowledge of approximate depth beneath the surface (or height above it) he or she is.\n\n'
        'These functions do not use charges either.\n\n'
        'The <i>rod of lordly might</i> cannot be recharged. When its charges are exhausted, all spell-like functions cease as do weapon functions 2 and 3, but the rod continues to work in all other ways.'
    )
),
MagicItem( name = 'Rod of Resurrection',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This rod enables the cleric to resurrect the dead - even <a href="/creatures/elf">elven</a>, <a href="/creatures/dwarf">dwarven</a>, <a href="/creatures/gnome">gnome</a>, or <a href="/creatures/halfling">halfling</a> - as if he or she were of high enough level to cast <a href="/spells/resurrection-cleric-lvl-7">the spell</a>, and no rest will be required as the rod bestows lifegiving effects. The rod can be used once per day. The number of charges used to resurrect a character depends on class and race:\n\n'
        '<table>'
        '<tr><th>Class</th><th>Charges</th></tr>'
        '<tr><td>Cleric</td><td>1</td></tr>'
        '<tr><td>Druid</td><td>2</td></tr>'
        '<tr><td>Fighter</td><td>2</td></tr>'
        '<tr><td>Paladin</td><td>1</td></tr>'
        '<tr><td>Ranger</td><td>2</td></tr>'
        '<tr><td>Magic-User</td><td>3</td></tr>'
        '<tr><td>Illusionist</td><td>3</td></tr>'
        '<tr><td>Thief</td><td>3</td></tr>'
        '<tr><td>Assassin</td><td>4</td></tr>'
        '<tr><td>Monk</td><td>3</td></tr>'
        '<tr><td>Bard</td><td>2</td></tr>'
        '</table>\n\n'
        'Add the class charge to the race charge.\n\n'
        '<table>'
        '<tr><th>Race</th><th>Charges</th></tr>'
        '<tr><td>Dwarf</td><td>3</td></tr>'
        '<tr><td>Elf</td><td>4</td></tr>'
        '<tr><td>Gnome</td><td>3</td></tr>'
        '<tr><td>Half-elf</td><td>2</td></tr>'
        '<tr><td>Halfling</td><td>2</td></tr>'
        '<tr><td>Half-orc</td><td>4</td></tr>'
        '<tr><td>Human</td><td>1</td></tr>'
        '</table>\n\n'
        'Multi-classed characters use the least favorable category. The rod cannot be recharged.'
    )
),
MagicItem( name = 'Rod of Rulership',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The individual who possesses this magic rod is able to exercise rulership (command the obedience and fealty) or creatures within 12" when he or she activates the device. From 200 to 500 hit dice (or levels of experience) can be ruled, but creatures with 15 or greater intelligence and 12 or more hit dice/levels are entitled to a saving throw versus magic. Ruled creatures will obey the wielder of the <i>rod of rulership</i> as if he or she were their absolute suzerain, but if some command given is absolutely contrary to the nature of the commanded, the magic will be broken. The rod takes 5 segments to activate. Each charge lasts for 1 turn. The rod cannot be recharged.'
),
MagicItem( name = 'Rod of Smiting',
    category = MagicItemCategory.ROD,
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This rod is a +3 magic weapon which inflicts 4-11 (d8 +3) hit points of damage. Against golems the rod does 8-22 (2d8 +6) hit points of damage, any score of 20 or better completely destroys the monster, but any hit upon a golem drains 1 charge. The rod does normal damage (4-11) versus creatures of the <i>outer planes</i> such as demons, devils, and <a href="/creatures/night-hag">night hags</a>. Any score of 20 or better draws off 1 charge and causes triple damage: (d8 +3)x3. The rod cannot be recharged.'
),
MagicItem( name = 'Rod of Alertness',
    category = MagicItemCategory.ROD,
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This magical rod is indistinguishable from a <i>footman\'s mace +1</i>. However, upon usage, its true powers will reveal themselves. The rod bestows +1 to the possessor\'s die rolls for being surprised, and in combat the possessor gains +1 on initiative die rolls. If it is grasped firmly, the rod will enable the concentrating character to <a href="/spells/know-alignment-cleric-lvl-2"><i>detect alignment</i></a>, <a href="/spells/detect-evil-cleric-lvl-1"><i>evil</i>, <i>good</i>, <a href="/spells/detect-illusion-magic-user-lvl-3"><i>illusion</i></a>, <a href="/spells/detect-invisibility-magic-user-lvl-2"><i>invisibility</i></a>, <a href="/spells/detect-lie-cleric-lvl-4"><i>lie</i></a>, or <a href="/spells/detect-magic-cleric-lvl-1"><i>magic</i></a>. The use of any of these <i>detect</i> powers does not expend any of the charges in the rod.\n\n'
        'If the <i>rod of alertness</i> is planted in the ground, and the possessor wills it to alertness, the rod will then "sense" any creature within a 12" radius, provided that the creature has intent to harm the possessor. Each of the eight flanges of the macelike head of the rod will then cast a <a href="/spells/light-magic-user-lvl-1"><i>light</i></a> spell along one of the cardinal directions (N, NE, E, etc.) at 6" range, and at the same time the rod will create the effect of a <a href="/spells/prayer-cleric-lvl-3"><i>prayer</i></a> spell upon all friendly (to the possessor) creatures in a 2" radius. Immediately thereafter, the rod will send forth a mental alert to these same friendly creatures, warning them of possible danger from the unfriendly creature(s) within the 12" radius. Lastly, the rod can be used to simulate the casting of an <a href="/spells/animate-object-cleric-lvl-6"><i>animate object</i></a> spell, utilizing any 16 (or fewer) objects specially designated by the possessor and placed roughly around the perimeter of a 6"-radius circle centered on the rod - 16 selected shrubs, 16 specially shaped branches, or the like. Functions excluding the <i>animate object</i> dweomer require 1 charge, and the animation also requires 1 charge, so if all of the rod\'s protective devices are utilized at once, 2 charges are expended. The rod can be recharged by a cleric of 16th or higher level, so long as at least 1 charge remains in the rod when the recharging is attempted.'
    )
),
MagicItem( name = 'Rod of Flailing',
    category = MagicItemCategory.ROD,
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This magical weapon radiates a faint dweomer of the <i>alteration</i> sort when magic is detected for. Upon the command of its possessor, the weapon activates, changing from a normal-seeming rod to a double-headed flail. In close-quarters, or if the wielder is mounted, it is the small, horseman\'s weapon; otherwise, it is a footman\'s weapon, i.e. base damage done is 2-5/2-5 (S-M/L) or 2-7/2-8 (S-M/L). The rod has special features beyond this: In either form, the weapon is +3 for hitting and damage. Better still, each of the weapon\'s two heads is checked for when the possessor attacks, so double hits can be scored, either on a single opponent or on two opponents who are man-sized or smaller and standing side by side. If the holder of the rod expends 1 charge, that character gains +4 on protection and +4 on saving throws for 1 turn. The rod need not be in weapon-form for this protection benefit to be employed, and transforming it into a weapon (or back into a rod) does not expend any charges.'
),
MagicItem( name = 'Rod of Passage',
    category = MagicItemCategory.ROD,
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This highly dweomered item allows its wielder to perform any of the following, one at a time, one per round: <a href="/spells/astral-spell-cleric-lvl-7"><i>astral travel</i></a>, <a href="/spells/dimension-door-magic-user-lvl-4"><i>dimension door</i></a>, <a href="/spells/passwall-magic-user-lvl-5"><i>passwall</i></a>, <a href="/spells/phase-door-magic-user-lvl-7"><i>phase door</i></a>, and <a href="/spells/teleport-without-error-magic-user-lvl-7"><i>teleport without error</i></a>. It is necessary to expend 1 charge to activate the rod, but once it is activated the possessor can perform each of the listed functions one time. The rod remains charged for 1 day, or until each of the five functions is used. None of the functions can be used a second time unless another charge is expended, whereupon all five of the functions again become available. With respect to <i>astral travel</i>, the wielder can elect to use the rod on as many as five creatures (including the wielder) desirous of becoming astral and traveling thus; however, any other remaining functions of the rod are cancelled by this action. The rod travels into the Astral Plane along with the affected creatures (of which the wielder must be one), and cannot be used ir reactivated until it is returned from the Astral Plane. This five-in-one effect will not work with respect to the rod\'s other powers - <i>passwall</i>, for instance; only <i>astral travel</i> can be used more than once per activation, and only in the manner described above. The rod exudes a magical aura of the <i>alteration-evocation</i>sort. Because the physical bodies of the travelers, and their possessions, are actually empowered to become astral, the recharging of the rod requires a magic-user of 20th or higher level.'
),
MagicItem( name = 'Rod of Security',
    category = MagicItemCategory.ROD,
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'Each time a charge is expended, this item creates a non-dimensional space, a "pocket paradise", where the rod\'s possessor and as many as 199 other creatures are able to stay in complete safety and security for a period of time, the maximum being 200 days divided by the number of creatures affected. Thus, one creature (the rod\'s possessor) can stay for 200 days; four creatures can stay for 50 days; a group of 60 creatures can stay for 3 days. (All fractions are rounded down, so that a group numbering between 101 and 200 inclusive can stay for one day only.) While the recipients of the rod\'s power are within this "paradise", they do not age (except from magical causes such as the casting of a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spell), and natural healing and curing takes place at twice the normal rate. Fresh water and food (fruits and vegetables only) are in abundance; the climate is comfortable for all creatures involved, so that protection from elements is not necessary. Activation of the rod simply causes the wielder and as many creatures as were touched with the item to be removed from the place where they are and transported instantaneously to the paradise. (Members of large groups can hold hands or otherwise touch each other, and thus all be "touched" by the rod at one time. When the dweomer is cancelled or expires, all of the affected creatures instantly reappear in the location they occupied when the rod was activated. If something else occupies the space that a traveller would be returning to, then his or her body is displaced a sufficient distance to provide the space required for "re-entry". The rod can be recharged by the joint efforts of a cleric of 16th or higher level and a magic-user of 18th or higher level.'
),
MagicItem( name = 'Rod of Splendor',
    category = MagicItemCategory.ROD,
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('The possessor of this rod is automatically and continually bestowed with a charisma of 18 for as long as the item is held or carried, and whatever garments the possessor wears (including armor) will appear to be of finest quality and condition, although no special magical benefit (such as change in armor class) is enjoyed. If the possessor already has a charisma score of 18 or greater, the rod does not further enhance this attribute. When the possessor expends 1 charge, the rod actually creates and garbs him or her in clothing of noble sort - the finest fabrics, plus adornments of furs and jewels. This apparel is actually created by the magic of the rod, and remains permanently in existence unless the possessor attempts to sell any part of it, or if any garb is forcibly taken from him or her. In either of those cases, all of the apparel immediately disappears. The garments may be freely given to other characters or creatures, however, and will remain whole and sound afterward. If the possessor is bedecked in one of these magically created outfits, the garb cannot be replaced or added to by expenditure of another charge; in such a case, the charge is simply wasted. The value of any noble garb created by the wand wil be from 7,000 to 10,000 gp (d4 +6). The fabric will be worth 1,000 gp, furs 5,000 gp, and jewel trim from 1,000 to 4,000 gp, i.e. 10 gems of 100 gp value each, 10 gems of 200 gp value each, or 20 gems of 100 gp value, and so forth.\n\n'
        'The second power of the rod, also requiring 1 charge to bring about, is the creation of a palatial tent - a huge pavilion of silk encompassing between 1,500 and 3,000 square feet. Inside the tent will be temporary furnishings and foodstuffs suitable to the splendor of the pavilion and in sufficient supply to entertain as many as 100 persons. The tent and its trappings will last for one day, at the end of which time the pavilion may be maintained by expending another charge; otherwise, the tent and all objects associated with it (including any items that were taken out of the tent) will disappear. This rod cannot be recharged.'
    )
)
]
