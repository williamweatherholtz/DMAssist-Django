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
    def __init__(self, name, category, source, desc,
        activation_time=None,
        xp_value = [0,0],
        gold_value = [0,0]
    ):
        self.name = name
        self.category = category
        self.xp_value = xp_value
        self.gold_value = gold_value
        self.activation_time = activation_time
        self.source = source
        self.desc = desc

potions = [
MagicItem(name = 'Potion of Animal Control',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [400,400],
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
MagicItem(name = 'Potion of Clairaudience',
    xp_value = [250,250],
    gold_value = [400,400],
    category = MagicItemCategory.POTION,
    desc = 'This potion empowers the creature drinking it to hear as the third level magic-user <a href="/spells/clairaudience-magic-user-lvl-3">spell</a> of the same name. It can be used, however, to <i>clairaudit</i> unknown areas within 3". Its effects last for 2 turns only.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Clairvoyance',
    category = MagicItemCategory.POTION,
    xp_value = [300,300],
    gold_value = [500,500],
    desc = 'This potion empowers the individual to see as the third level magic-user spell, <a href="/spells/clairvoyance-magic-user-lvl-3"><i>clairvoyance</i></a>. It differs from the spell in that unknown areas up to 3" distant can be seen. Its effects last for 1 turn only.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Climbing',
    category = MagicItemCategory.POTION,
    xp_value = [300,300],
    gold_value = [500,500],
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
MagicItem(name = 'Potion of Delusion',
    category = MagicItemCategory.POTION,
    xp_value = [0,0],
    gold_value = [150,150],
    desc = 'This potion affects the mind of the character so that he or she believes the liquid is some other potion (<i>healing</i>, for example, is a good choice - damage is "restored" by drinking it, and only death or rest after an adventure will reveal that the potion only caused the imbiber to believe that he or she was aided). If several individuals taste this potion, it is still 90% probable that they will all agree it is the same potion (or whatever type the DM announces or hints at).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Diminution',
    category = MagicItemCategory.POTION,
    xp_value = [300,300],
    gold_value = [500,500],
    desc = 'When this potion is quaffed, the individual, and all he or she carries and wears, will diminish in size to as small as 5% of normal size. If half of the contents are swallowed, the person shrinks to 50% of normal size. The effects of this potion last for 6 turns plus 2-5 turns (d4 + 1).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Dragon Control',
    category = MagicItemCategory.POTION,
    xp_value = [500,1000],
    gold_value = [5000,9000],
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
MagicItem(name = 'Potion of ESP',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [850,850],
    desc = 'The <i>ESP</i> potion bestows an ability which is the same as the second level <a href="/spells/esp-magic-user-lvl-2">magic-user spell</a> of the same name, except that its effects last for 5-40 (5d8) rounds, i.e. 5 to 40 minutes.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Extra-Healing',
    category = MagicItemCategory.POTION,
    xp_value = [400,400],
    gold_value = [800,800],
    desc = 'This potion restores 6-27 (3d8 + 3) hit points of damage when wholly consumed, or 1-8 hit points of damage for each one-third potion.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Fire Resistance',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [400,400],
    desc = 'This potion bestows magical invulnerability to all forms of normal fire (such as bonfires, burning oil, or even huge pyres of flaming wood) upon the person drinking it. It furthermore gives resistance to such fires as generated by molten lava, a <a href="/spells/wall-of-fire-druid-lvl-5/"><i>wall of fire</i></a>, a <a href="/spells/fireball-magic-user-lvl-3/"><i>fireball</i></a>, fiery dragon breath and similar intense flame/heat. All damage from such fires is reduced by -2 from each die of damage, and if a saving throw is applicable, it is made at +4. Note: If but one-half of the potion is consumed it confers invulnerability to normal fires and half the benefits noted above (-1, +2). The potion lasts 1 turn, or 5 rounds for half doses.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Flying',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [750,750],
    desc = 'A flying potion enables the individual drinking it to fly in the same manner as the third level magic-user spell, <a href="/spells/fly-magic-user-lvl-3"><i>fly</i></a>.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Gaseous Form',
    category = MagicItemCategory.POTION,
    xp_value = [300,300],
    gold_value = [400,400],
    desc = 'By imbibing this magical liquid, the individual causes his or her body, as well as what it carries and wears, to become gaseous in form and able to flow accordingly at a base speed of 3"/round. (A <a href="/spells/gust-of-wind-magic-user-lvl-3/"><i>gust of wind</i></a> spell, or even normal strong air currents, will blow the gaseous form backwards at air speed.) The gaseous form is transparent and insubstantial. It wavers and shifts. It cannot be harmed except by magical fires or lightnings, in which case damage is normal. A whirlwind will inflict double damage upon any creature in <i>gaseous form</i>. When in such condition the individual is able to enter any space which is not airtight, i.e., a small crack or hole which allows air to penetrate also allows entry by a creature in gaseous form. The entire potion must be consumed to achieve this result, and the effects last the entire duration.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Giant Control',
    category = MagicItemCategory.POTION,
    xp_value = [400,900],
    gold_value = [1000,6000],
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
MagicItem(name = 'Potion of Giant Strength',
    category = MagicItemCategory.POTION,
    xp_value = [500,750],
    gold_value = [900,1400],
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
MagicItem(name = 'Potion of Growth',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [300,300],
    desc = 'This potion causes the person consuming it to enlarge in both height and weight, his or her garments and other worn and carried gear likewise growing in size. Strength is increased sufficiently to allow bearing normal armor and weapons, but does not add to combat. Movement increases to that of a giant of approximately equal size. Each quarter of the potion consumed causes 6\' height growth, i.e. a full potion increases height by 24\'.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Healing',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [400,400],
    desc = 'An entire potion must be consumed in a single drinking (round) in order for this liquor to restore 4-10 (2d4 + 2) hit points of damage. (Cf. <i>extra-healing</i>.)',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Heroism',
    category = MagicItemCategory.POTION,
    xp_value = [300,300],
    gold_value = [500,500],
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
MagicItem(name = 'Potion of Human Control',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [900,900],
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
MagicItem(name = 'Potion of Invisibility',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [500,500],
    desc = 'When this potion is consumed it confers <i>invisibility</i> similar to the <a href="/spells/invisibility-magic-user-lvl-2/">spell</a> of the same name. As actions involving combat cause termination of the non-visible state, the individual possessing the potion can quaff a single gulp - equal to 1/8 the contents of the container - to bestow <i>invisibility</i> for 3-6 turns.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Invulnerability',
    category = MagicItemCategory.POTION,
    xp_value = [350,350],
    gold_value = [500,500],
    desc = 'This potion confers immunity to non-magical weapons and attacks from creatures with no magical properties (see <b>CREATURES STRUCK ONLY BY MAGICAL WEAPONS</b> in the Dungeon Master\'s Guide) or with fewer than 4 hit dice. Thus, an 8th level character without a magical weapon could not harm the imbiber of an <i>invulnerability</i> potion. It further improves armor class rating by 2 classes and gives a bonus of +2 to the individual on his or her saving throws versus all forms of attack. Its effects are realized only when the entire potion is consumed, and they last for 5-20 rounds. Only fighters can use this potion.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Levitation',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [400,400],
    desc = 'A <i>levitation</i> potion enables the consumer to <i>levitate</i> in much the same manner as the second level <a href="/spells/levitate-magic-user-lvl-2">magic-user spell</a> of the same name. The potion allows levitation of the individual only, subject to a maximum weight of 6,000 g.p. equivalent, so it is possible that the individual drinking the potion could carry another person.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Longevity',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [1000,1000],
    desc = 'The <i>longevity</i> potion reduces the character\'s game age by from 1-12 years when it is imbibed, but each time one is drunk there is a 1% cumulative chance that it will have the effect of reversing all age removal from previously consumed <i>longevity</i> potions. The potion otherwise restores youth and vigor. It is also useful to counter magical or monster-based aging attacks. The entire potion must be consumed to achieve the results.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Oil of Etherealness',
    category = MagicItemCategory.POTION,
    xp_value = [600,600],
    gold_value = [1500,1500],
    desc = 'This potion is actually a light oil which is applied externally to the dress and exposed flesh. It then confers <i>etherealness</i>. In the ethereal state the individual can pass through solid objects - sideways, upwards, downwards - or to different <i>planes</i>. Naturally, the individual cannot touch non-ethereal objects. The oil takes effect 3 rounds after application and it lasts for 4 + 1-4 turns unless removed with a weak acidic solution prior to the expiration of its normal effective duration. It can be applied to objects as well as creatures; one potion is sufficient to anoint a normal human and such gear as he or she typically carries (2 or 3 weapons, garments, armor, shield, and the usual miscellaneous gear carried). Ethereal individuals are invisible. (Cf. <a href="/spells/phase-door-magic-user-lvl-7"><i>phase door</i></a> spell, and <b>TRAVEL IN THE KNOWN PLANES OF EXISTENCE</b> in the Dungeon Master\'s Guide.)',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Oil of Slipperiness',
    category = MagicItemCategory.POTION,
    xp_value = [400,400],
    gold_value = [750,750],
    desc = 'Similar to the <i>oil of etherealness</i>, this liquid is to be applied externally. This application makes it impossible for the individual to be grabbed or grasped/hugged by any opponent or constricted by snakes or tentacles. (Note that a roper could still inflict weakness, but that the monster\'s tentacles could not entwine the opponent coated with <i>oil of slipperiness</i>.) In addition, such obstructions as webs, magical or otherwise, will not affect an anointed individual; and bonds such as ropes, manacles, and chains can be slipped free. Magical ropes and the like are not effective against this oil. If poured on a floor or on steps there is a 95% chance/round that creatures standing on the surface will slip and fall. The oil lasts 8 hours to wear off normally, or it can be wiped off with an alcohol solution (such as wine).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Philter of Love',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [300,300],
    desc = 'This potion is such as to cause the individual drinking it to become <i>charmed</i> (cf. <a href="/spells/charm-person-magic-user-lvl-1"><i>charm</i></a> spells) with the first creature seen after consuming the draught, or actually become enamored and <i>charmed</i> if the creature is of similar race and of the opposite sex. Charming effects wear off in 4 + 1-4 turns, but the enamoring effects last until a <a href="/spells/dispel-magic-cleric-lvl-3"><i>dispel magic</i></a> spell is cast upon the individual.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Philter of Persuasiveness',
    category = MagicItemCategory.POTION,
    xp_value = [400,400],
    gold_value = [850,850],
    desc = 'When this potion is imbibed the individual becomes more charismatic. Thus, he or she gains a bonus of 25% on reaction dice rolls. The individual is also able to <i>suggest</i> (cf. the magic-user <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a> spell) once per turn to as many creatures as are within a range of 3" of him or her.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Plant Control',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [300,300],
    desc = 'A <i>plant control</i> potion enables the individual who consumed it to influence the behavior or vegetable life forms - including normal plants, fungi, and even molds and <a href="/creatures/shambling-mound">shambling mounds</a> - within the parameters of their normal abilities. The imbiber can cause the vegetable forms to remain still/silent, move, entwine, etc. according to their limits. Vegetable monsters with intelligence of 5 or higher are entitled to a saving throw versus magic. Plants within a 2" x 2" square can be controlled subject to the limitations set forth above, for from 5-20 rounds. Self-destructive control is not directly possible if the plants are intelligent. (Cf. <a href="/spells/charm-plants-magic-user-lvl-7"><i>charm plants</i></a> spell.) Control range is 9".',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Poison',
    category = MagicItemCategory.POTION,
    xp_value = [0,0],
    gold_value = [0,0],
    desc = 'A <i>poison</i> potion is simply a highly toxic liquid in a potion flask. Typically, <i>poison</i> potions are odorless and of any color. Ingestion, introduction of the poison through a break in the skin, or possibly just skin contact, will cause death. Poison can be weak (+4 to +1 on saving throw), average, or deadly (-1 to -4 or more on saving throw). Some poison can be such that a <a href="/spells/neutralize-poison-cleric-lvl-4"><i>neutralize poison</i></a> spell will simply lower the toxicity level by 40% - say from a -4 to a +4 on saving throw potion. You might wish to allow characters to hurl poison flasks (see <b>COMBAT</b> in the Dungeon Master\'s Guide).',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Polymorph Self',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [350,350],
    desc = 'This potion duplicates the effects of the fourth level <a href="/spells/polymorph-self-magic-user-lvl-4">magic-user spell</a> of the same name in most respects.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Speed',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [450,450],
    desc = 'A potion of <i>speed</i> increases movement and combat capabilities of the imbiber by 100%. Thus, a movement rate of 9" becomes 18", and a character normally able to attack but once per round would gain double attacks in a round. Note that this does not reduce spell casting time, however (cf. <a href="/spells/haste-magic-user-lvl-3"><i>haste</i></a> spell). Use of a <i>speed</i> potion ages the individual by 1 year. The other effects last from 5-20 rounds, the aging is permanent.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Super-Heroism',
    category = MagicItemCategory.POTION,
    xp_value = [450,450],
    gold_value = [750,750],
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
MagicItem(name = 'Potion of Sweet Water',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [250,250],
    desc = 'This liquid is not actually a potion to be drunk (though if it is drunk it will taste good), but it is to be added to other liquids in order to change them to pure, drinkable water. It will neutralize poison and ruin magic potions (no saving throw). The contents of the container will change up to 100,000 cubic feet of polluted or salt or alkaline water to fresh water. It will turn up to 1,000 cubic feet of acid into pure water. The effects of the potion are permanent, but subject to later contamination or infusion after an initial period of 5-20 rounds.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Treasure Finding',
    category = MagicItemCategory.POTION,
    xp_value = [600,600],
    gold_value = [2000,2000],
    desc = 'A potion of <i>treasure finding</i> empowers the drinker with a location sense, so that he or she can point to the direction of the nearest mass of treasure. The treasure must be within 24" or less, and its mass must equal metal of at least 10,000 copper pieces or 100 gems or any combination thereof. Note that only valuable metals (copper, silver, electrum, gold, platinum, etc.) and gems (and jewelry, of course) are located; worthless metals or magic without precious metals/gems are not found. The consumer of the potion can "feel" the direction in which treasure lies, but not its distance. Intervening substances other than special magical words or lead-lined walls will not withstand the powers which the liquor bestows upon the individual. The effects of the potion last for from 5-20 rounds. (Clever players will attempt triangulation.)',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem(name = 'Potion of Undead Control',
    category = MagicItemCategory.POTION,
    xp_value = [700,700],
    gold_value = [2500,2500],
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
MagicItem(name = 'Potion of Water Breathing',
    category = MagicItemCategory.POTION,
    xp_value = [400,400],
    gold_value = [900,900],
    desc = 'It is 75% likely that a <i>water breathing</i> potion will contain two doses, 25% probable that there will be four in the container. The elixir allows the character drinking it to breathe normally in liquids which contain oxygen suspended within them. This ability lasts for one full hour per dose of potion quaffed, with an additional 1-10 rounds (minutes) variable. Thus, a character who has consumed a <i>water breathing</i> potion could enter the depths of a river, lake, or even the ocean and not drown while the magical effects of the potion persisted.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),

#UNEARTHED POTIONS
MagicItem( name = 'Elixir of Health',
    category = MagicItemCategory.POTION,
    xp_value = [350,350],
    gold_value = [2000,2000],
    desc = 'This special potion cures blindness, deafness, disease, feeblemindedness, insanity, infection, infestation, poisoning, and rot. It will not heal wounds or restore hit points lost through any of the above causes. Half a flask will cure any one or two of the listed problems. Imbibing the whole potion will cure any and all of the above afflictions that the drinker may be suffering.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Elixir of Life',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [2500,2500],
    desc = 'This potent draught will restore life to any creature, even if at a negative hit point level equal to up to 20% of total hit points. (Thus, it will benefit even a creature at -10 hit points, so long as that creature has a full-strength hit point total of 50 or more.) The power of the elixir will function only if administered internally within 5 rounds of the occurence of death. One turn later, the recipient will be unconscious but at 1 hit point strength. For each negative hit point neutralized in this fashion, the recipient must rest for one day or else receive a <a href="/spells/cure-light-wounds-cleric-lvl-1"><i>cure light wounds</i></a> spell to offset the need for that one day of rest. A <a href="/spells/cure-serious-wounds-cleric-lvl-4"><i>cure serious wounds</i></a> spell will count for two days of rest, a <a href="/spells/cure-critical-wounds-cleric-lvl-5"><i>cure critical wounds</i></a> spell for three, and a <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> spell for seven days. Demi-humans are affected by this elixir.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Elixir of Madness',
    category = MagicItemCategory.POTION,
    desc = 'A single sip of this stuff will cause the imbiber to go mad, as if he or she were affected by a <a href="/spells/symbol-magic-user-lvl-8"><i>symbol</a> of insanity</i>. Once any creature is affected by the elixir, the dweomer from the entire flask instantly disappears, and the remaining draught is merely foul-tasting liquid.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Elixir of Youth',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [10000,10000],
    desc = 'Quaffing this rare and highly dweomered elixir will reverse aging. The entire contents of the flask must be consumed; sipping from it initially will reduce the potency of the liquid. Taking the full-potency dose reduces the imbiber\'s age by 2-5 years, and drinking the lower-potency liquid reduces age by only 1-3 years.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Potion of Fire Breath',
    category = MagicItemCategory.POTION,
    xp_value = [400,400],
    gold_value = [4000,4000],
    desc = 'This magical draught allows the imbiber to retain the dweomer of the fluid for up to six turns before belching forth a tongue of flame. After the expiration of this time limit, however, the potion becomes impotent, and there is a 10% chance that the flames will erupt in the imbiber\'s own system, inflicting double damage upon him or her, with no saving throw allowed. Each potion container holds enough liquid for four small draughts. If a small draught only is quaffed, then the imbiber is able to breathe forth a 1" wide cone of fire up to 2" long which inflicts 3-12 points of damage. If a double draught is taken, range and damage are doubled; and if a triple draught is quaffed, then ranged and damage are tripled. If the entire contents are taken at once, then the width of the breath of flame is 2" and the length is 8", and damage inflicted is 5-50 points. Saving throws versus <i>breath weapon</i> apply, for half damage, in all cases.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Acid Resistance',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [5000,5000],
    desc = 'When this oil is applied to skin, cloth, or any other material, it confers virtual invulnerability to acid. The oil will not wear off quickly; an application lasts for one full day before becoming impotent. However, each time material or flesh is exposed to acid, the potency of the oil is diminished by as many minutes as the acid would have caused points of damage to exposed flesh. Thus, if a <a href="/creatures/black-dragon"><i>black dragon</i></a> of largest size and greatest age breathed upon a person protected by this oil, each breath would lower the oil\'s remaining protection time by 64 minutes, or 32 minutes if a successful saving throw versus <i>breath weapon</i> is made. Each flask contains sufficient oil for one man-sized creature (and accoutrements) for 24 hours. Or, 24 such man-sized creatures could each by coated for one hour\'s time; any combination of number of creatures and duration of potency between these extremes is also possible. (A horse is equivalent to eight man-sized creatures.)',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Disenchantment',
    category = MagicItemCategory.POTION,
    xp_value = [750,750],
    gold_value = [3500,3500],
    desc = 'This special oil allows the removal of all <i>enchantment/charm</i> dweomers placed upon living things. If the contents of a flask of this substance are rubbed on a creature, all enchantments and charms placed upon it are removed. If the oil is rubbed onto objects which bear a dweomer of the <i>enchantment/charm</i> sort, this magic will be lost for 21 to 30 turns (d10 +20); after that time has elapsed, the oil will have lost its potency, and the item will regain its former dweomer. The oil does not radiate any magical qualities once it is applied, and masks the dweomer of whatever it coats, so that an item so coated will not show any dweomer if magic is detected for as long as the oil remains effective.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Elemental Invulnerability',
    category = MagicItemCategory.POTION,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    desc = 'This precious substance has equal chances for being of any of the four basic sorts - air, earth, fire, or water. (Roll d4 to determine which sort is discovered.) This oil gives total invulnerability to normal elemental forces on the Prime Material Plane: normal wind storms, fire, earth slides, floods, and so forth. Additionally, there is a 10% chance that any container of this oil which is discovered will be usable on any of the Elemental or Paraelemental Planes. The oil allows the person(s) treated to operate freely and without danger of harm by elemental forces. Of course, monsters do other sorts of damage, and such attacks by elemental creatures will still be effective, but at -1 per die of damage. The oil comes in sufficient quantity to coat one individual for eight days duration, or eight individuals for one day.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Fiery Burning',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [4000,4000],
    desc = 'When this substance is subjected to air, it bursts into flame, the fire being so hot that it will inflict 5-30 points (5d6) of damage to any creature coated with the oil (saving throw vs. spell applicable for half damage). If hurled, a flask containing this oil will always break. Any creature within 1" of the place of impact of the oil flask is subject to the effects, but a maximum of six such creatures can be affected. (The oil can, for instance, be used to consume the bodies of as many as six regenerating creatures such as <a href="/creatures/troll">trolls</a>.) If the flask is opened, the creature holding it will immediately suffer 1-4 points of damage. Unless that creature then proceeds to roll equal to or less than its dexterity on 2d10, the flask will not be re-stoppered in time to prevent the oil from exploding, with effects as described above.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Fumbling',
    category = MagicItemCategory.POTION,
    xp_value = [0,0],
    gold_value = [1000,1000],
    desc = 'This viscous substance will initially seem to be of a useful sort - <i>acid resistance</i>, <i>elemental invulnerability</i>, or <i>slipperiness</i>, for instance - until the wearer is under stress in a melee combat situation. At that point, he or she will have a 50% chance each round of fumbling and dropping whatever he or she holds - weapon, shield, spell components, and so forth. Only a thorough bath of solvent (alcohol, turpentine, etc.) will remove the substance before its potency wears off.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Impact',
    category = MagicItemCategory.POTION,
    xp_value = [750,750],
    gold_value = [5000,5000],
    desc = 'This magical substance is charged with a powerful dweomer which has beneficial effects upon blunt weapons and missiles of all sorts, magical and non-magical. When applied to a blunt weapon such as a club, hammer, or mace, it causes the weapon to both be magical and deliver extra damage. When the oil is applied to a missile, its effect is to make it both magical and very deadly upon impact. Missiles upon which the <i>oil of impact</i> will properly function are hurled hammers, hurled clubs, sling stones, and sling bullets. A flask of this substance will contain from 3-5 applications. Each application will last for 9-12 rounds on a hand-held weapon, but when applied to a missile weapon the substance has but a single "charge." With respect to missiles, however, only a small amount need to be used, so that 4-5 sling missiles or 2 larger weapons can be treated with a single application. If the oil is used on a hand-held weapon, its dweomer will bestow +3 status to the weapon\'s hit probability and cause +6 damage on a successful hit. Missiles will be +3 both "to hit" and to damage.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Oil of Sharpness',
    category = MagicItemCategory.POTION,
    xp_value = [300,500],
    gold_value = [3000,5000],
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
MagicItem( name = 'Oil of Timelessness',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [2000,2000],
    desc = 'This smooth liquid appears to be an oil of any sort - even possibly of poisonous nature. When applied to any matter which was formerly alive (leather, leaves, paper, wood, dead flesh, etc.), it enables that substance to resist the passage of time, each year of actual time affecting the object as if only a day had passed. The substance never wears off, though it can be magically removed. The object coated with the oil also gains a +1 bonus on any saving throws which must be made for it. There is sufficient oil within one flask to coat one horse, eight humans, or an equivalent area/volume of some other eligible object or substance.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Philter of Beauty',
    category = MagicItemCategory.POTION,
    xp_value = [250,250],
    gold_value = [1500,1500],
    desc = 'When this substance is consumed, the individual gains +1 on charisma (18 maximum) and +1 to +4 on his or her comeliness score for the duration of the liquid\'s effect. All reactions pertaining to charisma and comeliness apply, but if the effects wear off within sight of any creature that was influenced by the enhanced charisma and comeliness, then the creature(s) will certainly have a hostile reaction to this turn of events and attack the individual.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Philter of Glibness',
    category = MagicItemCategory.POTION,
    xp_value = [500,500],
    gold_value = [2500,2500],
    desc = 'This magical draught allows the imbiber to fluently speak - even tell lies - smoothly, believably, and undetectably. Magical investigation (such as <a href="/spells/detect-lie-cleric-lvl-4"><i>detect lie</i></a>) will not give the usual results, but will reveal that some minor "stretching of the truth" might be occuring.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Philter of Stammering and Stuttering',
    category = MagicItemCategory.POTION,
    xp_value = [0,0],
    gold_value = [1500,1500],
    desc = 'When this liquid is consumed, it will seem to be a beneficial draught - one of <i>glibness</i> or <i>persuasiveness</i>, for instance. But whenever something meaningful must be spoken (the verbal component of a spell, the text of a scroll, conversation with a monster, etc.), the beverage\'s true effect will be revealed - nothing can be said properly, and reactions of all creatures hearing such nonsense will be at -25% penalty.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Potion of Rainbow Hues',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [800,800],
    desc = 'This rather syrupy draught must be stored in a metallic container. A full flask holds sufficient liquid for seven hours\' effect. The imbiber only has to concentrate on some color or colors and he or she will turn that very hue in less than one segment. Any color or combination of colors is possible, if the user of the magical drink simply holds the thought in his mind for the space of time required for the hue(s) to be effected. If the potion is quaffed sparingly, it is possible to get seven draughts of one hour duration apiece.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Potion of Ventriloquism',
    category = MagicItemCategory.POTION,
    xp_value = [200,200],
    gold_value = [800,800],
    desc = 'When it is imbibed, this potion enables the drinker to duplicate the effects of a <a href="/spells/ventriloquism-magic-user-lvl-1"><i>ventriloquism</i></a> spell as if he or she were a magic-user. The potion lasts for six such uses, or until its effects fade due to expiration of time.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Potion of Vitality',
    category = MagicItemCategory.POTION,
    xp_value = [300,300],
    gold_value = [2500,2500],
    desc = 'This potion enables the consumer to be refreshed and full of vitality despite exertion, lack of sleep, and going without food and drink for as long as seven days. If the potion is consumed after one or more days of such exertion or deprivation, it will nullify the adverse effects and still bestow vitality for the remaining number of days up to seven. In addition, the potion is proof against poisons and diseases for the indicated period - and while the potion is in effect, the beneficiary will recover lost hit points at the rate of 1 every 4 hours.',
    source = SourceBook.UNEARTHED_ARCANA
)
]


scrolls = [
MagicItem( name = 'Protection from Demons',
    category = MagicItemCategory.SCROLL,
    xp_value = [2500,2500],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = ('This scroll requires 1 full round to read if it is to protect against all sorts of demons, including demon princes, 7 segments to protect against demons of <a href="/creatures/type-6-demon">type VI</a> or lower, and only 3 segments to protect against <a href="/creatures/type-3-demon">type III</a> or lower. The circle of protection generated springs outwards from the scroll reader in a 10\' radius. No demon protected against can penetrate the circle physically or magically or in any way, but the person(s) within can launch attacks, if otherwise possible, upon demons. The protection moves with the reader of the scroll. Its effect lasts for 5-20 (5d4) rounds.\n\n'
        'Note that the protection radius is not an actual physical globe, and if the user forces a demon into a place from which further retreat is impossible (e.g., a corner), and then continues forward until the demon would be within the radius of the circle, the demon is not harmed, and the protection is considered voluntarily broken and disappears. There is no way in which this can be used as an offensive weapon.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem( name = 'Protection from Devils',
    category = MagicItemCategory.SCROLL,
    xp_value = [2500,2500],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'This scroll is nearly identical to the <i>protection from demons</i> scroll. It requires 1 round to read if it is to protect against all kinds of devils, including arch-devils, 7 segments to protect against greater devils or lower, and 3 segments to protect against lesser devils or lower.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem( name = 'Protection from Elementals',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = (6, TimeUnit.segment),
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
MagicItem( name = 'Protection from Lycanthropes',
    category = MagicItemCategory.SCROLL,
    xp_value = [1000,1000],
    activation_time = TimePeriod(4, TimeUnit.segment),
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
MagicItem( name = 'Protection from Magic',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = TimePeriod(8, TimeUnit.segment),
    desc = ('This scroll invokes a very powerful and invisible globe of anti-magic in a 5\' radius from the reader. It prevents any form of magic from passing into or out of its confines, but normal things are not restricted by it. As with other protections, the globe of anti-magic moves with its invoker. Any magical item which touches the globe must be saved for with a 50% likelihood of the object being drained of all magic from the power of the globe, i.e. save equals 11 or better with d20. The protection lasts for 5-30 (5d6) rounds.\n\n'
        'If multiple magic items encounter the globe simultaneously, the leading item (a magic sword held in advance of its holder, for instance) is the first affected, then the others are checked in order of decreasing power until the first item fails its save, at which time the globe is cancelled and the item is drained of its magic.'
    ),
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem( name = 'Protection from Petrification',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(5, TimeUnit.segment),
    desc = 'A 10\' radius circle of protection extends from, and moves with, the reader of this scroll. All within its confines are absolutely immune to any attack forms, magical or otherwise, which cause flesh to turn to stone. The protection lasts for 5-20 (5d4) rounds.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem( name = 'Protection from Possession',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'This scroll generates a magic circle of 10\' radius which extends from, and moves with, the reader. All creatures within its confines are protected from possession by magical spell attacks such as <a href="/spells/magic-jar-magic-user-lvl-5"><i>magic jar</i></a>; attack forms aimed at possession or mental control or psychic energy drain which are psionically based or magically based, or demon, devil, <a href="/creatures/night-hag">night hag</a>, or similar creature possession (obsession). This protects even dead bodies if they are within the magic circle. The protection lasts for 10 to 60 rounds in 90% of these scrolls; 10% have power which lasts 10 to 60 turns, but the protection is <i>stationary</i>.',
    source = SourceBook.DUNGEON_MASTERS_GUIDE
),
MagicItem( name = 'Protection from Undead',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = TimePeriod(4, TimeUnit.segment),
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
MagicItem( name = 'Protection from Acid',
    category = MagicItemCategory.SCROLL,
    xp_value = [2500,2500],
    activation_time = TimePeriod(5, TimeUnit.segment),
    desc = 'The reader of the scroll is protected from all forms of acid, up to a damage limit of 20 hit dice or a time limit of 9-12 turns (d4 +8), whichever comes first. Thus, the scroll would provide safety from three separate breath-weapon attacks be a <a href="/creatures/black dragon</a> of smallest size (normally 6 HD of damage per attack), with a small amount of protection yet unused - assuming that the attacks all take place before the time limit expires.',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Breath Weapons, Dragon',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'Only the individual reading this scroll is protected. Protection is not limited by alignment type or type of breath; it extends to all forms of dragon breath, and lasts for 6-12 rounds (2d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Cold',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(3, TimeUnit.segment),
    desc = 'Protection extends outward from the reader within a 3" diameter sphere. All within this area are protected from the effects of normal cold as low as absolute zero. Against magical cold, the liquid acts as the clerical spelll <a href="/spells/resist-cold-cleric-lvl-1"><i>resist cold</i></a>, but with enhanced benefits (+6 on saving throw, damage one-quarter normal or one-eighth if save is made). The duration of the effect is 5-8 turns (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Electricity',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = TimePeriod(5, TimeUnit.segment),
    desc = 'Protection is provided in a 2" diameter sphere centered on the reader. All protected are immune to any electrical attacks and associated effects. Protection lasts for 3-12 rounds (3d4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Fire',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(8, TimeUnit.segment),
    desc = 'Protection extends to a 3" diameter sphere centered on the reader. All within this area are able to withstand flame and heat of the hottest sort, even of magical or elemental nature. Protection lasts for 5-8 turns (d4  +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Gas',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(3, TimeUnit.segment),
    desc = 'The scroll generates a 1" diameter sphere of protection centered on the reader, and all within this area are immune to the effects of any form of gas - poison gas, breath weapons which are gaseous in nature, spells which generate gas clouds such as <a href="/spells/stinking-cloud-magic-user-lvl-2"><i>stinking cloud</i></a> and <a href="/spells/cloudkill-magic-user-lvl-5"><i>cloudkill</i></a>, and all similar forms of noxious, toxic vapors. The scroll\'s protection lasts for 5-8 rounds (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Illusions',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = TimePeriod(7, TimeUnit.segment),
    desc = 'Only the individual reading the scroll is protected, and the benefit extends to any form of <i>illusion/phantasm</i> magic witnessed by the individual. Protection lasts for 5-30 rounds (5d6).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Paralyzation',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'Only the reader is affected by the dweomer of this scroll. The protection extends to all forms of paralyzation, muscle and nerve paralysis included. A <a href="/spells/hold-monster-magic-user-lvl-5"><i>hold</i></a> spell will not work upon the protected individual, nor will any sort of paralysis brought about by gas. Protection lasts for 2-5 turns (d4 +1).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Plants',
    category = MagicItemCategory.SCROLL,
    xp_value = [1000,1000],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'Protection extends to a 1" diameter sphere centered on the reader. All forms of vegetable life, including fungi, slimes, molds, and the like are unable to penetrate the protective sphere. If it is moved toward such plant life which is capable of movement, the plant will be pushed away. If the protective sphere is pushed up against an immobile, firmly fixed form of plant life (such as a well-rooted shrub, bush, or tree), the sphere will not be able to be moved farther in that direction unless the reader of the scroll has enough strength and mass to be able to uproot the plant under normal circumstances. Protection lasts for 5-8 turns (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Poison',
    category = MagicItemCategory.SCROLL,
    xp_value = [1000,1000],
    activation_time = TimePeriod(3, TimeUnit.segment),
    desc = 'Protection afforded by the scroll extends only to the reader. No form of poison - ingested, insinuated, contacted, breathed, etc. - will affect the protected individual, and any such poison in the reader\'s system is permanently neutralized by the dweomer of the scroll. Protection lasts for 3-12 rounds (d10 +2).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Traps',
    category = MagicItemCategory.SCROLL,
    xp_value = [2000,2000],
    activation_time = TimePeriod(0, TimeUnit.variable),
    desc = ('There are three forms of this scroll - those that protect from mechanical traps (50%), magical traps (30%), and those that protect from any form of trap (20%).\n\n'
        '<b>Mechanical</b>: Reading time: 4 segments. Protection extends only to the reader. Traps of mechanical nature do not function against the reader, but neither are they revealed. Protection lasts for 5-20 rounds (5d4).\n\n'
        '<b>Magical</b>: Reading time: 8 segments. Protection extends in a 1" diameter sphere centered on the reader. Magical traps do not function against those in the area of protection, but neither are they revealed. Protection lasts for 3-12 rounds (d10 +2).\n\n'
        '<b>Any trap</b>: Reading time: 1 round. Protection extends in a 1" diameter sphere centered on the reader. The dweomer prevents the functioning of any trap, but does not reveal any that may exist within the protective sphere. Protection lasts for 2-8 rounds (2d4).'
    ),
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Water',
    category = MagicItemCategory.SCROLL,
    xp_value = [1500,1500],
    activation_time = TimePeriod(6, TimeUnit.segment),
    desc = 'Protection extends in a 1" diameter sphere centered on the reader. All forms of water - liquid, solid, and vapor, ice, hail, snow, sleet, steam, and so forth - are unable to penetrate the sphere of protection. If those being protected come upon a form of water, the substance simply will not touch them; thus, they will not slip on ice, sink into a body of water, etc. Protection lasts for 5-8 turns (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Weapons, Magical',
    category = MagicItemCategory.SCROLL,
    xp_value = [1000,1000],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'Protection extends only to the reader. The form of magic weapon indicated is prevented from touching/harming the protected individual - but note that missile protection does not extends to missiles created by spell casting (such as <a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a>) or the use of spell-like power. Protection lasts for 5-8 rounds (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
),
MagicItem( name = 'Protection from Weapons, Non-magic',
    category = MagicItemCategory.SCROLL,
    xp_value = [1000,1000],
    activation_time = TimePeriod(1, TimeUnit.round),
    desc = 'Protection extends in a 1" diameter sphere centered on the reader. The form of non-magical weapon indicated is prevented from touching/harming the protected individual - but note that missile protection does not extend to normal missiles of large size, such as projectiles from a catapult or objects hurled by giants. Protection lasts for 5-8 rounds (d4 +4).',
    source = SourceBook.UNEARTHED_ARCANA
)
]

rings = [
MagicItem( name = 'Ring of Contrariness',
    category = MagicItemCategory.RING,
    xp_value = [0,0],
    gold_value = [1000,1000],
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
MagicItem( name = 'Ring of Delusion',
    category = MagicItemCategory.RING,
    xp_value = [0,0],
    gold_value = [2000,2000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>delusion ring</i> will convince the wearer that it is some other sort of ring, a ring of whatever sort the wearer really desires. As the wearer will be completely convinced that the ring is actually one with other magical properties, he or she will unconsciously use his or her abilities of any sort (including those of other magical items available) to actually produce a result commensurate with the supposed properties of the <i>delusion ring</i>. As referee, you will have to be most judicious in determining how successful the self-delusion can be, as well as how observers can be affected and what they will observe. The ring can be removed at any time.'
),
MagicItem( name = 'Ring of Djinni Summoning',
    category = MagicItemCategory.RING,
    xp_value = [3000,3000],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'One of the fabled rings of fantasy legend, the "genie" ring is most useful indeed, for it a special "gate" by means of which a certain <a href="/creatures/djinni">djinni</a> can be summoned from the Elemental Plane of Air. When the ring is rubbed the summons is served, and the djinni will appear on the next round. The djinni will faithfully obey and serve the wearer of the ring, but if the servant of the ring is ever killed, the ring becomes non-magical and worthless.'
),
MagicItem( name = 'Ring of Elemental Command',
    category = MagicItemCategory.RING,
    xp_value = [5000,5000],
    gold_value = [25000,25000],
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
MagicItem( name = 'Ring of Feather Falling',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring protects its wearer by automatic activation of a <a href="/spells/feather-fall-magic-user-lvl-1"><i>feather fall</i></a> if the individual falls 5\' or more. (Cf. <a href="/spells/feather-fall-magic-user-lvl-1"><i>feather fall</i></a> spell.)'
),
MagicItem( name = 'Ring of Fire Resistance',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The wearer of this ring is totally immune to the effects of normal fires - torches, flaming oil, bonfires, etc. Very large and hot fires, molten lava, demon immolation, <a href="/creatures/hell-hound">hell hound</a> breath, or a <a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a> spell will cause 10 hit points of damage per round (1 per segment) if the wearer is directly within such conflagration. Exceptionally hot fires such as <a href="/creatures/red-dragon">red dragon</a> breath, <a href="/creatures/pyrohydra">pyrohydra</a> breath, <a href="/spells/fireball-magic-user-lvl-3"><i>fireballs</i></a>, <a href="/spells/flame-strike-cleric-lvl-5"><i>flame strike</i></a>, <a href="/spells/fire-storm-druid-lvl-7"><i>fire storm</i></a>, etc. are saved against at +4 on the die roll, and all damage dice are calculated at -2 per die, but each die is never less than 1 in any event. (As a rule of thumb, consider very hot fires as those which have a maximum initial exposure of up to 24 hit points, those of exceptional heat 25 or more hit points.)'
),
MagicItem( name = 'Ring of Free Action',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring enables the wearer to move and attack freely and normally whether attacked by a <a href="/spells/web-magic-user-lvl-2"><i>web</i></a>, <a href="/spells/hold-monster-magic-user-lvl-5"><i>hold</i></a>, or <a href="/spells/slow-magic-user-lvl-3"><i>slow</i></a> spell, or even while under water. In the former case the spells have no effect, while in the latter the individual moves at normal (surface) speed and does full damage even with such cutting weapons as axes and scimitars and with such smashing weapons as flails, hammers, and maces, insofar as the weapon used is held rather than hurled. Thus will not, however, enables <i>water breathing</i> without the further appropriate magic.'
),
MagicItem( name = 'Ring of Human Influence',
    category = MagicItemCategory.RING,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring has the effect of raising the wearer\'s charisma to 18 with respect to encounter reactions with humans/humanoids. The wearer can make a <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a> to any human or humanoid conversed with (saving throw applies). The wearer can also <i>charm</i> up to 21 levels/hit dice of human/humanoids (saving throws apply) just as if he or she were using the magic-user spell, <a href="/spells/charm-person-magic-user-lvl-1"><i>charm person</i></a> The two latter uses of the ring are applicable but once per day. <i>Suggestion</i> or <i>charm</i> requires 3 segments of casting time.'
),
MagicItem( name = 'Ring of Invisibility',
    category = MagicItemCategory.RING,
    xp_value = [1500,1500],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The wearer of an <i>invisibility ring</i> is able to become invisible at will, instantly. This non-visible state is exactly the same as the magic-user <a href="/spells/invisibility-magic-user-lvl-2"><i>invisibility</i></a> spell, except that 10% of these rings also have <i>inaudibility</i> as well, making the wearer absolutely silent. If the wearer wishes to speak, he or she breaks all silence features in order to do so.'
),
MagicItem( name = 'Ring of Mammal Control',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This ring enables its wearer to exercise complete control over mammals with intelligence of 4 or less (<i>animal</i> or <i>semi</i>-intelligent mammals). Up to 30 hit dice of mammals can be controlled. Control extends to such limits as to enable the wearer to have the creatures controlled actually kill themselves, but complete concentration is required. (Note: the ring does not affect bird-mammal combinations, humans, semi-humans, and monsters such as <a href="/creatures/lammasu">lammasu</a>, <a href="/creatures/shedu">shedu</a>, <a href="/creatures/manticore">manticores</a>, etc.) If you are in doubt about any monster, it is NOT a mammal.\n\n'
        'Obviously, rats, weasels, herd animals, dolphins, and even <a href="/creatures/unicorn">unicorns</a> are mammals, but intelligence will preclude control of the better ones. Control time is 3 segments.'
    )
),
MagicItem( name = 'Ring of Multiple Wishes',
    category = MagicItemCategory.RING,
    xp_value = [5000,5000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring contains 2-8 (2d4) <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spells. As with any <i>wish</i>, you must be very judicious in how you handle the request. If players are greedy and grasping, be sure to "crock" them. Interpret their wording exactly, twist the wording, or simply rule the request is beyond the power of the magic. In any case, the <i>wish</i> is used up, whether or not (or how) the <i>wish</i> was granted. Note that no <i>wish</i> is able to cancel the decrees of god-like beings, unless it comes from another such creature.'
),
MagicItem( name = 'Ring of Protection',
    category = MagicItemCategory.RING,
    xp_value = [2000,4000],
    gold_value = [10000,20000],
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
MagicItem( name = 'Ring of Regeneration',
    category = MagicItemCategory.RING,
    xp_value = [5000,5000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'There are 2 forms of this ring: The standard <i>regeneration ring</i> restores 1 hit point of damage (and will replace lost limbs or organs eventually also) per turn. It will bring its wearer back from death (but if poison is the cause, the saving throw must be made or else the wearer dies again from the poison still in his or her system). Only total destruction of all living tissue by fire or acid or similar means will prevent <i>regeneration</i>. Of course the ring must be worn, and its removal stops regeneration processes. The rare form is the <i>vampiric regeneration ring</i>. This ring bestows one-half of the value of hit points of damage the wearer inflicts upon opponents in hand-to-hand (melee, non-missile, non-spell) combat immediately upon its wearer (fractions dropped). It does not otherwise cause regeneration or restore life, limb or organ. To determine which type of ring is discovered roll percentile dice: 01-90 = <i>ring of regeneration</i>, 91-00 = <i>vampiric regeneration ring</i>. In no case can the wearer\'s hit point total exceed that initially generated.'
),
MagicItem( name = 'Ring of Shooting Stars',
    category = MagicItemCategory.RING,
    xp_value = [3000,3000],
    gold_value = [15000,15000],
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
MagicItem( name = 'Ring of Spell Storing',
    category = MagicItemCategory.RING,
    xp_value = [2500,2500],
    gold_value = [22500,22500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>ring of spell storing</i> will contain 2-5 (d4 +1) spells which the wearer can employ just as if he or she were a spell user of the level appropriate to use the spell in question. The class of spells contained within the ring is determined in the same fashion as the spells on scrolls. The level of each spell is determined as follows:\n\n'
        'cleric: d6, if 6 is rolled roll d4 instead\n'
        'druid: as cleric\n'
        'magic-user: d8, if 8 is rolled roll d6 instead\n'
        'illusionist: as cleric\n\n'
        'Which spell type of any given level is contained by the ring is also randomly determined. The ring has the empathic ability to impart to the wearer the names of its spells. Once class, level, and type are determined, the properties of the ring are <i>fixed</i> and <i>unchangeable</i>. Once a spell is cast from the ring, it can only be restored by a character of appropriate class and level of experience, i.e. a 12th level magic-user is needed to restore a 6th level magic-user spell to the ring. Spells stores require 5 segments each to cast.'
    )
),
MagicItem( name = 'Ring of Spell Turning',
    category = MagicItemCategory.RING,
    xp_value = [2000,2000],
    gold_value = [17500,17500],
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
MagicItem( name = 'Ring of Swimming',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>ring of swimming</i> bestows the ability to swim at a full 21" base speed upon the wearer, assuming, of course, he or she is clad only in garments appropriate for such activity. It further enables the wearer to dive up to 50\' into water without injury, providing the depth of the water is at least 1½\' per 10\' of diving elevation; and the wearer can stay underwater for up to 4 rounds before a 1 hour (floating) rest is needed. The ring confers the ability to stay afloat under all but typhoon-like conditions.'
),
MagicItem( name = 'Ring of Telekinesis',
    category = MagicItemCategory.RING,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
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
MagicItem( name = 'Ring of Three Wishes',
    category = MagicItemCategory.RING,
    xp_value = [3000,3000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Although the ring contains 3 <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spells instead of a variable number, it is otherwise the same as a <i>multiple wish</i> ring except that 25% (01-25) contain 3 <a href="/spells/limited-wish-magic-user-lvl-7"><i>limited wish</i></a> spells.'
),
MagicItem( name = 'Ring of Warmth',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>warmth</i> ring provides its wearer with body heat even in conditions of extreme cold where the wearer has no clothing whatsoever. It also provides restoration of cold-sustained damage at the rate of 1 hit point of damage per turn. It increases saving throws versus cold-based attacks by +2 and reduces damage sustained by -1 per die.'
),
MagicItem( name = 'Ring of Water Walking',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ring enables the wearer to walk upon any liquid without sinking into it; this includes mud, quicksand, oil, running water, and even snow. The ring wearer\'s feet do not actually contact the surface he or she is walking upon when liquid or water is being walked upon (but oval depressions about 1½\' long and 1 inch deep per 100 pounds of weight of the walker will be observed in hardening mud or set snow). Rate of movement is standard movement for the individual wearing this ring. Up to 1,200 pounds weight can be supported by a <i>water walking</i> ring.'
),
MagicItem( name = 'Ring of Weakness',
    category = MagicItemCategory.RING,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This cursed ring causes the wearer to lose 1 point of strength and 1 point of constitution per turn until the individual reaches 3 in each ability area. This loss is not noticeable until the individual actually observes his or her weakened state due to some exertion (such as combat or heavy lifting), for the ring will also make the wearer <i>invisible</i> at will (and also cause the rate of strength and constitution point loss to double). Note that when full weakness is attained the wearer will be unable to function in his or her class. The <i>weakness</i> ring can be removed only if a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell, followed by a <a href="/spells/dispel-magic-magic-user-lvl-3"><i>dispel magic</i></a> spell, is cast upon the ring. There is a 5% chance that the ring is reversed, being a <i>ring of berserk strength</i>. This form gradually increases strength and constitution to 18 each (roll percentile dice for bonus strength if the wearer is a fighter). Increase is 1 point per ability per turn. However, once 18s in both abilities are reached, the wearer will always melee with any opponent he or she meets, immediately, regardless of circumstances. Points lost from the ring are restored by rest on a 1 day for 1 point basis, with 1 point of each ability lost being restored in 1 day of rest. Berserk strength is lost when the ring is removed, as are constitution points gained.'
),
MagicItem( name = 'Ring of Wizardry',
    category = MagicItemCategory.RING,
    xp_value = [4000,4000],
    gold_value = [50000,50000],
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
MagicItem( name = 'Ring of X-Ray Vision',
    category = MagicItemCategory.RING,
    xp_value = [4000,4000],
    gold_value = [35000,35000],
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
MagicItem( name = 'Ring of Animal Friendship',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'When the wearer of this ring approaches within 1" of any animal(s) of <i>neutral</i> alignment and <i>animal</i> intelligence, the creature(s) must save versus spell. If they succeed, they will then move rapidly away from the ring wearer. If the saving throw fails, then the creature(s) will become docile and follow the ring wearer around. The dweomer of the item functions at 6th level, so up to 12 hit dice of animals can be affected by this ring. Those feeling friendship for the wearer will actually guard and protect the individual if he or she expends a charge from the ring to cause such behavior. A ring of this sort typically has 27 charges when discovered, and it cannot be recharged. A druid wearing this ring can influence twice the prescribed hit dice worth of animals (24 rather than 12), and a ranger is able to influence 18 hit dice worth of animals.'
),
MagicItem( name = 'Anything Ring',
    category = MagicItemCategory.RING,
    xp_value = [5000,5000],
    gold_value = [55000,55000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This ring will initially appear to be a standard <i>ring of warmth</i>. However, the wearer may command three other functions from the ring, choosing from among the other standard sorts of magical rings. The period of such functioning will be one operation in the case of a ring which has such a function type (<i>djinni summoning</i>, <i>wishes</i>, etc.). Otherwise the effect will last for 1 day (24 hours). Any ring function so commanded will never be usable again; for example, the ring cannot be made to give more than one <a href="/spells/wish-magic-user-lvl-9">wish</a>. After three singular uses of this sort, the ring will turn into a non-magical piece of jewelry worth from 100 to 600 gp.'
),
MagicItem( name = 'Ring of Blinking',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'When the wearer of this ring issues the proper verbal command, the dweomer of the item activates, and he or she is then affected exactly as if a <a href="/spells/blink-magic-user-lvl-3"><i>blink</i></a> spell were operating upon his or her person. The effect always lasts for 6 rounds. The ring then ceases to function for 6 turns (1 hour) while it replenishes itself. The command word is usually engraved somewhere on the ring. The ring will activate whenever this word is spoken, even though the command might be given by someone other than the wearer, provided that the word is spoken within 10 feet of the ring.'
),
MagicItem( name = 'Ring of Boccob',
    category = MagicItemCategory.RING,
    xp_value = [250,250],
    gold_value = [2500,2500],
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
MagicItem( name = 'Ring of Chameleon Power',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'Whenever the wearer of this ring desires, he or she is able to magically blend in with the surroundings. This enables 90% invisibility in foliage, against walls, and so forth. If the wearer is associating with creatures with intelligence of 4 or greater at a distance of 6" or less, the dweomer of the ring enables the wearer to seem to be one of those creatures, but each turn of such association carries a 5% cumulative chance that the creatures will detect the ring wearer for what he or she actually is. Thus, such an association can never persist for more than 20 turns without the wearer being detected, because at the end of that time the chance of detection has risen to 100%. In addition, creatures with 16 or greater intelligence use their intelligence score as an addition to the base chance of detection - i.e., 21% at the end of turn 1, 26% at the end of turn 2, and so forth, if a creature of 16 intelligence is involved. Creatures with 3 or lower intelligence will instinctively and automatically detect the wearer if they come within a 1" radius of him or her.'
),
MagicItem( name = 'Ring of Clumsiness',
    category = MagicItemCategory.RING,
    xp_value = [0,0],
    gold_value = [3000,3000],
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
MagicItem( name = 'Ring of Faerie',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [7500,7500],
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
MagicItem( name = 'Ring of Jumping',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'In a single segment the wearer of this ring is able to call forth its power so as to be able to leap 30 feet ahead, or 10 feet backwards or straight up, with an arc of about 2 feet for every 10 feet traveled (cf. 1st-level magic-user spell, <a href="/spells/jump-magic-user-lvl-1"><i>jump</i></a>). The wearer must use the ring\'s power carefully, for it can perform only four times per day.'
),
MagicItem( name = 'Ring of Mind Shielding',
    category = MagicItemCategory.RING,
    xp_value = [500,500],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This form of magic ring is usually of fine workmanship and wrought from heavy gold. The wearer is so shielded as to be completely immune to <a href="/spells/esp-magic-user-lvl-2"><i>ESP</i></a>, <a href="/spells/detect-lie-cleric-lvl-4"><i>detect lie</i></a>, <a href="/spells/know-alignment-cleric-lvl-2"><i>know alignment</i></a>, and telepathic reading of the mind. If the wearer is also possessed of psionic power, he or she has the benefit of a <i>thought shield</i> defense at no point cost, all all psionic attack damage suffered by the wearer is at -2 points while the ring is worn. Furthermore, the wearer is more capable of dealing with a <i>psionic blast</i> attack, gaining +1 on saving throws versus such attacks if the wearer is not psionically endowed, or -3 on damage if the wearer does possess psionics.'
),
MagicItem( name = 'Ring of the Ram',
    category = MagicItemCategory.RING,
    xp_value = [750,750],
    gold_value = [7500,7500],
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
MagicItem( name = 'Ring of Shocking Grasp',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This ordinary-seeming ring will radiate only a faint, unidentifiable aura of magic when examined, but it contains a strong dweomer when used to inflict damage upon an opponent. If the wearer attacks an enemy, attempting to touch that individual with the hand upon which the ring is worn, a successful "to hit" roll indicates that the touch has taken place, and from 7-14 points of damge (d8 +6) are delivered to the target creature. After three discharges of this nature, regardless of the time elapsed betweeen them, the ring will be inert for 1 turn. It is of note that when actually functioning, this ring causes a circular, charged extrusion to appear on the palm of the wearer\'s hand.'
),
MagicItem( name = 'Ring of Sustenance',
    category = MagicItemCategory.RING,
    xp_value = [500,500],
    gold_value = [3500,3500],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This magical ring provides its wearer with life-sustaining nourishment even though he or she might go for days without food or drink. The ring also refreshes the body and mind, so that its wearer needs to sleep only two hours per day to gain the benefit of eight hours of sleep. The ring must be worn for a full week in order to function properly, and if it is removed it immediately loses its benefits and must again be worn for a week to reattune itself to the wearer. After functioning (in either or both capacities) for any period of seven consecutive days, a <i>ring of sustenance</i> will cease to function for a week while it replenishes its dweomer.'
),
MagicItem( name = 'Ring of Truth',
    category = MagicItemCategory.RING,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'There is little doubt that wearing a ring of this nature is a mixed blessing. While any lie told to the wearer is detectable as such by him or her, by the same token he or she is unable to tell any sort of falsehood. Any attempt to lie results in speaking the literal truth, but in turn the wearer is able to discern the last prevarication on the part of another. In fact, the voice of the liar rises to a falsetto due to the power of the ring. If the wearer of the ring encounters some magic which enables falsehoods to otherwise be spoken without detection (such as someone under the effects of an <a href="/spells/detect-lie-cleric-lvl-4"><i>undetectable lie</i></a> spell or a <i>philter of glibness</i>, no lie is noticed, but the ring wearer will not hear the voice of the person so dweomered, whether or not he or she is trying to listen.'
)
]

rods = [
MagicItem( name = 'Rod of Absorption',
    category = MagicItemCategory.ROD,
    xp_value = [7500,7500],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This rod acts as a magnet and draws magic spells of any nature (cleric, druid, magic-user, or illusionist) into itself, nullifying their effects but storing their <i>potential</i> within until the wielder chooses to release this energy in the form of spells of his or her own casting. The magic absorbed must have been directed at the character possessing the rod. (Cf. <i>ring of spell turning</i>). The wielder can instantly detect the spell level and decide on whether to react or not when the rod absorbs it. The wielder can use the energy to cast any spell he or she has memorized, in but 1 segment, without loss of spell memory, as long as the spell so cast is of equal or lesser level than the one absorbed. Excess levels are stored as potential, and can be cast in like manner (in 1 segment with no spell memory loss) as any level spell so long as the wielder knows the spell and has it memorized.\n\n'
        'The <i>rod of absorbption</i> can never be recharged. It absorbs 50 spell levels and can thereafter only discharge any remaining potential it might have within. The wielder will know this upon grasping the item. If it has charges used, this indicates that it has already absorbed that many spell levels and they have been used.\n\n'
        'Example: a cleric has a <i>rod of absorption</i> and uses it to nullify the effect of a <a href="/spells/hold-person-magic-user-lvl-3"><i>hold person</i></a> spell cast at him by a magic-user. The rod has now absorbed 3 spell levels, can absorb 47 more, and the cleric can, in 1 segment, cast any first, second, or third level spell he or she has memorized, <i>without</i> memory loss of that spell, by using the stored potential of the rod. Assume the cleric casts a <a href="/spells/hold-person-cleric-lvl-2"><i>hold person</i></a> back. This spell is only second level to him or her, so the rod then holds 1 spell level of potential, and can absorb 47 more still, with 2 charges permanently disposed of.'
    )
),
MagicItem( name = 'Rod of Beguiling',
    category = MagicItemCategory.ROD,
    xp_value = [5000,5000],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This rod enables its possessor to radiate an emotional and mental wave of fellow-feeling to all creatures with any intelligence whatsoever (1 or higher intelligence). The effect is to cause all such creatures within a 2" radius of the device to be virtually charmed by the individual and beguiled into regarding him or her as their comrade, friend, and/or mentor (no saving throw). The beguiled creatures will love and respect the rod wielder. They will trustingly listen and obey insofar as communication is possible, and the instruction seems plausible and does not outwardly consign the beguiled to needless injury or destruction or go against their nature or alignment. Each charge of the rod beguiles for 1 turn. It can be recharged.'
),
MagicItem( name = 'Rod of Cancellation',
    category = MagicItemCategory.ROD,
    xp_value = [10000,10000],
    gold_value = [15000,15000],
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
    xp_value = [6000,6000],
    gold_value = [20000,20000],
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
    xp_value = [10000,10000],
    gold_value = [35000,35000],
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
    xp_value = [8000,8000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The individual who possesses this magic rod is able to exercise rulership (command the obedience and fealty) or creatures within 12" when he or she activates the device. From 200 to 500 hit dice (or levels of experience) can be ruled, but creatures with 15 or greater intelligence and 12 or more hit dice/levels are entitled to a saving throw versus magic. Ruled creatures will obey the wielder of the <i>rod of rulership</i> as if he or she were their absolute suzerain, but if some command given is absolutely contrary to the nature of the commanded, the magic will be broken. The rod takes 5 segments to activate. Each charge lasts for 1 turn. The rod cannot be recharged.'
),
MagicItem( name = 'Rod of Smiting',
    category = MagicItemCategory.ROD,
    xp_value = [4000,4000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This rod is a +3 magic weapon which inflicts 4-11 (d8 +3) hit points of damage. Against golems the rod does 8-22 (2d8 +6) hit points of damage, any score of 20 or better completely destroys the monster, but any hit upon a golem drains 1 charge. The rod does normal damage (4-11) versus creatures of the <i>outer planes</i> such as demons, devils, and <a href="/creatures/night-hag">night hags</a>. Any score of 20 or better draws off 1 charge and causes triple damage: (d8 +3)x3. The rod cannot be recharged.'
),
MagicItem( name = 'Rod of Alertness',
    category = MagicItemCategory.ROD,
    xp_value = [7000,7000],
    gold_value = [50000,50000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This magical rod is indistinguishable from a <i>footman\'s mace +1</i>. However, upon usage, its true powers will reveal themselves. The rod bestows +1 to the possessor\'s die rolls for being surprised, and in combat the possessor gains +1 on initiative die rolls. If it is grasped firmly, the rod will enable the concentrating character to <a href="/spells/know-alignment-cleric-lvl-2"><i>detect alignment</i></a>, <a href="/spells/detect-evil-cleric-lvl-1"><i>evil</i>, <i>good</i>, <a href="/spells/detect-illusion-magic-user-lvl-3"><i>illusion</i></a>, <a href="/spells/detect-invisibility-magic-user-lvl-2"><i>invisibility</i></a>, <a href="/spells/detect-lie-cleric-lvl-4"><i>lie</i></a>, or <a href="/spells/detect-magic-cleric-lvl-1"><i>magic</i></a>. The use of any of these <i>detect</i> powers does not expend any of the charges in the rod.\n\n'
        'If the <i>rod of alertness</i> is planted in the ground, and the possessor wills it to alertness, the rod will then "sense" any creature within a 12" radius, provided that the creature has intent to harm the possessor. Each of the eight flanges of the macelike head of the rod will then cast a <a href="/spells/light-magic-user-lvl-1"><i>light</i></a> spell along one of the cardinal directions (N, NE, E, etc.) at 6" range, and at the same time the rod will create the effect of a <a href="/spells/prayer-cleric-lvl-3"><i>prayer</i></a> spell upon all friendly (to the possessor) creatures in a 2" radius. Immediately thereafter, the rod will send forth a mental alert to these same friendly creatures, warning them of possible danger from the unfriendly creature(s) within the 12" radius. Lastly, the rod can be used to simulate the casting of an <a href="/spells/animate-object-cleric-lvl-6"><i>animate object</i></a> spell, utilizing any 16 (or fewer) objects specially designated by the possessor and placed roughly around the perimeter of a 6"-radius circle centered on the rod - 16 selected shrubs, 16 specially shaped branches, or the like. Functions excluding the <i>animate object</i> dweomer require 1 charge, and the animation also requires 1 charge, so if all of the rod\'s protective devices are utilized at once, 2 charges are expended. The rod can be recharged by a cleric of 16th or higher level, so long as at least 1 charge remains in the rod when the recharging is attempted.'
    )
),
MagicItem( name = 'Rod of Flailing',
    category = MagicItemCategory.ROD,
    xp_value = [2000,2000],
    gold_value = [20000,20000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This magical weapon radiates a faint dweomer of the <i>alteration</i> sort when magic is detected for. Upon the command of its possessor, the weapon activates, changing from a normal-seeming rod to a double-headed flail. In close-quarters, or if the wielder is mounted, it is the small, horseman\'s weapon; otherwise, it is a footman\'s weapon, i.e. base damage done is 2-5/2-5 (S-M/L) or 2-7/2-8 (S-M/L). The rod has special features beyond this: In either form, the weapon is +3 for hitting and damage. Better still, each of the weapon\'s two heads is checked for when the possessor attacks, so double hits can be scored, either on a single opponent or on two opponents who are man-sized or smaller and standing side by side. If the holder of the rod expends 1 charge, that character gains +4 on protection and +4 on saving throws for 1 turn. The rod need not be in weapon-form for this protection benefit to be employed, and transforming it into a weapon (or back into a rod) does not expend any charges.'
),
MagicItem( name = 'Rod of Passage',
    category = MagicItemCategory.ROD,
    xp_value = [5000,5000],
    gold_value = [50000,50000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This highly dweomered item allows its wielder to perform any of the following, one at a time, one per round: <a href="/spells/astral-spell-cleric-lvl-7"><i>astral travel</i></a>, <a href="/spells/dimension-door-magic-user-lvl-4"><i>dimension door</i></a>, <a href="/spells/passwall-magic-user-lvl-5"><i>passwall</i></a>, <a href="/spells/phase-door-magic-user-lvl-7"><i>phase door</i></a>, and <a href="/spells/teleport-without-error-magic-user-lvl-7"><i>teleport without error</i></a>. It is necessary to expend 1 charge to activate the rod, but once it is activated the possessor can perform each of the listed functions one time. The rod remains charged for 1 day, or until each of the five functions is used. None of the functions can be used a second time unless another charge is expended, whereupon all five of the functions again become available. With respect to <i>astral travel</i>, the wielder can elect to use the rod on as many as five creatures (including the wielder) desirous of becoming astral and traveling thus; however, any other remaining functions of the rod are cancelled by this action. The rod travels into the Astral Plane along with the affected creatures (of which the wielder must be one), and cannot be used ir reactivated until it is returned from the Astral Plane. This five-in-one effect will not work with respect to the rod\'s other powers - <i>passwall</i>, for instance; only <i>astral travel</i> can be used more than once per activation, and only in the manner described above. The rod exudes a magical aura of the <i>alteration-evocation</i>sort. Because the physical bodies of the travelers, and their possessions, are actually empowered to become astral, the recharging of the rod requires a magic-user of 20th or higher level.'
),
MagicItem( name = 'Rod of Security',
    category = MagicItemCategory.ROD,
    xp_value = [3000,3000],
    gold_value = [30000,30000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'Each time a charge is expended, this item creates a non-dimensional space, a "pocket paradise", where the rod\'s possessor and as many as 199 other creatures are able to stay in complete safety and security for a period of time, the maximum being 200 days divided by the number of creatures affected. Thus, one creature (the rod\'s possessor) can stay for 200 days; four creatures can stay for 50 days; a group of 60 creatures can stay for 3 days. (All fractions are rounded down, so that a group numbering between 101 and 200 inclusive can stay for one day only.) While the recipients of the rod\'s power are within this "paradise", they do not age (except from magical causes such as the casting of a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spell), and natural healing and curing takes place at twice the normal rate. Fresh water and food (fruits and vegetables only) are in abundance; the climate is comfortable for all creatures involved, so that protection from elements is not necessary. Activation of the rod simply causes the wielder and as many creatures as were touched with the item to be removed from the place where they are and transported instantaneously to the paradise. (Members of large groups can hold hands or otherwise touch each other, and thus all be "touched" by the rod at one time. When the dweomer is cancelled or expires, all of the affected creatures instantly reappear in the location they occupied when the rod was activated. If something else occupies the space that a traveller would be returning to, then his or her body is displaced a sufficient distance to provide the space required for "re-entry". The rod can be recharged by the joint efforts of a cleric of 16th or higher level and a magic-user of 18th or higher level.'
),
MagicItem( name = 'Rod of Splendor',
    category = MagicItemCategory.ROD,
    xp_value = [2500,2500],
    gold_value = [25000,25000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('The possessor of this rod is automatically and continually bestowed with a charisma of 18 for as long as the item is held or carried, and whatever garments the possessor wears (including armor) will appear to be of finest quality and condition, although no special magical benefit (such as change in armor class) is enjoyed. If the possessor already has a charisma score of 18 or greater, the rod does not further enhance this attribute. When the possessor expends 1 charge, the rod actually creates and garbs him or her in clothing of noble sort - the finest fabrics, plus adornments of furs and jewels. This apparel is actually created by the magic of the rod, and remains permanently in existence unless the possessor attempts to sell any part of it, or if any garb is forcibly taken from him or her. In either of those cases, all of the apparel immediately disappears. The garments may be freely given to other characters or creatures, however, and will remain whole and sound afterward. If the possessor is bedecked in one of these magically created outfits, the garb cannot be replaced or added to by expenditure of another charge; in such a case, the charge is simply wasted. The value of any noble garb created by the wand wil be from 7,000 to 10,000 gp (d4 +6). The fabric will be worth 1,000 gp, furs 5,000 gp, and jewel trim from 1,000 to 4,000 gp, i.e. 10 gems of 100 gp value each, 10 gems of 200 gp value each, or 20 gems of 100 gp value, and so forth.\n\n'
        'The second power of the rod, also requiring 1 charge to bring about, is the creation of a palatial tent - a huge pavilion of silk encompassing between 1,500 and 3,000 square feet. Inside the tent will be temporary furnishings and foodstuffs suitable to the splendor of the pavilion and in sufficient supply to entertain as many as 100 persons. The tent and its trappings will last for one day, at the end of which time the pavilion may be maintained by expending another charge; otherwise, the tent and all objects associated with it (including any items that were taken out of the tent) will disappear. This rod cannot be recharged.'
    )
)
]

staves = [
MagicItem( name = 'Staff of Command',
    category = MagicItemCategory.STAVE,
    xp_value = [5000,5000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This device has 3 functions, only 2 of which will be effective if the wielder is a magic-user, but all 3 work when the staff is in a cleric\'s hands. The 3 functions are:\n\n'
        '1. <i>Human influence</i>: This power duplicates that of the ring of the same name. Each <i>suggestion</i> or <i>charm</i> draws 1 charge from the staff.\n\n'
        '2. <i>Mammal control/animal control</i>: This power functions only as <i>mammal control</i> (as the ring of the same name) when the staff is used by a magic-user, but in the hands of a cleric it is <i>animal control</i> (as the potion of that name, all types of animals listed). Either use drains 1 charge per turn or fraction thereof.\n\n'
        '3. <i>Plant control</i>: This function duplicates that of the potion of the same name, but for each 1" square area of plants controlled for 1 turn or less than 1 charge is used. A magic-user cannot control plants at all.'
        'The staff can be recharged.'
    )
),
MagicItem( name = 'Staff of Curing',
    category = MagicItemCategory.STAVE,
    xp_value = [6000,6000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device can <i>cure disease</i>, <i>cure blindness</i>, <i>cure wounds</i> (6-21 hit points, 3d6 +3), or <i>cure insanity</i>. Each function drains 1 charge. The device can be used but once per day on any person (dwarf, elf, gnome, half-elf, halfling, half-orc included), and no function may be employed more than twice per day, i.e. the staff can only function 8 times during a 24 hour period. It can be recharged.'
),
MagicItem( name = 'Staff of the Magi',
    category = MagicItemCategory.STAVE,
    xp_value = [15000,15000],
    gold_value = [75000,75000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This potent staff contains many spell powers and other functions as well so as to be a walking arsenal in one device. The staff has the following powers which do not drain charges:\n\n'
        '<a href="/spells/detect-magic-magic-user-lvl-1"><i>detect magic</i></a>\n'
        '<a href="/spells/enlarge-magic-user-lvl-1"><i>enlarge</i></a>\n'
        '<a href="/spells/hold-portal-magic-user-lvl-1"><i>hold portal</i></a>\n'
        '<a href="/spells/light-magic-user-lvl-1"><i>light</i></a>\n'
        '<a href="/spells/protection-from-evil-magic-user-lvl-1"><i>protection from evil/good</i></a>\n\n'
        'The following powers drain 1 charge per usage:\n\n'
        '<a href="/spells/invisibility-magic-user-lvl-2"><i>invisibility</i></a>\n'
        '<a href="/spells/knock-magic-user-lvl-2"><i>knock</i></a>\n'
        '<a href="/spells/pyrotechnics-magic-user-lvl-2"><i>pyrotechnics</i></a>\n'
        '<a href="/spells/web-magic-user-lvl-2"><i>web</i></a>\n'
        '<a href="/spells/dispel-magic-magic-user-lvl-3"><i>dispel magic</i></a>\n'
        '<a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a>\n'
        '<a href="/spells/lightning-bolt-magic-use-lvl-3"><i>lightning bolt</i></a>\n'
        '<a href="/spells/ice-storm-magic-user-lvl-4"><i>ice storm</i></a>\n'
        '<a href="/spells/wall-of-fire-magic-user-lvl-4"><i>wall of fire</i></a>\n'
        '<a href="/spells/passwall-magic-user-lvl-5"><i>passwall</i></a>\n\n'
        'These powers drain 2 charges per usage:\n\n'
        '<i>whirlwind</i>\n'
        '<i>plane travel</i>\n'
        '<a href="/spells/conjure-elemental-magic-user-lvl-5"><i>conjure elemental</i></a>\n'
        '<a href="/spells/telekinesis-magic-user-lvl-5"><i>telekinesis</i></a>\n\n'
        'The <i>whirlwind</i> is identical to that caused by a <a href="/creatures/djinni">djinni</a>. <i>Plane travel</i> is similar to the psionic ability of <i>probability travel</i> (q.v.), but travel is possible only to the various planes. The staff can be used to conjure 1 <i>elemental</i> of each type per day, each having 8 hit dice. <i>Telekinesis</i> is at 8th level also, i.e. 200 pounds maximum weight.\n\n'
        'The <i>staff of the magi</i> adds +2 to all saving throws versus magic. The staff can be used to <i>absorb</i> magic-user spell energy directed at its wielder, but if the staff absorbs energy beyond its charge limit it will explode just as if a "retributive strike" (see below) had been made. The spell levels of energy absorbed count only as recharging the staff, but they cannot be redirected immediately, so if <i>absorption</i> is desired, that is the only application possible by the staff wielder that round. Note also that the wielder has no idea of how many spell levels are cast at him, for the staff does not communicate this knowledge as does a <i>rod of absorption</i>. Therefore, absorbing spells can be risky. Absorption is the only way this staff can be recharged.\n\n'
        '<i>Retributive strike</i> is a breaking of the staff. It must be purposeful and declared by the magic-user wielding it. When this is done all levels of spell energy in the staff take hit points of damage equal to 8 times the number of spell levels of energy (1 to 25), those between 1"-2" take 6 x levels, and those 2"-3" distant take 4 x levels. Successful saving throws versus magic indicate only one-half damage is sustained. The magic-user breaking the staff has a 50% chance of <i>plane travelling</i> to another plane of existence, but if he or she does not, the explosive release of spell energy totally destroys him or her. This, and the <i>staff of power</i>, are the only magic items capable of a retributive strike.'
    )
),
MagicItem( name = 'Staff of Power',
    category = MagicItemCategory.STAVE,
    xp_value = [12000,12000],
    gold_value = [60000,60000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The <i>staff of power</i> is also a very potent magic item, with offensive and defensive abilities. It has these powers:\n\n'
        '<a href="/spells/continual-light-magic-user-lvl-2"><i>continual light</i></a>\n'
        '<a href="/spells/darkness-15-radius-magic-user-lvl-2"><i>darkness, 5\' radius</i></a>\n'
        '<a href="/spells/levitate-magic-user-lvl-2"><i>levitation</i></a>\n'
        '<a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a> or <a href="/spells/lightning-bolt-magic-use-lvl-3"><i>lightning bolt</i></a>\n'
        '<a href="/spells/ray-of-enfeeblement-magic-user-lvl-2"><i>ray of enfeeblement</i></a>\n'
        '<a href="/spells/cone-of-cold-magic-user-lvl-5"><i>cone of cold</i></a> or <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a>\n\n'
        'These functions cost 1 charge each. The following powers drain 2 charges each:\n\n'
        '<a href="/spells/shield-magic-user-lvl-1"><i>shield</a>, 5\' radius</i>\n'
        '<a href="/spells/globe-of-invulnerability-magic-user-lvl-6"><i>globe of invulnerability</i></a>\n'
        '<i>paralyzation</i>\n\n'
        '<i>Paralyzation</i> is a ray from the end of the staff which extends in a cone 4" long and 2" wide at its base.\n\n'
        'The wielder of this staff gains +2 on armor class and saving throws. He or she may use the staff to smite opponents. It strikes as a +2 magic weapon and does 3-8 hit points of damage; if 1 charge is expended, the staff does double damage, but 2 charges do not triple damage.\n\n'
        'You may determine alternate powers shown by random die roll.'
    )
),
MagicItem( name = 'Staff of the Serpent',
    category = MagicItemCategory.STAVE,
    xp_value = [7000,7000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('There are 2 varieties of this staff, the "Python" and the "Adder".\n\n'
        'The <i>python</i> strikes as a +2 magic weapon and does 3-8 hit points of damage when it hits. If the cleric throws the staff to the ground, its 6\' lengthens and thickens to become a constrictor snake, 25\' long (AC 3, 49 hit points, 9" movement). This happens in 1 round. The snake will <i>entwine</i> if it scores a hit, the opponent being constricted for 4-10 hit points of damage per round, and the victim will be so engaged until it or the <i>python</i> is destroyed. Note that the <i>python</i> will return to its owner upon command. If it is destroyed while in snake form the staff is destroyed.\n\n'
        'The <i>adder</i> strikes as a +1 magic weapon and does 2-4 hit points of damage when it hits. Upon command the head of the staff becomes that of an actual serpent (AC 5, 20 hit points). This head remains for 1 full turn. When a hit is scored, damage is not incresed, but the victim must save versus poison or be slain. Only evil clerics will employ an <i>adder</i> staff. If the snake head is killed, the staff is destroyed.\n\n'
        'Neither staff has or requires charges. 60% of these staves are <i>pythons</i>.'
    )
),
MagicItem( name = 'Staff of Striking',
    category = MagicItemCategory.STAVE,
    xp_value = [6000,6000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This oaken staff is the equivalent of a +3 magic weapon. (If weapon vs. armor type adjustment is made, the <i>staff of striking</i> is always treated as the most favorable weapon type vs. any armor.) It causes 4-9 (d6 +3) points of damage when a hit is scored. This expends a charge. If 2 charges are expended, bonus damage is doubled (d6 +6); if 3 charges are expended, bonus damage is tripled (d6 +9). No more than 3 charges can be expended per strike. The staff can be recharged.'
),
MagicItem( name = 'Staff of Withering',
    category = MagicItemCategory.STAVE,
    xp_value = [8000,8000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>staff of withering</i> is a +1 magic weapon. A hit from it causes 2-5 points of damage. If 2 charges are expended when a hit is scored, the creature struck will also age 10 years, its abilities and life span adjusted for the resulting age increase. If 3 charges are expended when a hit is made, 1 of the opponent creature\'s limbs can be made to shrivel and become useless unless it saves versus magic (check by random number generation for which member is struck). Note that ageless creatures (undead, demons, devils, etc.) cannot be aged or withered. Each effect of the staff is cumulative, so that 3 charges will score damage, age, <i>and</i> wither. Aging a dwarf is of little effect, while aging a dragon could actually aid the creature.'
),
MagicItem( name = 'Staff-Mace',
    category = MagicItemCategory.STAVE,
    xp_value = [1500,1500],
    gold_value = [12500,12500],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This clerical weapon appears as nothing more than a normal wooden staff of the type used when trekking in the wilderness. It gives off a very feint dweomer of the <i>alteration</i> sort. Upon command, it will take on one of these three forms, whichever is desired by the possessor:\n\n'
        'Quarterstaff: <i>quarterstaff +3</i>, iron-shod\n'
        'Great Mace: <i>footman\'s mace +1</i>, iron\n'
        'Mace: <i>horseman\'s mace +2</i>, iron\n\n'
        'This item is typically made of bronzewood, reinforced by heavy bands and tips of iron.'
    )
),
MagicItem( name = 'Staff of Slinging',
    category = MagicItemCategory.STAVE,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This magical quarterstaff appears to be nothing more than a +1 weapon - unless grasped by a druid, whereupon its power of slinging becomes evident. This power, which can only be employed by a druid, is activated when one end of the staff is touched to a heavy object of roughly spherical shape (a stone, metal ball, pottery crock, etc.) of up to nine inches in diameter, and five pounds in weight. The object adheres to the end of the staff, and the wielder need then only swing the staff in an overhand arc to release the missile toward a desired target. The missile leaves the staff on the down-stroke of the overhand swing and travels in a low, rising trajectory, with the missile going 1 foot upwards for every 1" traveled. Of course, the arc may be higher, or the missile aimed so as to travel nearly vertically - in the latter case, reverse the arcing ratio so that 1 foot of distance laterally is covered for every 1" of vertical rise. The maximum range of such a missile is 18", with limits of 6" and 12" on short and medium range, respectively.\n\n'
        'This staff also carries charges, and a druid wielding the item can expend 1 charge and thereby use the staff to hurl a missile of large size, just as if the wielder were a <a href="/creatures/stone-giant">stone giant</a>: range out to 30", 3-30 points of damage per hit. Whether used as a magical quarterstaff or by employing one of its slinging powers, the staff bestows +1 to the wielder\'s chance to hit and +1 per die to damage dealt out. The weapon may be recharged by a druid of 12th or higher level.'
    )
),
MagicItem( name = 'Staff-Spear',
    category = MagicItemCategory.STAVE,
    xp_value = [1000,3500],
    gold_value = [5000,25000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('When this seemingly ordinary quarterstaff is examined magically, it will have an aura of <i>alteration</i>. Upon proper command, it will shoot forth from its upper end a long and sharp spear blade which makes the weapon into a spear rather than a staff. Upon a second command, the length of the weapon will elongate to a full 12 feet, and the third command will recall it to its original form of a regular staff. The powers and value of each staff-spear are determined randomly when the item is first employed:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>To hit & damage</th><th>X.P. value</th><th>G.P. sale value</th></tr>'
        '<tr><td>1-6</td><td>+1</td><td>1000</td><td>1000</td><td>5000</td></tr>'
        '<tr><td>7-10</td><td>+2</td><td>1500</td><td>1500</td><td>7500</td></tr>'
        '<tr><td>11-13</td><td>+3</td><td>2000</td><td>2000</td><td>10000</td></tr>'
        '<tr><td>14-16</td><td>+4</td><td>2500</td><td>2500</td><td>15000</td></tr>'
        '<tr><td>17-19</td><td>+5</td><td>3000</td><td>3000</td><td>20000</td></tr>'
        '<tr><td>20</td><td>+3*</td><td>3500</td><td>3500</td><td>25000</td></tr>'
        '</table>'
        '* does damage as ranseur (2-8), but still acts as spear if used to thrust or when set to receive a charge'
    )
),
MagicItem( name = 'Staff of Swarming Insects',
    category = MagicItemCategory.STAVE,
    xp_value = [100,5000],
    gold_value = [500,25000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'A staff of this sort is typically shortish and quite stout. When initially obtained or encountered, much of its length is covered with finely done carvings depicting all sorts of winged biting and stinging flying insects (bees, deerflies, horseflies, wasps, and the like). Any cleric-type character (cleric, druid, shaman, witch doctor, etc.) holding it can command the staff to create a swarm of such insects, at the same time expending one of the staff\'s charges. Range is 6" +1" per clerical level of the user. The number of insects produced is 60 plus 10 per level. Every 10 insects will inflict 1 point of damage upon the target victim, regardless of armor class, unless the victim is protected by a force field, engulfed in flames, etc. Note, however, that the insects will not affect creatures larger than man-sized with a natural armor class of 5 or better. When a vulnerable target is attacked by the swarm of flying insects, the creature will be unable to do anything other than attempt to dislodge/kill the things. The insect attack lasts for 1 round. Each time the staff is employed, one of the insect-shapes carved into its wooden surface will disappear, so it is easy to determine how many charges are left in the staff. Unlike others of its ilk, a staff of this sort can have as many as 50 charges initially. However, it cannot be recharged.'
),
MagicItem( name = 'Staff of Thunder & Lightning',
    category = MagicItemCategory.STAVE,
    xp_value = [8000,8000],
    gold_value = [20000,20000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('Casual examination of this stout quarterstaff will show it to be exceptional, and if it is magically examined, it will radiate a dweomer of the <i>alteration</i> sort. Constructed of very stout wood (ash, oak, bronzewood, of the like) and bound with iron set with silver rivets, it has the properties of a +2 magic weapon without any expenditure of its magical charges. Its other magical properties are as follows:\n\n'
        'THUNDER: The staff strikes as a +3 weapon, and unless the opponent struck saves versus <i>rods, staves, and wands</i>, he, she, or it will be <i>stunned</i> from the noise of the staff\'s impact - unable to take any further action in the round struck, and automatically having last initiative in the following round. This power requires the expenditure of 1 charge.\n\n'
        'LIGHTNING: A short spark of electricity leaps forth when the opponent is struck, and in addition to staff damage, from 2-12 additional points of damage from shock are bestowed (cf. <i>wand of lightning</i>). Note that the staff might not score a hit, but the electrical discharge discounts any form of metal armor (making the target effectively AC 10 for this purpose), so only such damage might apply. This power requires the expenditure of 1 charge.\n\n'
        'THUNDERCLAP: The staff sends forth a cone of deafening noise, ½" wide at the apex, 4" long, and 2" wide at its furthest point from the source. All creatures within this cone, wholly or partially, must save versus <i>rods, staves, and wands</i> or be <i>stunned</i> for 1-2 rounds (unable to attack during this time) and unable to hear for 1-2 additional rounds. Those who save are unable to hear for 1-4 rounds, but suffer no loss of attacks. This function requires the expenditure of 2 charges.\n\n'
        'LIGHTNING STROKE: A bolt similar to that from a <i>wand of lightning</i> is generated, but it is of eight dice (8d6) strength, causing 16-48 points of damage (rolls of 1 are counted as 2) to those who fail a saving throw. The stroke can be single or forked. This function of the rod uses 2 charges.\n\n'
        'THUNDER & LIGHTNING: This power combines the <i>thunderclap</i>, described above, with a forked lightning bolt as in the <i>lightning stroke</i>. Damage from the lightning is a total of 8d6 with rolls of 1 or 2 counted as rolls of 3, for a range of 24-48 points. A saving throw applies, with deafness and half damage suffered by those who are successful. This power requires the expenditure of 4 charges.\n\n'
        'The time required to activate any function is a number of segments equal to the number of charges expended; thus, the <i>thunder & lightning</i> function costs 4 charges and requires 4 segments to operate.'
    )
),
MagicItem( name = 'Staff of the Woodlands',
    category = MagicItemCategory.STAVE,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This sort of staff is always made from oak, ask, or yew, finely grained, beautifully carved, and bound and shod with bronze. It is effective only in the hands of a druid. Each such staff has the following powers, which each expend one charge per use:\n\n'
        '<a href="/spells/wall-of-thorns-druid-lvl-6"><i>Wall of thorns</i></a>\n'
        '<a href="/spells/animal-friendship-druid-lvl-1"><i>Animal friendship</i></a> and <a href="/spells/speak-with-animals-druid-lvl-1"><i>speak with animals</i></a>\n'
        '<i>Animate tree</i>: This function duplicates the ability of a <a href="/creatures/treant">treant</a> to cause a large tree to move at a 3" rate and attack as if it were a largest-sized treant, and in all other respects become a virtual treant for eight rounds per charge expended. Note that one round is required for the tree to animate, and it will return to rooting on the eighth, so only six of the initial eight rounds are effectively available for attack function.\n\n'
        'In addition to these powers, each such staff has a magical weapon value, and those with a lesser value also have additional magical powers, which do not require charges and can be employed once per day. The <i>staff of the woodlands +4</i> has no additional powers. The <i>staff +3</i> also confers upon the user the power of a <a href="/spells/pass-without-trace-druid-lvl-1"><i>pass without trace</i></a> spell. The <i>staff +2</i> has the powers of <i>pass without trace</i> and <a href="/spells/barkskin-druid-lvl-2"><i>barkskin</i></a>. The <i>staff +1</i> confers the powers of the <i>staff +2</i> plus the power of the <a href="/spells/tree-druid-lvl-3"><i>tree</i></a> spell. To determine which sort of staff has been discovered, assign even chances for each of the four types.'
    )
)
]

wands = [
MagicItem( name = 'Wand of Conjuration'
    category = MagicItemCategory.WAND,
    xp_value = [7000,7000],
    gp_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Grasping of this device enables a magic-user to immediately recognize any cast or written magic-user conjuration/summoning spell (<a href="/spells/unseen-servant-magic-user-lvl-1"><i>unseen servant</i></a>, <i>monster summoning</i>, <a href="/spells/conjure-elemental-magic-user-lvl-5"><i>conjure elemental</i></a>, <a href="/spells/death-spell-magic-user-lvl-6"><i>death spell</i></a>, <a href="/spells/invisible-stalker-magic-user-lvl-6"><i>invisible stalker</i></a>, <a href="/spells/limited-wish-magic-user-lvl-7"><i>limited wish</i></a>, <a href="/spells/symbol-magic-user-lvl-8"><i>symbol</i></a>, <a href="/spells/maze-illusionist-lvl-5"><i>maze</i></a>, <a href="/spells/gate-magic-user-lvl-9"><i>gate</i></a>, <a href="/spells/prismatic-sphere-magic-user-lvl-9"><i>prismatic sphere</i></a>, <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>). The wand has the following powers which require expenditure of 1 charge:\n\n'
        '<i>unseen servant</i>\n'
        '<i>monster summoning</i>*\n\n'
        '* A maximum of 6 charges may be expended, 1 per level of the <i>monster summoning</i>, or 6 <a href="/spells/monster-summoning-i-magic-user-lvl-3"><i>monster summoning I</i></a>, 3 <a href="/spells/monster-summoning-ii-magic-user-lvl-4"><i>monster summoning II</i></a>, 2 <a href="/spells/monster-summoning-iii-magic-user-lvl-5"><i>monster summoning III</i></a>, or any combination totalling 6. The magic-user must be of a sufficient experience level to cast the appropriate <i>summoning</i> spell. The <i>monster summoning</i> takes 5 segments.\n\n'
        'The wand can also conjure up a <i>curtain of blackness</i> - a veil of total black which absorbs all light. The <i>curtain of blackness</i> can cover a maximum area of 600 square feet (60\' x 10\', 40\' x 15\', 30\' x 20\'), but it must stretch from ceiling to floor, wall to wall. The <i>curtain</i> costs 2 charges to conjure. The veil of total lightlessness can be penetrated only by physical means or magic. The wand also enables its wielder to construct a <a href="/spells/prismatic-sphere-magic-user-lvl-9"><i>prismatic sphere</i></a> (or <a href="/spells/prismatic-wall-illusionist-lvl-7"><i>wall</i></a>), once color at a time, red to violet, at a 1 charge per color cost. Each function of the wand takes 5 segments of time, and only 1 function per round is possible. The wand may be recharged.'
    )
),
MagicItem( name = 'Wand of Enemy Detection'
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gp_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand gives off a pulse and points in the direction of any hostile creature(s) intent upon the bearer of the device. The creature(s) can be invisible, ethereal, astral, out of phase, hidden, disguised, or in plain sight. Detection range is a 6" sphere. The function requires 1 charge to operate for 1 turn. The wand can be recharged.'
),
MagicItem( name = 'Wand of Fear'
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gp_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'When the <i>fear</i> wand is activated a pale amber ray springs from the tip of the wand, a cone 6" long by 2" in base diameter, which flashes on in 1 segment and instantly disappears. Each creature touched by the ray must save versus a <i>wand</i> or react as per the <a href="/spells/remove-fear-cleric-lvl-1"><i>fear</i></a> spell (first level cleric spell, <i>remove fear</i> reversal), i.e. turn and move at fastest possible speed away from the wand user for 6 rounds. Each usage costs 1 charge. It can operate but once per round. The wand can be recharged.'
),
MagicItem( name = 'Wand of Fire'
    category = MagicItemCategory.WAND,
    xp_value = [4500,4500],
    gp_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This wand can be employed in 4 separate functions which duplicate the following magic-user spells:\n\n'
        '1. <a href="/spells/burning-hands-magic-user-lvl-1"><i>Burning hands</i></a>: The wand emits a plane of fire, a fan-shaped sheet 10\' wide at its terminus and 12\' long. Each creature touched takes 6 hit points of damage. The plane appears in 1 segment, shoots forth its dark red flames, and snuffs out in less than 1 second. It expends 1 charge.\n\n'
        '2. <a href="/spells/pyrotechnics-magic-user-lvl-2"><i>Pyrotechnics</i></a>: This function exactly duplicates the spell of the same name. It requires 2 segments to activate. It expends 1 charge.\n\n'
        '3. <a href="/spells/fireball-magic-user-lvl-3"><i>Fireball</i></a>: The wand coughs forth a pea-sized sphere which streaks out to the desired range (or to a maximum of 16") and bursts in a fiery violet-red blast, exactly as a <i>fireball</i> cast by a spell of that name would. The function takes 2 segments. It expends 2 charges. The <i>fireball</i> does 6 hit dice of damage, but all 1\'s are counted as 2\'s, i.e. the burst does 12-36 hit points. A saving throw versus <i>wand</i> is applicable.\n\n'
        '4. <a href="/spells/wall-of-fire-magic-user-lvl-4"><i>Wall of fire</i></a>: The wand can be used to draw a fiery curtain of purplish-red flames which exactly duplicates the <i>wall of fire</i> spell cast by a magic-user, i.e. a sheet of flame 12 square " (1" x 12", 2" x 6", 3" x 4", etc.) which lasts for 6 rounds, causes 8-18 hit points damage (2d6 +6) if touched (2-8 hit points if within 1" of the fire, 1-4 if within 2"), and can also be made as a ring-shape around the wand user (but the circle is only 2¼" in diameter). This function requires 3 segments. It expends 2 charges.\n\n'
        'The <i>wand of fire</i> can operate but once per round. It can be recharged.'
    )
),
MagicItem( name = 'Wand of Frost'
    category = MagicItemCategory.WAND,
    xp_value = [6000,6000],
    gp_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>frost</i> wand can perform 3 functions which duplicate magic-user spells:\n\n'
        '1. <a href="/spells/ice-storm-magic-user-lvl-4"><i>Ice storm</i></a>: A silvery ray springs forth from the wand and in 1 segment an <i>ice</i> (or <i>sleet</i>) <i>storm</i> occurs up to 6" distant from the wand holder. This function requires 1 charge.\n\n'
        '2. <a href="/spells/wall-of-ice-magic-user-lvl-4"><i>Wall of Ice</i></a>: The silvery ray will form a <i>wall of ice</i>, 6 inches thick, and a square area equal to 6" (1" x 6", 2" x 3", etc.) in 2 segments at a cost of 1 charge.\n\n'
        '3. <a href="/spells/cone-of-cold-magic-user-lvl-5"><i>Cone of cold</i></a>: Dancing white crytalline motes spray forth from the wand in a cone with a 6" length and a terminal diameter of 2". The cold comes forth in 2 segments but lasts but 1 second. The temperature is c. -100°F., and damage is 6 hit dice, treating all 1\'s rolled as 2\'s (6d6, (12-36). The cost is 2 charges per use. Saving throw versus a <i>wand</i> is applicable.\n\n'
        'The wand can function but once per round, and may be recharged.'
    )
),
MagicItem( name = 'Wand of Illumination'
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gp_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This wand has 4 separate functions, 3 of which approximate magic-user spells, and 1 of which is singular:\n\n'
        '1. <a href="/spells/dancing-lights-magic-user-lvl-1"><i>Dancing lights</i></a>: In 1 segment the wand will produce this effect at a cost of 1 charge.\n\n'
        '2. <a href="/spells/light-magic-user-lvl-1"><i>Light</i></a>: The <i>illumination</i> wand sends forth <i>light</i> in 2 segments time at an expenditure of 1 charge.\n\n'
        '3. <a href="/spells/continual-light-magic-user-lvl-2"><i>Continual light</i></a>: This function requires only 2 segments to perform, but the cost is 2 charges.\n\n'
        '4. <i>Sunburst</i>: When this effect is called forth the wand delivers a sudden flash of brilliant greenish-white light, with blazing golden rays. The range of this <i>sunburst</i> is 12" maximum, and its duration is but 1/10 of a second. Its area of effect is a globe of 4" diameter. Any undead within this globe take 6-36 hit points of damage, with no saving throw. Creatures within or facing the burst must save versus a <i>wand</i> or be blinded for 2-12 segments and unable to do anything during that period. (Of course, the creatures in question must have ocular organs sensitive to the visible light spectrum). The function requires 3 segments and expends 3 charges.\n\n'
        'The wand can be recharged.'
    )
),
MagicItem( name = 'Wand of Illusion'
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gp_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>illusion</i> wand creates both audible and visual illusions (cf. <a href="/spells/audible-glamer-magic-user-lvl-2"><i>audible glamer</i></a>, <a href="/spells/phantasmal-force-magic-user-lvl-3"><i>phantasmal force</i></a>). The wand emits an invisible ray, with a 14" maximum range. The effect takes 3 segments to commence. The wand wielder must concentrate on the <i>illusion</i> in order to maintain it, but he or she may move normally (not melee) and still do so. Each portion - audible and visual - costs 1 charge to effect and 1 per round to continue. The wand may be recharged.'
),
MagicItem( name = 'Wand of Lightning'
    category = MagicItemCategory.WAND,
    xp_value = [4000,4000],
    gp_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This wand has 2 functions which closely resemble magic-user spells:\n\n'
        '1. <i>Shock</i>: This function causes the recipient to take 1-10 hit points of damage, with no saving throw, when struck in melee combat. Any "to hit" score discounts metallic armor and shield (giving opponents armor class 10) but not plain leather or wood. Magic bonuses on metallic armor do not affect armor class, but such items as a <i>ring of protection</i> do. The shock uses 1 charge.\n\n'
        '2. <a href="/spells/lightning-bolt-magic-use-lvl-3"><i>Lightning bolt</i></a>: The possessor of the wood can discharge a bolt of <i>lightning</i>. The stroke can be either the forked or straight bolt (cf. magic-user spell, <i>lightning bolt</i>). Damage is 12-36 (6d6, treating 1\'s as 2\'s), but a saving throw is applicable. This function uses 2 charges. It requires 2 segments to discharge.\n\n'
        'The wand may be recharged. It can perform but 1 function per round.'
    )
),
MagicItem( name = 'Wand of Magic Detection'
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gp_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand is similar in operation to the <i>enemy detection</i> wand. If any form of magic is in operation, or a magic item exists, within a 3" radius, the <i>magic detection</i> wand will pulse and point to the strongest source. Note that the wand will point to a person upon whom a spell has been cast. Operation requires 1 round, and successive rounds will point out successively less powerful magic radiation. The category of magic (abjuration, alteration, etc.) can be determined if one round is spent concentrating on the subject emanation. 1 charge is expended per turn (or fraction thereof) of use. Starting with the second round of continuous use, there is a 2% cumulative chance per round that the wand will temporarily malfunction and indicate non-magical items as magical, or vice-versa. The wand may be recharged.'
),
MagicItem( name = 'Wand of Metal and Mineral Detection'
    category = MagicItemCategory.WAND,
    xp_value = [1500,1500],
    gp_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand also has a 3" radius range and pulses and points to the largest mass of metal within its effective area of operation. However, the wielder can concentrate on a specific metal or mineral type (gold, platinum, quartz, beryl, diamond, corundum, etc.); if the specific type is within range the wand will point to any and all places it is located, and the wand possessor will know the approximate quantity as well. Each operation requires 1 round. Each charge powers the wand for 1 full turn. The wand may be recharged.'
),
MagicItem( name = 'Wand of Magic Missiles'
    category = MagicItemCategory.WAND,
    xp_value = [4000,4000],
    gp_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>missiles</i> wand discharges <i>magic missiles</i> which are similar to those of the first level magic-user spell, <a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a>. The device fires a <i>magic missile</i> which causes 2-5 hit points of damage. It operates as the spell of the same name, always hitting its target when wielded by a magic-user, otherwise requiring a "to hit" die roll. Each missile takes 3 segments to discharge, and costs 1 charge. A maximum of 2 may be expended in 1 round. The wand may be recharged.'
),
MagicItem( name = 'Wand of Negation'
    category = MagicItemCategory.WAND,
    xp_value = [3500,3500],
    gp_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device operates to negate the spell or spell-like function(s) of rods, staves, wands and other magical items. The individual with the <i>negation</i> wand points the device, and a pale gray beam shoots forth to touch the target - device or individual. This will totally negate any wand function, and make any other spell or spell-like function from a device 75% likely to be negated, whether it is a low-level spell, or even if it is an ultra-powerful spell. Operation of the wand requires but 1 segment of a round. It can function but once per round, and each negation drains 1 charge. The wand cannot be recharged.'
),
MagicItem( name = 'Wand of Paralyzation'
    category = MagicItemCategory.WAND,
    xp_value = [3500,3500],
    gp_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand shoots forth a thin ray of bluish color to a maximum range of 6". If the ray touches any creature it must save versus <i>wands</i> or be rigidly immobile for from 5-20 rounds. A save indicates the ray missed, and there was no effect. Each operation takes 3 segments and costs 1 charge. The wand may operate once per round. It may be recharged. (Note that as soon as the ray touches 1 creature it <i>stops</i>; the wand can attack only 1 target per round.)'
),
MagicItem( name = 'Wand of Polymorphing'
    category = MagicItemCategory.WAND,
    xp_value = [3500,3500],
    gp_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>polymorphing</i> wand emits a green beam, a thin ray which darts forth to a maximum distance of 6". If this beam touches any creature, it must make its saving throw versus <i>wands</i> (success indicating a miss) or be <a href="/spells/polymorph-other-magic-user-lvl-4"><i>polymorphed (others)</i></a> as the spell of the same name. The wand wielder may opt to form the victim into a snail, frog, insect, etc. as long as the result is a small and inoffensive creature. The possessor of the want may elect to <i>touch</i> a creature with the device instead. When this is done (unwilling creatures must be <i>hit</i> and they are also entitled to a saving throw) the recipient is surrounded by dancing motes of sparkling emerald light, and then transforms into whatever creature-shape the wand wielder has stated. This is the same magical effect as the <a href="/spells/polymorph-self-magic-user-lvl-4"><i>polymorph (self)</i></a> spell. Either function requires 3 segments. Each draws 1 charge. Only 1 function per round is possible. The wand may be recharged.'
),
MagicItem( name = 'Wand of Secret Door and Trap Location'
    category = MagicItemCategory.WAND,
    xp_value = [5000,5000],
    gp_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand has an effective radius of 1½" for secret door location, 3" for trap location. When the wand is energized it will pulse and point to whichever thing it is to locate if a secret door/trap is within location range. Note that it locates either one or the other, not both during one operation. It requires 1 round to function and draws 1 charge. The wand may be recharged.'
),
MagicItem( name = 'Wand of Wonder'
    category = MagicItemCategory.WAND,
    xp_value = [6000,6000],
    gp_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The <i>wand of wonder</i> is a strange and unpredictable device which will generate any number of strange effects, randomly, each time it is used. The usual effects are shown on the table below, but you may alter those for any or all of these wands in your campaign as you see fit, although it is recommended that you follow the <i>pattern</i> shown. The functions of the wand are:\n\n'
        '01-10: <a href="/spells/slow-magic-user-lvl-3"><i>slow</i></a> creature pointed at for 1 turn\n'
        '11-18: <i>deludes</i> wielder for 1 round into believing the wand functions as indicated by a second die roll\n'
        '19-25: <a href="/spells/gust-of-wind-magic-user-lvl-3"><i>gust of wind</i></a>, double force of spell\n'
        '26-30: <a href="/spells/stinking-cloud-magic-user-lvl-2"><i>stinking cloud</i></a> at 3" range\n'
        '31-33: <i>heavy rain</i> falls for 1 round in 6" radius of wand wielder\n'
        '34-36: <a href="/spells/monster-summoning-i-magic-user-lvl-3"><i>summon</i></a> <a href="/creatures/rhinoceros">rhino</a> (1-25), <a href="/creatures/elephant">elephant</a> (26-50) or mouse (51-00)\n'
        '37-46: <a href="/spells/lightning-bolt-magic-use-lvl-3"><i>lightning bolt</i></a> (7" x ½") as wand\n'
        '47-49: <i>stream of 600 large butterflies</i> pour forth and flutter around for 2 rounds, blinding everyone (including wielder)\n'
        '50-53: <a href="/spells/enlarge-magic-user-lvl-1"><i>enlarge</i></a> target if in 6" of wand\n'
        '54-58: <a href="/spells/darkness-15-radius-magic-user-lvl-2"><i>darkness</i></a> in a 3" diameter hemisphere at 3" center distance from wand\n'
        '59-62: <i>grass</i> grows in area of 16" square before wand, or grass existing there grows to 10 times normal size\n'
        '63-65: <i>vanish</i> any non-living object of up to 1,000 pounds mass and up to 30 cubic feet in size (object is ethereal)\n'
        '66-69: <i>diminish</i> wand wielder to 1/12\' height\n'
        '70-79: <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a> as wand\n'
        '80-84: <a href="/spells/invisibility-magic-user-lvl-2"><i>invisibility</i></a> covers wand wielder\n'
        '85-87: <i>leaves grow from target</i> if in 6" of wand\n'
        '88-90: <i>10-40 gems</i> of 1 g.p. base value shoot forth in a 3" long stream, each causing 1 h.p. or damage to any creature in path - roll 5d4 for number of hits\n'
        '91-97: <i>shimmering colors</i> dance and play over a 4" x 3" area in front of wand - creatures therein blinded for 1-6 rounds\n'
        '98-00: <a href="/spells/stone-to-flesh-magic-user-lvl-6"><i>flesh to stone</i></a> (or reverse if target is stone) if target is within 6"\n\n'
        'The wand uses 1 charge per function. It may not be recharged. Where applicable, saving throws should be made.'
    )
),
MagicItem( name = 'Anything Wand'
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gp_value = [12500,12500],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This device will perform as if it were an ordinary <i>wand of wonder</i>, although it will have no more than 50 usages before being totally expended. In addition, it has three other special uses: Upon command, it will perform as if it were any other sort of known wand, but it can only duplicate the effects of any given wand once. If it is commanded to duplicate a single kind of wand more than once, the second or third such command will have no effect - and after three such demands, successful or not, the wand will be totally drained and useless. The item cannot be recharged.'
),
MagicItem( name = 'Buckler Wand'
    category = MagicItemCategory.WAND,
    xp_value = [500,500],
    gp_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This is a shortish, thick wand about 1½ feet in length with an exceptionally sharp point on one end and a trigger mechanism built into the opposite end, which is blunt. The wand is usable by any character except one of the cleric class, and can be activated in a single segment. When the thick end is grasped firmly and the trigger pressed, the tip of the wand becomes the equivalent of a <i>dagger +1</i> and the rest of the shaft blossoms into a round shield of buckler size having a +1 magic value. The whole becomes equal to a <i>spiked buckler +1</i>. Because of its dweomer, it can be employed by magic-users, but no spells can be cast when it is in buckler form unless the possessor is a multi-classed character with fighter abilities in addition to magic-user abilities. A thief who employs the wand\'s powers cannot <i>climb walls</i> or perform other abilities requiring the use of his or her hands while holding the device.'
),
MagicItem( name = 'Wand of Defoliation'
    category = MagicItemCategory.WAND,
    xp_value = [1000,1000],
    gp_value = [6000,6000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This wand is never constructed of any sort of wood; instead, ivory or bone is typically the major component. It has the following functions:\n\n'
        'When 1 charge is expended, all chlorophyll in a 3" radius from the wand is destroyed. Thus, leaves turn to autumnal colors and drop off, grass becomes brown and dry, and so forth.\n\n'
        'When 2 charges are expended, all normal plant life within the 3" radius area of effect withers and dies. Sentient plant creatures and other non-normal sorts of plants will not necessarily be killed, but they will each suffer 1-6 (1d6) points of damage. If so desired, the possessor of the wand can direct the force of this power into a cone-shaped area of 3" length, widening to 1" diameter at the farthest point from the wand. Effects are the same as for the spherical area of effect, except that sentient and non-normal plant life within the cone will suffer 6-36 points of damage (6d6) instead of only 1-6. Any plant-creature or other non-normal plant that lies partially within the conical area of effect is entitled to a saving throw (versus <i>rods, staves, and wands</i>), and if successful takes only one-half damage (3d6).'
    )
),
MagicItem( name = 'Wand of Earth and Stone'
    category = MagicItemCategory.WAND,
    xp_value = [1000,1500],
    gp_value = [10000,15000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('A wand of this sort is typically of shortish length and tipped with some form of mineral. It is imbued with the following dweomers:\n\n'
        '<a href="/spells/dig-magic-user-lvl-4"><i>Dig</i></a> ½ charge per use\n'
        '<a href="/spells/passwall-magic-user-lvl-5"><i>Passwall</i></a> 1 charge per use\n'
        '<a href="/spells/move-earth-magic-user-lvl-6"><i>Move earth</i></a> 2 charges per use\n\n'
        'In addition, 50% of all such wands (the higher-valued ones) have the following two powers:\n\n'
        '<a href="/spells/transmute-rock-to-mud-magic-user-lvl-5"><i>Transmute mud to rock</i></a> 1 charge per use\n'
        '<i>Transmute rock to mud</i> 1 charge per use'
    )
),
MagicItem( name = 'Wand of Fireballs'
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gp_value = [16000,16000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This wand simply enables the wielder to cast a <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a> spell as if he or she were a magic-user of 6th level. The wand takes only 1 segment to activate and 1 segment to activate the <i>fireball</i>. Damage is 6-36 points (6d6), with saving throw applicable for half damage. The wand can be recharged by any magic-user of 8th or higher level.'
),
MagicItem( name = 'Wand of Flame Extinguishing'
    category = MagicItemCategory.WAND,
    xp_value = [1250,1250],
    gp_value = [10000,10000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This sort of wand has three separate functions:\n\n'
        'When applied to fires of normal sort and size, no charges are expended in extinguishing such fires. Normal size includes anything up to the size of a bonfire or a fire in a regular fireplace - equal to four to six billets of wood burning hotly.\n\n'
        'When applied to large normal fires, flaming oil in quantity equal to a gallon or more, the fire produced by a demon or devil, a <i>flame tongue</i> sword, or a <a href="/spells/burning-hands-magic-user-lvl-1"><i>burning hands</i></a> spell, 1 charge is expended from the wand. Continual magic flames, such as those of a sword or a creature able to ignite, will be extinguished for 6 rounds and will flare up again after that time.\n\n'
        'When applied to large magical fires such as a <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a>, <a href="/spells/flame-strike-cleric-lvl-5"><i>flame strike</i></a>, or <a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a>, 2 charges are expended from the wand as the flames are extinguished.\n\n'
        'If one charge of the device is used upon a creature which is composed of flame (a <a href="/creatures/fire-elemental">fire elemental</a>, for instance), the wand inflicts 6-36 (6d6) points of damage upon the creature.'
    )
),
MagicItem( name = 'Wand of Force'
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gp_value = [30000,30000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('Although it is rumored that the concept of such a wand has taken many forms, the one which has been standardized, so to speak, is a tri-function device which requires considerable operator knowledge only in the application of its third function.\n\n'
        'Firstly, a <i>wand of force</i> enables the wielder to cause a shaft of nearly invisible, blue-white energy to spring forth from its tip. This shaft of energy extends 4 feet and is equal to a +5 bastard sword with respect to hit probability and damage. This usage expends 1 charge per turn.\n\n'
        'Secondly, a <i>wand of force</i> can be employed to create a <a href="/spells/wall-of-force-magic-user-lvl-5"><i>wall of force</i></a> duplicating the fifth-level magic-user spell of the same name as if cast by a 10th-level magic-user. This function expends 1 charge per <i>wall</i> created, and a single usage per round is possible.\n\n'
        'Thirdly, a <i>wand of force</i> can be employed to create a nearly invisible plane of energy which performs as if it had been created by the casting of a <a href="/spells/bigbys-forceful-hand-magic-user-lvl-6"><i>Bigby\'s Forceful Hand</i></a> spell. The wand user must actually be a magic-user in order to activate this function, and regardless of his or her level, one of the various <i>Bigby\'s Hand/Fist</i> spells must be recorded for study (not necessarily for casting) in the spell books of the wand wielder. Use of this function expends ½ charge per round.\n\n'
        'Fighters of all types are able to use the first and second functions of the wand. The device can be recharged by a magic-user of 16th or higher level, and in addition it can draw sufficient energy to regain a single charge by being touched to any of the following: a manifestation of one of the <i>Bigby\'s Hand/Fist</i> spells, a manifestation of the <a href="/spells/mordenkainens-sword-magic-user-lvl-7"><i>Mordenkainen\'s Sword</i></a> spell, or a manifestation of a <i>wall of force</i>. Touching any of these things with the wand causes the effect of a <a href="/spells/disintegrate-magic-user-lvl-6"><i>disintegrate</i></a> spell, destroying the spell/manifestation instantly, and enabling the wand to absorb power equivalent to a single charge.'
    )
),
MagicItem( name = 'Wand of Ice Storms'
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gp_value = [20000,20000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This device enables the wielder to cause an <a href="/spells/ice-storm-magic-user-lvl-4"><i>ice storm</i></a> just as if he or she were a magic-user of 7th level. Either damaging hail or sleet and slippery conditions are possible (see the <i>ice storm</i> spell explanation). Activation time is 1 segment, and causing the dweomer to emerge from the wand likewise requires 1 segment. The wand can be recharged by a magic-user of 9th or higher level.'
),
MagicItem( name = 'Wand of Lightning Bolts'
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gp_value = [16000,16000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'A wand of this nature enables the possessor to cast a <a href="/spells/lightning-bolt-magic-use-lvl-3"><i>lightning bolt</i></a> as if he or she were a magic-user of 6th level. Damage is 6-36 (6d6) points, with saving throw applicable for half damage. Either form of bolt (forked or single stroke) is possible. The wand takes 1 segment to activate, and another 1 segment is required to discharge the lightning. The device can be recharged by a magic-user of 8th or higher level.'
),
MagicItem( name = 'Wand of Metal Command'
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gp_value = [10000,10000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This wand appears to be nothing more useful than a <i>wand of metal and mineral detection</i>, but in the hands of a <a href="/creatures/dwarf">dwarf</a> or <a href="/spells/gnome">gnome</a>, its exceptional powers become operational:\n\n'
        'If 1 charge is expended, the wand can transmute gold to lead, or lead to gold. The range of this power is 3", and the amount of metal so converted will be 1 to 6 pounds (10 to 60 gp weight).\n\n'
        'If 2 charges are expended, the user can <a href="/spells/heat-metal-druid-lvl-2"><i>heat metal</i></a> in the same fashion as the druid spell of the same name. Range is 3", and only a single target area of 3-foot diameter can be affected, causing up to 600 gp weight of metal within this area to become heated.\n\n'
        'If 3 charges are expended, the possessor of the wand can cast any one of the following spells just as if he or she were an 18th-level magic-user: <a href="/spells/crystalbrittle-magic-user-lvl-9"><i>crystalbrittle</i></a>, <a href="/spells/glassee-magic-user-lvl-6"><i>glassee</i></a>, or <a href="/spells/glassteel-magic-user-lvl-8"><i>glassteel</i></a>.'
    )
)
MagicItem( name = 'Wand of Size Alteration'
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gp_value = [20000,20000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'A wand of this sort enables the wielder to cause any single creature of virtually and size to <i>enlarge</i> or <i>diminish</i> in size. Either effect will cause a 50% change in size. Relative strength and power also increases or decreases proportionally, providing the weaponry employed is proportionate - or usable. For humanoid creatures enlarged, strength is roughly proportionate to that of a giant of corresponding size; for example, 9 feet tall equals a <a href="/creature/hill-giant">hill giant</a> and 19 strength, 13 feet tall equals a <a href="/creatures/fire-giant">fire giant</a> and 22 strength. The wand\'s power has a range of 1". The target creature and all it is wearing or carrying is affected unless a saving throw succeeds - but note that a willing target need not make a saving throw. The effect of the wand can be removed by a <a href="/spells/dispel-magic-cleric-lvl-3"><i>dispel magic</i></a> spell, but if this is done the target must make a system shock roll. It can also be countered if the possessor of the wand wills the effect to be cancelled before the duration of the effect expires. Each usage of the wand (but not the cancellation of an effect) expends 1 charge. It can be recharged by a magic-user of 12th or higher level.'
)
MagicItem( name = 'Wand of Steam and Vapor'
    category = MagicItemCategory.WAND,
    xp_value = [4500,4500],
    gp_value = [25000,25000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('A wand of this sort has two separate functions, each of which requires the expenditure of 1 charge:\n\n'
        'STEAM: In one segment the wand will spout forth a jet of super-heated steam in a cone 1" x 3" x 5". Any creature within this area takes 6-36 (6d6) points of damage. The cloud persists, slowly cooling, so that on the second round it inflicts 4d6 damage, and on the third and last round it causes 2d6 damage. Saving throws apply for half damage in all cases. Naturally, fire-dwelling or fire-using creatures will not be harmed by the steam - unless they are harmed by dampness.\n\n'
        'VAPOR: In one segment the wand will gout forth billows of warm, steamy vapors. These vapors are equal to a <a href="/spells/fog-cloud-illusionist-lvl-2"><i>fog cloud</i></a> of 4" depth, 6" height, and 8" breadth. This vaporous cloud persists for 6 rounds, remaining stationary unless moved about by magical or non-magical breezes or winds. Cold-using creatures will suffer 1 point of damage per round while inside the vapor cloud, and cold-dwelling creatures will take twice that amount of damage.'
    )
)
]
