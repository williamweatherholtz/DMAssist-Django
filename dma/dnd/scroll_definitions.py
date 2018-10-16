from .sourcebook import SourceBook
from .time import TimePeriod, TimeUnit

class Scroll():
    def __init__(self, name, read_time, desc, source):
        self.name = name
        self.description = desc
        self.source = source

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
