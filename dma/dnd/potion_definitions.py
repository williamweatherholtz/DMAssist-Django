from .sourcebook import SourceBook

class Potion():
    def __init__(self, name, desc, source):
        self.name = name
        self.description = desc
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
'''
Potion(name = '',
    desc = ''
),
'''
