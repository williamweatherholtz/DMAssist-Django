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
        activation_time = TimePeriod(0, TimeUnit.round),
        xp_value = [0,0],
        gold_value = [0,0]
    ):
        self.name = name
        self.category = category
        self.xp_value = xp_value
        self.gold_value = gold_value
        self.activation_time = activation_time
        self.source = source
        self.description = desc

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
    desc = ('This magical substance resembles the fine oil used to clean and protect metal armor and weapons. If it is carefully rubbed on the blade of any edged or pointed weapon, the oil will have the effect of making it equivalent to a magic weapon. One such application will last for 9-12 rounds. A flask of the substance will contain from 3-5 applications. The dweomer of the <i>oil of sharpness</i> is determined by die roll:\n\n'
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
    activation_time = TimePeriod(6, TimeUnit.segment),
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
    desc = 'This ring enables the wearer to move and attack freely and normally whether attacked by a <a href="/spells/web-magic-user-lvl-2"><i>web</i></a>, <a href="/spells/hold-monster-magic-user-lvl-5"><i>hold</i></a>, or <a href="/spells/slow-magic-user-lvl-3"><i>slow</i></a> spell, or even while under water. In the former case the spells have no effect, while in the latter the individual moves at normal (surface) speed and does full damage even with such cutting weapons as axes and scimitars and with such smashing weapons as flails, hammers, and maces, insofar as the weapon used is held rather than hurled. This will not, however, enable <i>water breathing</i> without the further appropriate magic.'
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
        '<a href="/spells/lightning-bolt-magic-user-lvl-3"><i>lightning bolt</i></a>\n'
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
        '<a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a> or <a href="/spells/lightning-bolt-magic-user-lvl-3"><i>lightning bolt</i></a>\n'
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
MagicItem( name = 'Wand of Conjuration',
    category = MagicItemCategory.WAND,
    xp_value = [7000,7000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Grasping of this device enables a magic-user to immediately recognize any cast or written magic-user conjuration/summoning spell (<a href="/spells/unseen-servant-magic-user-lvl-1"><i>unseen servant</i></a>, <i>monster summoning</i>, <a href="/spells/conjure-elemental-magic-user-lvl-5"><i>conjure elemental</i></a>, <a href="/spells/death-spell-magic-user-lvl-6"><i>death spell</i></a>, <a href="/spells/invisible-stalker-magic-user-lvl-6"><i>invisible stalker</i></a>, <a href="/spells/limited-wish-magic-user-lvl-7"><i>limited wish</i></a>, <a href="/spells/symbol-magic-user-lvl-8"><i>symbol</i></a>, <a href="/spells/maze-illusionist-lvl-5"><i>maze</i></a>, <a href="/spells/gate-magic-user-lvl-9"><i>gate</i></a>, <a href="/spells/prismatic-sphere-magic-user-lvl-9"><i>prismatic sphere</i></a>, <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>). The wand has the following powers which require expenditure of 1 charge:\n\n'
        '<i>unseen servant</i>\n'
        '<i>monster summoning</i>*\n\n'
        '* A maximum of 6 charges may be expended, 1 per level of the <i>monster summoning</i>, or 6 <a href="/spells/monster-summoning-i-magic-user-lvl-3"><i>monster summoning I</i></a>, 3 <a href="/spells/monster-summoning-ii-magic-user-lvl-4"><i>monster summoning II</i></a>, 2 <a href="/spells/monster-summoning-iii-magic-user-lvl-5"><i>monster summoning III</i></a>, or any combination totalling 6. The magic-user must be of a sufficient experience level to cast the appropriate <i>summoning</i> spell. The <i>monster summoning</i> takes 5 segments.\n\n'
        'The wand can also conjure up a <i>curtain of blackness</i> - a veil of total black which absorbs all light. The <i>curtain of blackness</i> can cover a maximum area of 600 square feet (60\' x 10\', 40\' x 15\', 30\' x 20\'), but it must stretch from ceiling to floor, wall to wall. The <i>curtain</i> costs 2 charges to conjure. The veil of total lightlessness can be penetrated only by physical means or magic. The wand also enables its wielder to construct a <a href="/spells/prismatic-sphere-magic-user-lvl-9"><i>prismatic sphere</i></a> (or <a href="/spells/prismatic-wall-illusionist-lvl-7"><i>wall</i></a>), once color at a time, red to violet, at a 1 charge per color cost. Each function of the wand takes 5 segments of time, and only 1 function per round is possible. The wand may be recharged.'
    )
),
MagicItem( name = 'Wand of Enemy Detection',
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand gives off a pulse and points in the direction of any hostile creature(s) intent upon the bearer of the device. The creature(s) can be invisible, ethereal, astral, out of phase, hidden, disguised, or in plain sight. Detection range is a 6" sphere. The function requires 1 charge to operate for 1 turn. The wand can be recharged.'
),
MagicItem( name = 'Wand of Fear',
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'When the <i>fear</i> wand is activated a pale amber ray springs from the tip of the wand, a cone 6" long by 2" in base diameter, which flashes on in 1 segment and instantly disappears. Each creature touched by the ray must save versus a <i>wand</i> or react as per the <a href="/spells/remove-fear-cleric-lvl-1"><i>fear</i></a> spell (first level cleric spell, <i>remove fear</i> reversal), i.e. turn and move at fastest possible speed away from the wand user for 6 rounds. Each usage costs 1 charge. It can operate but once per round. The wand can be recharged.'
),
MagicItem( name = 'Wand of Fire',
    category = MagicItemCategory.WAND,
    xp_value = [4500,4500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This wand can be employed in 4 separate functions which duplicate the following magic-user spells:\n\n'
        '1. <a href="/spells/burning-hands-magic-user-lvl-1"><i>Burning hands</i></a>: The wand emits a plane of fire, a fan-shaped sheet 10\' wide at its terminus and 12\' long. Each creature touched takes 6 hit points of damage. The plane appears in 1 segment, shoots forth its dark red flames, and snuffs out in less than 1 second. It expends 1 charge.\n\n'
        '2. <a href="/spells/pyrotechnics-magic-user-lvl-2"><i>Pyrotechnics</i></a>: This function exactly duplicates the spell of the same name. It requires 2 segments to activate. It expends 1 charge.\n\n'
        '3. <a href="/spells/fireball-magic-user-lvl-3"><i>Fireball</i></a>: The wand coughs forth a pea-sized sphere which streaks out to the desired range (or to a maximum of 16") and bursts in a fiery violet-red blast, exactly as a <i>fireball</i> cast by a spell of that name would. The function takes 2 segments. It expends 2 charges. The <i>fireball</i> does 6 hit dice of damage, but all 1\'s are counted as 2\'s, i.e. the burst does 12-36 hit points. A saving throw versus <i>wand</i> is applicable.\n\n'
        '4. <a href="/spells/wall-of-fire-magic-user-lvl-4"><i>Wall of fire</i></a>: The wand can be used to draw a fiery curtain of purplish-red flames which exactly duplicates the <i>wall of fire</i> spell cast by a magic-user, i.e. a sheet of flame 12 square " (1" x 12", 2" x 6", 3" x 4", etc.) which lasts for 6 rounds, causes 8-18 hit points damage (2d6 +6) if touched (2-8 hit points if within 1" of the fire, 1-4 if within 2"), and can also be made as a ring-shape around the wand user (but the circle is only 2¼" in diameter). This function requires 3 segments. It expends 2 charges.\n\n'
        'The <i>wand of fire</i> can operate but once per round. It can be recharged.'
    )
),
MagicItem( name = 'Wand of Frost',
    category = MagicItemCategory.WAND,
    xp_value = [6000,6000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>frost</i> wand can perform 3 functions which duplicate magic-user spells:\n\n'
        '1. <a href="/spells/ice-storm-magic-user-lvl-4"><i>Ice storm</i></a>: A silvery ray springs forth from the wand and in 1 segment an <i>ice</i> (or <i>sleet</i>) <i>storm</i> occurs up to 6" distant from the wand holder. This function requires 1 charge.\n\n'
        '2. <a href="/spells/wall-of-ice-magic-user-lvl-4"><i>Wall of Ice</i></a>: The silvery ray will form a <i>wall of ice</i>, 6 inches thick, and a square area equal to 6" (1" x 6", 2" x 3", etc.) in 2 segments at a cost of 1 charge.\n\n'
        '3. <a href="/spells/cone-of-cold-magic-user-lvl-5"><i>Cone of cold</i></a>: Dancing white crytalline motes spray forth from the wand in a cone with a 6" length and a terminal diameter of 2". The cold comes forth in 2 segments but lasts but 1 second. The temperature is c. -100°F., and damage is 6 hit dice, treating all 1\'s rolled as 2\'s (6d6, (12-36). The cost is 2 charges per use. Saving throw versus a <i>wand</i> is applicable.\n\n'
        'The wand can function but once per round, and may be recharged.'
    )
),
MagicItem( name = 'Wand of Illumination',
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This wand has 4 separate functions, 3 of which approximate magic-user spells, and 1 of which is singular:\n\n'
        '1. <a href="/spells/dancing-lights-magic-user-lvl-1"><i>Dancing lights</i></a>: In 1 segment the wand will produce this effect at a cost of 1 charge.\n\n'
        '2. <a href="/spells/light-magic-user-lvl-1"><i>Light</i></a>: The <i>illumination</i> wand sends forth <i>light</i> in 2 segments time at an expenditure of 1 charge.\n\n'
        '3. <a href="/spells/continual-light-magic-user-lvl-2"><i>Continual light</i></a>: This function requires only 2 segments to perform, but the cost is 2 charges.\n\n'
        '4. <i>Sunburst</i>: When this effect is called forth the wand delivers a sudden flash of brilliant greenish-white light, with blazing golden rays. The range of this <i>sunburst</i> is 12" maximum, and its duration is but 1/10 of a second. Its area of effect is a globe of 4" diameter. Any undead within this globe take 6-36 hit points of damage, with no saving throw. Creatures within or facing the burst must save versus a <i>wand</i> or be blinded for 2-12 segments and unable to do anything during that period. (Of course, the creatures in question must have ocular organs sensitive to the visible light spectrum). The function requires 3 segments and expends 3 charges.\n\n'
        'The wand can be recharged.'
    )
),
MagicItem( name = 'Wand of Illusion',
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>illusion</i> wand creates both audible and visual illusions (cf. <a href="/spells/audible-glamer-magic-user-lvl-2"><i>audible glamer</i></a>, <a href="/spells/phantasmal-force-magic-user-lvl-3"><i>phantasmal force</i></a>). The wand emits an invisible ray, with a 14" maximum range. The effect takes 3 segments to commence. The wand wielder must concentrate on the <i>illusion</i> in order to maintain it, but he or she may move normally (not melee) and still do so. Each portion - audible and visual - costs 1 charge to effect and 1 per round to continue. The wand may be recharged.'
),
MagicItem( name = 'Wand of Lightning',
    category = MagicItemCategory.WAND,
    xp_value = [4000,4000],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This wand has 2 functions which closely resemble magic-user spells:\n\n'
        '1. <i>Shock</i>: This function causes the recipient to take 1-10 hit points of damage, with no saving throw, when struck in melee combat. Any "to hit" score discounts metallic armor and shield (giving opponents armor class 10) but not plain leather or wood. Magic bonuses on metallic armor do not affect armor class, but such items as a <i>ring of protection</i> do. The shock uses 1 charge.\n\n'
        '2. <a href="/spells/lightning-bolt-magic-user-lvl-3"><i>Lightning bolt</i></a>: The possessor of the wood can discharge a bolt of <i>lightning</i>. The stroke can be either the forked or straight bolt (cf. magic-user spell, <i>lightning bolt</i>). Damage is 12-36 (6d6, treating 1\'s as 2\'s), but a saving throw is applicable. This function uses 2 charges. It requires 2 segments to discharge.\n\n'
        'The wand may be recharged. It can perform but 1 function per round.'
    )
),
MagicItem( name = 'Wand of Magic Detection',
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand is similar in operation to the <i>enemy detection</i> wand. If any form of magic is in operation, or a magic item exists, within a 3" radius, the <i>magic detection</i> wand will pulse and point to the strongest source. Note that the wand will point to a person upon whom a spell has been cast. Operation requires 1 round, and successive rounds will point out successively less powerful magic radiation. The category of magic (abjuration, alteration, etc.) can be determined if one round is spent concentrating on the subject emanation. 1 charge is expended per turn (or fraction thereof) of use. Starting with the second round of continuous use, there is a 2% cumulative chance per round that the wand will temporarily malfunction and indicate non-magical items as magical, or vice-versa. The wand may be recharged.'
),
MagicItem( name = 'Wand of Metal and Mineral Detection',
    category = MagicItemCategory.WAND,
    xp_value = [1500,1500],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand also has a 3" radius range and pulses and points to the largest mass of metal within its effective area of operation. However, the wielder can concentrate on a specific metal or mineral type (gold, platinum, quartz, beryl, diamond, corundum, etc.); if the specific type is within range the wand will point to any and all places it is located, and the wand possessor will know the approximate quantity as well. Each operation requires 1 round. Each charge powers the wand for 1 full turn. The wand may be recharged.'
),
MagicItem( name = 'Wand of Magic Missiles',
    category = MagicItemCategory.WAND,
    xp_value = [4000,4000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>missiles</i> wand discharges <i>magic missiles</i> which are similar to those of the first level magic-user spell, <a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a>. The device fires a <i>magic missile</i> which causes 2-5 hit points of damage. It operates as the spell of the same name, always hitting its target when wielded by a magic-user, otherwise requiring a "to hit" die roll. Each missile takes 3 segments to discharge, and costs 1 charge. A maximum of 2 may be expended in 1 round. The wand may be recharged.'
),
MagicItem( name = 'Wand of Negation',
    category = MagicItemCategory.WAND,
    xp_value = [3500,3500],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device operates to negate the spell or spell-like function(s) of rods, staves, wands and other magical items. The individual with the <i>negation</i> wand points the device, and a pale gray beam shoots forth to touch the target - device or individual. This will totally negate any wand function, and make any other spell or spell-like function from a device 75% likely to be negated, whether it is a low-level spell, or even if it is an ultra-powerful spell. Operation of the wand requires but 1 segment of a round. It can function but once per round, and each negation drains 1 charge. The wand cannot be recharged.'
),
MagicItem( name = 'Wand of Paralyzation',
    category = MagicItemCategory.WAND,
    xp_value = [3500,3500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand shoots forth a thin ray of bluish color to a maximum range of 6". If the ray touches any creature it must save versus <i>wands</i> or be rigidly immobile for from 5-20 rounds. A save indicates the ray missed, and there was no effect. Each operation takes 3 segments and costs 1 charge. The wand may operate once per round. It may be recharged. (Note that as soon as the ray touches 1 creature it <i>stops</i>; the wand can attack only 1 target per round.)'
),
MagicItem( name = 'Wand of Polymorphing',
    category = MagicItemCategory.WAND,
    xp_value = [3500,3500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>polymorphing</i> wand emits a green beam, a thin ray which darts forth to a maximum distance of 6". If this beam touches any creature, it must make its saving throw versus <i>wands</i> (success indicating a miss) or be <a href="/spells/polymorph-other-magic-user-lvl-4"><i>polymorphed (others)</i></a> as the spell of the same name. The wand wielder may opt to form the victim into a snail, frog, insect, etc. as long as the result is a small and inoffensive creature. The possessor of the want may elect to <i>touch</i> a creature with the device instead. When this is done (unwilling creatures must be <i>hit</i> and they are also entitled to a saving throw) the recipient is surrounded by dancing motes of sparkling emerald light, and then transforms into whatever creature-shape the wand wielder has stated. This is the same magical effect as the <a href="/spells/polymorph-self-magic-user-lvl-4"><i>polymorph (self)</i></a> spell. Either function requires 3 segments. Each draws 1 charge. Only 1 function per round is possible. The wand may be recharged.'
),
MagicItem( name = 'Wand of Secret Door and Trap Location',
    category = MagicItemCategory.WAND,
    xp_value = [5000,5000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This wand has an effective radius of 1½" for secret door location, 3" for trap location. When the wand is energized it will pulse and point to whichever thing it is to locate if a secret door/trap is within location range. Note that it locates either one or the other, not both during one operation. It requires 1 round to function and draws 1 charge. The wand may be recharged.'
),
MagicItem( name = 'Wand of Wonder',
    category = MagicItemCategory.WAND,
    xp_value = [6000,6000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The <i>wand of wonder</i> is a strange and unpredictable device which will generate any number of strange effects, randomly, each time it is used. The usual effects are shown on the table below, but you may alter those for any or all of these wands in your campaign as you see fit, although it is recommended that you follow the <i>pattern</i> shown. The functions of the wand are:\n\n'
        '01-10: <a href="/spells/slow-magic-user-lvl-3"><i>slow</i></a> creature pointed at for 1 turn\n'
        '11-18: <i>deludes</i> wielder for 1 round into believing the wand functions as indicated by a second die roll\n'
        '19-25: <a href="/spells/gust-of-wind-magic-user-lvl-3"><i>gust of wind</i></a>, double force of spell\n'
        '26-30: <a href="/spells/stinking-cloud-magic-user-lvl-2"><i>stinking cloud</i></a> at 3" range\n'
        '31-33: <i>heavy rain</i> falls for 1 round in 6" radius of wand wielder\n'
        '34-36: <a href="/spells/monster-summoning-i-magic-user-lvl-3"><i>summon</i></a> <a href="/creatures/rhinoceros">rhino</a> (1-25), <a href="/creatures/elephant">elephant</a> (26-50) or mouse (51-00)\n'
        '37-46: <a href="/spells/lightning-bolt-magic-user-lvl-3"><i>lightning bolt</i></a> (7" x ½") as wand\n'
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
MagicItem( name = 'Anything Wand',
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gold_value = [12500,12500],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This device will perform as if it were an ordinary <i>wand of wonder</i>, although it will have no more than 50 usages before being totally expended. In addition, it has three other special uses: Upon command, it will perform as if it were any other sort of known wand, but it can only duplicate the effects of any given wand once. If it is commanded to duplicate a single kind of wand more than once, the second or third such command will have no effect - and after three such demands, successful or not, the wand will be totally drained and useless. The item cannot be recharged.'
),
MagicItem( name = 'Buckler Wand',
    category = MagicItemCategory.WAND,
    xp_value = [500,500],
    gold_value = [5000,5000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This is a shortish, thick wand about 1½ feet in length with an exceptionally sharp point on one end and a trigger mechanism built into the opposite end, which is blunt. The wand is usable by any character except one of the cleric class, and can be activated in a single segment. When the thick end is grasped firmly and the trigger pressed, the tip of the wand becomes the equivalent of a <i>dagger +1</i> and the rest of the shaft blossoms into a round shield of buckler size having a +1 magic value. The whole becomes equal to a <i>spiked buckler +1</i>. Because of its dweomer, it can be employed by magic-users, but no spells can be cast when it is in buckler form unless the possessor is a multi-classed character with fighter abilities in addition to magic-user abilities. A thief who employs the wand\'s powers cannot <i>climb walls</i> or perform other abilities requiring the use of his or her hands while holding the device.'
),
MagicItem( name = 'Wand of Defoliation',
    category = MagicItemCategory.WAND,
    xp_value = [1000,1000],
    gold_value = [6000,6000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This wand is never constructed of any sort of wood; instead, ivory or bone is typically the major component. It has the following functions:\n\n'
        'When 1 charge is expended, all chlorophyll in a 3" radius from the wand is destroyed. Thus, leaves turn to autumnal colors and drop off, grass becomes brown and dry, and so forth.\n\n'
        'When 2 charges are expended, all normal plant life within the 3" radius area of effect withers and dies. Sentient plant creatures and other non-normal sorts of plants will not necessarily be killed, but they will each suffer 1-6 (1d6) points of damage. If so desired, the possessor of the wand can direct the force of this power into a cone-shaped area of 3" length, widening to 1" diameter at the farthest point from the wand. Effects are the same as for the spherical area of effect, except that sentient and non-normal plant life within the cone will suffer 6-36 points of damage (6d6) instead of only 1-6. Any plant-creature or other non-normal plant that lies partially within the conical area of effect is entitled to a saving throw (versus <i>rods, staves, and wands</i>), and if successful takes only one-half damage (3d6).'
    )
),
MagicItem( name = 'Wand of Earth and Stone',
    category = MagicItemCategory.WAND,
    xp_value = [1000,1500],
    gold_value = [10000,15000],
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
MagicItem( name = 'Wand of Fireballs',
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gold_value = [16000,16000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This wand simply enables the wielder to cast a <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a> spell as if he or she were a magic-user of 6th level. The wand takes only 1 segment to activate and 1 segment to activate the <i>fireball</i>. Damage is 6-36 points (6d6), with saving throw applicable for half damage. The wand can be recharged by any magic-user of 8th or higher level.'
),
MagicItem( name = 'Wand of Flame Extinguishing',
    category = MagicItemCategory.WAND,
    xp_value = [1250,1250],
    gold_value = [10000,10000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This sort of wand has three separate functions:\n\n'
        'When applied to fires of normal sort and size, no charges are expended in extinguishing such fires. Normal size includes anything up to the size of a bonfire or a fire in a regular fireplace - equal to four to six billets of wood burning hotly.\n\n'
        'When applied to large normal fires, flaming oil in quantity equal to a gallon or more, the fire produced by a demon or devil, a <i>flame tongue</i> sword, or a <a href="/spells/burning-hands-magic-user-lvl-1"><i>burning hands</i></a> spell, 1 charge is expended from the wand. Continual magic flames, such as those of a sword or a creature able to ignite, will be extinguished for 6 rounds and will flare up again after that time.\n\n'
        'When applied to large magical fires such as a <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a>, <a href="/spells/flame-strike-cleric-lvl-5"><i>flame strike</i></a>, or <a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a>, 2 charges are expended from the wand as the flames are extinguished.\n\n'
        'If one charge of the device is used upon a creature which is composed of flame (a <a href="/creatures/fire-elemental">fire elemental</a>, for instance), the wand inflicts 6-36 (6d6) points of damage upon the creature.'
    )
),
MagicItem( name = 'Wand of Force',
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gold_value = [30000,30000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('Although it is rumored that the concept of such a wand has taken many forms, the one which has been standardized, so to speak, is a tri-function device which requires considerable operator knowledge only in the application of its third function.\n\n'
        'Firstly, a <i>wand of force</i> enables the wielder to cause a shaft of nearly invisible, blue-white energy to spring forth from its tip. This shaft of energy extends 4 feet and is equal to a +5 bastard sword with respect to hit probability and damage. This usage expends 1 charge per turn.\n\n'
        'Secondly, a <i>wand of force</i> can be employed to create a <a href="/spells/wall-of-force-magic-user-lvl-5"><i>wall of force</i></a> duplicating the fifth-level magic-user spell of the same name as if cast by a 10th-level magic-user. This function expends 1 charge per <i>wall</i> created, and a single usage per round is possible.\n\n'
        'Thirdly, a <i>wand of force</i> can be employed to create a nearly invisible plane of energy which performs as if it had been created by the casting of a <a href="/spells/bigbys-forceful-hand-magic-user-lvl-6"><i>Bigby\'s Forceful Hand</i></a> spell. The wand user must actually be a magic-user in order to activate this function, and regardless of his or her level, one of the various <i>Bigby\'s Hand/Fist</i> spells must be recorded for study (not necessarily for casting) in the spell books of the wand wielder. Use of this function expends ½ charge per round.\n\n'
        'Fighters of all types are able to use the first and second functions of the wand. The device can be recharged by a magic-user of 16th or higher level, and in addition it can draw sufficient energy to regain a single charge by being touched to any of the following: a manifestation of one of the <i>Bigby\'s Hand/Fist</i> spells, a manifestation of the <a href="/spells/mordenkainens-sword-magic-user-lvl-7"><i>Mordenkainen\'s Sword</i></a> spell, or a manifestation of a <i>wall of force</i>. Touching any of these things with the wand causes the effect of a <a href="/spells/disintegrate-magic-user-lvl-6"><i>disintegrate</i></a> spell, destroying the spell/manifestation instantly, and enabling the wand to absorb power equivalent to a single charge.'
    )
),
MagicItem( name = 'Wand of Ice Storms',
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gold_value = [20000,20000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'This device enables the wielder to cause an <a href="/spells/ice-storm-magic-user-lvl-4"><i>ice storm</i></a> just as if he or she were a magic-user of 7th level. Either damaging hail or sleet and slippery conditions are possible (see the <i>ice storm</i> spell explanation). Activation time is 1 segment, and causing the dweomer to emerge from the wand likewise requires 1 segment. The wand can be recharged by a magic-user of 9th or higher level.'
),
MagicItem( name = 'Wand of Lightning Bolts',
    category = MagicItemCategory.WAND,
    xp_value = [2000,2000],
    gold_value = [16000,16000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'A wand of this nature enables the possessor to cast a <a href="/spells/lightning-bolt-magic-user-lvl-3"><i>lightning bolt</i></a> as if he or she were a magic-user of 6th level. Damage is 6-36 (6d6) points, with saving throw applicable for half damage. Either form of bolt (forked or single stroke) is possible. The wand takes 1 segment to activate, and another 1 segment is required to discharge the lightning. The device can be recharged by a magic-user of 8th or higher level.'
),
MagicItem( name = 'Wand of Metal Command',
    category = MagicItemCategory.WAND,
    xp_value = [2500,2500],
    gold_value = [10000,10000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('This wand appears to be nothing more useful than a <i>wand of metal and mineral detection</i>, but in the hands of a <a href="/creatures/dwarf">dwarf</a> or <a href="/spells/gnome">gnome</a>, its exceptional powers become operational:\n\n'
        'If 1 charge is expended, the wand can transmute gold to lead, or lead to gold. The range of this power is 3", and the amount of metal so converted will be 1 to 6 pounds (10 to 60 gp weight).\n\n'
        'If 2 charges are expended, the user can <a href="/spells/heat-metal-druid-lvl-2"><i>heat metal</i></a> in the same fashion as the druid spell of the same name. Range is 3", and only a single target area of 3-foot diameter can be affected, causing up to 600 gp weight of metal within this area to become heated.\n\n'
        'If 3 charges are expended, the possessor of the wand can cast any one of the following spells just as if he or she were an 18th-level magic-user: <a href="/spells/crystalbrittle-magic-user-lvl-9"><i>crystalbrittle</i></a>, <a href="/spells/glassee-magic-user-lvl-6"><i>glassee</i></a>, or <a href="/spells/glassteel-magic-user-lvl-8"><i>glassteel</i></a>.'
    )
),
MagicItem( name = 'Wand of Size Alteration',
    category = MagicItemCategory.WAND,
    xp_value = [3000,3000],
    gold_value = [20000,20000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = 'A wand of this sort enables the wielder to cause any single creature of virtually and size to <i>enlarge</i> or <i>diminish</i> in size. Either effect will cause a 50% change in size. Relative strength and power also increases or decreases proportionally, providing the weaponry employed is proportionate - or usable. For humanoid creatures enlarged, strength is roughly proportionate to that of a giant of corresponding size; for example, 9 feet tall equals a <a href="/creature/hill-giant">hill giant</a> and 19 strength, 13 feet tall equals a <a href="/creatures/fire-giant">fire giant</a> and 22 strength. The wand\'s power has a range of 1". The target creature and all it is wearing or carrying is affected unless a saving throw succeeds - but note that a willing target need not make a saving throw. The effect of the wand can be removed by a <a href="/spells/dispel-magic-cleric-lvl-3"><i>dispel magic</i></a> spell, but if this is done the target must make a system shock roll. It can also be countered if the possessor of the wand wills the effect to be cancelled before the duration of the effect expires. Each usage of the wand (but not the cancellation of an effect) expends 1 charge. It can be recharged by a magic-user of 12th or higher level.'
),
MagicItem( name = 'Wand of Steam and Vapor',
    category = MagicItemCategory.WAND,
    xp_value = [4500,4500],
    gold_value = [25000,25000],
    source = SourceBook.UNEARTHED_ARCANA,
    desc = ('A wand of this sort has two separate functions, each of which requires the expenditure of 1 charge:\n\n'
        'STEAM: In one segment the wand will spout forth a jet of super-heated steam in a cone 1" x 3" x 5". Any creature within this area takes 6-36 (6d6) points of damage. The cloud persists, slowly cooling, so that on the second round it inflicts 4d6 damage, and on the third and last round it causes 2d6 damage. Saving throws apply for half damage in all cases. Naturally, fire-dwelling or fire-using creatures will not be harmed by the steam - unless they are harmed by dampness.\n\n'
        'VAPOR: In one segment the wand will gout forth billows of warm, steamy vapors. These vapors are equal to a <a href="/spells/fog-cloud-illusionist-lvl-2"><i>fog cloud</i></a> of 4" depth, 6" height, and 8" breadth. This vaporous cloud persists for 6 rounds, remaining stationary unless moved about by magical or non-magical breezes or winds. Cold-using creatures will suffer 1 point of damage per round while inside the vapor cloud, and cold-dwelling creatures will take twice that amount of damage.'
    )
)
]

misc_magic = [
MagicItem( name = 'Alchemy Jug',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [12000,12000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This magical device can pour forth varying liquids upon command. The quantity of each liquid is dependent upon the liquid itself. The <i>jug</i> can pour only 1 kind of liquid on any given day, 7 pourings maximum. The liquids pourable and quantity per pouring are:\n\n'
        '<table>'
        '<tr><th>Liquid</th><th>Quantity</th></td>'
        '<tr><td>salt water</td><td>16 gallons</td></tr>'
        '<tr><td>fresh water</td><td>8 gallons</td></tr>'
        '<tr><td>beer</td><td>4 gallons</td></tr>'
        '<tr><td>vinegar</td><td>2 gallons</td></tr>'
        '<tr><td>wine</td><td>1 gallon</td></tr>'
        '<tr><td>ammonia</td><td>1 quart</td></tr>'
        '<tr><td>oil</td><td>1 pint</td></tr>'
        '<tr><td>aqua regia</td><td>2 gills (8 oz.)</td></tr>'
        '<tr><td>alcohol</td><td>1 gill (4 oz.)</td></tr>'
        '<tr><td>chlorine</td><td>8 drams (1 oz.)</td></tr>'
        '<tr><td>cyanide</td><td>4 drams (½ oz.)</td></tr>'
        '</table>\n\n'
        'The jug will pour forth 2 gallons per round, so it will require 8 rounds to complete 1 pouring of salt water.'
    )
),
MagicItem( name = 'Amulet of Inescapable Location',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device is typically worn on a chain or as a brooch which pins on. It appears to be an amulet which prevents location, scrying (crystal ball viewing and the like), or detection/influence by <i>ESP/telepathy</i>. Actually, the amulet doubles the likelihood and/or range of these location and detection modes, however. Normal determination attempts, including <a href="/spells/detect-magic-cleric-lvl-1"><i>detect magic</i></a>, will not reveal its true nature.'
),
MagicItem( name = 'Amulet of Life Protection',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This pendant or brooch device serves as a ward for the psyche (soul). The wearer cannot be <i>possessed</i> by <a href="/spells/magic-jar-magic-user-lvl-5"><i>magic jar</i> spell or any similar mental attack, including demonic or diabolic means. If the wearer is slain, the psyche enters the amulet and is protected for 7 full days. Thereafter it goes to the plane of its alignment, however. If the amulet is destroyed during the 7 days, the psyche is utterly and irrevocably annihilated. Note: psionic attack modes <i>psionic blast</i> or <i>psychic crush</i> will not harm the wearer.'
),
MagicItem( name = 'Amulet of the Planes',
    category = MagicItemCategory.MISC,
    xp_value = [6000,6000],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The <i>amulet of the planes</i> is a device which enables the individual possessing it to transport himself or herself instantly to or from any one of the upper levels of the Outer Planes. This travel is absolutely safe, but until the individual learns the device, transport will be random. Roll d6, 1-3 = do not add 12, 4-6 = add 12 to d12 for 1-24 random results:\n\n'
        '1-2: Seven Heavens\n'
        '3: Twin Paradises\n'
        '4: Elysium\n'
        '5: Happy Hunting Grounds\n'
        '6-7: Olympus\n'
        '8: Gladsheim\n'
        '9: Limbo\n'
        '10: Pandemonium\n'
        '11-12 Abyss\n'
        '13: Tarterus\n'
        '14: Hades\n'
        '15: Gehenna\n'
        '16-17: Nine Hells\n'
        '18: Acheron\n'
        '19: Nirvana\n'
        '20: Arcadia\n'
        '21-24: Prime Material Plane\n\n'
        'You may alternatively have the following results:\n\n'
        '22: Ethereal Plane\n'
        '23: Astral Plane\n'
        '24: Prime, but alternate Earth'
    )
),
MagicItem( name = 'Amulet of Proof Against Detection and Location',
    category = MagicItemCategory.MISC,
    xp_value = [4000,4000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device wards the wearer against all divination and mental or magical location and/or detection. The wearer cannot be detected through <a href="/spells/clairaudience-magic-user-lvl-3"><i>clairaudience</i></a>, <a href="/spells/clairvoyance-magic-user-lvl-3"><i>clairvoyance</i></a>, <a href="/spells/esp-magic-user-lvl-2"><i>ESP</i></a>, <i>telepathy</i>, <i>crystal balls</i>, or any other scrying devices. No aura is discernible on the wearer, and predictions cannot be made regarding him or her, unless some powerful being is consulted.'
),
MagicItem( name = 'Apparatus of Kwalish',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('When initially found this item will certainly appear as a large iron barrel. It has a secret catch which opens a hatch in one end. Inside are 10 levers:\n\n'
        '1: extends legs and tail/retract same\n'
        '2: uncover foreward porthole/cover same\n'
        '3: uncover side portholes/cover same\n'
        '4: extends pincers and feelers/retract same\n'
        '5: snap pincers\n'
        '6: forward/left or right\n'
        '7: backwards/left or right\n'
        '8: open "eyes" with <a href="/spells/continual-light-magic-user-lvl-2"><i>continual light</i></a> inside/close "eyes"\n'
        '9: raise (levitate)/sink\n'
        '10: open hatch/close hatch\n\n'
        'The <i>apparatus</i> moves forward at a 3" speed, backwards at 6". The 2 pincers extend forward 4\' and snap for 2-12 hit points damage each if they hit a creature - 25% chance, no reduction for armor, but dexterity reduction applies. The device can operate in waters up to 900\' deep. It can hold 2 human-sized persons and enough air to operate for 2-5 hours at maximum capacity. The <i>apparatus</i> is AC 0 and will take 100 hit points damage to cause a leak, 200 to stave in a side. When the device is fully operating the whole appears as something like a giant lobster.'
    )
),
MagicItem( name = 'Arrow of Direction',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [17500,17500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'An <i>arrow of direction</i> typically appears to be a normal (or possibly magic) arrow. Its magical properties make it function much as a <a href="/spells/locate-object-magic-user-lvl-2"><i>locate object</i></a> spell, however, empowering the arrow to show the direction of the desired way. Once per day the device can be tossed into the air; it will fall and point towards the desired way, and this process can be repeated 7 times during the next 7 turns. Note: the arrow will point only towards requested way/location. The request can be only for one of the following: stairway (up or down), sloping passage (up or down), dungeon exit or entrance, cave, cavern. Requests must be phrased by distance (nearest, farthest, highest, lowest) or by direction (north, south, east, west, etc.).'
),
MagicItem( name = 'Bag of Beans',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This bag is constructed of heavy cloth. It is about 2\' wide and 4\' long (the size of any other bag or large sack). When it is opened and examined it will reveal several large pebble-like objects. If these objects are dumped out of the bag they will each explode for 5-20 hit points of damage each, all creatures within a 10\' radius must save versus magic or take full damage. To be removed safely, the beans in the bag must be taken out by hand; <a href="/spells/telekinesis-magic-user-lvl-5">telekinesis</a> will not work, nor can they be worked out using tools in any way which will not explode them. Each pebble-like bean must be placed in dirt and watered. From each, in succession, will spring some creature or object. It is suggested that 3-12 beans are optimum, and only 1 or 2 will be beneficial, the others being monsters or useless things. For example:\n\n'
        '#1: 3 <a href="/creatures/shrieker">shriekers</a> spring up and begin wailing\n'
        '#2: an <a href="/spells/ice-storm-magic-user-lvl-4"><i>ice storm</i></a> strikes the area\n'
        '#3: a poisonous raspberry bush with animated runners shoots up, but each of its 5-20 berries is a gem of 100 or 500 g.p. base value (or perhaps just worthless glass)\n'
        '#4: a hole opens in the ground; a <a href="/creatures/purple-worm">purple worm</a> can be below or a djinni ring...\n'
        '#5: smoke and gases cover an area of 50\' radius for 5 turns, and creatures therein cannot see and will be blinded for 1-6 rounds even when they step out of the cloud\n'
        '#6: a <a href="/creatures/wyvern">wyvern</a> grows instantly and attacks; its sting is a <i>javelin of piercing</i>\n'
        '#7: poison gas seeps out slowly forming a cloud of 20\' radius which persists for 1 turn; while it lasts it might turn some dirt at its center to magic dust (<i>appearance</i>, <i>vanishing</i>, <i>sneezing and choking</i> ...)\n\n'
        'Thought, imagination and judgment are required with this item.'
    )
),
MagicItem( name = 'Bag of Devouring',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1500,1500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This bag appears as a typical sack - possibly appearing to be empty, possibly as having <i>beans</i> in its bottom. The sack is, however, the lure used by an extra-dimensional creature. It is one of its feeding orifices. Any substance of animal or vegetable nature is subject to "swallowing" if it is thrust within the bag. The <i>bag of devouring</i> is 90% likely to ignore any initial intrusions, but anytime it senses living human flesh within, it is 60% likely to close and attempt to draw the whole victim within - base 75% chance for success less strength bonus for "damage", each +1 = -5% on base chance. Thus an 18 strength character (with +2 damage) is only 65% likely to be drawn into the bag, while a 5 strength character (with -1 damage) is 80% likely to be drawn in. The bag radiates magic. It can hold up to 30 cubic feet of matter. It will act as a <i>bag of holding</i> (normal capacity), but each turn it has a 5% cumulative chance of "swallowing" the contents and then "spitting the stuff out" in some non-space. Creatures drawn within are consumed in 7 segments of a round, eaten, and forever gone.'
),
MagicItem( name = 'Bag of Holding',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('As with other magic bags, this one appears to be a common cloth sack of about 2\' x 4\' size. The <i>bag of holding</i> opens into a non-dimensional space, and its inside is larger than its outside dimensions. Regardless of what is put into this item, the <i>bag of holding</i> always weighs a fixed amount. This weight, the bag\'s weight limit in contents, and its volume content are dependent upon its quality as shown below:\n\n'
        '<table>'
        '<tr><th>Dice</th><th>Weight</th><th>Weight Limit</th><th>Volume Limit</th></tr>'
        '<tr><td>01-30</td><td>15 pounds</td><td>250 pounds</td><td>30 cubic feet</td></tr>'
        '<tr><td>31-70</td><td>15 pounds</td><td>500 pounds</td><td>70 cubic feet</td></tr>'
        '<tr><td>71-90</td><td>35 pounds</td><td>1,000 pounds</td><td>150 cubic feet</td></tr>'
        '<tr><td>91-00</td><td>60 pounds</td><td>1,500 pounds</td><td>250 cubic feet</td></tr>'
        '</table>\n\n'
        'If overloaded, or sharp objects are placed within so as to pierce it, the bag will rupture and be ruined, and the contents will be lost forever in the vortices of nilspace.'
    )
),
MagicItem( name = 'Bag of Transmuting',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [500,500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This magical sack appears to be a <i>bag of holding</i> of one of the 4 quality types. It will perform properly for 2-5 uses (or more if the usages are made within a few days time). However, at some point the magic field will waver, and precious metals and gems within the bag will be turned into common metals and stones of no worth. When emptied, the bag will burst to pour forth these transmuted metals and minerals. Any magic items (other than artifacts and relics) placed in the bag will become ordinary and dull lead, glass or wood as appropriate (no saving throw) once the transmuting effects have begun.'
),
MagicItem( name = 'Bag of Tricks',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('As is usual, a <i>bag of tricks</i> appears to be of typical size for sacks, and visual or other examination will not reveal any contents. However, if an individual reaches inside, he or she will feel a small, fuzzy object. If this is withdrawn and tossed 1\' to 20\' away, it will balloon into one of the following animals, which will obey and fight for the individual who brought it into being until the current combat terminates. The animals inside a bag of tricks are dependent upon which sort of bag is found. Roll d10 to determine which type:\n\n'
        '<b>Type 1-5</b>\n'
        '<table>'
        '<tr><th>Die</th><th>Animal</th><th>AC</th><th>Hit Dice</th><th>Hit Points</th><th>Damage per Attack</th></tr>'
        '<tr><td>1</td><td>Weasel</td><td>6</td><td>½</td><td>2</td><td>1</td></tr>'
        '<tr><td>2</td><td>Skunk</td><td>9</td><td>½</td><td>2</td><td>Musk</td></tr>'
        '<tr><td>3</td><td>Badger</td><td>4</td><td>1 +2</td><td>7</td><td>1-2/1-2/1-3</td></tr>'
        '<tr><td>4</td><td>Wolf</td><td>7</td><td>2 +2</td><td>12</td><td>2-5</td></tr>'
        '<tr><td>5</td><td>Lynx, giant</td><td>6</td><td>2 +2</td><td>12</td><td>1-2/1-2/1-4 -- 1-3/1-3</td></tr>'
        '<tr><td>6</td><td>Wolverine</td><td>5</td><td>3</td><td>15</td><td>1-4/1-4/2-5 + musk</td></tr>'
        '<tr><td>7</td><td>Boar</td><td>7</td><td>3 +3</td><td>18</td><td>3-12</td></tr>'
        '<tr><td>8</td><td>Stag, giant</td><td>7</td><td>5</td><td>25</td><td>4-16 or 1-4/1-4</td></tr>'
        '</table>\n\n'
        '<b>Type 6-8</b>\n'
        '<table>'
        '<tr><th>Die</th><th>Animal</th><th>AC</th><th>Hit Dice</th><th>Hit Points</th><th>Damage per Attack</th></tr>'
        '<tr><td>1</td><td>Rat</td><td>7</td><td>½</td><td>2</td><td>1</td></tr>'
        '<tr><td>2</td><td>Owl</td><td>7</td><td>½</td><td>3</td><td>1-3/1-3</td></tr>'
        '<tr><td>3</td><td>Dog</td><td>7</td><td>1 +1</td><td>6</td><td>1-4</td></tr>'
        '<tr><td>4</td><td>Goat</td><td>7</td><td>1 +1</td><td>8</td><td>1-6</td></tr>'
        '<tr><td>5</td><td>Ram</td><td>6</td><td>2</td><td>10</td><td>2-5</td></tr>'
        '<tr><td>6</td><td>Bull</td><td>7</td><td>4</td><td>20</td><td>1-6/1-6</td></tr>'
        '<tr><td>7</td><td>Bear</td><td>6</td><td>5 +5</td><td>30</td><td>1-6/1-6/1-8 -- 2-12</td></tr>'
        '<tr><td>8</td><td>Lion</td><td>5/6</td><td>5 +5</td><td>28</td><td>1-4/1-4/1-10 -- 2-7/2-7</td></tr>'
        '</table>\n\n'
        '<b>Type 9-0</b>\n'
        '<table>'
        '<tr><th>Die</th><th>Animal</th><th>AC</th><th>Hit Dice</th><th>Hit Points</th><th>Damage per Attack</th></tr>'
        '<tr><td>1</td><td>Jackal</td><td>7</td><td>½</td><td>2</td><td>1-2</td></tr>'
        '<tr><td>2</td><td>Eagle</td><td>7</td><td>1</td><td>5</td><td>1-2/1-2/1</td></tr>'
        '<tr><td>3</td><td>Baboon</td><td>7</td><td>1 +1</td><td>6</td><td>1-4</td></tr>'
        '<tr><td>4</td><td>Ostrich</td><td>7</td><td>3</td><td>15</td><td>1-4 or 2-8</td></tr>'
        '<tr><td>5</td><td>Leopard</td><td>6</td><td>3 +2</td><td>17</td><td>1-3/1-3/1-6 -- 1-4/1-4</td></tr>'
        '<tr><td>6</td><td>Jaguar</td><td>6</td><td>4 +2</td><td>21</td><td>1-3/1-3/1-8 -- 2-5/2-5</td></tr>'
        '<tr><td>7</td><td>Buffalo</td><td>7</td><td>5</td><td>25</td><td>1-8/1-8</td></tr>'
        '<tr><td>8</td><td>Tiger</td><td>6</td><td>5 +5</td><td>30</td><td>2-5/2-5/1-10 -- 2-8/2-8</td></tr>'
        '</table>\n\n'
        'Only 1 creature can be drawn forth at a time. It alone exists until it is slain or 1 turn has elapsed and it is ordered back into the <i>bag of tricks</i>. Another animal may then be brought forth, but it could be another just like the one which was drawn previously. Note that only one roll is made for type of <i>bag</i>, but type of creature is rolled for each time one is drawn forth. Up to 10 creatures maximum may be drawn from the bag each week.'
    )
),
MagicItem( name = 'Beaker of Plentiful Potions',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This container resembles a jug or flask. It is a magical beaker with alchemical properties which compound from 2-5 doses of from 2-5 potions of any sort as initially determined by random selection. Different potion sorts are layered in the container, and each pouring takes 1 round and spills forth 1 dose of 1 potion type. Roll d4, +1 , to find the number of potions the beaker contains. Roll for each potion contained so as to find what it is - <i>delusion</i> and <i>poison</i> are possible - and record type by order of occurrence. Duplication is possible. If the container holds only 2 potions it will dispense them 1 each per day, 3 times per week; if 3 are contained, it will dispense them 1 each per day, 2 times per week; and if 4 or 5 are contained it will pour each forth but 1 time per week. Once opened, the beaker will gradually lose the ability to produce potions. This reduction in ability results in the permanent loss of one potion type per month.'
),
MagicItem( name = 'Folding Boat',
    category = MagicItemCategory.MISC,
    xp_value = [10000,10000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>folding boat</i> will always be discovered as a small wooden "box" - about 1\' long, ½\' wide, and ½\' deep. It will, of course, radiate magic if detection is possible. The "box" can contain other things. If a command word is given, the box will unfold itself to form a boat of 10\' length, 4\' width and 2\' depth. A second (different) command word will cause it to unfold to a 24\' long, 8\' wide, and 6\' deep ship. The former will have 1 pair of oars, an anchor, a mast, and lateen sail. The latter is decked, has single rowing seats, 5 sets of oars, a steering oar, anchor, a deck cabin, a mast, and square sail. The first can hold 3 or 4 persons comfortably, the second will carry 15 persons with ease. A third word of command will cause the boat/ship to fold itself into a box once again. You may have the words of command inscribed visibly or invisibly on the box, have them written elsewhere - perhaps on an item within the box, or you might simply have them lost and require a search (via <a href="/spells/legend-lore-magic-user-lvl-6"><i>legend lore</i></a>, consulting a sage, physical search of the dungeon, etc.) to discover them.'
),
MagicItem( name = 'Book of Exalted Deeds',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This holy book is sacred to clerics of <i>good</i> alignment. Reading of the work will require 1 week, but upon completion the <i>good</i> cleric will gain 1 point of wisdom and experience points sufficient to place him or her exactly halfway into the next level of experience. Clerics neither <i>good</i> nor <i>evil</i> will lose 20,000-80,000 experience points from perusal of the work (a negative x.p. total is possible, requiring <a href="/spells/restoration-cleric-lvl-7"><i>restoration</i></a> but not lowering level below 1st). <i>Evil</i> clerics will lose 1 full experience level, dropping to the lowest possible number of experience points possible number of experience points possible to hold the level; they will furthermore have to <i>atone</i> by <a href="/spells/atonement-cleric-lvl-5">magical means</a> or by offering up 50% of everything they gain for 2-5 adventures, losing the appropriate number of experience points as well, or gain no further experience. Fighters who handle or read the book will not be affected, although a <i>paladin</i> will feel it to be <i>good</i>. Magic-users who read it will suffer the loss of 1 point of intelligence unless they save versus magic; and if they do save they will lose from 2,000-20,000 experience points. A thief who handles or reads the work will sustain 5-30 hit points of damage and must save versus magic or lose 1 point of dexterity and have a 10%-60% chance of giving up his or her profession to become a <i>good</i> cleric if wisdom is 15 or higher. Assassins handling or reading the <i>book of exalted deeds</i> will take 5-40 hit points of damage and must save versus magic or commit suicide. Monks are not harmed by the work, nor can they understand it. Bards are treated as neutral clerics, experience point loss being from <i>bard</i> experience only. Note that except as indicated above, this writing cannot be distinguished by cover or scansion from <i>any</i> other magic book, libram, tome, etc. It must be perused. (This applies also to other magical writings detailed hereafter.) Once perused, the book vanishes, never to be seen again, nor can the same player character ever benefit from perusing the like a second time.'
),
MagicItem( name = 'Book of Infinite Spells',
    category = MagicItemCategory.MISC,
    xp_value = [9000,9000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This magical writing bestows spell use ability upon its possessor, but upon first reading the work any character not already able to use spells will suffer 5-20 hit points of damage and be <i>stunned</i> for 5-20 turns. Thereafter, he or she can examine the writing without further harm. The <i>book of infinite spells</i> contains from 23-30 (22 + d8) pages. The nature of each page must be determined by random die roll. Use the following table:\n\n'
        '01-30: blank page\n'
        '31-50: cleric spell\n'
        '51-60: druid spell\n'
        '61-95: magic-user spell\n'
        '96-00: illusionist spell\n\n'
        'If a spell is written on a page, roll d10 for all except magic-user spell, for which a d12 is rolled, to determine spell level. Results of 8-10 (or 10-12) indicate a d6 (d8 for magic-user spells) is to be rolled instead. When level is known, determine the particular spell by random means also. Record page contents secretly, and DO NOT REVEAL THIS INFORMATION TO THE HOLDER OF THE BOOK.\n\n'
        'Once a page is turned it can never be flipped back, i.e. paging through the book is a one-way trip. When the last page is turned, the book vanishes. The owner of the <i>book of infinite spells</i> can cast the spell to which the book is opened, but once per day only, unless the spell is one which the character would normally be able to cast by reason of class and level, in which case the spell can be cast up to 4 times per day due to the book\'s magical powers. The book need <i>not</i> be in the actual presence of the owner in order to empower spell ability, so he or she can store it in a place of safety while adventuring and still cast spells by means of its power. Each time a spell is cast there is a chance the energy connected with its use will cause the page to magically turn (despite <i>all</i> precautions). The owner will know this and possibly even benefit from the turning by gaining access to a new spell. The chance of a page turning is as follows:\n\n'
        '10% when spell-caster employing spells usable by his or her class and/or level\n'
        '20% when spell-caster using spell foreign to his or her class and/or level\n'
        '25% when non-spell caster using cleric spell\n'
        '30% when non-spell caster using magic-user spell\n\n'
        'Treat the spell use just as if a scroll were being employed, including time of casting, spell failure, etc.'
    )
),
MagicItem( name = 'Book of Vile Darkness',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This work of ineffable <i>evil</i> is meat and drink to clerics of that alignment. To fully consume the contents requires 1 week of reading, but when such has been accomplished, the <i>evil</i> cleric will gain 1 point of wisdom and experience points sufficient to place him or her exactly halfway into the next level of experience. Clerics neither <i>good</i> nor <i>evil</i> who read this book will either lose 30,000-120,000 experience points or become evil without benefit from the work; there is a 50% chance for either. <i>Good</i> clerics perusing the pages of the unspeakable <i>Book of Vile Darkness</i> will have to save versus poison or die; and if they do not die they must save versus magic or become <i>permanently insane</i>. In the latter event, even if the save is successful, the cleric loses 250,000 experience points, less 10,00 for each of his or her points of wisdom. Other characters of <i>good</i> alignment will take 5-30 hit points of damage from handling the tome and if they look inside there is an 80% chance of a <a href="/creatures/night-hag"><i>night hag</i></a> will thereafter come to the character that night and attack. Non-evil <i>neutral</i> characters will take 5-20 hit points of damage from handling the book, and reading its pages will cause them to save versus poison or become <i>evil</i>, immediately seeking out an evil cleric to confirm their new alignment. (Cf. <i>Book of Exalted Deeds</i> for other details.)'
),
MagicItem( name = 'Boots of Dancing',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The magical <i>boots of dancing</i> will expand or contract to fit any foot size, from <a href="/creatures/halfling">halfling</a> to giant (just as other magic boots will do, of course). They radiate a dim magic if detection is used. They are indistinguishable from other magic boots, and until actual melee combat is engaged in they will function exactly as if they were one of the other 4 types of useful boots. When in melee combat, or if the wearer is fleeing from the actuality of same, the <i>boots of dancing</i> will impede his or her movement, begin to tap and shuffle, heel and toe, or shuffle off to Buffalo, making the wearer behave exactly as if <a href="/spells/ottos-irresistible-dance-magic-user-lvl-8"><i>Otto\'s Irresistible Dance</i></a> spell had been cast upon him or her (-4 from armor class rating, no saving throws possible, and no attacks possible). Only a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell will allow the boots to be removed once their true nature comes forth.'
),
MagicItem( name = 'Boots of Elvenkind',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These soft boots enable the wearer to move without sound of footfall in virtually any surroundings. Thus the wearer can walk across a patch of dry leaves or over a normally creaky wooden floor and make only a whisper of noise - say 95% chance of silence in the worst of conditions, 100% in the best.'
),
MagicItem( name = 'Boots of Levitation',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'As other magical boots, these soft footgear will expand or contract to fit giant to <a href="/creatures/halfling">halfling</i>-sized feet. <i>Boots of levitation</i> allow the wearer, at will, to ascend or descend vertically. The speed of ascent/descent is 20\' per round (minute). There is no limitation on usage. The amount of weight the boots can levitate is randomly determined in 14 pound increments by rolling d20 and adding the result to a base of 280 pounds, i.e. a given pair of boots can <i>levitate</i> from 294 to 560 pounds of weight. Thus, an <a href="/creatures/ogre">ogre</a> could be wearing such boots, but its weight would be too great to <i>levitate</i>. (Cf. second level magic-user spell, <a href="/spells/levitate-magic-user-lvl-2"><i>levitation</i></a>.)'
),
MagicItem( name = 'Boots of Speed',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These boots enable the wearer to run at the speed of a fast horse, viz. 24" base movement speed. For every 10 pounds (100 g.p. equivalent) of weight over 200 pounds, the wearer is slowed 1" in movement, so a 180 pound human with 60 pounds of gear would move at 20" base movement rate, and if a sack of 500 gold pieces were being carried in addition, the movement rate would be slowed yet another 5". For every hour of continuous fast movement, the wearer must rest 1 hour. No more than 8 hours of continuous fast movement are possible before the wearer <i>must</i> rest. <i>Boots of speed</i> give +2 to armor class value in combat situations where movement of this sort is possible.'
),
MagicItem( name = 'Boots of Striding and Springing',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The wearer of these magical boots has a base movement rate of 12", regardless of size or weight. This speed can be maintained tirelessly for up to 12 hours per day, but thereafter the boots no longer function for 12 hours - assume they "recharge" for that period. In addition to the <i>striding</i> factor, these boots also have a <i>springing</i> factor. While "normal" paces for the individual wearing this type of footgear are 3\' long, the boots also enable forward jumps of up to 30\', backward leaps of 9\', and vertical springs of 15\'. If circumstances permit the use of such movement in combat, the wearer can effectively strike and spring away when he or she has <i>initiative</i> during a melee round. However, such activity has a degree of danger, and there is a base 20% chance that the wearer of the boots will stumble and be stunned the following round; adjust the 20% chance downward by 3% for each point of dexterity above 12 of the wearer, i.e. 17% at 13 dexterity, 14% at 14, 11% at 15, 8% at 16, 5% at 17, and but 2% at 18 dexterity. In any event, the wearer increases armor class value by +1 due to the quickness of movement these boots imbue, so armor class 2 becomes 1, armor class 1 becomes 0, etc.'
),
MagicItem( name = 'Bowl Commanding Water Elementals',
    category = MagicItemCategory.MISC,
    xp_value = [4000,4000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This large container is usually fashioned from blue or green stone of semi-precious value such as malachite or lapis lazuli. Sometimes jade will be used. It is about 1\' in diameter, half that deep, and relatively fragile. When the bowl is filled with water, fresh or salt, and certain words are spoken, an elemental of 12 hit dice will appear. The summoning words require 1 round to speak. Note that if salt water is used, the elemental will be stronger (+2 per hit die, maximum 8 h.p. per die, however). Control and similar information are given under <i>Elemental</i> in <b>ADVANCED DUNGEONS AND DRAGONS, MONSTER MANUAL</b>. (Cf. <i>bowl of watery death</i>.)'
),
MagicItem( name = 'Bowl of Watery Death',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device exactly resembles a <i>bowl commanding water elementals</i>, including color, design, magic radiation, etc. However, when it is filled with water, the magic-user must save versus magic or be shrunk to the size of a small ant and plunged into the center of the bowl. Note: if salt water is poured into the bowl the saving throw is at -2. The victim will drown in from 3-8 rounds, unless magic is used to save the individual, for he or she cannot be physically removed from the <i>bowl of watery death</i> except by magical means: <a href="/spells/animal-growth-druid-lvl-5"><i>animal growth</i></a>, <a href="/spells/enlarge-magic-user-lvl-1"><i>enlarge</i></a>, or <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> are the only spells which will free the victim, and restore normal size; a <i>growth</i> potion poured into the water will have the same effect; a <i>sweet water</i> potion will allow the victim another saving throw, i.e. a chance that the curse magic of the bowl works only briefly. If the victim drowns, death is permanent, no <a href="/spells/resurrection-cleric-lvl-7"><i>resurrection</i></a> is possible, and even a <i>wish</i> will not work.'
),
MagicItem( name = 'Bracers of Defense',
    category = MagicItemCategory.MISC,
    xp_value = [1000,4000],
    gold_value = [6000,24000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('These items appear to be some sort of wrist or arm guards. Their magic bestows an effective armor class equal to actually wearing armor and employing a shield. Of course, if armor is actually worn, the <i>bracers</i> will not be effective, but they do work in conjunction with other magical items of protection. The armor class the <i>bracers of defense</i> bestow is determined by random dicing on the table below:\n\n'
        '<table>'
        '<tr><th>Percentile Roll</th><th>Armor Class</th></tr>'
        '<tr><td>01-05</td><td>8</td></tr>'
        '<tr><td>06-15</td><td>7</td></tr>'
        '<tr><td>16-35</td><td>6</td></tr>'
        '<tr><td>36-50</td><td>5</td></tr>'
        '<tr><td>51-70</td><td>4</td></tr>'
        '<tr><td>71-85</td><td>3</td></tr>'
        '<tr><td>86-00</td><td>2</td></tr>'
        '</table>\n\n'
        'Bracers of defense have an experience point value of 3,000 and a gold value of 500 per armor class above 10, i.e., AC 6 is worth 2,000 in x.p., 12,000 g.p. if sold.'
    )
),
MagicItem( name = 'Bracers of Defenselessness',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [2000,2000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These items appear to be some sort of <i>bracers of defense</i>, and they will actually serve as one of the above types until the wearer is attacked in anger by a dangerous enemy. At that moment, the <i>bracers</i> will lower armor class to 10 and negate any and all other magical protections and dexterity bonuses. Thereafter the bracers can only be removed by means of a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell.'
),
MagicItem( name = 'Brazier Commanding Fire Elementals',
    category = MagicItemCategory.MISC,
    xp_value = [4000,4000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device appears to be a normal container for holding burning coals unless magic is detected for. It enables a magic-user to summon an elemental of 12 hit dice strength from the <i>Elemental Plane of Fire</i>. A fire must be lit in the <i>brazier</i> - usually 1 round is required to do so. If sulphur is added the elemental will be of +1 on each hit die, i.e. 2-9 hit points per hit die. The <a href="/creatures/fire-elemental">fire elemental</a> will appear as soon as the fire is burning and a command word is uttered.'
),
MagicItem( name = 'Brazier of Sleep Smoke',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device is exactly similar to the <i>brazier commanding fire elementals</i>. However, when a fire is started within it the burning will cause great clouds of magical smoke to pour forth in a cloud of 1" radius from the brazier. All creatures within the cloud must save versus magic or fall into a deep sleep. At the same moment a <a href="/creatures/fire-elemental">fire elemental</a> of 12 hit dice will appear and attack the nearest creature. Sleeping creatures can be only be awakened by means of a <a href="/spells/dispel-magic-cleric-lvl-3"><i>dispel magic</i></a> or <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell.'
),
MagicItem( name = 'Brooch of Shielding',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The <i>brooch of shielding</i> appears to be a piece of silver or gold jewelry, usually (90%) without gems inset, which is meant to fasten a cloak or cape. It has the property, however, to absorb <a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missiles</i></a> of the sort generated by spell, wand, or other magic device. A <i>brooch</i> can absorb up to 101 hit points of <i>magic missile</i> damage before it melts and becomes useless. Its use can normally be determined only by means of a <a href="/spells/detect-magic-magic-user-lvl-1"><i>detect magic</i></a> spell and then experimentation.'
),
MagicItem( name = 'Broom of Animated Attack',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [3000,3000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Indistinguishable from a normal broom, except by means of detection of its magic, and completely identical to a <i>broom of flying</i> by all tests short of attempted use, the <i>broom of animated attack</i> is a very nasty item. If a command word ("fly", "soar", etc.) is spoken, the <i>broom</i> will do a loop the loop with its hopeful rider, dumping him or her off on his or her head from 6\' to 9\' off the ground. The broom will then attack the stunned victim, swatting the face with the straw/twig end to blind and beating with the "bald headed end", the handle. Each such attack takes place twice per round, the <i>broom</i> attacking as if it were a 4 hit die monster. The straw end will cause blindness for 1 round if it hits. The other end causes 1-3 hit points of damage when it hits. The broom is armor class 7 and takes 18 hit points to destroy.'
),
MagicItem( name = 'Broom of Flying',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This magical broom is able to fly through the air at up to 30" movement speed. The broom can carry 182 pounds at this rate, but every 14 additional pounds slows movement by 1". The device can climb or dive at about 30 degrees. A command word must be used, the word to be determined by you as desired. The broom will travel alone to any destination named. It will come up to 30" to its owner when he or she speaks the command word.'
),
MagicItem( name = 'Bucknard\'s Everfull Purse',
    category = MagicItemCategory.MISC,
    xp_value = [1500,4000],
    gold_value = [15000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Appearing as nothing more than a leather pouch or small bag, this magical poke is most useful to its owner, for each morning it will duplicate certain coins - and possibly gems as well. When found, the <i>purse</i> will be full of coins. If totally emptied, and left so for more than a few minutes, the magic of the <i>purse</i> is lost, but if 1 of each type of coin is placed within the bag, the next morning 26 of each applicable type will be found inside. <i>Bucknard\'s Everfull Purse</i> can contain:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>C.P.</th><th>S.P.</th><th>E.P.</th><th>G.P.</th><th>P.P.</th><th>Gems*</th></tr>'
        '<tr><td>01-50</td><td>-</td><td>26</td><td>26</td><td>26</td><td>-</td><td>-</td></tr>'
        '<tr><td>51-90</td><td>26</td><td>-</td><td>26</td><td>-</td><td>26</td><td>-</td></tr>'
        '<tr><td>91-00</td><td>26</td><td>-</td><td>26</td><td>-</td><td>-</td><td>26</td></tr>'
        '</table>\n\n'
        '* Base 10 g.p. gems which may increase to a maximum of 100 g.p. only.\n\n'
        'Once the type of bag is first determined by roll, its abilities will not change.\n\n'
        '(This item was designed to maintain spice, providing a constant source of funds without attracting undue attention to the bearer or necessitating chests of treasure.)'
    )
),
MagicItem( name = 'Candle of Invocation',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = '<i>Candles of Invocation</i> are specially <a href="/spells/bless-cleric-lvl-1"><i>blessed</i></a> and <a href="/spells/prayer-cleric-lvl-3"><i>prayered</i></a> tapers which are dedicated to the pantheon of gods of one of the nine alignments. The typical candle is not remarkable, but it will radiate magic if such is detected, and <i>good</i> or <i>evil</i> will be radiated also if appropriate. Simply burning the candle will generate a favorable aura for the individual so doing if the candle\'s alignment matches that of the character\'s. If burned by a cleric of the same alignment, the <i>candle</i> temporarily increases the cleric\'s level of experience by 2, allowing him or her to cast additional spells, and even normally unavailable spells, as if he or she were of the higher level, but only so long as the taper is aflame. Any burning also allows the casting of a <a href="/spells/gate-magic-user-lvl-9"><i>gate</i></a> spell, the respondent being of the alignment of the <i>candle</i>, but the taper is immediately consumed in the process. Each candle will burn for 4 hours. It is possible to extinguish the candle as any other, but it can be placed in a lantern or otherwise sheltered to protect it from drafts and other things which could put it out, without affecting its magical properties.'
),
MagicItem( name = 'Carpet of Flying',
    category = MagicItemCategory.MISC,
    xp_value = [7500,7500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The size, carrying capacity and speed of a <i>carpet</i> are determined by use of the table below. Each <i>carpet</i> has its own command word to activate it, and each is then controlled by spoken directions. If the device is within voice range, the command word will activate it. These rugs are of oriental make and design. Each is very beautiful and durable. Note, however, that tears or other rents cannot be repaired without special weaving techniques which are generally known only in the East.\n\n'
        '<table>'
        '<tr><th>Dice</th><th>Size</th><th>Capacity</th><th>Speed</th></tr>'
        '<tr><td>01-20</td><td>3\'x5\'</td><td>1 person</td><td>42"</td></tr>'
        '<tr><td>21-55</td><td>4\'x6\'</td><td>2 persons</td><td>36"</td></tr>'
        '<tr><td>56-80</td><td>5\'x7\'</td><td>3 persons</td><td>30"</td></tr>'
        '<tr><td>81-00</td><td>6\'x9\'</td><td>4 persons</td><td>24"</td></tr>'
        '</table>'
    )
),
MagicItem( name = 'Censer Controlling Air Elementals',
    category = MagicItemCategory.MISC,
    xp_value = [4000,4000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This perforated golden vessel resembles any thurible found in places of worship. If filled with incense and lit, a command word need only be spoken to summon forth a 12 hit dice-sized <a href="/creatures/air-elemental">air elemental</a> which will appear on the following round. If <i>incense of meditation</i> is burned within this ½\' wide, 1\' high vessel, the air elemental will have +3 on each of its hit dice, and it will <i>willingly</i> obey the commands of its summoner. Note that if the censer is extinguished, the elemental will remain and turn on the summoner.'
),
MagicItem( name = 'Censer of Summoning Hostile Air Elementals',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This thurible is indistinguishable from other censers - magical or ordinary. It is cursed, so that if any incense is burned within it from 1 to 4 enraged <a href="/creatures/air-elemental">air elementals</a> will appear, 1 per round, from the censer and attack any and all creatures within sight. The censer will burn and cannot be extinguished until either the summoner or the elementals have been killed.'
),
MagicItem( name = 'Chime of Opening',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>chime of opening</i> is a hollow mithral tube about 1\' long. When it is struck it sends forth magical vibrations which cause locks to open. Likewise lids, doors, valves, and portals will open when the <i>chime</i> is sounded. The device will function against normal bars, shackles, chains, bolts, etc. It also destroys the magic of a <a href="/spells/hold-portal-magic-user-lvl-1"><i>hold portal</i></a> spell or even a <a href="/spells/wizard-lock-magic-user-lvl-2"><i>wizard lock</i></a> cast by a magic-user of less than 15th level. The <i>chime</i> must be pointed at the area of the item or gate which is to be loosed or opened. It is then struck, a clear chiming ring sounds (which may attract monsters), and in 1 round 1 of the functions of the device will be completed, i.e., a lock opened, a shackle loosed, a secret door opened, the lid of a chest lifted, etc. Note that if a chest is chained, padlocked, locked, and <i>wizard locked</i>, it will take 4 or 5 soundings of the <i>chime of opening</i> to get it open. A <a href="/spells/silence-15-radius-cleric-lvl-2"><i>silence</i></a> spell negates the power of the device. The <i>chime</i> has 20-80 (20 + d6 x 10) charges before it will crack and become useless.'
),
MagicItem( name = 'Chime of Hunger',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [0,0],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device exactly resembles a <i>chime of opening</i>. When it is struck all creatures within 6" are immediately struck with ravenous hunger. Characters will tear into their rations, ignoring everything else, and even dropping everything they are holding in order to eat. Creatures without food immediately available will rush to where the <i>chime of hunger</i> sounded and attack any creatures there in order to kill and eat them. All creatures must eat for at least 1 round, but they are then entitled to a saving throw vs. magic on each successive round until such is made, i.e. hunger is satisfied. <i>Note</i>: It is recommended that the <i>chime of hunger</i> operate as one of <i>opening</i> for several rounds of use before its curse be put into operation.'
),
MagicItem( name = 'Cloak of Displacement',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [17500,17500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This item appears to be a normal cloak, but when it is worn by a character its magical properties distort and warp light waves. This <i>displacement</i> of light waves causes the wearer to appear to be from 1\' to 2\' from his or her actual position. Any attack by missile or melee strike which is aimed at the wearer will automatically miss the first time*. Thereafter the cloak affords +2 protection, i.e. 2 classes better on armor class, as well as +2 on saving throw dice versus attack forms directed at the wearer (such as spells, gaze weapon attacks, spitting and breath attacks, etc. which are aimed at the wearer of the <i>cloak of displacement</i>). Note that 75% of all <i>cloaks of displacement</i> are sized for humans or elves (persons 5\' to 6\' or so tall), and but 25% are sized for persons of about 4\' height (dwarves, gnomes, halflings).\n\n'
        '* This can apply to first attacks from multiple opponents <i>only</i> if the second and successive attackers were unable to observe the initial <i>displacement</i> miss.'
    )
),
MagicItem( name = 'Cloak of Elvenkind',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [6000,6000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>cloak of elvenkind</i> is of a plain neutral gray which is indistinguishable from any sort of ordinary cloak of the same color. However, when it is worn, with the hood drawn up around the head, it enables the wearer to be nearly invisible, for the <i>cloak</i> has chameleon-like powers. In the outdoors the wearer of a <i>cloak of elvenkind</i> is almost totally invisible in natural surroundings, nearly so in other settings. Note that the wearer is easily seen if violently or hastily moving, regardless of the surroundings. The invisibility bestowed is:\n\n'
        'Outdoors, natural surroundings\n'
        '100% heavy growth\n'
        '99% light growth\n'
        '95% open fields\n\n'
        'Outdoors, other\n'
        '98% rocky terrain\n'
        '90% buildings\n'
        '50% brightly lit room\n\n'
        'Underground\n'
        '95% torch/lantern light\n'
        '90% infravision\n'
        '50% <a href="/spells/light-magic-user-lvl-1"><i>light</i></a>/<a href="/spells/continual-light-magic-user-lvl-2"><i>continual light</i></a>\n\n'
        'Fully 90% of these cloaks are sized for human to elven-sized persons. The other 10% are sized for smaller persons (4\' or so in height).'
    )
),
MagicItem( name = 'Cloak of the Manta Ray',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This cloak appears to be made from leather. When it is donned it appears as a normal cloak until the wearer enters salt water, at which time the <i>cloak of the manta ray</i> adheres to the individual, and he or she appears nearly (90%) identical to a <a href="/creatures/manta-ray">manta ray</a>. The wearer is enabled to breath underwater and move as a manta ray - 18". The wearer also has an armor class of at least 6, that of a manta ray, and other magical protections or magical armor will improve that armor value. Although the <i>cloak</i> does not enable the wearer to bite opponents as a manta ray does, the garment does have a tail spine which the wearer can use to strike at opponents behind him or her -  damage is only 1-6 hit points, and there is no chance of stunning. This attack mode can be used in addition to other sorts, for the wearer can release his or her arms from the <i>cloak\'s</i> "wings" without sacrificing movement if so desired.'
),
MagicItem( name = 'Cloak of Poisonousness',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [2500,2500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This particular cloak is usually of woolen-like material, although it can be leathern. It can be handled without harm, and it radiates magic. A <a href="/spells/neutralize-poison-cleric-lvl-4"><i>neutralize poison</i></a> spell will not affect it. As soon as the <i>cloak of poisonousness</i> is actually worn, the wearer will be stricken stone dead. The <i>cloak</i> can only be removed with a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a>, which destroys the magical properties of the <i>cloak</i>. If a <i>neutralize poison</i> spell is then used, the person can possibly be revived by a <a href="/spells/raise-dead-cleric-lvl-5"><i>raise dead</i></a> or <a href="/spells/resurrection-cleric-lvl-7"><i>resurrection</i></a> spell, but there is a -10% chance of success because of the poison. <i>After</i> its effects are known, a small label saying "Nessus Shirt Company" might be seen at your option.'
),
MagicItem( name = 'Cloak of Protection',
    category = MagicItemCategory.MISC,
    xp_value = [1000,5000],
    gold_value = [10000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The various forms of this marvelous device all appear to be normal garments, whether made of cloth or leather. Each lends to its wearer benefits on armor class - each plus of the <i>cloak of protection</i> bettering armor class by 1 factor - and to saving throw - each plus being added to the wearer\'s saving throw dice rolls. Thus a +1 <i>cloak</i> would make armor class 10 (no armor) into armor class 9, and add +1 to saving throw dice rolls. To determine how powerful a given cloak is, use this table:\n\n'
        '<table>'
        '<tr><th>Roll</th><th>Protection</th></tr>'
        '<tr><td>01-35</th><th>+1 cloak</th></tr>'
        '<tr><td>36-65</td><td>+2 cloak</td></tr>'
        '<tr><td>66-85</td><td>+3 cloak</td></tr>'
        '<tr><td>86-95</td><td>+4 cloak</td></tr>'
        '<tr><td>96-00</td><td>+5 cloak</td></tr>'
        '</table>\n\n'
        'Note that this device can be combined with other items, or worn with leather armor. It cannot function in conjunction with any sort of magical armor, normal armor other than that of leather, or in conjunction with a shield of any sort.\n\n'
        'The <i>cloak</i> is worth 10,000 x.p. value and 1,000 g.p. value per plus of protection when sold.'
    )
),
MagicItem( name = 'Crystal Ball',
    category = MagicItemCategory.MISC,
    xp_value = [1000,2000],
    gold_value = [5000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This is the most common form of scrying device, a crystal sphere of about ½\' diameter. A magic-user can use the device to see over virtually any distance or into other planes of existence. The user of a <i>crystal ball</i> must know the subject which is to be viewed. Knowledge can be from personal acquaintance, possession of personal belongings, a likeness of the object, or accumulated information. Knowledge is the key to how successful location will be, not distance:\n\n'
        '<table>'
        '<tr><th>Subject is</th<th>Chance of Locating*</th></tr>'
        '<tr><td>Personally well known</td><td>100%</td></tr>'
        '<tr><td>Personally known slightly</td><td>85%</td></tr>'
        '<tr><td>Pictured</td><td>50%</td></tr>'
        '<tr><td>Part of in possession</td><td>50%</td></tr>'
        '<tr><td>Garment in possession</td><td>25%</td></tr>'
        '<tr><td>Well informed of</td><td>25%</td></tr>'
        '<tr><td>Slightly informed of</td><td>20%</td></tr>'
        '<tr><td>On another plane</td><td>25%</td></tr>'
        '</table>\n\n'
        '* Unless masked by magic or psionics.\n\n'
        'The chance of locating also dictates how long a magic-user will be able to view the subject, both with respect to length of period and frequency:\n\n'
        '<table>'
        '<tr><th>Chances of Locating*</th><th>Viewing Period</th><th>Frequency</th></tr>'
        '<tr><td>100% or more</td><td>1 hour</td><td>3 times/day</td></tr>'
        '<tr><td>99% to 90%</td><td>½ hour</td><td>3 times/day</td></tr>'
        '<tr><td>89% to 75%</td><td>½ hour</td><td>2 times/day</td></tr>'
        '<tr><td>74% to 50%</td><td>½ hour</td><td>1 time/day</td></tr>'
        '<tr><td>49% to 25%</td><td>¼ hour</td><td>1 time/day</td></tr>'
        '<tr><td>24% or less</td><td>10 minutes</td><td>1 time/day</td></tr>'
        '</table>\n'
        '*Unless masked by magic or psionics.\n\n'
        'Viewing beyond the periods or frequencies noted will cause the magic-user to make a saving throw versus magic each round, and failure to make it will permanently lower the character\'s intelligence by 1 point and drive him or her <i>insane</i> until <a href="/spells/heal-cleric-lvl-6"><i>healed</i></a>.\n\n'
        'Certain spells cast upon the user of the <i>crystal ball</i> might improve his or her ability. They are: <a href="/spells/comprehend-languages-magic-user-lvl-1"><i>comprehend languages</i></a>, <a href="/spells/read-magic-magic-user-lvl-1"><i>read magic</i></a>, <a href="/spells/infravision-magic-user-lvl-3"><i>infravision</i></a>, <a href="/spells/tongues-magic-user-lvl-3"><i>tongues</i></a>. Two spells can be cast <i>through</i> a <i>crystal ball</i>, with a 5% chance per level of experience of the magic-user of working correctly. The spells are: <a href="/spells/detect-magic-magic-user-lvl-1"><i>detect magic</i></a>, <a href="/spells/detect-evil-magic-user-lvl-2"><i>detect evil/good</i></a>.\n\n'
        'Certain <i>crystal balls</i> have additional powers. To determine this, consult the table below:\n\n'
        '<table>'
        '<tr><th>Roll</th><th>Crystal Ball Type</th></tr>'
        '<tr><td>01-50</td><td>crystal ball</td></tr>'
        '<tr><td>51-75</td><td>crystal ball with <a href="/spells/clairaudience-magic-user-lvl-3"><i>clairaudience</i></a></td></tr>'
        '<tr><td>76-90</td><td>crystal ball with <a href="/spells/esp-magic-user-lvl-2"><i>ESP</i></a></td></tr>'
        '<tr><td>91-00</td><td>crystal ball with <i>telepathy</i>*</td></tr>'
        '</table>\n'
        '* Communication only\n\n'
        'The spell function of the device operates at 10th level.\n\n'
        'Only creatures with intelligence of 12 or better have a chance of noticing the scrying. The base chance is determined by class.\n\n'
        '2% Fighter\n'
        '6% Paladin\n'
        '4% Ranger\n'
        '6% Thief\n'
        '5% Assassin\n'
        '1% Monk\n'
        '3% Bard\n\n'
        'For each factor of intelligence above 12 the creature has an additional arithmetically ascending cumulative chance beginning at 1%, i.e. 1%, 3%, 6%, 10%, 15%, 21%, at 13, 14, 15, 16, 17, and 18 intelligence. These creatures also have a cumulative chance of 1% per level of experience of detecting scrying. Treat monsters as one of above as is most applicable.\n\n'
        'Check each round of scrying, and if the percentage or less is rolled, the subject is aware of being watched. If a spell-user (cleric, druid, magic-user, or illusionist) is being observed, use the <b>DETECTION OF INVISIBILITY</b> table rather than the percentages above to determine whether observation is detected, checking each round.\n\n'
        '<table>'
        '<tr><th>Level of Creature</th><th>Hit Dice of Creature</th><th>12 INT</th><th>13-14 INT</th><th>15-16 INT</th><th>17+ INT</th></tr>'
        '<tr><td>7</td><td>7 & 7+</td><td>-</td><td>-</td><td>-</td><td>5%</td></tr>'
        '<tr><td>8</td><td>8 & 8+</td><td>-</td><td>-</td><td>5%</td><td>10%</td></tr>'
        '<tr><td>9</td><td>9 & 9+</td><td>-</td><td>5%</td><td>10%</td><td>15%</td></tr>'
        '<tr><td>10</td><td>10</td><td>5%</td><td>15%</td><td>20%</td><td>25%</td></tr>'
        '<tr><td>11</td><td>10+ - 11</td><td>15%</td><td>25%</td><td>30%</td><td>35%</td></tr>'
        '<tr><td>12</td><td>11+ - 12</td><td>25%</td><td>35%</td><td>40%</td><td>45%</td></tr>'
        '<tr><td>13</td><td>12+ - 13</td><td>35%</td><td>45%</td><td>50%</td><td>55%</td></tr>'
        '<tr><td>14</td><td>13+ - 14+</td><td>45%</td><td>55%</td><td>65%</td><td>75%</td></tr>'
        '<tr><td>15</td><td>15 and above</td><td>55%</td><td>65%</td><td>80%</td><td>95%</td></tr>'
        '</table>'
        'A <a href="/spells/dispel-magic-magic-user-lvl-3"><i>dispel magic</i></a> will cause the <i>crystal ball</i> being used to cease functioning for 1 day. The various protections again <i>crystal ball</i> viewing will simply leave the device hazy and non-functioning.\n\n'
        '(Note: You may allow scrying devices for clerics and druids; water basins and mirrors are suggested. Have them function as normal <i>crystal balls</i>.)\n\n'
        'Crystal balls with an additional feature are worth 2,000 x.p. and 10,000 g.p. when sold.'
    )
),
MagicItem( name = 'Crystal Hypnosis Ball',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [3000,3000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This cursed item type is indistinguishable from a normal <i>crystal ball</i>, and it radiates magic, but not evil, if detected for. Any magic-user attempting to use it will become hypnotized, and a telepathic <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a> will be implanted in his or her mind. The user of the device will believe that the desired object was viewed, but actually he or she became partially under the influence of a powerful magic-user, <a href="/creatures/lich">lich</a>, or even some power/being from another plane. Each further use will bring the <i>crystal ball</i> gazer more under the influence of the creature, either as a servant, tool, or possession object. As referee, you must decide whether to make this a gradual or sudden affair according to the surroundings and circumstances peculiar to the finding of the <i>crystal hypnosis ball</i> and the character(s) locating it.'
),
MagicItem( name = 'Cube of Force',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [20000,20000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A device of but about the size of a large die - perhaps ¾ of an inch across - the <i>cube of force</i> enables its possessor to put up a <i>wall of force</i> 1" per side around his or her person, and this cubic screen is impervious to the attack forms shown on the table below. The <i>cube</i> has 36 charges, and each day this energy is restored. The holder presses one face of the <i>cube</i> to activate or deactivate the field:\n\n'
        '<table>'
        '<tr><th>Cube Face</th><th>Charge Cost per Turn/Movement Rate</th><th>Effect</th></tr>'
        '<tr><td>one</td><td>1/1"</td><td>keeps out gases, wind, etc.</td></tr>'
        '<tr><td>two</td><td>2/8"</td><td>keeps out non-living matter</td></tr>'
        '<tr><td>three</td><td>3/6"</td><td>keeps out living matter</td></tr>'
        '<tr><td>four</td><td>4/4"</td><td>keeps out magic</td></tr>'
        '<tr><td>five</td><td>6/3"</td><td>keeps out all things</td></tr>'
        '<tr><td>six</td><td>0/normal</td><td>deactivates</td></tr>'
        '</table>\n\n'
        'When the force screen is up, the following attack forms cost extra charges from the cube in order to maintain the integrity of the screen. Note that these spells cannot be csat either into or out of the cube:\n\n'
        '<table>'
        '<tr><th>Spell/Attack</th><th>Extra Charge Cost</th></tr>'
        '<tr><td>catapult-like missiles</td><td>1</td></tr>'
        '<tr><td>very hot normal fires</td><td>2</td></tr>'
        '<tr><td><i>horn of blasting</i></td><td>6</td></tr>'
        '<tr><td><a href="/spells/delayed-blast-fireball-magic-user-lvl-7"></td><td>3</td></tr>'
        '<tr><td><a href="/spells/disintegrate-magic-user-lvl-6"><i>disintegrate</i></a></td><td>6</td></tr>'
        '<tr><td><a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a></td><td>3</td></tr>'
        '<tr><td><a href="/spells/fire-storm-druid-lvl-7"><i>fire storm</i></a></td><td>3</td></tr>'
        '<tr><td><a href="/spells/flame-strike-cleric-lvl-5"><i>flame strike</i></a></td><td>3</td></tr>'
        '<tr><td><a href="/spells/lightning-bolt-magic-user-lvl-3"><i>lightning bolt</i></a></td><td>4</td></tr>'
        '<tr><td><a href="/spells/meteor-swarm-magic-user-lvl-9"><i>meteor swarm</i></a></td><td>8</td></tr>'
        '<tr><td><a href="/spells/passwall-magic-user-lvl-5"><i>passwall</i></a></td><td>3</td></tr>'
        '<tr><td><a href="/spells/phase-door-magic-user-lvl-7"><i>phase door</i></a></td><td>5</td></tr>'
        '<tr><td><a href="/spells/prismatic-spray-illusionist-lvl-7"><i>prismatic spray</i></a></td><td>7</td></tr>'
        '<tr><td><a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a></td><td>2</td></tr>'
        '</table>'
        'The <i>cube of force</i> can be of any hard mineral, ivory or bone.'
    )
),
MagicItem( name = 'Cube of Frost Resistance',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [14000,14000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device resembles a <i>cube of force</i>. When the <i>cube</i> is activated it encloses an area of 1" per side, and the temperature within this area is always 65°F. The field will absorb all cold-based attacks, i.e. <a href="/spells/cone-of-cold-magic-user-lvl-5"><i>cone of cold</i></a>, <a href="/spells/ice-storm-magic-user-lvl-4"><i>ice storm</i></a>, and even <a href="/creatures/white-dragon">white dragon\'s</a> breath. However, if the field is subjected to more than 50 hit points of cold in any turn (10 rounds) it collapses and cannot be renewed for 1 hour. If it receives over 100 hit points of damage in 1 turn the <i>cube</i> is destroyed. Note: cold below 0 degrees F. effectively inflicts 2 hit points of cold for every -10°, so that the <i>cube</i> is at -2 at -1 to -10° F., -4 at -11 to -20, etc. Thus, at -40° F. the device can withstand only 42 hit points.'
),
MagicItem( name = 'Cubic Gate',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [17500,17500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Another small cubic device, this item is fashioned from carnelian. The 6 sides of the cube are each keyed to a plane, 1 of which will always be the <i>Prime Material</i>, of course. The other 5 can be chosen by any means desired. If the side of the <i>cubic gate</i> is pressed but once, it opens a nexus to the appropriate plane, and there is a 10% chance per turn that <i>something</i> will come through it looking for food, fun, and/or trouble. If the side is pressed twice, the creature so doing, along with all creatures in a 5\' radius will be drawn through the nexus to the other plane. It is impossible to open more than 1 nexial link at once.'
),
MagicItem( name = 'Daern\'s Instant Fortress',
    category = MagicItemCategory.MISC,
    xp_value = [7000,7000],
    gold_value = [27500,27500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This metal cube is of small size, but when activated it grows to form a metal tower 20\' square and 30\' high, with arrow slits on all sides and a machicolated battlement atop it, the metal extending 10\' into the ground. It has a small door which will open only to the command of the owner of the <i>fortress</i>, <a href="/spells/knock-magic-user-lvl-2"><i>knock</i></a> spells notwithstanding. The adamantite walls of <i>Daern\'s Instant Fortress</i> are totally unaffected by normal weapons other than those of catapult type. The whole can take 200 points of damage before the tower collapses. Note that damage sustained is cumulative. The <i>fortress</i> cannot be repaired, although a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> will restore 10 points of damage sustained. It requires but 1 round to cause the <i>fortress</i> to spring up, but the person or persons nearby must be careful not to be caught by its sudden growth, or else they will sustain 10-100 hit points of damage. The door will always be facing the owner of the device when it becomes a <i>fortress</i>, and it will open and close instantly at his command.'
),
MagicItem( name = 'Decanter of Endless Water',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [3000,3000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This flask is quite ordinary looking, but if magic is <a href="/spells/detect-magic-magic-user-lvl-1"><i>detected</i></a> it will radiate that property. The <i>decanter</i> has a stopper, and if this is removed, and the proper words spoken, it will pour forth a stream of fresh or salt water as ordered. There are separate command words for the amount as well as the type of water. Water can be made to come forth as follows:\n\n'
        'Stream: pours out 1 gallon per round\n'
        'Fountain: 5\' long stream at 5 gallons per round\n'
        'Geyser: 20\' long stream at 30 gallons per round\n\n'
        'The last shown application causes considerable back pressure, and the holder must be well braced or be knocked over. The force of the geyser will kill small animals and insects (mice, moles, small bats, etc.). The command word must be given to cease.'
    )
),
MagicItem( name = 'Deck of Many Things',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>deck of many things</i> (beneficial and baneful) usually is found contained within a box or leather pouch. Each deck contains a number of thin plaques or plates. These sheets are usually of ivory or vellum. Each is engraved and/or inscribed with glyphs, characters, and magical sigils. As soon as one of these sheets is drawn forth from the pack, its magic is bestowed upon the person who drew it, for better or worse. The character gaining a <i>deck of many things</i> may announce that only 1 will be drawn from the pack, or he or she may opt to draw forth 2, 3, or even 4, but the number <i>must</i> be announced prior to the first plaque withdrawn. Note that if the <i>jester</i> is drawn, the possessor of the <i>deck</i> may elect to draw 2 additional cards. Each time a plaque is taken from the <i>deck</i> it is replaced unless the draw is a <i>jester</i> or <i>fool</i>, in which case the plaque is discarded from the pack. The <i>deck</i> will contain either 13 or 22 plaques, 75%/25% chance. Additional plaques in a 22 card <i>deck</i> are indicated by an asterisk (*) before their names. To simulate the plaques you may use the normal playing card indicated:\n\n'
        'Sun (KD): Gain beneficial miscellaneous magic item and 50,000 experience points\n'
        'Moon (QD): You are granted 1-4 <a href="/spells/wish-magic-user-lvl-9"><i>wishes</i></a>\n'
        'Star (JD): Immediately gain 2 points on your major ability\n'
        '*Comet (2D): Defeat the next monster you meet to gain 1 level\n'
        'Throne (KH): Gain charisma of 18 and small keep\n'
        'Key (QH): Gain a treasure map plus 1 magic weapon\n'
        'Knight (JH): Gain the service of a 4th level fighter\n'
        '*Gem (2H): Gain your choice of 20 jewelry or 50 gems\n'
        '<b>The Void</b> (KC): Body functions, but soul is trapped elsewhere\n'
        'Flames (QC): Enmity between you and a devil\n'
        'Skull (JC): Defeat Death or be forever destroyed\n'
        '*Talons (2C): All magic items you possess are torn from you\n'
        'Ruin (KS): Immediately lose all wealth and real property\n'
        'Euryale (QS): Minus 3 on all saving throws vs. petrification\n'
        'Rogue (JS): One of your henchmen turns against you\n'
        '*Balance (2S): Change alignment or be judged\n'
        'Jester (J): Gain 10,000 experience points <b>or</b> 2 more draws from the <i>deck</i>\n'
        '*Fool (J with Trademark): Lose 10,000 experience points; draw again\n'
        '*Vizier (AD): Know the answer to your next dilemma\n'
        '*Idiot (AC): Lose 1-4 points of intelligence, you may draw again\n'
        '*Fates (AH): Avoid any situation you choose... once\n'
        '*<b>Donjon</b> (AS): You are <a href="/spells/imprisonment-magic-user-lvl-9"><i>imprisoned</i></a>\n\n'
        'Upon drawing the last plaque possible, or immediately upon drawing the plaques in <b>bold face (The Void, Donjon)</b>, the <i>deck disappears</i>. The plaques are explained below:\n\n'
        'Sun: Roll on the MISCELLANEOUS MAGIC TABLE (III.E, 1-5) until a useful item (other than artifacts or relics) is indicated. The player gets experience points for this as well.\n\n'
        'Moon: This is best represented by a moonstone gem with the appropriate number of wishes shown as gleams therein. These <a href="/spells/wish-magic-user-lvl-9"><i>wishes</i></a> are the same as the ninth level magic-user spell and must be used in a number of turns equal to the number received.\n\n'
        'Star: If the 2 points would place the character\'s score at 19, use 1 or both in any of the other abilities in this order: constitution, charisma, wisdom, dexterity, intelligence, strength.\n\n'
        'Comet: The player must single-handedly defeat the next monster - singular or plural - of hostile nature or the benefit is lost. If successful, the character moves to the mid-point of the next experience level.\n\n'
        'Throne: If charisma is 18 already, the individual still gains +25% on encounter and loyalty reactions. He or she becomes a real leader in people\'s eyes. The castle gained will be near to any stronghold already possessed.\n\n'
        'Key: Roll a treasure map with +20% on the dice. The weapon with it must be one usable by the character, so use the table for SWORDS (III.G), MISCELLANEOUS WEAPONS (III.H), or RODS, <i>et al.</i> (III.D.) as needed.\n\n'
        'Knight: The hero will join as the character\'s henchman and loyally serve until death. The hero has +1 per die (18 maximum) on each ability roll.\n\n'
        'Gem: This indicates wealth. The jewelry will all be gold set with gems, the gems all of 1,000 g.p. base value. With this wealth should come experience points equal in value, but never more than sufficient for 1 level rise in experience.\n\n'
        '<b>The Void</b>: This lightless black plaque spells instant disaster. The character\'s body functions, and he or she speaks like an automaton, but the psyche is trapped in a prison somewhere - in an object on a far planet or plane, possibly in the possession of a demon. A <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> will not bring the character back, but the plane of entrapment might be revealed.\n\n'
        'Flames: Hot anger, jealousy, envy, are but a few of the possible motivational forces for the enmity. The devil is usually of the <i>Greater</i> sort, possibly even an <i>Arch-devil</i>. The enmity can never be satisfied, save one or the other is slain.\n\n'
        'Skull: A minor Death appears (AC -4; 33 hit points; strike with a scythe for 2-16 hit points, never missing, always striking first in a round) and the character must fight it alone - if others help, they get minor Deaths to fight as well. If the character is slain he or she is slain <i>forever</i>. Treat the Death as undead with respect to spells. Cold or fire do not harm it, neither does electrical energy.\n\n'
        'Talons: When this plaque is drawn each and every magic item owned or possessed by the character drawing are irrevocably gone. This happens instantly.\n\n'
        'Ruin: As implied, when this plaque is drawn every bit of money (including all gems, jewelry, and like previous and valuable treasure and art) and all real property and buildings thereon currently owned are lost forever.\n\n'
        'Euryale: The Medusa-like visage of this plaque brings a curse which only the Fates card or god-like beings can remove. The -3 is permanent otherwise.\n\n'
        'Rogue: When this plaque is drawn, 1 of the character\'s henchman will be totally alienated and forever hostile henceforward. If the character has no henchmen, the enmity of some powerful personage - community or religious - can be substituted. The hatred will be secret until the time is ripe for devastating effect.\n\n'
        'Balance: As "weighed in the balance and found wanting", the character must change, and perform accordingly, to a radically different alignment, i.e. lawful-chaotic, good-evil, neutral-non-neutral. Failure brings judgment, and if there is substantial deviation from professed alignment, the character will be destroyed permanently.\n\n'
        'Jester: This plaque actually makes either pack more beneficial if the experience point award is taken. It is <i>always</i> discarded when drawn, unlike all others except the <i>Fool</i>.\n\n'
        'Fool: The payment and draw are mandatory!\n\n'
        'Vizier: This plaque empowers the character drawing it with the ability to call upon supernatural wisdom to solve any single problem or answer fully any question whenever he or she so requests. Whether the information gained can be successfully acted upon is another question entirely.\n\n'
        'Idiot: As indicated, the mongoloid countenance causes loss of 1-4 (d4) points of intelligence immediately. They are lost and cannot be regained (although points can be restored by other means). The additional draw is optional.\n\n'
        'Fates: This plaque enables the character to avoid even an instantaneous occurence if so desired, for the fabric of reality is unraveled and respun, so to speak. Note that it does not allow something <i>to</i> happen, only <i>not to</i> take place. This reversal is for the individual character only, and the party must still endure the confrontation.\n\n'
        '<b>Donjon</b>: This signifies <i>imprisonment</i> - either by <a href="/spells/imprisonment-magic-user-lvl-9">spell</a> or by some creature/being at your option. All gear and spells will be stripped from the victim in any case.'
    )
),
MagicItem( name = 'Drums of Deafening',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [500,500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This item is a pair of kettle drums, radiating magic if so detected, but otherwise unremarkable. If either is struck nothing happens, but if both are sounded together all creatures within 7" are permanently <i>deaf</i> and will remain so until a <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> spell or similar cure is used to restore shattered eardrums. Furthermore, those within 1" of the drums will be stunned by the noise for from 2-8 rounds. Each drum is a hemisphere of about 1½\' diameter.'
),
MagicItem( name = 'Drums of Panic',
    category = MagicItemCategory.MISC,
    xp_value = [6500,6500],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These kettle drums are unremarkable in appearance. If both of the pair are sounded, all creatures within 12", save for a "safe zone" of 2" radius from the <i>drums</i>, must make their saving throw versus magic or turn and move directly away from the sound for 1 full turn. Each turn thereafter, the panicked creatures may attempt to save versus magic again. Each failure brings another turn of movement away from the <i>drums of panic</i>. Movement is at fastest possible speed while fleeing in panic, and 3 rounds of rest are required for each 1 turn of fast movement after the saving throw is made. Creatures with intelligence of 2 make saving throws at -2, those with 1 or less save at -4. Each drum is a hemisphere of about 1½\' diameter.'
),
MagicItem( name = 'Dust of Appearance',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [4000,4000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This fine powder appears much like any other dust unless a careful examination is conducted. The latter will reveal it to be more like a metal dust, but very fine and very light. One handful of this substance flung into the air will coat all objects, making them visible even if they are invisible, out of phase, astral, or ethereal. Note that the <i>dust</i> will also reveal <a href="/spells/mirror-image-magic-user-lvl-2"><i>mirror images</i></a> and <a href="/spells/project-image-magic-user-lvl-5"><i>projected images</i></a> for what they are, and it likewise negates the effects of <i>cloaks of displacement</i> or <i>elvenkind</i> or <i>robes of blending</i>. Appearance lasts for 2-20 turns. It is typically in small silk packets or hollow bone blow tubes. A packet can be shaken out to cover an area with a radius of 10\' from the user. A tube can be blown in a cone shape, 1\' wide at the start, 15\' at the end, and 20\' long. From 5 to 50 containers can be in one place.'
),
MagicItem( name = 'Dust of Disappearance',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [8000,8000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This dust exactly resembles that of <i>appearance</i>, and it is typically found stored in the same manner and quantity. All things touched by it reflect and bend light of all sorts (infra-red and ultra-violet included) so as to become invisible to sight or virtually any other means of normal detection or even magical means such as <a href="/spells/detect-invisibility-magic-user-lvl-2"><i>detect invisibility</i></a> spells, but not <i>dust of appearance</i>. Invisibility bestowed by the <i>dust</i> lasts for 2 to 20 turns, 11-20 if carefully sprinkled upon an object. Attack while thus invisible is possible, always by surprise if the opponent is unable to note invisible things and always at an armor class 4 places better while invisibility lasts. Note that unlike the <a href="/spells/invisibility-magic-user-lvl-2"><i>invisibility</i></a> spell, attack while using the <i>dust of appearance</i> will not obviate the <i>invisibility</i>.'
),
MagicItem( name = 'Dust of Sneezing and Choking',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This fine dust appears to be either <i>Dust of Appearance</i> or <i>Dust of Disappearance</i>. If spread, however, it will cause those within a 20\' radius to fall into fits of sneezing and coughing, those failing to save versus poison die immediately, those who do being disabled by the choking for 5-20 rounds.'
),
MagicItem( name = 'Efreeti Bottle',
    category = MagicItemCategory.MISC,
    xp_value = [9000,9000],
    gold_value = [45000,45000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This item is typically fashioned of brass or bronze, with a lead stopper bearing special seals. It not uncommonly has a thin stream of smoke issuing from it. There is a 10% chance that the <a href="/creatures/efreeti">efreeti</a> will be insane and attack immediately upon being released. There is also a 10% chance that the efreeti of the bottle will only grant 3 <a href="/spells/wish-magic-user-lvl-9"><i>wishes</i></a>. The other 80% of the time, however, the inhabitant of the bottle will serve normally. When opened, the efreeti issues from the bottle in but 1 segment.'
),
MagicItem( name = 'Eversmoking Bottle',
    category = MagicItemCategory.MISC,
    xp_value = [500,500],
    gold_value = [2500,2500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This metal urn is identical to an <i>efreeti bottle</i>. It does nothing but smoke, however. The amount of smoke will be very great if the stopper is pulled out, pouring from the bottle and totally obscuring vision in a 50,000 cubic foot area in 1 round. The bottle, left unstoppered, will fill another 10,000 cubic feet of space with smoke each round until 120,000 cubic feet of space is fogged, and this area will continue to remain so smoked until the <i>eversmoking bottle</i> is <i>stoppered</i>. The <i>bottle</i> can only be resealed if a command word is known.'
),
MagicItem( name = 'Eyes of Charming',
    category = MagicItemCategory.MISC,
    xp_value = [4000,4000],
    gold_value = [24000,24000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This item consists of a pair of convex crystal lenses which fit over the user\'s eyes. When in place, the wearer is able to <a href="/spells/charm-person-magic-user-lvl-1"><i>charm persons</i></a> merely by meeting their gaze. Those failing to save versus magic are charmed as per the spell. One person per round can be thus looked at. Saving throws are at -2 if the wearer has both lenses, at +2 if he or she wears only 1 of a pair of <i>eyes of charming</i>.'
        'Note: Mixing magical eye types is certain to cause immediate insanity for 2-8 (2d4) turns.'
    )
),
MagicItem( name = 'Eyes of the Eagle',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [18000,18000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('These optics are also of special crystal and fit over the eyes of the wearer. They give vision 100 times greater than normal at distances of 1\' or more, i.e. the wearer can see at 2,000\' what a person could normally see at 20\'. Wearing only 1 of the cusps will cause the character to become dizzy, and in effect stunned, for 1 round. Thereafter, 1 eye must always be covered to avoid this vertigo.'
        'Note: Mixing magical eye types is certain to cause immediate insanity for 2-8 (2d4) turns.'
    )
),
MagicItem( name = 'Eyes of Minute Seeing',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Appearing much the same as any other magical lenses, <i>eyes of minute seeing</i> enable the wearer to see 100 times better at distances of 1\' or less. Thus, tiny seams, minute marks, even the impression left from writing can be seen, thus secret compartments and hidden joints can be noted and the information acted upon. The effect of wearing but one of these crystals is the same as given for <i>eyes of the eagle</i>.'
        'Note: Mixing magical eye types is certain to cause immediate insanity for 2-8 (2d4) turns.'
    )
),
MagicItem( name = 'Eyes of Petrification',
    category = MagicItemCategory.MISC,
    xp_value = [0,12500],
    gold_value = [0,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Totally indistinguishable from any other magical cusps, the effect of donning these lenses is instantaneous: the wearer is turned to stone. Note: 25% of these devices work as the gaze of a <a href="/creatures/basilisk">basilisk</a> does, including reflection of the weapon turning the gazer to stone.\n\n'
        'Note: Mixing magical eye types is certain to cause immediate insanity for 2-8 (2d4) turns.\n\n'
        'Standard <i>eyes</i> have no x.p. or g.p. value when sold, while those with reverse effect are worth 12,500 x.p. and 50,000 g.p.'
    )
),
MagicItem( name = 'Figurine of Wondrous Power',
    category = MagicItemCategory.MISC,
    xp_value = [100,100],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('There are various <i>figurines</i>, but all have the following in common. Each is apparently a statuette of small size, but an inch or so high. When the <i>figurine</i> is tossed down and a command word spoken, however, it becomes a living creature which obeys and serves its owner. If any <i>figurine</i> is destroyed in its statuette form it is forever ruined, all magic is lost, and it has no power. If slain in animal-like form the <i>figurine</i> simply reverts to its statuette conformation and can be used again at a later time as long as the statuette is not broken. When <i>figurines of wondrous power</i> are indicated, roll on the table below to determine the type:\n\n'
        '01-15: ebony fly\n'
        '16-30: golden lions (pair)\n'
        '31-40: ivory goats (trio)\n'
        '41-55: marble elephant\n'
        '56-65: obsidian steed\n'
        '66-85: onyx dog\n'
        '86-00: serpentine owl\n\n'
        '<i>Ebony Fly</i>: At a word the small carving grows to the size of a pony. The <i>ebony fly</i> is armor class 4, has 4+4 hit dice, air maneuverability class C, and flies at 48" movement rate without a rider, at 36" carrying up to 210 pounds weight, and 24" carrying from 211 to 350 pounds weight. The item can be used a maximum of 3 times per week, 12 hours per day. When 12 hours have expired, or in any event when the command word is spoken, the <i>ebony fly</i> shrinks to statuette size.\n\n'
        '<i>Golden Lions</i>: A pair of <i>golden lions</i> are exceptionally useful as they become 2 normal adult male lions (armor class 5/6, 5+2 hit dice, and normal attack modes). If slain in combat, the lions cannot be brought back from statuette form for 1 full week; otherwise, they can be used once every day. They enlarge and shrink upon speaking the command word.\n\n'
        '<i>Ivory Goats</i>: Each goat of this trio of statuettes looks slightly different, for each has a different function. These are:\n\n'
        '1. <i>The Goat of Travelling</i>: This statuette provides a speedy and enduring mount of armor class 6, with 24 hit points and 2 attacks (horns) for 1-8 each (consider as 4 hit dice monster). It moves at 48" bearing 280 pounds or less, and at -1" for every additional 14 pounds of weight carried. The goat can travel a maximum of 1 day each week - continuously or in any combination of periods totalling 24 hours. At this point, or when the command word is uttered, it returns to its small form for not less than 1 day before it can again be used.\n\n'
        '2. <i>The Goat of Travail</i>: When commanded, this statuette becomes an enormous creature, larger than a bull, with sharp hooves (4-10/4-10), a vicious bite (2-8), and a pair of wicked horns of exceptional size (2-12/2-12). If it is charging to attack, it may only use its horns, but +6 damage is added to each hit on that round, i.e., 8-18 h.p. damage per horn. It is armor class 0, has 96 hit points, and attacks as a 16 hit dice monster. It can be called to life but once per month. It moves 24".\n\n'
        '3. <i>The Goat of Terror</i>: When called upon with the proper command word, this statuette becomes a destrier-like mount, 36" movement, armor class 2, 48 hit points, and no attacks itself. However, its rider can employ the goat\'s horns as weapons, one horn as a +3 spear (lance), the other as a +6 sword. When ridden versus an opponent, the <i>goat of terror</i> radiates <i>terror</i> in a 3" radius, and any opponent in this radius must make a saving throw versus magic or lose 50% of strength and suffer at least -3 on "to hit" dice rolls, all due to weakness caused by terror. When all opponents are slain, or upon the proper command, the <i>goat</i> returns to its statuette form. It can be used once every 2 weeks.\n\n'
        'After 3 uses each of the <i>goats</i> loses its magical abilities forever.\n\n'
        '<i>Marble Elephant</i>: These are the largest of the <i>figurines</i>, each statuette being about the size of a human hand. Upon utterance of the command word, a <i>marble elephant</i> can be caused to grow to the size and specifications of a true elephant or return to statuette form. The animal created from the statuette is fully obedient to its commander, serving as a beast of burden, mount, or attacking alone. The type of <i>marble elephant</i> obtained is determined as follows:\n\n'
        '01-50: Asiatic (<a href="/creatures/elephant">Elephant</a>)\n'
        '51-90: African (<a href="/creatures/elephant">Loxodont</a>)\n'
        '91-93: Prehistoric (<a href="/creatures/mammoth">Mammoth</a>)\n'
        '94-00: Prehistoric (<a href="/creatures/mastodon">Mastodon</a>)\n\n'
        'The statuette can be used a maximum of 24 hours at a time, 4 times per month.\n\n'
        '<i>Obsidian Steed</i>: An <i>obsidian steed</i> appears as a small, nearly shapeless lump of black stone. Only careful inspection will reveal that it vaguely resembles some form of quadruped, and of course, if magic is detected for, the piece of rock which is the <i>steed</i> figurine will be noted as radiating some dweomer (magic). Upon speaking the command word, the near formless piece of obsidian becomes a true <a href="/creatures/nightmare"><i>nightmare</i></a>. It will allow itself to be ridden, but if the rider is of good alignment, it is 10% likely per use to carry its "master" to the floor of <i>Hades\'</i> first layer and then return to its statuette form. The statuette can be used for a 24 hour period maximum, once per week. Note that when the <i>obsidian steed</i> becomes astral or ethereal its rider and gear likewise so become, thus travel to other planes is easily accomplished by means of this item.\n\n'
        '<i>Onyx Dog</i>: When commanded, this statuette changes into a creature which has the same properties as a <a href="/creatures/war-dog"><i>war dog</i></a>, except that it is endowed with intelligence of 8-10, can communicate in the common tongue, and has exceptional olfactory and visual abilities. The olfactory power enables the <i>onyx dog</i> to scent the trail of a known creature 100% of the time if it is 1 hour or less old, -10% per hour thereafter, and subject to being thrown off by false trails, breaks, water, and masking or blocking substances or scents. The visual power enables the <i>onyx dog</i> to use 90\' range infravision, spotting hidden (such as in shadows) things 80% of the time, normally invisible things 65% of the time, and noting astral, ethereal, and out-of-phase things 50% of the time. An <i>onyx dog</i> can be used for up to 6 continuous hours, once per week. It obeys only its owner.\n\n'
        '<i>Serpentine Owl</i>: A <i>serpentine owl</i> becomes a normal-sized horned <a href="/creatures/owl">owl</a> (AC 7; 24" move; 2-4 hit points; 1-2/1-2 hit points of damage when attacking) if its possessor so commands, or it can become a <a href="/creatures/giant-owl"><i>giant owl</i></a> if its owner so requires. The latter usage, however, is limited to 3 times; thereafter the statuette loses all of its magical properties. The <i>normal-sized</i> form of the magical statuette moves with 95% silence, has infravision to 90\', can see in normal, above ground darkness as if it were full light, and twice as well as a human at that. Its hearing is so keen as to be able to detect a mouse moving at 60\' distance; thus silent movement chances are reduced 50% with respect to the <i>serpentine owl</i> in smaller form. Furthermore, it can and will communicate with its owner by telepathic means, informing of all its sees and hears according to its (<i>low</i>, 2-4) intelligence in normal-size. If commanded to giant-size, a <i>serpentine owl</i> is in all respects the same as a <a href="/creatures/giant-owl"><i>giant owl</i></a>. As with most other <i>figurinesof wondrous power</i>, this one readily obeys all commands of its owner.\n\n'
        'The x.p. and g.p. values are per hit die of the figurine.'
    )
),
MagicItem( name = 'Flask of Curses',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This item appears much the same as any beaker, bottle, container, decanter, flask, jug, etc. It has magical properties, but detection will not reveal the nature of the <i>flask of curses</i>. It often contains liquid substance too, or it may emit smoke. When the <i>flask</i> is first unstoppered, a <i>curse</i> of some sort will be visited upon the person or persons nearby (it will subsequently be harmless). The suggestions given for the <i>curse</i> reverse of the cleric <a href="/spells/bless-cleric-lvl-1"><i>bless</i></a> spell, and those stated for typical <i>curses</i> found on a scroll are recommended for use here as well, or some monster can appear and attack all creatures in sight, etc.'
),
MagicItem( name = 'Gauntlets of Dexterity',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A pair of these gloves appears to be nothing more than light leather handwear of the everyday sort. Naturally, they radiate magic if so detected. They size themselves magically to fit any hand, from that of a huge human to that of a small halfling, when drawn on. A pair of <i>gauntlets of dexterity</i> increase overall dexterity by 4 points if at 6 or less, by 2 points if at 7-13, and be 1 point if dexterity is 14 or higher. Furthermore, wearing these gloves enables non-thief characters to <i>pick pockets</i> or <i>open locks</i> as if he or she were a 4th level thief; if worn by a thief they increase these abilities by adding 10% to the normal percentage chance for the character\'s level.'
),
MagicItem( name = 'Gauntlets of Fumbling',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These gauntlets may be of supple leather or heavy protective gloves suitable for use with armor of ring, scale, schain, etc. In the former instance these gauntlets will appear to be of <i>dexterity</i>, in the latter case of <i>ogre power</i>. They will perform according to every test just as if they were other <i>gauntlets</i>, but when an enemy is actively seeking to harm their wearer, or in some similar life or death situation, their curse is activated, and he or she will become very clumsy, with a 50% chance each round of dropping anything held in either hand - not from both singly. The <i>gauntlets</i> will also lower overall dexterity by 2 points. Once the curse is activated, the gloves can only be removed by means of a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell or a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>.'
),
MagicItem( name = 'Gauntlets of Ogre Power',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A pair of <i>ogre power</i> gauntlets appear the same as typical handwear for armor. The wearer of these gloves, however, is imbued with 18/00 strength in his or her hands, arms, and shoulders. When striking with the hand or with a weapon hurled or held, the gauntlets add +3 to hit probability and +6 to damage inflicted when a hit is made. These gauntlets are particularly desirable when combined with a <i>girdle of giant strength</i> and a hurled weapon. They enlarge or shrink to fit human to <a href="/creatures/halfling">halfling</a>-sized hands.'
),
MagicItem( name = 'Gauntlets of Swimming and Climbing',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A pair of these gloves appear as normal lightweight handwear, but they are most useful magic items, and radiate their dweomer if a detection is attempted. The wearer can have hands of large (human) or small (<a href="/creatures/halfling">halfling</a>) size. He or she will be enabled to swim as fast as a <a href="/creatures/triton">triton</a> (15") under water, and as fast as a <a href="/creatures/merman">merman</a> (18") on the surface. Of course, these <i>gauntlets</i> do not empower the wearer to breathe water. These gloves also give the wearer a very strong and able gripping and holding ability with respect to climbing, so as to enable him or her to climb vertical or nearly vertical surfaces, upwards or downwards, with a 95% probability of not slipping and falling - and if the wearer is a thief the <i>gauntlets</i> increase success probability to 99.5%.'
),
MagicItem( name = 'Gem of Brightness',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [17500,17500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This crystal appears to be nothing more than a gem in rather rough, long prismed shape. Upon utterance of the proper spell words, however, the crystal will emit bright light of 3 sorts. It can be caused to shed a pale light in a cone-shape 10\' long, emanating from the <i>gem</i> to a radius of 2½\' at the end of the beam. This does not discharge any of the energy of the device. Another command will cause the <i>gem of brightness</i> to send out a very bright ray of light of only 1\' diameter but of 50\' length, and any creature who is struck in the eyes by this beam will be dazzled for 1-4 rounds and unable to see. The creature struck is entitled to a saving throw versus magic to determine whether or not its eyes were shut or averted in time. This use of the <i>gem</i> expends 1 energy charge. The third manner in which the item may be used is to cause it to flare in a blinding flash of light in a cone 30\' long and 5\' radius at its terminus. Although this glare lasts but a moment, all creatures within its area must save versus magic or be blinded for 1-4 rounds and thereafter suffer a penalty of -1 to -4 on hit probability dice rolls due to permanent eye damage. This use expends 5 charges. Dazzling or blindness effect can be removed by a <a href="/spells/cure-blindess-cleric-lvl-3"><i>cure blindness</i></a> spell; eye damage can be cured only by a <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> spell. The <i>gem of brightness</i> has 50 charges and cannot be recharged. A <a href="/spells/darkness-15-radius-magic-user-lvl-2"><i>darkness</i></a> spell will drain 1 of its charges, or make it useless for 1 round, at the option of the <i>gem</i> owner. A <a href="/spells/continual-darkness-illusionist-lvl-3"><i>continual darkness</i></a> spell will cause it to be useless for 1 day, or expend 5 charges, at the option of the owner.'
),
MagicItem( name = 'Gem of Seeing',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'One of these finely cut and polished stones is normally indistinguishable from a jewel of the ordinary sort, although a <a href="/spells/detect-magic-magic-user-lvl-1"><i>detect magic</i></a> will reveal its dweomer. When gazed through, the <i>gem of seeing</i> enables the user to detect all hidden, illusionary, invisible, astral, ethereal, or out of phase things within viewing range. Peering through the crystal is time consuming and tedious. The viewing range of the <i>gem</i> is 30" for a cursory manner, 2 rounds to view a 100\' square area in a careful way. There is a 5% chance each time the <i>gem</i> is used that the viewer will see an hallucination, see something that is not there, or possibly see through some real things as if it were an illusion.'
),
MagicItem( name = 'Girdle of Femininity/Masculinity',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This broad leather band appears to be a normal belt used commonly by all sorts of adventurers, but of course it is magical. If buckled on, it will <i>immediately</i> change the sex of its wearer to the opposite gender. Its magical curse fulfilled, the belt then loses all power. The original sex of the character cannot be restored by any normal means, although a <a href="/spells/wish-magic-user-lvl-9">wish</i> <i>might</i> do so (50% chance), and a powerful being can alter the situation, i.e., it takes a god-like creature to set matters aright with certainty. 10% of these girdles actually remove <i>all</i> sex from the wearer.'
),
MagicItem( name = 'Girdle of Giant Strength',
    category = MagicItemCategory.MISC,
    xp_value = [200,200],
    gold_value = [2500,2500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This belt looks similar to those normal to adventuring. It is imbued with very powerful magic, of course, and when worn it increases the physical prowess of its wearer as follows:\n\n'
        '<table>'
        '<tr><th>Dice Roll</th><th>Type of Giant Strength</th><th>Rating</th><th>To Hit</th><th>Damage</th><th>Open Doors*</th></tr>'
        '<tr><td>01-30</td><td>Hill</td><td>19</td><td>+3</td><td>+7</td><td>7 in 8 (3)</td></tr>'
        '<tr><td>31-50</td><td>Stone</td><td>20</td><td>+3</td><td>+8</td><td>7 in 8 (3)</td></tr>'
        '<tr><td>51-70</td><td>Frost</td><td>21</td><td>+4</td><td>+9</td><td>9 in 10 (4)</td></tr>'
        '<tr><td>71-85</td><td>Fire</td><td>22</td><td>+4</td><td>+10</td><td>11 in 12 (4)</td></tr>'
        '<tr><td>86-95</td><td>Cloud</td><td>23</td><td>+5</td><td>+11</td><td>11 in 12 (5)</td></tr>'
        '<tr><td>96-00</td><td>Storm</td><td>24</td><td>+6</td><td>+12</td><td>19 in 20 (7 in 8)</td></tr>'
        '</table>\n\n'
        '* The number in parentheses is the number of chances out of 6 (8 for storm giant strength) for the character to be able to force open a locked, barred, magically held, or <a href="/spells/wizard-lock-magic-user-lvl-2"><i>wizard locked</i></a> door, but only one attempt ever (per door) may be made, and if it fails, no further attempts can succeed.\n\n'
        'The wearer of the girdle is able to otherwise <i>hurl rocks</i> and <i>bend bars</i> as if he or she had imbibed a <i>potion of giant strength</i>. These abilities are:\n\n'
        '<table>'
        '<tr><th>Type><th>Weight Allowance</th><th colspan="3">Rock Hurling</th><th>Bend Bars/Lift Gates</th></tr>'
        '<tr><th></th><th></th><th>Range</th><th>Base Damage</th><th>Rock Weight**</th><th></th></tr>'
        '<tr><td>Hill</td><td>+4,500</td><td>8"</td><td>1-6</td><td>140</td><td>50%</td></tr>'
        '<tr><td>Stone</td><td>+5,000</td><td>16"</td><td>1-12</td><td>198</td><td>60%</td></tr>'
        '<tr><td>Frost</td><td>+6,000</td><td>10"</td><td>1-8</td><td>156</td><td>70%</td></tr>'
        '<tr><td>Fire</td><td>+7,500</td><td>12"</td><td>1-8</td><td>170</td><td>80%</td></tr>'
        '<tr><td>Cloud</td><td>+9,000</td><td>14"</td><td>1-10</td><td>184</td><td>90%</td></tr>'
        '<tr><td>Storm</td><td>+12,000</td><td>16"</td><td>1-12</td><td>212</td><td>100%</td></tr>'
        '</table>\n\n'
        '** Approximate average missile weight.\n\n'
        'The strength gained is <i>not</i> cumulative with normal or magical strength bonuses except with regard to use in combination with <i>gauntlets of ogre power</i> and magic war hammers.'
    )
),
MagicItem( name = 'Helm of Brilliance',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [60000,60000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('When discovered, a <i>helm of brilliance</i> appears to be nothing more than an ordinary piece of armor for head protection, viz. a helmet, basinet, sallet, etc. of iron or steel. When worn, it functions only upon the utterance of a special command word. When so empowered the true nature of the <i>helm</i> is visible to all. The <i>helm</i> is armor of +2 value. It is of brilliant silver and polished steel, and set with 10 diamonds, 20 rubies, 30 fire opals, and 40 opals - each of large size and magicked - which perform as explained below. When struck by bright light the helm will scintillate and send forth reflective rays in all directions from its crown-like spikes set with gems. The jewels\' functions are:\n\n'
        '   Diamond: <a href="/spells/prismatic-spray-illusionist-lvl-7"><i>Prismatic spray</i></a> (as the seventh level illusionist spell)\n'
        '   Ruby: <a href="/spells/wall-of-fire-druid-lvl-5"><i>Wall of fire</i></a> (as the fifth level druid spell)\n'
        '   Fire Opal: <a href="/spels/fireball-magic-user-lvl-3"><i>Fireball</i></a> (as the third level magic-user spell)\n'
        '   Opal: <a href="/spells/light-cleric-lvl-1"><i>Light</i></a> (as the first level cleric spell)\n\n'
        'Each gem is can perform its spell-like power in but 1 segment, but each is usable only once. The <i>helm</i> may be thus used once per round. The level of the spell is doubled to obtain the level at which the spell was cast with respect to range, duration, and such considerations. Until all of its jewels are magically expended, a <i>helm of brilliance</i> also is capable of the following magical properties when activated:\n\n'
        '   1. It glows with a bluish light when undead are within 30\', this light causing pain and 1-6 points of damage to all such creatures save <a href="/creatures/skeleton">skeletons</a> and <a href="/creatures/zombie">zombies</a>.\n\n'
        '   2. The wearer may command any sword he or she wields to become a <i>sword of flame</i>, this being additional to its other special properties if any; 1 round of time is required to effect this fire.\n\n'
        '   3. The wearer may <a href="/spells/produce-flame-druid-lvl-5"><i>produce flame</i></a> just as if he or she were a 5th level druid.\n\n'
        '   4. The wearer is protected just as if a double strength <i>fire resistance</i> ring were worn, but this protection cannot be augmented by further magical means.\n\n'
        'Once all of its jewels have lost their magic, the <i>helm</i> loses all of its powers. The gems turn to worthless powder when this occurs. Removing a jewel destroys the gem. They may <i>not</i> be re-magicked.\n\n'
        'If for any reason the wearer fails to make his or her saving throw versus a magical fire attack, he or she must attempt another saving throw for the helmet without magical additions. If this is failed, the remaining gems on the helm will all overload and detonate, causing in multiple whatever effects the gems would normally have.'
    )
),
MagicItem( name = 'Helm of Comprehending Languages and Reading Magic',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Appearing as a normal war helmet, a <i>helm of comprehending languages and reading magic</i> enables its wearer to understand 90% of strange tongues and writings, 80% of magical writings. (Note these percentage figures apply to whether <i>all</i> or <i>none</i> of the speaking/writing or inscription is understandable. Understanding does not necessarily imply spell use.) This device is equal to a normal helmet of the type accompanying armor class 5.'
),
MagicItem( name = 'Helm of Opposite Alignment',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'By appearance this metal hat is simply a typical helmet. By test, it will radiate an indeterminate dweomer. Once placed upon the head, however, its curse <i>immediately</i> takes place, and the <i>alignment</i> of the wearer is radically altered - good to evil, neutral to some absolute commitment (LE, LG, CE, CG) as radically different from former alignment as possible. Alteration in alignment is mental and, once effected, is desired by the individual whom the magic changed. Only a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>, or <a href="/spells/alter-reality-illusionist-lvl-7"><i>alter reality</i></a>, can restore former alignment, and the affected individual will <i>not</i> make any attempt to return to former alignment. If a paladin is concerned, he or she must undergo a special <a href="/spells/quest-cleric-lvl-5"><i>quest</i></a> and <a href="/spells/atonement-cleric-lvl-5"><i>atone</i></a> if the curse is to be obliterated. Note that once a <i>helm of opposite alignment</i> has functioned it loses all of its magical properties.'
),
MagicItem( name = 'Helm of Telepathy',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This sturdy metal helmet appears to be a normal piece of headgear, although it will radiate magic if this is detected for. The wearer of a <i>helm of telepathy</i> is able to determine the thoughts of creatures within a 6" range, provided the wearer knows the language used by such creatures (the racial tongue will be used in thoughts in preference to the common, the common in preference to alignment languages), and there is not more than 3\' of solid stone, ¼\' of iron, or any solid sheeting of lead or gold between the wearer and the creatures. The thought pick-up is directional. Concious effort must be made to pick up thoughts. The wearer may communicate by language with any creature within range if there is a mutually known speech, or emotions may be transmitted (empathy) so that a creature will receive the emotional message of the wearer. If the wearer of the <i>helm</i> desires to implant a <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a> (see the third level magic-user spell of that name), he or she may attempt to do so as follows: For every 2 points of intelligence <i>greater</i> than the subject, the wearer is 5% more likely to be successful; but for every 1 point of intelligence <i>lower</i> than the subject, the probability decreases by 5%. Thus the subject creature receiving the <i>suggestion</i> gains a saving throw versus magic with a -1 for every 2 points of intelligence lower than the telepathist, but +1 for every 1 point of intelligence <i>higher</i> than the wearer of the <i>helm</i>, and if intelligence is equal no adjustment is made when the saving throw is rolled. The <i>helm of telepathy</i> gives a +4 with respect to psionic related attacks (see Dungeon Masters Guide ATTACK MATRICES). It increases total psionic strength by 40 points.'
),
MagicItem( name = 'Helm of Teleportation',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This is another helmet of normal appearance which will give off a magical aura if detected for. Any character wearing this device may <a href="/spells/teleport-magic-user-lvl-5"><i>teleport</i></a> once per day, exactly as if he or she were a magic-user, i.e. the destination must be known, and a risk is involved. If a magic-user has access to this device, its full powers can be employed, for the wearer can then memorize a <i>teleportation</i> spell, and use the helm to refresh his or her memory so as to be able to repeat the spell up to 3 times upon objects or characters and still be able to personally <i>teleport</i> by means of the <i>helm</i>. As long as the magic-user retains the <i>teleportation</i> spell uncast, he or she can personally teleport up to 6 times before the memory of the spell is lost, and even then a usage of the <i>helm</i> remains as noted above.'
),
MagicItem( name = 'Helm of Underwater Action',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'When this <i>helm</i> is viewed, it is indistinguishable from a normal helmet, but detection will reveal it as magical, and the possessor will be able to both see and breathe under water. Visual properties of the helm are activated when small lenses are drawn across the device from compartments on either side of the helmet. They allow the wearer to see 5 times farther than normal water and light conditions allow for normal human vision. (Note that weeds, obstructions, etc. will block vision in the usual manner.) If the command word is spoken, the <i>helm of underwater action</i> creates a globe of air around the wearer\'s head, and maintains it, until the command word is again spoken. Thus, the wearer can breathe freely.'
),
MagicItem( name = 'Horn of Blasting',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [55000,55000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This magical horn appears as a normal trumpet, but it will reveal a dweomer if a detection for magic is cast upon it. It can be sounded as a normal horn, but if the correct word is spoken and the instrument then winded in the proper manner, it has the following effects:\n\n'
        '1. A cone of sound, 12" long and 3" wide at the base, issues forth from the <i>horn</i> and all within it must save versus magic. Those saving are <i>stunned</i> for 1 round and <i>deafened</i> for 2. Those failing the saving throw sustain 1-10 hit points of damage, are <i>stunned</i> for 2 rounds and <i>deafened</i> for 4.\n\n'
        '2. A wave of ultrasonic sound issues from the <i>horn</i> at the same time, a 1\' wide, 10" long pulse, which causes a weakening of such materials as metal, stone, and wood, the weakening equal in effect to 3 times the damage caused by a hit from a missile hurled by a large catapult, i.e. 18 structural points, or sufficient to smash a drawbridge or flatten a normal cottage.\n\n'
        'If a <i>horn of blasting</i> is winded magically more than once per day there is a 10% cumulative chance that it will explode itself and inflict 5-50 hit points of damage upon the person sounding it.\n\n'
        'There are no charges upon a <i>horn</i>, but the device is subject to stresses as noted above, and each times it is used to magical effect there is a 2% cumulative chance of the instrument shivering itself. In the latter case, no damage is inflicted on the character blowing it.'
    )
),
MagicItem( name = 'Horn of Bubbles',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [0,0],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This musical instrument will radiate magic if detected for. It appears as a normal horn, or possibly any one of the many magical ones. It will sound a note and call forth a mass of bubbles which completely surround and blind the individual who blew the horn for 2-20 rounds, but these bubbles will only appear in the presence of a creature actively seeking to slay the character who winded the <i>horn</i> so their appearance might be delayed for a very short of extremely lengthy period.'
),
MagicItem( name = 'Horn of Collapsing',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The <i>horn</i> appears to be a normal musical instrument, perhaps a bugle or warning horn of some sort. If it is sounded without first speaking the proper rune, or 10% of the time in any event, the following will result:\n\n'
        '<i>Outside</i>: A rain of fist-sized rocks will strike the individual sounding the <i>horn</i>, from 2-12 in number, each causing 1-6 hit points of damage.\n\n'
        '<i>Indoors</i>: The ceiling overhead will collapse when the device is blown, so the character will take from 3-36 hit points of damage.\n\n'
        '<i>Underground</i>: The area immediately above the character sounding the horn will fall upon him or her. The damage is 5-20 hit points base, multiplied by 1 factor for each 10\' of height from which the material above drops (i.e., twice damage if a 20\' ceiling, three times damage if a 30\' ceiling, etc.).\n\n'
        'Proper use of a <i>horn of collapsing</i> enables the character to sound it while it is pointed at the roof overhead from 30\' to 60\' beyond the user. The effect is to collapse a section of roof up to 20\' wide and 20\' long (10\' radius from the central aiming point) which inflicts damage as noted above if <i>indoors</i> or <i>underground</i> only.'
    )
),
MagicItem( name = 'Horn of the Tritons',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [17500,17500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This device is a conch shell horn which can be blown but once per day, except by a triton who can sound it 3 times daily. A <i>horn of the tritons</i> can do any 1 of the following functions when properly blown:\n\n'
        '1. Calm rough waters in a 1 mile radius (this has the effect of dispelling a <a href="/creatures/water-elemental">water elemental</a> or <a href="/creatures/water-weird">water weird</a>);\n\n'
        '2. Summon 5-20 <a href="/creatures/hippocampus">hippocampi</a> (1-2), 5-30 <a href="/creatures/giant-sea-horse">giant sea horses</a> (3-5), or 1-10 <a href="/creatures/sea-lion">sea lions</a> (6) if the character is in a body of water wherein such creatures dwell (the creatures summoned will be friendly to and obey, to the best of their understanding, the character who sounded the <i>horn</i>; or\n\n'
        '3. Panic marine creatures with animal, or lower, intelligence so as to cause them to flee unless each saves versus magic, and those who do save must take a -5 penalty on their "to hit" dice rolls for 3-18 turns (30-180 rounds).\n\n'
        'Any sounding of a <i>horn of the tritons</i> can be heard by all tritons within a 1 league radius.'
    )
),
MagicItem( name = 'Horn of Valhalla',
    category = MagicItemCategory.MISC,
    xp_value = [1000,3000],
    gold_value = [15000,45000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('There are 4 varieties of this magical device. Each summons a number of bersekers from Valhalla to fight for the character who summoned them by blowing the horn. Each variety of <i>horn</i> can be blown but once every 7 days. These horns all appear to be normal instruments until their command word is discovered. The type of <i>horn</i>, its powers, and who is able to employ it are shown below:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Type of Horn</th><th>Berserk Fighters Summoned</th><th>Usable By</th></tr>'
        '<tr><td>1-8</td><td>Silver</td><td>4-10 2nd level</td><td>any class</td></tr>'
        '<tr><td>9-15</td><td>Brass</td><td>3-9 3rd level</td><td>Cleric, Fighter, Thief</td></tr>'
        '<tr><td>16-18</td><td>Bronze</td><td>2-8 4th level</td><td>Cleric, Fighter</td></tr>'
        '<tr><td>19-20</td><td>Iron</td><td>2-5 5th level</td><td>Fighter</td></tr>'
        '</table>\n\n'
        'Any character whose class is unable to employ a particular sort of a <i>horn of Valhalla</i> will be attacked by the berserk fighters summoned when the character winds the horn.\n\n'
        'Fighters summoned are armor class 4, have 6 hit points per die, armed with sword and spear (50%), or battle axe and spear (50%). They gladly fight whomever the possessor of the horn commands, until they or their opponent(s) are slain, or 6 turns have elapsed, whichever occurs first.\n\n'
        'Fully 50% of these <i>horns</i> are aligned and will summon only fighters of the <i>horn\'s</i> alignment. A radical alignment difference will cause the <i>horn</i> blower to be attacked by the fighters.\n\n'
        'A silver or brass <i>horn</i> has an x.p. value of 1,000 and g.p. value of 15,000. Double for a <i>bronze horn</i>, triple for an <i>iron horn</i>.'
    )
),
MagicItem( name = 'Horseshoes of Speed',
    category = MagicItemCategory.MISC,
    xp_value = [2000,2000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These iron shoes are magical and will not wear out. They consist of 4 normal-appearing horse shoes, but when affixed to any horse\'s hooves, they double the animal\'s speed. There is a 1% chance per 7 leagues travelled that 1 will drop off, and if this passes unnoticed, the horse\'s speed will drop to 150% normal rate. If 2 are lost, speed is normal.'
),
MagicItem( name = 'Horseshoes of a Zephyr',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These iron shoes can be affixed as normal horseshoes, and they allow a horse to travel without actually touching the ground, so water can be passed over or no tracks made on any sort of ground. The horse is able to move at normal speeds, and it will not tire for as long as 12 hours continuous riding per day when wearing these magical horseshoes.'
),
MagicItem( name = 'Incense of Meditation',
    category = MagicItemCategory.MISC,
    xp_value = [500,500],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The small rectangular blocks of sweet-smelling <i>incense of meditation</i> are indistinguishable from non-magical incense until one is lit. When burning, the special fragrance and pearly-hued smoke of this special incense are recognizable by any cleric of 5th or higher level. When a cleric lights a block of the <i>incense of meditation</i> and spends 8 hours praying and meditating nearby, the <i>incense</i> will enable him or her to gain full and best spell effects. Thus, <i>cure wounds</i> spells are always maximum, spell effects are of the broadest area possible, and saving throws against their effects are at -1, and when dead are brought back to life the cleric reduces their chance of <i>not</i> surviving by one-half (rounded down). When this item of magic is discovered, there will be from 2-8 pieces of incense. One piece burns for 8 hours; the effects remain for 24 hours.'
),
MagicItem( name = 'Incense of Obsession',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [500,500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'These strange blocks of incense exactly resemble <i>incense of meditation</i>. If set alight and meditation and prayer are conducted while the <i>incense of obsession</i> is nearby, its odor and smoke will cause the cleric to become totally confident that his or her spell ability is superior due to the magical incense. The cleric will be completely determined to use his or her spells at every opportunity, typically when not needed or when useless. Nonetheless, the cleric will remain obsessed with his or her abilities and spells until all are cast or 24 hours have elapsed. There are 2-8 pieces of this incense normally, each burning for 1 hour.'
),
MagicItem( name = 'Ioun Stones',
    category = MagicItemCategory.MISC,
    xp_value = [300,300],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('There are 14 sorts of useful <i>ioun stones</i>. These magical stones always float in the air and must be within 3\' of their owner to be efficacious. The new possessor of the <i>stones</i> must hold each and then release it, so it takes up a circling orbit, whirling and trailing, circling at 1\' to 3\' radius of his or her head. Thereafter, they must be grasped or netted to separate them from their owner. The owner may voluntarily seize and stow the <i>stones</i> (at night, for example) to keep them safe. He or she would of course lose the benefits during that time. From 1-10 <i>ioun stones</i> will be found. Dice for the property of each <i>stone</i>, a duplication indicating a stone which is burned out and useless:\n\n'
        '<table>'
        '<tr><th>Dice Roll</th><th>Color of Stone</th><th>Shape</th><th>Use</th></tr>'
        '<tr><td>1</td><td>pale blue</td><td>rhomboid</td><td>adds 1 point to strength (18 maximum)</td></tr>'
        '<tr><td>2</td><td>scarlet & blue</td><td>sphere</td><td>adds 1 point to intelligence (18 maximum)</td></tr>'
        '<tr><td>3</td><td>incandescent blue</td><td>sphere</td><td>adds 1 point to wisdom (18 maximum)</td></tr>'
        '<tr><td>4</td><td>deep red</td><td>sphere</td><td>adds 1 point to dexterity (18 maximum)</td></tr>'
        '<tr><td>5</td><td>pink</td><td>rhomboid</td><td>adds 1 point to constitution (18 maximum)</td></tr>'
        '<tr><td>6</td><td>pink & green</td><td>sphere</td><td>adds 1 point to charisma (18 maximum)</td></tr>'
        '<tr><td>7</td><td>pale green</td><td>prism</td><td>adds 1 level of experience</td></tr>'
        '<tr><td>8</td><td>clear</td><td>spindle</td><td>sustains person without food or water</td></tr>'
        '<tr><td>9</td><td>iridescent</td><td>spindle</td><td>sustains person without air</td></tr>'
        '<tr><td>10</td><td>pearly white</td><td>spindle</td><td>regenerates 1 h.p. of damage/turn</td></tr>'
        '<tr><td>11</td><td>pale lavender</td><td>ellipsoid</td><td>absorbs spells up to 4th level*</td></tr>'
        '<tr><td>12</td><td>lavender & green</td><td>ellipsoid</td><td>absorbs spells up to 8th level**</td></tr>'
        '<tr><td>13</td><td>vibrant purple</td><td>prism</td><td>stores 2-12 levels of spells</td></tr>'
        '<tr><td>14</td><td>dusty rose</td><td>prism</td><td>gives +1 protection</td></tr>'
        '<tr><td>15-20</td><td>any</td><td>burned out, "dead" stone***</td><td></td></tr>'
        '</table>\n\n'
        '*After absorbing 10-40 spell levels the stone burns out and turns to dull gray, forever useless.\n\n'
        '**After absorbing 20-80 spell levels the stone burns out and turns dull gray, forever useless.\n\n'
        '***Adds 10 points to psionic strength total, 50 maximum points.\n\n'
        'Whenever <i>ioun stones</i> are exposed to attack, they are treated as armor class -4 and take 10 hit points of damage to destroy. They save as if they were of hard metal, +3.\n\n'
        'The x.p. and g.p. values are per stone.'
    )
),
MagicItem( name = 'Instrument of the Bards',
    category = MagicItemCategory.MISC,
    xp_value = [1000,7000],
    gold_value = [5000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('There are 7 magical instruments. Each can be fully utilized only by a bard, particularly a bard of at least as high a <i>college</i> as the instrument is named for, i.e. Fochlucan, Mac-Fuirmidh, Doss, etc. Bards of lower status, as well as other characters able to play such an <i>instrument</i>, will be able to use the device with only limited results. The 7 <i>instruments</i> are described below:\n\n'
        '<i>Fochlucan Bandore</i>: If this small, 3-stringed instrument is played by a 1st level bard (<i>probationer</i>) or a non-bard, it has a 50% chance per round of playing to cast a <a href="/spells/faerie-fire-druid-lvl-1"><i>faerie fire</i></a> spell, but there is a 10% chance that the musician will be limned by the glow, if the spell is so cast, rather than the desired target. A bard of Fochlucan or higher college casts the <i>faerie fire</i> spell at base 50% per level of bard experience above 1st, reducing the reverse effect by 1% per level above 1st. Furthermore, the <i>bandore</i> also has the following song properties when properly played:\n\n'
        '1. add 10% to the bard\'s <i>charm</i> percentage;\n'
        '2. cast an <a href="/spells/entangle-druid-lvl-1"><i>entangle</i></a> spell once per day;\n'
        '3. cast a <a href="/spells/shillelagh-druid-lvl-1"><i>shillelagh</i></a> spell once per day; and\n'
        '4. enable the bard to <a href="/spells/speak-with-animals-druid-lvl-1"><i>speak with animals</i></a> once per day.\n\n'
        'If a 1st level bard attempts these powers, there is a 30% chance that they will work, but a 70% chance that the player will take 2-8 hit points of damage.\n\n'
        '<i>Mac-Fuirmidh Cittern</i>: This lute-like instrument is 50% likely to deliver 3-12 hit points of damage to any non-bard or bard under 5th level who picks it up and attempts to play it. A 5th or higher level bard who uses the <i>cittern</i> has a 15% better chance of <i>charming</i> and can sing the following songs once per day which:\n\n'
        '1. cast a <a href="/spells/barkskin-druid-lvl-2"><i>barkskin</i></a> spell;\n'
        '2. <a href="/spells/cure-light-wounds-druid-lvl-2"><i>cure light wounds</i></a>; and\n'
        '3. cast an <a href="/spells/obscurement-druid-lvl-2"><i>obscurement</i></a> spell.\n\n'
        'Lower level bards cannot use the <i>cittern</i> even if they do not harm themselves (whether they take damage or not).\n\n'
        '<i>Doss Lute</i>: This instrument is 60% likely to deliver 4-16 hit points of damage to any non-bard or bard under 8th level who picks it up and attempts to play it. An 8th or higher level bard who plays the <i>lute</i> has a 20% better chance of <i>charming</i> and can sing magical songs once per day which:\n\n'
        '1. cast a <a href="/spells/hold-animal-druid-lvl-3"><i>hold animal</i></a>;\n'
        '2. <a href="/spells/neutralize-poison-druid-lvl-3"><i>neutralize poison</i></a>; and\n'
        '3. cast a <a href="/spells/protection-from-fire-druid-lvl-3"><i>protection from fire</i></a> in a 10\' radius.\n\n'
        '<i>Canaith Mandolin</i>: The <i>mandolin</i> is 70% likely to cause 5-20 hit points of damage upon any non-bard or bard of under the 11th level who attempts to utilize its powers by playing it. An 11th or higher level bard is able to employ the instrument to add 25% to his or her <i>charming</i> ability and also to cast the following spells once per day:\n\n'
        '1. <a href="/spells/cure-serious-wounds-druid-lvl-4"><i>cure serious wounds</i></a>;\n'
        '2. <a href="/spells/dispel-magic-druid-lvl-4"><i>dispel magic</i></a>; and\n'
        '3. cast a <a href="/spells/protection-from-lightning-druid-lvl-4"><i>protection from lightning</i></a> in a 10\' radius.\n\n'
        '<i>Cli Lyre</i>: A Cli Lyre is 80% likely to cause 6-24 hit points of damage upon any non-bard or bard of less than the 14th level of experience who plays it. A 14th or higher level bard adds 30% to <i>charming</i> ability and can cast the following spells by singing and playing on the <i>Lyre</i>, once each per day:\n\n'
        '1. <a href="/spells/control-winds-druid-lvl-5"><i>control winds</i></a>;\n'
        '2. <a href="/spells/transmute-rock-to-mud-magic-user-lvl-5"><i>transmute rock to mud</i></a>; and\n'
        '3. create a <a href="/spells/wall-of-fire-druid-lvl-5"><i>wall of fire</i></a>.\n\n'
        '<i>Anstruth Harp</i>: This powerful instrument is 90% likely to cause 8-32 hit points of damage to any non-bard or bard of less than 17th level who attempts to strum it. In the hands of a 17th or higher level bard the <i>harp</i> adds 35% to <i>charming</i> abilities and can by played so as to cast the following spells, one each per day:\n\n'
        '1. <a href="/spells/cure-critical-wounds-druid-lvl-6"><i>cure critical wounds</i></a>;\n'
        '2. create a <a href="/spells/wall-of-thorns-druid-lvl-6"><i>wall of thorns</i></a>; and\n'
        '3. cast a <a href="/spells/weather-summoning-druid-lvl-6"><i>weather summoning</i></a>.\n\n'
        '<i>Ollamh Harp</i>: If an <i>Ollamh Harp</i> is played by any non-bard or bard of under 20th level it will inflict 10-40 hit points of damage upon such an individual. When played by a bard of 20th or higher level, it adds 40% to his or her <i>charming</i> abilities and can cast one each of the following spells daily:\n\n'
        '1. <a href="/spells/confusion-druid-lvl-7"><i>confusion</i></a>;\n'
        '2. <a href="/spells/control-weather-druid-lvl-7"><i>control weather</i></a>; and\n'
        '3. <a href="/spells/fire-storm-druid-lvl-7"><i>fire storm</i></a>.\n\n'
        '<b>General Properties of All Bard Instruments:</b>\n\n'
        'Each and every instrument looks exactly alike due to powerful dweomers placed upon them.\n\n'
        'Any character able to play one of these instruments can sing so as to do one of the following for as many turns as the order of the college, i.e. 1-7, a <i>magnus alumni</i> for 8 turns with <i>any</i> of the 7, once each per day:\n\n'
        '1. put up a 10\' radius <a href="/spells/protection-from-evil-magic-user-lvl-1"><i>protection from evil</i></a>;\n'
        '2. become <a href="/spells/invisibility-magic-user-lvl-2"><i>invisible</i></a> (although the strumming and singing can still be heard distantly, the exact location is impossible to discover unless detection of invisibility is possible);\n'
        '3. <a href="/spells/levitate-magic-user-lvl-2"><i>levitate</i></a>; and\n'
        '4. <a href="/spells/fly-magic-user-lvl-3"><i>fly</i></a>.\n\n'
        'Each ability of the instrument takes 5 segments to activate, and not less than 1 full round to complete.\n\n'
        'If the bard\'s charming ability exceeds 100% with instrument bonus, the creature saving against the magic does so at -1 for every 5% above 100%, 3% or 4% being rounded to the next 5%, i.e. 3% = 5%, 8% = 10%, 13% = 15%, etc.\n'
        'The type of instrument found is determined by the table below:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Instrument</th></tr>'
        '<tr><td>1-5</td><td>Fochlucan Bandore</td></tr>'
        '<tr><td>6-9</td><td>Mac-Fuirmidh Cittern</td></tr>'
        '<tr><td>10-12</td><td>Doss Lute</td></tr>'
        '<tr><td>13-15</td><td>Canaith Mandolin</td></tr>'
        '<tr><td>16-17</td><td>Cli Lyre</td></tr>'
        '<tr><td>18-19</td><td>Anstruth Harp</td></tr>'
        '<tr><td>20</td><td>Ollamh Harp</td></tr>'
        '</table>'
    )
),
MagicItem( name = 'Iron Flask',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [0,0],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('One of these special containers will typically be inlaid with runes of silver and stoppered by a brass plug bearing a seal of great dweomer set round with sigils, glyphs, and special symbols. When the user speaks a command, he or she can force any creature from another plane (daemon, demon, devil, elemental, etc.) <i>into</i> the container, provided the creature does not make its saving throw versus magic - after magic resistance, if any, is checked. Range is 6". Only 1 creature at a time can be so contained. Loosing the stopper frees the captured creature; and if the individual loosing the plug knows the command word, the creature can be forced to serve for 1 turn (or to perform a <i>minor</i> service which takes up to 1 hour of time). If freed without command knowledge, dice for the creature\'s reaction... Any attempt to force the same creature into the <i>flask</i> a second time allows it a +2 on its saving throw and makes it VERY angry and totally hostile. A discovered bottle can contain:\n\n'
        '01-50: empty\n'
        '51-54: <a href="/creatures/air-elemental">air elemental</a>\n'
        '55-56: demon (type I-III)\n'
        '57: demon (type IV-VI)\n'
        '58-59: devil (lesser)\n'
        '60: devil (greater)\n'
        '61-65: <a href="/creatures/djinni">djinni</a>\n'
        '66-69: <a href="/creatures/earth-elemental">earth elemental</a>\n'
        '70-72: <a href="/creatures/efreeti">efreeti</a>\n'
        '73-76: <a href="/creatures/fire-elemental">fire elemental</a>\n'
        '77-81: <a href="/creatures/invisible-stalker">invisible stalker</a>\n'
        '82-83: <a href="/creatures/mezzodaemon">mezzodaemon</a>\n'
        '84-85: <a href="/creatures/night-hag">night hag</a>\n'
        '86: <a href="/creatures/nycadaemon">nycadaemon</a>\n'
        '87-89: <a href="/creatures/rakshasa">rakshasa</a>\n'
        '90-93: <a href="/creatures/salamander">salamander</a>\n'
        '94-97: <a href="/creatures/water-elemental">water elemental</a>\n'
        '98-99: <a href="/creatures/wind-walker">wind walker</a>\n'
        '00: <a href="/creatures/xorn">xorn</a>'
    )
),
MagicItem( name = 'Javelin of Lightning',
    category = MagicItemCategory.MISC,
    xp_value = [250,250],
    gold_value = [3000,3000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>javelin of lightning</i> is considered equal to a +2 magic weapon, although it has neither "to hit" nor damage bonuses. It has a range of 9" and whenever it strikes, the <i>javelin</i> then becomes the head of a ½" wide, 3" long stroke of lightning. Any creature hit by the <i>javelin</i> suffers 1-6 hit points of damage, plus 20 hit points of electrical damage. Any other creatures in the path of the back stroke take either 20 or 10 hit points of damage. (Draw a straight line between point of impact 3" back in the direction of the character hurling it.) From 2-5 will be found. The <i>javelin</i> is consumed in the lightning discharge.'
),
MagicItem( name = 'Javelin of Piercing',
    category = MagicItemCategory.MISC,
    xp_value = [250,250],
    gold_value = [3000,3000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This weapon is not actually hurled, as when a command word is spoken; the <i>javelin of piercing</i> launches itself. Range is 6", all distances considered as <i>short</i> range. The javelin is +6 "to hit" and inflicts 7-12 hit points of damage. (Note this missile will fly horizontally, vertically, or any combination thereof to the full extent of its range.) From 2-8 will be found. The magic of the <i>javelin</i> is good for only 1 throw.'
),
MagicItem( name = 'Jewel of Attacks',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This gleaming gem radiates magic and appears to be a valuable item. It is cursed, however, and it brings both 100% more likelihood of encountering wandering monsters and 100% greater likelihood of pursuit when monsters are encountered and the party seeks to evade them by flight. Once picked up, the <i>jewel of attacks</i> will always magically return to its finder (secreting itself in pouch, bag, pack, pocket, etc.) until a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell or an <a href="/spells/atonement-cleric-lvl-5"><i>atonement</i></a> is cast upon him or her.'
),
MagicItem( name = 'Jewel of Flawlessness',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,100000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This magical gem appears to be a very fine stone of some sort, but if magic is detected for, its dweomer will be noted. When a <i>jewel of flawlessness</i> is placed with other gems, it increases the likelihood of their being more valuable by 100%, i.e., the chance for each stone going up in value increases from 1 in 10 to 2 in 10. The <i>jewel</i> has from 10-100 facets, and whenever a gem increases in value because of the magic of the <i>jewel of flawlessness</i> (a roll of 2 on d10), 1 of these facets disappears. When all are gone, the <i>jewel</i> is a spherical stone of no value.'
        'The g.p. value of the gem is 1,000 g.p. per facet.'
    )
),
MagicItem( name = 'Keoghtom\'s Ointment',
    category = MagicItemCategory.MISC,
    xp_value = [500,500],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This sovereign salve is useful for drawing poison, curing disease, or healing wounds. A jar of the ungent is small - perhaps three inches in diameter and one inch deep - but contains 5 applications. Placed upon a poisoned wound (or swallowed), it detoxifies any poison or disease. Rubbed on the body, the <i>ointment</i> heals 9-12 points of damage. 1-3 jars will commonly be found.'
),
MagicItem( name = 'Libram of Gainful Conjuration',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This mystic compilation contains much arcane knowledge for magic-users (including illusionists) of <i>neutral</i> (neutral, chaotic neutral, lawful neutral) alignment. If a character of this class and alignment spends a full week, cloistered and undisturbed, pondering its contents, he or she will gain experience points sufficient to place him or her exactly at the mid-point of the next higher level. When this occurs, the <i>libram</i> will disappear - totally gone - and that same character can never benefit again from reading such a work. Any non-neutral magic-user reading so much as a line of the <i>libram</i> will take 5-20 points of damage, be unconcious for a like number of turns, and must seek a cleric to <a href="/spells/atonement-cleric-lvl-5"><i>atone</i></a> in order to regain the ability to progress in experience (until doing so, he or she will gain no further experience). Any non-magic-user perusing the work will be required to save versus magic in order to avoid <i>insanity</i>. Those characters going <i>insane</i> must receive a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> and rest for 1 month or have a cleric <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> them.'
),
MagicItem( name = 'Libram of Ineffable Damnation',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This work is exactly like the <i>Libram of Gainful Conjuration</i> except that it benefits <i>evil</i> magic-users, and non-evil characters of that class will <i>lose</i> 1 level of experience merely from looking inside of its brass-bound covers, in addition to the other ill effects of perusing but 1 line of its contents.'
),
MagicItem( name = 'Libram of Silver Magic',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This mystic text is the reverse of the <i>Libram of Ineffable Damnation</i>, greatly beneficial to <i>good</i> magic-users, most baneful to non-good ones. Like all magical works of this sort, it vanishes after 1 week of study, and the character having benefited from it can never be so aided again.'
),
MagicItem( name = 'Lyre of Building',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The enchantments placed upon this instrument make it indistinguishable from a normal one; and even if its magic is detected, it cannot be told from an <i>instrument of the bards</i> until it is played. If the proper chords are struck, the <i>lyre</i> will negate the effects of a <i>horn of blasting</i>, a <a href="/spells/disintegrate-magic-user-lvl-6"><i>disintegrate</i></a> spell, or the effects of 6 rounds of an attack of an earth elemental - all as pertains to constructions. Such playing of these negatory chords can be done once per day. The <i>lyre</i> is also useful with respect to actual building, of course. Once per week its strings can be strummed so as to produce actual chords which magically construct buildings, mines, tunnels, ditches, or whatever. The effect produced in but 3 turns of such playing is equal to the work of 100 men laboring for 3 days. If a false chord is struck, all effects of the <i>lyre</i> are 20% likely to be negated. A false chord is only 5% likely once the character knows the proper ones, but if disturbed by physical or mental attack while playing, the likelihood rises to 50%.'
),
MagicItem( name = 'Manual of Bodily Health',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'As with all magical writings of this nature, the metal-bound <i>Manual of Bodily Health</i> appears to be an arcane, rare, but non-magical book. If a <a href="/spells/detect-magic-cleric-lvl-1"><i>detect magic</i></a> spell is cast upon it, the <i>manual</i> will radiate an aura of magic. Any single character who reads the work (24 hours of time over 3-5 days) will know how to increase his or her constitution by 1 point by following a regimen of special dietary intake and breathing exercises over a 1 month period. The book disappears immediately upon completion of its contents. The 1 point of constitution is gained only after the prescribed regimen is followed. In 3 months the knowledge of the secrets to bodily health will be forgotten. The knowledge cannot be articulated or recorded by the reader. The <i>manual</i> will not be useful to any character a second time, nor will other than a single character be able to benefit from it.'
),
MagicItem( name = 'Manual of Gainful Exercise',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This work is similar to the <i>Manual of Bodily Health</i>, but its reading and prescribed course of action will result in the addition of 1 point to the reader\'s strength.'
),
MagicItem( name = 'Manual of Golems',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This compilation is a treatise on the construction and animation of a golem. It contains all of the information and incantations necessary to make 1 of the 4 sorts of golems. It will take a considerable amount of time, and be expensive as well, to construct and animate the golem. During this period, a single magic-user or cleric must have the <i>manual</i> at hand to study, and he or she must not be interrupted. The type of <i>manual</i> found is determined as noted below:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Type of Golem</th><th>Construction Time</th><th>G.P. Cost</th></tr>'
        '<tr><td>1-5</td><td><a href="/creatures/clay-golem">Clay</a> (C)</td><td>1 month</td><td>65,000</td></tr>'
        '<tr><td>6-17</td><td><a href="/creatures/flesh-golem">Flesh</a> (M)</td><td>2 months</td><td>50,000</td></tr>'
        '<tr><td>18</td><td><a href="/creatures/iron-golem">Iron</a> (M)</td><td>4 months</td><td>100,000</td></tr>'
        '<tr><td>19-20</td><td><a href="/creatures/stone-golem">Stone</a> (M)</td><td>3 months</td><td>80,000</td></tr>'
        '</table>\n\n'
        'Once the golem is finished, the writing fades and the book is consumed in flames. When the ashes of the <i>manual</i> are sprinkled upon the golem it becomes fully animated. It is assumed that the user of the manual is of 10th or higher level. For every level of experience under 10th there is a cumulative 10% chance that the golem will fall to pieces within 1 turn of completion of its construction due to the maker\'s imperfect understanding.\n\n'
        'If a cleric reads a work for magic-users, he or she will lose 10,000-60,000 experience points. A magic-user reading a clerical work will lose 1 level of experience. Any other class of character will suffer 6-36 hit points of damage from opening the work.'
    )
),
MagicItem( name = 'Manual of Puissant Skill at Arms',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This scholarly study contains expert advice and instruction regarding weapon use and various attack and defense modes. Any single fighter (including a bard, but <i>not</i> a paladin or ranger) who reads the <i>manual</i> and practices the skills described therein for 1 month will go up to the mid-point of the next higher level. The book disappears after it is read, and the knowledge therein will be forgotten within 3 months, so it must be acted upon with reasonable expedition. The fighter cannot articulate what he or she has read, nor can it be recorded in any fashion. A paladin or ranger will understand the work but it cannot benefit either class. Any cleric (including druid), thief (including assassin), or monk who handles/reads the <i>manual</i> will not understand it. If a magic-user (including an illusionist) so much as scans a few of its letters, he or she will be stunned for 1-6 turns and lose 10,000-60,000 experience points as the work is so opposed to the magic-using profession. Only one perusal of the work will benefit the same character.'
),
MagicItem( name = 'Manual of Quickness of Action',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The heavy covers and metal bindings of this compilation will not distinguish it from any of scores of semi-valuable, non-magical texts. This work contains secret formulae and prescriptions for unguents and exercises which enable a single reader to assimilate the text (3 days of uninterrupted study) and then practice the skills detailed therein. If this practice is faithfully done for 1 month, the character will gain 1 point of dexterity. While the <i>manual</i> will disappear immediately after reading, the contents will be remembered for 3 months (although the reader will <i>not</i> be able to articulate or otherwise record the information he or she retains). Only after the month of training will the dexterity bonus be gained. Further perusal of a similar text will not add further to the same character\'s dexterity.'
),
MagicItem( name = 'Manual of Stealthy Pilfering',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This guide to expertise at thievery is so learned and erudite that any single thief who reads it and then spends 1 month thereafter practicing the skills therein will gain experience points sufficient to place him or her at the mid-point of the next higher level. The text disappears after reading, but knowledge is retained for 3 months - as with other magical texts of this sort, the knowledge cannot be recorded or told of, however. Any additional reading of a like <i>manual</i> is of no benefit to the same character. Assassins who read the work will gain but 5,000 additional experience points after the contents have been read and pondered for 1 week. Fighters, magic-users, and monks will not comprehend the work. Clerics, rangers, and paladins who read even a word of the book take 5-20 hit points of damage, are <i>stunned</i> for a like number of rounds, and if a saving throw versus magic is failed, they lose 5,000-20,000 experience points as well. In addition, such characters must <a href="/spells/atonement-cleric-lvl-5"><i>atone</i></a> within 1 day or lose 1 point of wisdom.'
),
MagicItem( name = 'Mattock of the Titans',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [7000,7000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This huge digging tool is 10\' long and weighs over 100 pounds. Any giant-sized creature with a strength of 20 or more can use it to loosen (or tumble) earth (or earthern ramparts) in a 100 cubic foot area in 1 turn. It will smash rock in a 20 cubic feet area in the same amount of time. If used as a weapon, it is +3 "to hit" and does 5-30 hit points of damage, exclusive of strength bonuses. (Cf. <i>girdle of giant strength.)'
),
MagicItem( name = 'Maul of the Titans',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [7000,7000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This huge mallet is 8\' long and weighs over 150 pounds. Any giant-sized creature with strength of 21 or greater can employ it to drive piles of up to 2\' diameter into normal earth at 4\' per blow - 2 blows per round. The <i>maul</i> will smash to flinders an oaken door of up to 10\' height by 4\' width by 2 inch thickness in 1 blow - 2 if the door is heavily bound with iron. If used as a weapon it is +2 "to hit" and inflicts 10-40 hit points of damage, exclusive of strength bonuses.'
),
MagicItem( name = 'Medallion of ESP',
    category = MagicItemCategory.MISC,
    xp_value = [1000,3000],
    gold_value = [10000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('An <i>ESP Medallion</i> appears to be a normal neck chain - usually fashioned from bronze, copper, or nickel-silver - with pendant disc. The device enables the wearer to concentrate and pick up thoughts in a path 1" wide at the <i>medallion</i> and broadening 2\' every 10\' from the device the magic reaches, up to an 11\' maximum width at 50\' (5"). It requires a full round for a character to so use the device. The <i>medallion</i> is prevented from functioning by stone of over 3\' thickness, metal of over 1/6\' thickness, or any continuous sheeting of lead, gold or platinum of any thickness greater than paint. The medallion malfunctions (with no result) on a die roll of 6 on d6, and the device must be checked each time it is used. The character using the device can pick up only the surface thoughts of creatures in the path of the ESP area. The general distance can be determined, but all thoughts will be understandable only if the user knows the language of the thinkers. If the creatures use no language, only the prevailing emotions can be felt - understood only with an <i>ESP-Empathy</i> device (see below). Note that undead and mindless golems have neither readable thoughts nor emotions. (See also <b>PSIONICS</b>.) The type of <i>medallion</i> found is determined below:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Medallion</th></tr>'
        '<tr>1-15<td></td><td>30\' range</td></tr>'
        '<tr>16-18<td></td><td>30\' range with empathy</td></tr>'
        '<tr>19<td></td><td>60\' range</td></tr>'
        '<tr>20<td></td><td>90\' range</td></tr>'
        '</table>\n\n'
        'Note that thoughts cannot be sent through any <i>medallion of ESP</i>.'
    )
),
MagicItem( name = 'Medallion of Thought Projection',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device is exactly like an <i>ESP Medallion</i> in every respect, even as to the range it functions at. However, in addition to picking up the thoughts of creatures, it broadcasts the thoughts of the user to the creatures in the path of the beam, thus alerting them. Note: it functions correctly, <i>without projecting thoughts</i>, on a roll of 6.'
),
MagicItem( name = 'Mirror of Life Trapping',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This crystal device is usually about 4 square feet in area, framed in metal, wood, etc. It is usable only by magic-users, although it cana be affixed to a surface to operate alone by giving a command word. A <i>mirror</i> has from 13 to 18 non-spatial/extra-dimensional compartments within it. Any creatures coming within 30\' of the device and looking at it so as to see its reflection must save versus magic or be <i>trapped</i> within the mirror in one of the cells. It is 100% probable that any creature not aware of the nature of the device will see its reflection, the probability dropping to 50% if the creature actively avoids so doing and 20% if the creature is aware that the mirror traps life. When a creature is trapped, it is taken bodily into the <i>mirror</i>. Size is not a factor, but automatons and non-living matter (including golems but excluding <i>intelligent</i> undead) are not trapped. The possessor of the mirror can call the reflection of any creature that is trapped within to the surface of the mirror, and the powerless creature can be conversed with. If mirror capacity is exceeded, 1 victim (random) will be set free to accommodate the latest one. If the mirror is broken, all victims are freed (usually to then attack the possessor of the device). Note that the possessor of a <i>mirror of life trapping</i> can speak a command word so as to free a trapped creature, but the cell of the creature must be known. Example: "In the name of Zagig the Great I command the occupant of the 3rd cell to come forth!"'
),
MagicItem( name = 'Mirror of Mental Prowess',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This magical mirror resembles an ordinary one. The possessor, however, knowing the proper commands can cause it to perform as follows:\n\n'
        '1. Read the thoughts of any creature reflected therein, even though these thoughts are in an unknown language;\n'
        '2. Scry with it as if it were a <i>crystal ball</i> with <a href="/spells/clairaudience-magic-user-lvl-3"><i>clairaudience</i></a>, but even being able to view into other planes if the viewer knows of them sufficiently;\n'
        '3. It can be used as a portal to visit other places (possibly other planes, as well, at the DM\'s option) by first scrying them and then stepping through to the place pictured - an invisible area remains on the "other side", and those using the portal can return if the correct spot can be found. (Note that creatures being scried can step through also if the place is found by them!);\n'
        '4. Once per week it will answer one short question, briefly, regarding a creature whose image is shown upon its surface.\n\n'
        'The typical <i>mirror</i> size is 5\'x2\'.'
    )
),
MagicItem( name = 'Mirror of Opposition',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [2000,2000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This mirror exactly resembles a normal mirror. Any creature reflected in its surface will cause an exact duplicate to come into being, and this opposite will immediately attack. Note that the duplicate will have all items and powers of the original (including magic), but upon the defeat or destruction of either, the duplicate and his or her items disappear completely.'
),
MagicItem( name = 'Necklace of Adaptation',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This chain will resemble a medallion. The wearer will be able to ignore gases of all sorts which affect creatures through respiration, breathe underwater, or even exist in airless space for up to 7 days.'
),
MagicItem( name = 'Necklace of Missiles',
    category = MagicItemCategory.MISC,
    xp_value = [100,2950],
    gold_value = [400,11800],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A device of this sort appears to be nothing but a cheap medallion or piece of valueless jewelry due to special enchantments placed upon it. If a character places it about his or her neck, however, that individual can see the necklace as it really is - a golden missile globes depending from a golden chain. Each sphere is detachable only by the wearer. They can be easily hurled up to 7" distance. When they arrive at the end of their trajectory they burst as a magical <a href="/spells/fireball-magic-user-lvl-3"><i>fireball</i></a>. The number of missiles, and their respective hit dice of <i>fireball</i> damage, are determined on the table below:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Number of Missiles and Missile Power</th></tr>'
        '<tr><td>1-4</td><td>one 5 HD, two 3 HD</td></tr>'
        '<tr><td>5-8</td><td>one 6 HD, two 4 HD, two 2 HD</td></tr>'
        '<tr><td>9-12</td><td>one 7 HD, two 5 HD, four 3 HD</td></tr>'
        '<tr><td>13-16</td><td>one 8 HD, two 6 HD, two 4 HD, four 2 HD</td></tr>'
        '<tr><td>17-18</td><td>one 9 HD, two 7 HD, two 5 HD, two 3 HD</td></tr>'
        '<tr><td>19</td><td>one 10 HD, two 8 HD, two 6 HD, four 4 HD</td></tr>'
        '<tr><td>20</td><td>one 11 HD, two 9 HD, two 7 HD, two 5 HD, two 3 HD</td></tr>'
        '</table>\n\n'
        'The size will show that there is a difference in power between globes, but the number of dice and damage each causes cannot generally be known.\n\n'
        'If the necklace is being worn or carried by a character who fails his or her saving throw versus a magical fire attack, the item must undergo a saving throw check as well. If it fails to save, all remaining missiles detonate simultaneously.\n\n'
        'The <i>necklace of missiles</i> has an x.p. value of 50 and g.p. value of 200 per hit die of each missile when sold.'
    )
),
MagicItem( name = 'Necklace of Prayer Beads',
    category = MagicItemCategory.MISC,
    xp_value = [1500,3000],
    gold_value = [9000,18000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A magical necklace of this sort appears to be a normal piece of non-valuable jewelry until it is placed about a character\'s neck. Even then, the true nature of the item will only be revealed if the wearer is a cleric (excluding druids and characters otherwise able to use spells of a clerical nature such as paladins and rangers). The <i>necklace of prayer beads</i> consists of 25-30 semi-precious (60%) and fancy (40%) stones. The wearer will be 25% more likely to successfully petition his or her deity to grant desired spells. There will also be 3-6 special beads (precious stones, gems of 1,000 g.p. base value) of the following sort (roll for each bead):\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Results</th></tr>'
        '<tr><td>1-5</td><td>BEAD OF ATONEMENT - as the <a href="/spells/atonement-cleric-lvl-5">5th level spell</a> of the same name</td></tr>'
        '<tr><td>6-10</td><td>BEAD OF BLESSING - as the <a href="/spells/bless-cleric-lvl-1">1st level spell</a> of the same name</td></tr>'
        '<tr><td>11-15</td><td>BEAD OF CURING - <a href="/spells/cure-blindess-cleric-lvl-3"><i>cures blindness</i></a>, <a href="/spells/cure-disease-cleric-lvl-3"><i>disease</i></a>, or <a href="/spells/cure-serious-wounds-cleric-lvl-4"><i>serious wounds</i></a> (as the appropriate spell does)</td></tr>'
        '<tr><td>16-17</td><td>BEAD OF KARMA - allows the cleric to cast his or her spells as if he or she were 4 levels higher (with respect to range, duration, etc.)</td></tr>'
        '<tr><td>18</td><td>BEAD OF SUMMONS - calls the cleric\'s deity (90% probability) to come to him or her in material form (but it had better be for some <i>good</i> reason!)</td></tr>'
        '<tr><td>19-20</td><td>BEAD OF WIND WALKING - as the <a href="/spells/wind-walk-cleric-lvl-7">7th level spell</a> of the same name</td></tr>'
        '</table>\n\n'
        'Each special bead can be used but once per day. If the cleric summons his or her deity, the deity will take the <i>necklace</i> as the least punishment for vain purposes in so doing. The function of each bead is known only when the bead is grasped and a <a href="/spells/commune-cleric-lvl-5"><i>commune</i></a> spell used. All powers of the special beads will be lost if they are removed from the necklace.\n\n'
        'The <i>necklace</i> has an x.p. value of 500 and g.p. value of 3,000 per special bead when sold.'
    )
),
MagicItem( name = 'Necklace of Strangulation',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Also covered by enchantments to completely mask its true nature, a <i>necklace of strangulation</i> can be discovered only when placed around a character\'s neck. The <i>necklace</i> immediately constricts and cannot be removed short of an <a href="/spells/alter-reality-illusionist-lvl-7"><i>alter reality</i></a>, <a href="/spells/limited-wish-magic-user-lvl-7"><i>limited wish</i></a> or <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spell. The wearer will suffer 6 hit points of strangulation damage per round until the character is dead and the <i>necklace</i> remains clasped until the character is a dry skeleton.'
),
MagicItem( name = 'Net of Entrapment',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This magical rope net is so strong as to defy strength under 20 and is equal to AC -10 with respect to blows aimed at cutting it. (Normal sawing attempts to cut it with dagger or sword will <i>not</i> succeed; it must be hacked at to sever a strand of its mesh.) Each net is 10\' square and has ¼\' mesh. It can be thrown 20\' so as to cover and close upon opponents; each in its area must save versus magic to avoid being entrapped. It can be suspended from a ceiling (or generally overhead) and drop upon a command word. It can be laid upon the floor and likewise close upwards upon command. The <i>net</i> stretches so as to close over an area of up to a 5\' cube in the latter case. It can be loosened by its possessor on command.'
),
MagicItem( name = 'Net of Snaring',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [6000,6000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This net exactly resembles a <i>net of entrapment</i>, but it functions only underwater. There, it can be commanded to shoot forth up to 3" distance to trap a creature. It is otherwise the same as the former magical net.'
),
MagicItem( name = 'Nolzur\'s Marvelous Pigments',
    category = MagicItemCategory.MISC,
    xp_value = [500,2000],
    gold_value = [3000,12000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('These magical emulsions enable their possessor to create actual objects simply by depicting their form in 2 dimensions. The variegated <i>pigments</i> are applied by a stick tipped with bristles, hair, or fur. The emulsion flows from the application to form the desired object as the wielder concentrates on the desired image. One pot of <i>Nolzur\'s Marvelous Pigments</i> is sufficient to create a 1,000 cubic foot object by depicting it 2 dimensionally over a 100 square foot surface. Thus, a 10\' x 10\' x 10\' pit, or a 10\' x 10\' x 10\' room, or a large door with a passage behind it, etc. can be created by application of the <i>pigments</i>. Note that only normal, inanimate things can be so created - doors, pits, flowers, trees, cells, etc.; not monsters, people, golems, and the like. The pigments must be applied to a surface, i.e. a floor, wall, ceiling, door, etc. From 1-4 containers of <i>pigments</i> will be found, usually with a single instrument about 1\' long with which to apply them. It takes 1 turn to depict an object with <i>pigments</i>. Objects of value depicted by <i>pigments</i> - precious metals, gems, jewelry, ivory, etc. - will <i>appear</i> valuable but will be tin, lead, paste gems, brass, bone, etc. Normal armor or weapons can, of course, be created.\n\n'
        'When sold, the x.p. value is 500 and g.p. value is 3,000 per pot of <i>pigments</i>.'
    )
),
MagicItem( name = 'Pearl of Power',
    category = MagicItemCategory.MISC,
    xp_value = [200,2400],
    gold_value = [2000,24000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This seemingly normal pearl of average size and coloration is a potent aid to a magic-user. Once a day, a <i>pearl of power</i> enables the possessor to recall any 1 spell as desired, even if the spell has already been cast. Of course, the magic-user must have the spell to be remembered amongst those he or she most recently memorized. The power of the <i>pearl</i> is determined below:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Level of Spell Recalled by Pearl</th></tr>'
        '<tr><td>01-25</td><td>first</td></tr>'
        '<tr><td>26-45</td><td>second</td></tr>'
        '<tr><td>46-60</td><td>third</td></tr>'
        '<tr><td>61-75</td><td>fourth</td></tr>'
        '<tr><td>76-85</td><td>fifth</td></tr>'
        '<tr><td>86-92</td><td>sixth</td></tr>'
        '<tr><td>93-96</td><td>seventh</td></tr>'
        '<tr><td>97-98</td><td>eighth</td></tr>'
        '<tr><td>99</td><td>ninth</td></tr>'
        '<tr><td>00</td><td>recalls 2 spells of 1st to 6th level (use d6)</td></tr>'
        '</table>\n\n'
        '1 in 20 of these <i>pearls</i> is of <i>opposite</i> effect, causing a spell to be forgotten. These pearls can be gotten rid of only by means of <a href="/spells/exorcise-cleric-lvl-4"><i>exorcism</i></a> or a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>!\n\n'
        'When sold, the x.p. value is 200 per level of spell, and g.p. value is 2,000 per level of spell.'
    )
),
MagicItem( name = 'Pearl of Wisdom',
    category = MagicItemCategory.MISC,
    xp_value = [500,500],
    gold_value = [5000,5000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Although it appears to be a normal pearl, a <i>pearl of wisdom</i> will cause a cleric to increase 1 point in wisdom if he or she retains the pearl for a 1 month period. The increse happens at the expiration of 30 days, but thereafter the pearl must be retained by the cleric and kept on his or her person, or the 1 point gain will be lost. Note that 1 in 20 of these magical pearls are cursed to work in reverse, but once the 1 point of wisdom is lost, the pearl turns to powder, and the loss is permanent barring some magical restoration means such as a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> or a <i>Tome of Understanding</i>.'
),
MagicItem( name = 'Periapt of Foul Rotting',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This engraved gem is magicked so as to appear to be a gem of small value. If any character claims it as his or her own, he or she will contract a terrible rotting disease, a form of leprosy which can be removed only by application of a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell followed by a <a href="/spells/cure-disease-cleric-lvl-3"><i>cure disease</i></a> and then a <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> or <a href="/spells/limited-wish-magic-user-lvl-7"><i>limited wish</i></a> or <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> spell. The rotting can also be countered by the crushing of a <i>periapt of health</i> and sprinkling of the dust thereof upon the afflicted character. Otherwise, the afflicted loses 1 point each of dexterity and constitution and charisma per week beginning 1 week after claiming the item, and when any score reaches 0, the character is dead. Each point lost due to the disease will be permanent regardless of subsequent removal of the affliction.'
),
MagicItem( name = 'Periapt of Health',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'The gem appears exactly as a <i>periapt of foul rotting</i>, but the possessor will be immune from all diseases save that of the latter <i>periapt</i> so long as he or she has it on his or her person.'
),
MagicItem( name = 'Periapt of Proof Against Poison',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('The <i>periapt of proof against poison</i> is <i>indistinguishable</i> from any of the other <i>periapts</i>. The character who has one of these magical gems is allowed a 10% saving throw per plus of <i>periapt</i> against poisons which normally disallow any such opportunity, a normal score for poisons which usually are at penalty, and a plus on all other poison saves:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Plus of Periapt</th></tr>'
        '<tr><td>1-8</td><td>+1</td></tr>'
        '<tr><td>9-14</td><td>+2</td></tr>'
        '<tr><td>15-18</td><td>+3</td></tr>'
        '<tr><td>19-20</td><td>+4</td></tr>'
        '</table>'
    )
),
MagicItem( name = 'Periapt of Wound Closure',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This magical stone looks exactly the same as the others of this ilk. The person possessing it will never need fear open, bleeding wounds, for the <i>periapt</i> prevents them. In addition, the <i>periapt</i> doubles the normal rate of healing, or allows normal healing of wounds which would not so do normally.'
),
MagicItem( name = 'Phylactery of Faithfulness',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'There is no means to determine what function this device performs until it is worn. The wearer of a <i>phylactery of faithfulness</i> will be aware of any action or item which will adversely affect his or her alignment and standing with his or her deity prior to performing the action of becoming associated with such an item, if a prior moment is taken to contemplate the action. The <i>phylactery</i> must be worn normally by the cleric, of course.'
),
MagicItem( name = 'Phylactery of Long Years',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device slows the aging process by one-quarter for as long as the cleric wears it. The reduction applies even to magical aging. Thus, if a cleric dons the <i>phylactery</i> at age 20, he or she will age 9 months every 12; so that in 12 chronological years, he or she will have aged but 9 and will physically be 29 rather than 32. 1 in 20 of these devices are cursed to operate in reverse.'
),
MagicItem( name = 'Phylactery of Monstrous Attention',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [2000,2000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'While this arm wrapping appears to be some sort of beneficial device, it actually draws the attention of supernatural creatures of exactly the opposite alignment of the cleric wearing it. This results in the cleric being plagued by powerful and hostile creatures whenever he or she is in an area where such creatures are or can appear. If the cleric is of 10th or higher level, the attention of his or her deity\'s most powerful enemy will be drawn, so as to cause this being to interfere directly. For example, a lawful good cleric attracts various demons and eventually the notice of <a href="/creatures/orcus">Orcus</a> or <a href="/creatures/demogorgon">Demogorgon</a>. Once donned, a <i>phylactery of monstrous attention</i> cannot be removed without an <a href="/spells/exorcise-cleric-lvl-4"><i>exorcism</i></a> spell and then a quest must be performed to re-establish the cleric in his or her alignment.'
),
MagicItem( name = 'Pipes of the Sewers',
    category = MagicItemCategory.MISC,
    xp_value = [1750,1750],
    gold_value = [8500,8500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A set of these wooden pipes appear to be nothing extraordinary, but if the possessor learns the proper tune, he or she can attract from 10-60 (d6 x 10) <a href="/creatures/giant-rat">giant rats</a> (80%) or 30-180 (3d6 x 10) normal <a href="/creatures/rat">rats</a> (20%) if either or both are within 40". For each 5" distance the rats have to travel there will be a 1 round delay. The piper must continue playing until the rats appear, and when they do so, they are 95% likely to obey the piper so long as he or she continues to play. If for any reason the piper ceases playing, the rats summoned will leave immediately. If they are again called it is 70% probable that they will come and obey, 30% likely that they will turn upon the piper. If the rats are under control of a creature such as a <a href="/creatures/vampire">vampire</a>, the piper\'s chance of taking over control is 30% per round of piping. Once control is assumed, there is a 70% chance of maintaining it if the other creature is actively seeking to reassert its control.'
),
MagicItem( name = 'Portable Hole',
    category = MagicItemCategory.MISC,
    xp_value = [5000,5000],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>portable hole</i> is a circle of magical cloth spun from the webs of a <a href="/creatures/phase-spider">phase spider</a> interwoven with strands of ether and beams of Astral Plane luminaries. When opened fully, a portable hole is 6\' in diameter, but it can be folded as small as a pocket handkerchief. When spread upon any surface, it causes an extra-dimensional hole 10\' deep to come into being. This hole can be "picked up" from inside or out by simply taking hold of the edges of the magical cloth and folding it up. Either way, the entrance disappears, but anything inside the "hole" remains. The only oxygen in the "hole" is that allowed by creation of the space, so creatures requiring the gas cannot remain inside for more than a turn or so without opening the space again by means of the magical cloth. The cloth does not accumulate weight even if its hole is filled with gold, for example. Each <i>portable hole</i> opens on its own particular non-dimensional space. If a <i>bag of holding</i> is placed within a <i>portable hole</i>, a rift to the Astral Plane is torn in the space, and the <i>bag</i> and the cloth are sucked into the void and forever lost. If a <i>portable hole</i> is placed within a <i>bag of holding</i>, it opens a <i>gate</i> to another plane, and the <i>hole</i>, <i>bag</i> and any creatures within a 10\' radius are drawn to the plane, the <i>portable hole</i> and <i>bag of holding</i> being <i>destroyed</i> in the process.'
),
MagicItem( name = 'Quaal\'s Feather Token',
    category = MagicItemCategory.MISC,
    xp_value = [500,1000],
    gold_value = [2000,7000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>feather token</i> is a small magical device of various forms to suit a special need. These various tokens are listed below. Each is usable but once:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Tokens</th></tr>'
        '<tr><td>1-4</td><td>ANCHOR - a <i>token</i> useful to moor a craft so as to render it immobile for 1 full day (or at any time prior upon command from the token\'s possessor).</td></tr>'
        '<tr><td>5-7</td><td>BIRD - a <i>token</i> which can be used to drive off any sort of hostile avian creatures or as a vehicle of transportation equal to a <a href="/creatures/roc">roc</a> of the largest size in all respects (1 day duration).</td></tr>'
        '<tr><td>8-10</td><td>FAN - a <i>token</i> which forms a huge flapping fan which can cause a <i>strong breeze</i> (cf. <b>DUNGEON MASTERS GUIDE: THE ADVENTURE, WATERBORNE ADVENTURES</b>) in an area large enough to propel one ship. This wind is not cumulative with existing wind speeds - if there is already a strong breeze blowing, this cannot be added to it to create a gale. It can, however, be used <i>against</i> it to create an area of relative calm or lesser winds (though this will not affect wave size in a storm, of course). The <i>fan</i> can be used up to eight hours a day. It will not function on land.</td></tr>'
        '<tr><td>11-13</td><td>SWAN BOAT - a <i>token</i> which forms a huge swan-like boat capable of swimming at 24" speed, and carrying 8 horses and gear or 32 men or any combination equal thereto (duration 1 day).</td></tr>'
        '<tr><td>14-18</td><td>TREE - a <i>token</i> which causes a great oak to spring into being - 6\' diameter trunk, 60\' height, 40\' top diameter.</td></tr>'
        '<tr><td>19-20</td><td>WHIP - a <i>token</i> which causes a huge leather whip to appear and be wielded against any opponent desired (+1 weapon, 9th level fighter "to hit" probability, 2-7 hit points damage plus save versus magic or be bound fast for 2-7 rounds) for up to 6 turn. (Cf. <i>Dancing Sword</i>.)</td></tr>'
        '</table>\n\n'
        'Other similar <i>tokens</i> may be added as desired.'
    )
),
MagicItem( name = 'Robe of the Archmagi',
    category = MagicItemCategory.MISC,
    xp_value = [6000,6000],
    gold_value = [65000,65000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('This normal-appearing garment can be <i>white</i> (45% - good alignment), <i>gray</i> (30% - neutral, but neither good nor evil, alignment), or <i>black</i> (25% - evil alignment). Its wearer gains the following powers:\n\n'
        '1. It serves as armor equal to AC 5;\n'
        '2. The <i>robe</i> confers a 5% magic resistance;\n'
        '3. It adds +1 to saving throw scores; and\n'
        '4. The robe reduces magic resistance and/or saving throws by 20%/-4 when the wearer casts any of the following spells: <a href="/spells/charm-monster-magic-user-lvl-4"><i>charm monster</i></a>, <a href="/spells/charm-person-magic-user-lvl-1"><i>charm person</i></a>, <a href="/spells/friends-magic-user-lvl-1"><i>friends</i></a>, <a href="/spells/hold-monster-magic-user-lvl-5"><i>hold monster</i></a>, <a href="/spells/hold-person-magic-user-lvl-3"><i>hold person</i></a>, <a href="/spells/polymorph-other-magic-user-lvl-4"><i>polymorph other</i></a>, <a href="/spells/suggestion-magic-user-lvl-3"><i>suggestion</i></a>.\n\n'
        'Color of a <i>robe of the archmagi</i> is not determinable until donned by a magic-user. If a white <i>robe</i> is donned by an evil wizard, he or she will take 18-51 (11d4 + 7) hit points of damage and lose 18,000-51,000 experience points, and the reverse is true with respect to a black <i>robe</i> donned by a good aligned magic-user. An evil or good magic-user putting on a gray robe, or a neutral magic-user donning either a white or black <i>robe</i>, incurs 6-24 hit points damage, 6,000-24,000 experience points loss, and the wearer will be moved towards the alignment of the <i>robe</i> by its enchantments, i.e. he or she should be vocally urged to change alignment to that of the robe, and the magic-user will have to take steps to keep his or her old alignment pure.'
    )
),
MagicItem( name = 'Robe of Blending',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [35000,35000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This ordinary appearing robe <i>cannot</i> be detected by magical means. When it is put on, however, the wearer will detect a dweomer and know that the garment has very special properties. A <i>robe of blending</i> enables its wearer to appear to be part of a rock wall, a plant, a creature of another sort - whatever is appropriate. The coloration, form, and even odor are produced by the robe, although it will not make its wearer appear to be more than twice/one-half normal height, and it does not empower language/noise capabilities - either understanding or imitating. (In situations where several different forms are appropriate, the wearer is obliged to state which form he wishes the <i>robe</i> to camouflage him or her as.) Creatures with <i>exceptional</i> (15+) or better intelligence have a 1% per intelligence point chance of detecting something amiss when they are within 3" of a <i>robe of blending</i>, and those creatures with <i>low</i> intelligence (5+) or better and 10 or more levels of experience or hit dice have a 1% per level or hit dice chance of likewise noting something unusual about a <i>robe</i>-wearing character. (The latter is cumulative with the former chance for detection, so an 18 intelligence magic-user of 12th level has a 30% chance - 18% + 12% - of noting something amiss.) There must be an initial check per eligible creature, and successive checks should be made each turn thereafter, if the same creatures are within the 3" range. All creatures acquainted with and friendly to the wearer will see him or her normally.'
),
MagicItem( name = 'Robe of Eyes',
    category = MagicItemCategory.MISC,
    xp_value = [4500,4500],
    gold_value = [50000,50000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This garment is most valuable (though it appears as a normal robe until it is put on), for its wearer is able to "see" in all directions at the same moment due to the scores of magical "eyes" which adorn te <i>robe</i>. The wearer is empowered with <i>infravisual</i> capability to 12" range, <i>ultravisual abilties</i>, and the power to see <i>displaced</i> or <i>out of phase</i> objects and creatures in their actual positions. The <i>robe of eyes</> sees <i>all</i> forms of invisible things within a 24" normal vision range (or 12" if infravision is being used). Of course, solid objects obstruct even the <i>robe\'s</i> powers of observation. While <i>invisibility</i>, <i>dust of disappearance</i>, a <i>robe of blending</i>, or even <a href="/spells/improved-invisibility-illusionist-lvl-4"><i>improved invisibility</i></a> are not proof against observation, astral or ethereal things cannot be seen by means of this robe. <i>Illusions</i> and secret doors also cannot be seen, but creatures camouflaged or hidden in shadows are easily detected, so ambush or surprise of a character wearing a <i>robe of eyes</i> is impossible. Furthermore, the <i>robe</i> enables its wearer to <i>track</i> as if he or she were a 12th level ranger. A <a href="/spells/light-cleric-lvl-1"><i>light</i></a> spell thrown directly on a <i>robe of eyes</i> will blind it for 1-3 rounds, a <a href="/spells/continual-light-magic-user-lvl-2"><i>continual light</i></a> for 2-8 rounds.'
),
MagicItem( name = 'Robe of Powerlessness',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A robe of this nature appears to be a robe of another sort, and detection of any sort will discover nothing more than the fact that it has a magic aura. As soon as a character dons this garment, he or she drops to 3 intelligence, forgets all spells and magical knowledge, and becomes weak as well (3 strength). The <i>robe</i> can be removed easily, but in order to restore mind and body, the character must have a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell and then a <a href="/spells/heal-cleric-lvl-6"><i>heal</i></a> spell placed upon his or her person.'
),
MagicItem( name = 'Robe of Scintillating Colors',
    category = MagicItemCategory.MISC,
    xp_value = [2750,2750],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This garment appears quite normal, but a magic aura is detectable. Unless the wearer has an intelligence of 15 or higher and a wisdom of 13 or more, he or she will be unable to cause a <i>robe of scintillating colors</i> to function. If intelligence and wisdom are sufficient, the wearer can cause the garment to become a shifting pattern of incredible hues, color after color cascading from the upper part of the <i>robe</i> to the hem in sparkling rainbows of dazzling light. Although this effect sheds light in a 40\' diameter sphere, it also has the powers of hypnotizing opponents and causing them to be unable to attack the wearer. It requires a full round for the wearer to cause the colors to begin "flowing" on the <i>robe</i>, but each round that they scintillate and move, any opponent not making its saving throw versus magic (or magic resistance check, then save) will stand transfixed for 2-5 rounds, hypnotized, and even when this effect wears off, additional saves must again be made in order to successfully attack. Furthermore, every round of continuous scintillation of the <i>robe</i> makes the wearer 5% more difficult to hit with missile attacks or hand-held or body weaponry (hands, fists, claws, fangs, horns, etc.) until a maximum of 25% (-5) is attained - 5 continuous rounds of the dazzling play of hues. After the initial round of concealment, the wearer is able to cast spells or engage in all forms of activity which do not require movement of more than 1" from his or her starting position. In non-combat situations, the <i>robe</i> will simply hypnotize creatures failing their saving throws versus magic for a period of 2-5 <i>turns</i>.'
),
MagicItem( name = 'Robe of Useful Items',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [15000,15000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('Although this appears to be an unremarkable item of apparel, if the <i>robe of useful items</i> is worn, the magic-user will note that it has small cloth patches in various shapes sewn onto it. The wearer, and <i>only</i> the wearer of the robe, can see, recognize, and detach any 1 of these patches in 1 round. Detaching a patch causes it to become an actual item as indicated below. A <i>robe</i> will always have 2 each of the following patches:\n\n'
        'dagger\n'
        'lantern (filled and lit)\n'
        'mirror (large)\n'
        'pole (10\')\n'
        'rope (50\' coil)\n'
        'sack (large)\n\n'
        'Additionally, the <i>robe</i> will have 4-16 of the following items which must be diced for:\n\n'
        '<table>'
        '<tr><th>Die Roll</th><th>Result</th></tr>'
        '<tr><td>01-08</td><td>Bag of 100 gold pieces</td></tr>'
        '<tr><td>09-15</td><td>Coffer (½\' x ½\' x 1\'), silver (500 g.p. value)</td></tr>'
        '<tr><td>16-22</td><td>Door, iron (up to 10\' wide and 10\' high and barred on 1 side - must be placed upright, will attach and hinge itself)</td></tr>'
        '<tr><td>23-30</td><td>Gems, 10 of 100 gold piece value each</td></tr>'
        '<tr><td>31-44</td><td>Ladder, wooden (24\' long)</td></tr>'
        '<tr><td>45-51</td><td>Mule (with saddle bags)</td></tr>'
        '<tr><td>52-59</td><td>Pit (10 cubic feet), open</td></tr>'
        '<tr><td>60-68</td><td>Potion of <i>extra healing</i></td></tr>'
        '<tr><td>69-75</td><td>Rowboat (12\' long)</td></tr>'
        '<tr><td>76-83</td><td>Scroll of 1 spell</td></tr>'
        '<tr><td>84-90</td><td><a href="/creatures/war-dog">War dogs</a>, pair</td></tr>'
        '<tr><td>91-96</td><td>Window (2\' x 4\' - up to 2\' deep)</td></tr>'
        '<tr><td>97-00</td><td>Roll twice more</td></tr>'
        '</table>\n\n'
        'Multiple items of the same kind are permissible. Once removed, any item may never be replaced.'
    )
),
MagicItem( name = 'Rope of Climbing',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A 60\' long <i>rope of climbing</i> is no thicker than a slender wand, weighs no more than 3 pounds, but is strong enough to support 3,000 pounds. Upon command the <i>rope</i> will snake forward, upward, downward, or any other direction at 10\' per round and attach itself securely wherever desired. It will return or unfasten itself likewise. In any event, one end of the <i>rope</i> must be held by a character when it performs such actions. It can also be commanded to <i>knot</i> itself, and this will cause large knots to appear at 1\' intervals along the rope; knotting shortens the <i>rope</i> to 50\' length while so knotted. Any magical rope which is broken or severed will immediately lose its special properties.'
),
MagicItem( name = 'Rope of Constriction',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This <i>rope</i> exactly resembles a <i>rope of climbing</i> or <i>entanglement</i>, but as soon as it is commanded to perform some action, it lashes itself about the neck of the character holding it, and from 1-4 others within 10\' of the victim (each entitled to a saving throw versus magic) and strangles and crushes the life from each and every such victim. Each round it delivers 2-12 hit points of damage, and it will continue to constrict until a <a href="/spells/dispel-magic-cleric-lvl-3"><i>dispel magic</i></a> is cast upon it. Note that any creature entwined by the <i>rope</i> cannot cast spells or otherwise free himself or herself by any means. This rope is AC -2 and takes 22 hit points to cut through; all hit points must be inflicted by the same creature (not the one entangled). Any magical rope which is broken or severed will immediately lose its special properties.'
),
MagicItem( name = 'Rope of Entanglement',
    category = MagicItemCategory.MISC,
    xp_value = [1250,1250],
    gold_value = [12000,12000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>rope of entanglement</i> is exactly the same in appearance as any other magical rope. Upon command, the <i>rope</i> will last forward 20\', or upwards 10\' to entangle and tie fast up to 8 man-sized creatures. (Figure 1 <a href="/creatures/storm-giant">storm giant</a> or <a href="/creatures/fire-giant">fire giant</a> = 2 <a href="/creatures/frost-giant">frost</a> or <a href="/creatures/stone-giant">stone</a> or <a href="/creatures/hill-giant">hill giants</a> = 3 <a href="/creatures/ogre">ogres</a> = 4 <a href="/creatures/bugbear">bugbears</a> = 6 <a href="/creatures/gnoll">gnolls</a> = 8 men = 10 elves = 12 dwarves = 16 gnomes or <a href="/creatures/kobold">kobolds</a>.) It takes but a single segment to strike, and another to entwine; the command requires 1 segment also, while the whole takes 3 segments to perform. The rope cannot be broken by sheer strength, it must be hit by an edged weapon. The rope cannot be broken by sheer strength, it must be hit by an edged weapon. The <i>rope</i> is AC -2 and takes 22 hit points to cut through; all hit points must be inflicted by the same creature (not the one entangled). Damage under 22 hit points will repair itself in 6 turns. If a <i>rope of entanglement</i> is severed, it is destroyed. Any magical rope which is broken or severed will immediately lose its special properties.'
),
MagicItem( name = 'Rug of Smothering',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1500,1500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This finely woven carpet resembles a <i>carpet of flying</i> and will give off magical radiations if detected for. The character seating himself or herself upon it and giving a command will be surprised, however, as the <i>rug of smothering</i> will tightly roll itself around that individual and suffocate him or her in 3-6 rounds. The <i>rug</i> cannot be physically prevented from so wrapping itself, and the <i>rug</i> can be prevented from smothering its victim only by the casting of any one of the following spells: <a href="/spells/alter-reality-illusionist-lvl-7"><i>alter reality</i></a>, <a href="/spells/animate-object-cleric-lvl-6"><i>animate object</i></a>, <a href="/spells/hold-plant-druid-lvl-4"><i>hold plant</i></a>, <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a>.'
),
MagicItem( name = 'Rug of Welcome',
    category = MagicItemCategory.MISC,
    xp_value = [6500,6500],
    gold_value = [45000,45000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A rug of this type appears exactly the same as a <i>carpet of flying</i>, and it performs the functions of one (6\' x 9\' size), but a <i>rug of welcome</i> has other powers in addition. Upon command it will function as a <i>rug of smothering</i>, entrapping any creature up to <a href="/creatures/ogre">ogre</a>-size which steps upon it. A <i>rug of welcome</i> will also elongate itself and stiffen to become as hard and strong as steel, the maximum length being 27\' long at 2\' width, to serve as a bridge, barricade, etc. In this latter form it is AC 0 and will take 100 hit points to destroy. Best of all, the possessor need only utter a word of command, and the <i>rug</i> will shrink to 1/12 size for easy storage and transportation.'
),
MagicItem( name = 'Saw of Mighty Cutting',
    category = MagicItemCategory.MISC,
    xp_value = [1750,1750],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This notched adamantite blade is 12\' long and over 1\' wide. It requires 18/00 or greater strength to operate alone, or 2 persons of 17 or greater strength to work in tandem. The blade will slice through a 2\' thick hardwood tree in 1 turn, a 4\' thick trunk in 3 turns, or a 1\' diameter tree in but 3 rounds. After 6 turns of cutting with the <i>saw</i>, the character or characters must rest for 6 turns before doing any further work.'
),
MagicItem( name = 'Scarab of Death',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [2500,2500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This small brooch or pin of magical nature appears to be one of the various amulets, brooches, or scarabs of beneficial sort. However, if it is held for more than 1 round or placed within a container (bag, pack, etc.) within 1\' of a warm living body for 1 turn, it will change into a horrible burrowing beetle-like creature. The thing will then tear through any leather or cloth, burrow into flesh, and reach the victim\'s heart in a single round, causing death. It then returns to its <i>scarab</i> form. (Hard wood, ceramic, bone, ivory, or metal will prevent the monster from coming to life, if the <i>scarab</i> is secured within a container of such substance.)'
),
MagicItem( name = 'Scarab of Enraging Enemies',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [8000,8000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'When one of these devices is displayed and a command uttered, all intelligent hostile creatures within a 4" radius must save versus magic or become <i>enraged</i>. Those making the saving throw may perform normally; <i>enraged</i> enemies will fly into a berserk fury and attack the nearest creature (even their own comrades) - +1 "to hit", +2 on damage, -3 on their own armor class. The rage will last for 7-12 rounds, and during this period, the <i>enraged</i> creatures will continually attack without reason or fear, moving on to attack other creatures nearest them if initial opponents are slain. A <i>scarab</i> of this type contains 19-24 charges.'
),
MagicItem( name = 'Scarab of Insanity',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [11000,11000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This scarab is absolutely indistinguishable from any other amulet, brooch, or scarab. When displayed and a command word is spoken, all other creatures within a 2" radius must save versus magic at -2 (and -10% from any magic resistance as well). Those failing the save are completely <i>insane</i> for 9-12 rounds, unable to cast spells or use reasoning of any sort (treat as a <a href="/spells/confusion-druid-lvl-7"><i>confusion</i></a> spell with no chance for acting in a non-confused manner). The <i>scarab</i> has 9-16 charges.'
),
MagicItem( name = 'Scarab of Protection',
    category = MagicItemCategory.MISC,
    xp_value = [2500,2500],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device appears to be any one of the various magical amulets, stones, etc. It gives off a faint dweomer, of course, and if it is held for 1 round by any character an inscription will appear on its surface letting the holder know it is a protective device. The possessor gains +1 on all saving throws versus magic, and if no save is normally possible, he or she gains one of 20, adjusted by any other magical protections which normally give bonuses to saving throw dice rolls. Thus, this device allows a save versus magic at base 20 against <a href="/spells/magic-missile-magic-user-lvl-1"><i>magic missile</i></a> attacks, for example, and if the target also has +4 for magical armor and +1 for a <i>ring of protection</i>, any roll of 15 or better would indicate that the <i>missiles</i> did no damage. The <i>scarab</i> can additionally absorb up to 12 life energy level draining attacks (2 level drains count as 2 absorbings) or <i>death touches</i>/<i>death rays</i>/<a href="/spells/finger-of-death-druid-lvl-7"><i>fingers of death</i></a>. However, upon absorbing 12 such attacks the <i>scarab</i> turns to powder - totally destroyed. 1 in 20 of these <i>scarabs</i> are reversed cursed items, giving the possessor a -2 on his or her dice. However, 1 in 5 of these cursed items are actually +2 if the curse is removed by a cleric of 16 or higher level. In this latter case, the scarab will have absorption capability of 24 rather than 12.'
),
MagicItem( name = 'Spade of Colossal Excavation',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [6500,6500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This digging tool is 8\' long with a spade-like blade 2\' wide and 3\' long. Any fighter with 18 strength can use this magical shovel to dig great holes. 1 cubic yard of normal earth can be excavated in 1 round. Every 10 rounds, the user must rest for 5 rounds. Hard pan clay takes twice as long to dig, as does gravel. Loose soil takes only half as long.'
),
MagicItem( name = 'Sphere of Annihilation',
    category = MagicItemCategory.MISC,
    xp_value = [3750,3750],
    gold_value = [30000,30000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A <i>sphere of annihilation</i> is a globe of absolute blackness, a ball of nothingness 2\' in diameter. A <i>sphere</i> is actually a hole in the continuity of the multiverse, a void. Any matter which comes in contact with a <i>sphere</i> is instantly sucked into the void, gone, utterly destroyed, <a href="/spells/wish-magic-user-lvl-9"><i>wishes</i></a> and similar magicks notwithstanding! A <i>sphere of annihilation</i> is basically static, resting in some spot just as if it were a normal hole. It can be caused to move, however, by mental effort, the brain waves of the individual concentrating on changing its position bending spatial fabrics so as to cause the hole to slide in some direction. Control range is 40\' initially, 1"/level once control is established. Basic movement rate is 10\' per round, modified as shown below. Concentration control is based on intelligence and level of experience - the higher the level the greater the mental power and discipline. For every 1 point of intelligence above 12, the magic-user adds 1%; for every 1 point over 15, he or she adds another 3%, i.e. 1% for each point from 13 to 15, and additional 3% for each point from 16-18 - a maximum of 12% bonus at 18 intelligence. The bonus applies to this table:\n\n'
        '<table>'
        '<tr><th>Level of Magic-User</th><th>Movement/Round</th><th>Probability of Control per Round</th></tr>'
        '<tr><td>up to 5th</td><td>8\'</td><td>15%</td></tr>'
        '<tr><td>6th-7th</td><td>9\'</td><td>20%</td></tr>'
        '<tr><td>8th-9th</td><td>10\'</td><td>30%</td></tr>'
        '<tr><td>10th-11th</td><td>11\'</td><td>40%</td></tr>'
        '<tr><td>12th-13th</td><td>12\'</td><td>50%</td></tr>'
        '<tr><td>14th-15th</td><td>13\'</td><td>60%</td></tr>'
        '<tr><td>16th-17th</td><td>14\'</td><td>70%</td></tr>'
        '<tr><td>18th-20th</td><td>15\'</td><td>75%</td></tr>'
        '<tr><td>21st & above</td><td>16\'</td><td>80%</td></tr>'
        '</table>\n\n'
        'Any <i>attempt</i> to control the <i>sphere</i> will cause it to move, but if control is not established, the <i>sphere</i> will slide <i>towards</i> the magic-user attempting to do so, and it will continue so moving for 1-4 rounds or longer, if the magic-user is within 30\' thereafter.\n\n'
        'If 2 or more magic-users attempt to control a <i>sphere of annihilation</i>, the strongest (the one with the highest percentage chance to control the <i>sphere</i>) is checked first, then the next strongest, etc. Control chance is reduced 5% per person, cumulative, when 2 or more magic-users concentrate on the <i>sphere</i>, even if they are attempting the same thing (co-operating). If none are successful, the <i>sphere</i> will slip towards the strongest. Control <i>must</i> be checked each and every round.\n\n'
        'Should a <a href="/spells/gate-magic-user-lvl-9"><i>gate</i></a> spell be cast upon a <i>sphere</i>, there is a 50% chance that the spell will destroy it, 35% that the spell will do nothing, and 15% that a gap will be torn in the spatial fabric, and everything in an 18" radius will be catapulted into another plane or universe. If a <i>rod of cancellation</i> touches a <i>sphere</i>, the two will cause a tremendous explosion as they negate each other. Everything within a 6" radius will sustain 30-120 (3d4 x 10) hit points of damage. A psionic using <i>probability travel</i> discipline when the <i>sphere</i> touches him or her will be able to do away with the sphere, and gain another major psionic power, if he or she succeeds in saving versus magic; failure indicates annihilation. (See <i>Talisman of the Sphere</i>.)'
    )
),
MagicItem( name = 'Stone of Controlling Earth Elementals',
    category = MagicItemCategory.MISC,
    xp_value = [1500,1500],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A stone of this nature is typically an oddly-shaped bit of extrusive rock, shaped and roughly polished. The possessor of such a stone needs but utter a single command word, and an <a href="/creatures/earth-elemental">earth elemental</a> of 12 hit dice size will come to the summoner if earth is available, an 8 hit dice elemental if rough, unhewn stone is the summoning medium. (An earth elemental cannot be summoned from worked stone, but one can be from mud, clay, or even sand, although one from sand is an 8 dice monster also. The area of summoning for an earth elemental must be at least 4\' square and have 4 cubic yards volume.) The elemental will appear in 1-4 rounds. For details of elementals and their control see <b>ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL</b>. One elemental per day can be summoned by means of the <i>stone</i>.'
),
MagicItem( name = 'Stone of Good Luck (Luckstone)',
    category = MagicItemCategory.MISC,
    xp_value = [3000,3000],
    gold_value = [25000,25000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This magical stone is typically a bit of rough polished agate or similar mineral. Its possessor gains a +1 (+5% where applicable) on all dice rolls involving factors such as saving, slipping, dodging, etc. - whenever a die or dice are rolled to find whether the character has an adverse happening befall or not. This luck does <i>not</i> affect "to hit" and damage dice or spell failure dice. Additionally, the <i>luckstone</i> gives the possessor a +/- 1%-10% (at owner\'s option) on rolls for determination of magic items or division of treasure. The <i>most</i> favorable results will always be gained with a <i>stone of good luck</i>.'
),
MagicItem( name = 'Stone of Weight (Loadstone)',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This magical stone appears to be any one of the other sorts, and testing will not reveal its nature. However, as soon as the possessor of a <i>stone of weight</i> is in a situation where he or she is required to move quickly in order to avoid an enemy - combat or pursuit - the item causes a 50% reduction in movement, and even attacks are reduced to 50% normal rate. Furthermore, the stone <i>cannot</i> be gotten rid of by any means - throwing it away or smashing it notwithstanding - and it will always turn up somewhere on the character\'s person. If a <a href="/spells/dispel-evil-cleric-lvl-5">dispel evil</i></a> is cast upon a <i>loadstone</i>, the item will disappear and no longer haunt the individual.'
),
MagicItem( name = 'Talisman of Pure Good',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [27500,27500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'If a high priest or priestess possesses one of these mighty <i>talismans</i>, he or she has the power to cause an evil cleric to be swallowed up forever by a flaming crack which will open at the feet of the victim and precipitate him or her to the center of the earth. The wielder of the <i>talisman</i> <b>must</b> be good, and if he or she is not exceptionally pure in thought and deed, the evil cleric will gain a saving throw versus magic. A <i>talisman of pure good</i> has 7 charges. It cannot be recharged. If a neutral cleric touches one of these magic stones, he or she will take 7-28 hit points of damage; and if an evil cleric touches one he or she will take 12-48 hit points of damage. Non-clerics will not be affected by the device.'
),
MagicItem( name = 'Talisman of the Sphere',
    category = MagicItemCategory.MISC,
    xp_value = [100,100],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This is a small adamantite loop and handle which will be useless in any but a magic-user\'s possession, and any other class touching a talisman of this sort will take 5-30 hit points of damage. When held by a magic-user concentrating on control of a <i>sphere of annihilation</i>, a <i>talisman of the sphere</i> doubles the intelligence bonus percentage for control, i.e. 2% per point of intelligence from 13-15, 6% per point of intelligence from 16-18. If control is established by the wielder of a <i>talisman</i>, he or she need check for continual control only every other round thereafter. If control is not established, the <i>sphere</i> will move towards the magic-user at maximum speed (16\'/round). Note that a <i>wand of negation</i> will have no effect upon a <i>sphere of annihilation</i>, but if the wand is directed at the <i>talisman</i> it will negate its power of control so long as the wand is so directed.'
),
MagicItem( name = 'Talisman of Ultimate Evil',
    category = MagicItemCategory.MISC,
    xp_value = [3500,3500],
    gold_value = [32500,32500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This device exactly resembles a <i>talisman of pure good</i> and is exactly its opposite in all respects. It has 6 charges.'
),
MagicItem( name = 'Talisman of Zagy',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>talisman</i> of this sort appears exactly the same as a <i>stone controlling earth elementals</i>. Its power is quite different, and these are dependent upon the charisma of the individual holding the <i>talisman</i>. Whenever a character touches a <i>Talisman of Zagy</i>, a reaction check is made as if the individual were meeting another creature. If a <i>hostile</i> reaction result is obtained, the device will act as a <i>stone of weight</i>, although discarding it or destroying it results only in 5-30 hit points of damage and the disappearance of the <i>talisman</i>. If a neutral reaction results, the <i>talisman</i> will remain with the character for 5-30 hours, or until a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> is made upon it, whichever first occurs, and it will then disappear. If a <i>friendly</i> reaction result is obtained, the character will find it impossible to be rid of the <i>talisman</i> for as many months as he or she has points of charisma. The device will grant 1 <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> for every 6 points of the character\'s charisma; and it will also grow warm and throb whenever its possessor comes within 20\' of a mechanical or magical trap. (If the <i>talisman</i> is not held, its warning heat and pulses will be of no avail.) Regardless of which reaction result is obtained, when its time period expires the <i>talisman</i> will disappear, but a base 10,000 g.p. gem (diamond) will remain in its stead.'
),
MagicItem( name = 'Tome of Clear Thought',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [48000,48000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A work of this nature is indistinguishable from any normal book (cf. <i>Manual of Bodily Health</i>). Any single character who reads a <i>tome of clear thought</i> will be able to practice mental excercises which will increase his or her intelligence by 1 point. Reading a work of this nature takes 48 hours time over 6 days, and immediately thereafter the book disappears. The reader must begin a program of concentration and mental disciplines within 1 week of reading the <i>tome</i>. After 1 full month of such exercise, intelligence goes up. If psionics are employed in the campaign and the character is previously a non-psionic, another check may be allowed. The knowledge gained from reading the work can never be recorded or articulated. Any further perusal of a <i>tome of clear thought</i> will be of no benefit to the character.'
),
MagicItem( name = 'Tome of Leadership and Influence',
    category = MagicItemCategory.MISC,
    xp_value = [7500,7500],
    gold_value = [40000,40000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This leather and brass bound book is similar to a <i>tome of clear thought</i>; but upon completion of reading and practice of what was revealed therein, charisma is increased by 1 point.'
),
MagicItem( name = 'Tome of Understanding',
    category = MagicItemCategory.MISC,
    xp_value = [8000,8000],
    gold_value = [43500,43500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'Identical to a <i>tome of clear thought</i>, this work increases wisdom by 1 point.'
),
MagicItem( name = 'Trident of Fish Command',
    category = MagicItemCategory.MISC,
    xp_value = [500,500],
    gold_value = [4000,4000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This three-tined fork atop a stout rod of 6\' length appears to be a barbed military fork of some sort. However, its magical properties enable its wielder to cause all fish - including sharks and eels, but excluding mollusks, crustaceans, amphibians, reptiles, mammals and similar sorts of non-piscine marine creatures - within a 6" radius to save versus magic (this uses one charge of the trident). Those which fail this throw are completely under empathic command, they will not attack the possessor of the <i>trident</i> nor any creature within 10\' of him or her, and the wielder of the device can cause them to move in whatever direction is desired and convey messages of emotion, i.e. fear, hunger, anger, indifference, repletion, etc. Fish which make their saving throw are free of empathic control, but they will not approach closer than 10\' of the <i>trident</i>. Fish which school must be checked as a single entity. A <i>trident</i> of this type contains 17-20 charges. It is otherwise a +1 magic weapon.'
),
MagicItem( name = 'Trident of Submission',
    category = MagicItemCategory.MISC,
    xp_value = [1250,1250],
    gold_value = [12500,12500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A weapon of this nature appears unremarkable, exactly as any normal trident. The wielder of a <i>trident of submission</i> causes any opponent struck to save versus magic. If the opponent fails to save, it must check morale the next round <i>instead</i> of attacking; if morale is <i>good</i>, the opponent may act normally next round, but if it is <i>poor</i>, the opponent will cease fighting and surrender, overcome with a feeling of hopelessness. The duration of this hopelessness is 2-8 rounds. Thereafter the creature is normal once again. The <i>trident</i> has 17-20 charges. A <i>trident</i> of this type is a +1 magic weapon.'
),
MagicItem( name = 'Trident of Warning',
    category = MagicItemCategory.MISC,
    xp_value = [1000,1000],
    gold_value = [10000,10000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A weapon of this type enables its wielder to determine the location, depth, species, and number of hostile and/or hungry marine predators within 24". A <i>trident of warning</i> must be grasped and pointed in order for the person using it to gain such information, and it requires 1 round to so scan a 24" radius hemisphere. There are 19-24 charges in a <i>trident</i> of this type, each charge sufficient to last for 2 rounds of scanning. The weapon is otherwise a +2 magical arm.'
),
MagicItem( name = 'Trident of Yearning',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A <i>trident of yearning</i> looks exactly like any normal trident, and its dweomer is also indistinguishable from the magic aura of other enchanted weapons of this sort. Any character grasping this type of trident immediately conceives an overwhelming desire to immerse himself or herself in as great a depth of water as is possible. The unquenchable longing so generated causes the affected character to instantly proceed toward the largest/deepest body of water - in any event one that is sufficient to completely cover his or her person - and immerse himself or herself therein permanently. The character cannot loose his or her grip on the <i>trident</i>, and only a <a href="/spells/water-breathing-druid-lvl-3"><i>water breathing</i></a> spell (after submersion) placed upon him or her, or use of a <a href="/spells/wish-magic-user-lvl-9"><i>wish</i></a> or <a href="/spells/alter-reality-illusionist-lvl-7"><i>alter reality</i></a>, will enable the character to do so. The <i>trident</i> is otherwise a -2 cursed magical weapon. Note that this item does not confer the ability to breathe underwater.'
),
MagicItem( name = 'Vacuous Grimoire',
    category = MagicItemCategory.MISC,
    xp_value = [0,0],
    gold_value = [1000,1000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'A book of this sort is totally impossible to tell from a normal one, although if a <a href="/spells/detect-magic-cleric-lvl-1"><i>detect magic</i></a> spell is cast, there will be a magical aura noted. Any character who opens the work and reads so much as a single glyph therein must make 2 saving throws versus magic. The first is to determine if 1 point of <i>intelligence</i> is lost or not, the second is to find if 2 points of <i>wisdom</i> are lost. Once opened and read, the <i>vacuous grimoire</i> remains, and it must be burned to be rid of it after first casting a <a href="/spells/remove-curse-cleric-lvl-3"><i>remove curse</i></a> spell. If the tome is placed with other books, its appearance will instantly alter to conform to one of the other works it is amongst.'
),
MagicItem( name = 'Well of Many Worlds',
    category = MagicItemCategory.MISC,
    xp_value = [6000,6000],
    gold_value = [12000,12000],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = 'This strange inter-dimensional device is exactly the same in appearance as a <i>portable hole</i>. Anything placed within is immediately cast into another world - a parallel earth, another planet, or a different plane at your option or by random determination. If the <i>well</i> is moved, the random factor again comes into play. It can be picked up, folded, etc. just as a <i>portable hole</i>. Note that things from the world the <i>well</i> touches can come through the opening, just as easily as from the initiating place.'
),
MagicItem( name = 'Wings of Flying',
    category = MagicItemCategory.MISC,
    xp_value = [750,750],
    gold_value = [7500,7500],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ('A pair of these magical wings appears to be nothing more than a plain cloak of old, black cloth. If the wearer speaks a command word, the cloak will turn into a pair of gigantic bat wings (20\' span) and empower the wearer to fly as follows:\n\n'
        '2 turns at 32" speed\n'
        '4 turns at 18" speed\n'
        '8 turns at 12" speed\n\n'
        'Combinations are possible at the ratio above. After the maximum number of possible turns flying, the wearer must rest for 1 hour - sitting, lying down, or sleeping. Shorter periods of flight do not require full rest, but only relative quiet such as slow walking for 1 hour. Any flying of less than 1 turn duration does not require any rest. Note that regardless of the length of time spent flying the <i>wings</i> can be used but once per day. They will support up to 500 pounds weight.'
    )
)
]
"""
,
MagicItem( name = '',
    category = MagicItemCategory.MISC,
    xp_value = [,],
    gold_value = [,],
    source = SourceBook.DUNGEON_MASTERS_GUIDE,
    desc = ''
)
"""

all_items = potions + scrolls + rings + rods + staves + wands + misc_magic
