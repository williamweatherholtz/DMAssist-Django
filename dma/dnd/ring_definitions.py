from .sourcebook import SourceBook

class Ring():
    def __init__(self, name, desc):
        self.name = name,
        self.desc = desc


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
