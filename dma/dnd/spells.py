from random import sample,choice
from decimal import Decimal

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
            sourcebook=None, desc="Missing description"):
        self.name = name
        self.role = spell_class
        self.level = level

        #additional information (not yet defined for most spells
        self.cast_time = cast
        self.duration = duration
        self.duration_per_level = duration_lvl
        self.sourcebook = sourcebook
        self.description = desc

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
        sourcebook=V,
        desc="Upon uttering the Bless spell, the caster raises the morale of friendly creatures by +1. Furthermore, it raises their \"to hit\" dice rolls by +1. A blessing, however, will affect only those not already engaged in melee combat. This spell can be reversed by the cleric to a curse upon enemies which lowers morale and \"to hit\" by -1. The caster determines at what range (up to 6\") he or she will cast the spell, and it then affects all creatures in on area 5\" square centred on the point the spell was cast upon. In addition to the verbal and somatic gesture components, the Bless requires holy water, while the Curse requires the sprinkling of specially polluted water."
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
        sourcebook=V,
        desc="This spell enables the cleric to issue a command of a single word. The command must be uttered in a language which the spell recipient is able to understand. The individual will obey to the best of his/her/its ability only so long as the command is absolutely clear and unequivocal, i.e. \"Suicide!\" could be a noun, so the creature would ignore the command. A command to \"Die!\" would cause the recipient to fall in a faint or cataleptic state for 1 round, but thereafter the creature would be alive and well. Typical command words are: back, halt, flee, run, stop, fall, fly, go, leave, surrender, sleep. rest, etc. Undead are not affected by a command. Creatures with intelligence of 13 or more, and creatures with 6 or more hit dice (or experience levels) are entitled to a saving throw versus magic. (Creatures with 13 or higher intelligence and 6 hit dice/levels do not get 2 saving throws!)"
    ),
    Spell('Create Water','C',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the cleric casts a Create Water spell, four gallons of water are generated for every level of experience of the caster, i.e. a 2nd level cleric creates eight gallons of water, a 3rd level twelve gallons, a 4th level sixteen gallons, etc. The water is clean and drinkable (it is just like rain water). Reversing the spell, Destroy Water, obliterates without trace (such as vapour, mist, fog or steam) a like quantity of water. Created water will last until normally used or evaporated, spilled, etc. Water can be created or destroyed in an area as small as will actually contain the liquid or in an area as large as 27 cubic feet (one cubic yard). The spell requires at least a drop of water to create, or a pinch of dust to destroy, water. Note that water cannot be created within a living thing."
    ),
    Spell('Cure Light Wounds','C',1,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Upon laying his or her hand upon a creature, the cleric causes from 1 to 8 hit points of wound or other injury damage to the creature's body to be healed. This healing will not affect creatures without corporeal bodies, nor will it cure wounds of creatures not living or those which can be harmed only by iron, silver, and/or magical weapons. Its reverse, Cause Light Wounds, operates in the same manner; and if a person is avoiding this touch, a melee combat \"to hit\" die is rolled to determine if the cleric's hand strikes the opponent and causes such a wound. Note that cured wounds are permanent only insofar as the creature does not sustain further damage, and that caused wounds will heal - or can be cured - just as any normal injury will. Caused light wounds are 1 to 8 hit points of damage."
    ),
    Spell('Detect Evil','C',1,
        cast=tp(1,R),
        duration=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="This is a spell which discovers emanations of evil, or of good in the case of the reverse spell, from any creature or object. For example, evil alignment or an evilly cursed object will radiate evil, but a hidden trop or an unintelligent viper will not. The duration of a Detect Evil (or Detect Good) spell is 1 turn + ½ turn (5 rounds, or 5 minutes) per level of the cleric. Thus a cleric of 1st level of experience can cast a spell with a 1½ turn duration, at 2nd level a 2 turn duration, 2½ at 3rd, etc. The spell has a path of detection 1\" wide in the direction in which the cleric is facing. It requires the use of the cleric's holy (or unholy) symbol as its material component, with the cleric holding it before him or her."
    ),
    Spell('Detect Magic','C',1,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V,
        desc="When the Detect Magic spell is cast, the cleric detects magical radiations in a path 1\" wide, and up to 3\", long, in the direction he or she is facing. The caster can turn 60° per round. Note that stone walls of 1' or more thickness, solid metal of but 1/12' thickness, or 3' or more of solid wood will black the spell. The spell requires the use of the cleric's holy (or unholy) symbol."
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
        sourcebook=V,
        desc="This spell causes excitation of molecules so as to make them brightly luminous. The light thus caused is equal to torch light in brightness, but its sphere is limited to 4\" in diameter. It lasts for the duration indicated (7 turns at 1st experience level, 8 at 2nd, 9 at 3rd, etc.) or until the caster utters a word to extinguish the light. The Light spell is reversible, causing darkness in the same area and under the same conditions, except the blackness persists for only one half the duration that light would last. If this spell is cast upon a creature, the applicable magic resistance and saving throw dice rolls must be made. Success indicates that the spell affects the area immediately behind the creature, rather than the creature itself. In all other cases, the spell takes effect where the caster directs as long as he or she has a line of sight or unobstructed path for the spell; fight can spring from air, rock, metal, wood, or almost any similar substance."
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
        sourcebook=V,
        desc="When this spell is cast, it acts as if it were a magical armour upon the recipient. The protection encircles the recipient at a one foot distance, thus preventing bodily contact by creatures of an enchanted or conjured nature such as aerial servants, demons, devils, djinn, efreet, elementals, imps, invisible stalkers, night hags, quasits, salamanders, water weirds, wind walkers, and xorn. Summoned animals or monsters are similarly hedged from the protected creature. Furthermore, any and all attacks launched by evil creatures incur a penalty of -2 from dice rolls \"to hit\" the protected creature, and any saving throws caused by such attacks are made at +2 on the protected creature's dice. This spell can be reversed to become Protection From Good, although it still keeps out enchanted evil creatures as well. To complete this spell, the cleric must truce a 3' diameter circle upon the floor (or ground) with holy water for Protection From Evil, with blood for Protection From Good - or in the air using burning incense or smouldering dung with respect to evil/good."
    ),
    Spell('Purify Food & Drink','C',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When cast, the spell will make spoiled, rotten, poisonous or otherwise contaminated food and/or water pure and suitable for eating and/or drinking. Up to 1 cubic foot of food and/or drink can be thus made suitable for consumption. The reverse of the spell putrefies food and drink, even spoiling holy water. Unholy water is spoiled by pure water."
    ),
    Spell('Remove Fear','C',1,
        cast=tp(4,S),
        duration=tp(0),
        sourcebook=V,
        desc="By touch, the cleric instils courage in the spell recipient, raising the creature's saving throw against magical fear attacks by +4 on dice rolls for 1 turn. If the recipient has already been affected by fear, and failed the appropriate saving throw, the touch allows another saving throw to be made, with a bonus of +1 on the dice for every level of experience of the caster, i.e. a 2nd level cleric gives a +2 bonus, a 3rd level +3, etc. A \"to hit\" dice roll must be made to touch an unwilling recipient. The reverse of the spell, Cause Fear, causes the victim to flee in panic at maximum movement speed away from the caster for 1 round per level of the cleric causing such fear. Of course, Cause Fear can be countered by Remove Fear and vice versa."
    ),
    Spell('Resist Cold','C',1,
        cast=tp(1,R),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is placed on a creature by a cleric, the creature's body is inured to cold. The recipient can stand zero degrees Fahrenheit without discomfort, even totally nude. Greater cold, such as that produced by a sword of cold, ice storm, cold wand, or white dragon's breath, must be saved against. All saving throws against cold are made with a bonus of +3, and damage sustained is one-half (if the saving throw is not made) or one-quarter (if the saving throw is made) of damage normal from that attack form. The resistance lasts for 1 turn per level of experience of the caster. A pinch of sulphur is necessary to complete this spell."
    ),
    Spell('Sanctuary','C',1,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When the cleric casts a Sanctuary spell, any opponent must make a saving throw versus magic in order to strike or otherwise attack him or her. If the saving throw is not made, the creature will attack another and totally ignore the cleric protected by the spell. If the saving throw is made, the cleric is subject to normal attack process including dicing for weapons to hit, saving throws, damage. Note that this spell does not prevent the operation of area attacks (Fireball, Ice Storm, etc.). During the period of protection afforded by this spell, the cleric cannot take offensive action, but he or she may use non-attack spells or otherwise act in any way which does not violate the prohibition against offensive action, This allows the cleric to heal wounds, for example, or to bless, perform an augury, chant, cast a light in the area (not upon on opponent!), and so on, The components of the spell include the cleric's holy/unholy symbol and a small silver mirror."
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
        sourcebook=V,
        desc="The cleric casting an Augury spell seeks to divine whether an action in the immediate future (within 3 turns) will be for the benefit of, or harmful to, the party. The base chance for correctly divining the augury is 70%, plus 1% far each level of the cleric casting the spell, i.e. 71% at 1st level, 72% at 2nd, etc, Your referee will determine any adjustments due far the particular conditions of each augury. For example, assume that a party is considering the destruction of a weird seal which closes a portal. Augury is used to find if weal or woe will be the ultimate result to the party. The material component for Augury is a set of gem-inlaid sticks, dragon bones, or similar tokens, or the wet leaves of on infusion which remain in the container after the infused brew is consumed. If the last method is used, a crushed pearl of at least 100 g.p. value must be added to the concoction before it is consumed."
    ),
    Spell('Chant','C',2,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V,
        desc="By means of the chant, the cleric brings into being a special favour upon himself or herself and his or her party, and causes harm to his or her enemies. Once the Chant spell is completed, all attacks, damage and saving throws made by those in the area of effect who are friendly to the cleric are at +1, while those of the cleric's enemies are at -1. This bonus/penalty continues as long as the cleric continues to chant the mystic syllables and is stationary. An interruption, however, such as an attack which succeeds and causes damage, grappling the chanter, or a magical silence, will break the spell."
    ),
    Spell('Detect Charm','C',2,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V,
        desc="When used by a cleric, this spell will detect whether or not a person or monster is under the influence of a Charm spell. Up to 10 creatures can be thus checked before the spell wanes. The reverse of the spell protects from such detection, but only a single creature can be so shielded."
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
        sourcebook=V,
        desc="When a cleric casts a find traps spell, all traps - concealed normally or magically - of magical or mechanical nature become visible to him or her. Note that this spell is directional. and the caster must face the desired direction in order to determine if a trap is laid in that particular direction."
    ),
    Spell('Hold Person','C',2,
        cast=tp(5,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell holds immobile, and freezes in places, from 1-3 humans or humanoid creatures (see below) for 5 or more melee rounds. The level of the cleric casting the Hold Person spell dictates the length of time the effect will last. The basic duration is 5 melee rounds at 1st level, 6 rounds at 2nd level, 7 rounds at 3rd level, etc. If the spell is cast at three persons, each gets a saving throw at the normal score; if only two persons are being enspelled, each makes their saving throw at -1 on their die; if the spell is cast at but one person, the saving throw die is at -2. Persons making their saving throws are totally unaffected by the spell. Creatures affected by a Hold Person spell are: brownies, dryads, dwarves, elves, gnolls, gnomes, goblins, half-elves, halflings, half-orcs, hobgoblins, humans, kobolds, lizard men, nixies, orcs, pixies, sprites, and troglodytes. The spell caster needs a small, straight piece of iron as the material component of this spell."
    ),
    Spell('Holy Symbol','C',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Know Allignment','C',2,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V,
        desc="A Know Alignment spell enables the cleric to exactly read the aura of a person - human, semi-human, or non-human. This will reveal the exact alignment of the person. Up to 10 persons can be examined with this spell. The reverse totally obscures alignment, even from this spell, of a single person for 1 turn, two persons for 5 rounds, etc. Certain magical devices will negate the ability to Know Alignment."
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
        sourcebook=V,
        desc="When this spell is placed upon a creature by a cleric, the creature's body is toughened to withstand heat, and boiling temperature is comfortable. The recipient of the resist tire spell can even stand in the midst of very hot or magical fires such as those produced by red-hot charcoal, a large amount of burning oil, flaming swords, fire storms, fire balls, meteor swarms. or red dragon's breath - but these will affect the creature, to some extent. The recipient of the spell gains a bonus of +3 an saving throws against such attack forms, and all damage sustained is reduced by 50%; therefore, if the saving throw is not made, the creature sustains one-half damage, and if the saving throw is mode only one-quarter damage is sustained, Resistance to fire lasts for 1 turn for each level of experience of the cleric placing the spell. The caster needs a drop of mercury as the material component of this spell."
    ),
    Spell('Silence 15\' Radius','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Upon casting this spell, complete silence prevails in the area of its effect. All sound is stopped, so all conversation is impossible, spells cannot be cast and no noise whatsoever issues forth, The spell can be cast into the air or upon an object. The spell of Silence lasts for 2 rounds for each level of experience of the cleric, i.e. 2 rounds at 1st level, 4 at 2nd, 6 at 3rd, 8 at 4th and so forth. The spell can be cast upon a creature, and the effect will then radiate from the creature and move as it moves. If the creature is unwilling, it saves against the spell, and if the saving throw is made, the spell effect locates about one foot behind the target creature."
    ),
    Spell('Slow Poison','C',2,
        cast=tp(1,S),
        duration=tp(0),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="When this spell is placed upon a poisoned individual it greatly slows the effects of any venom, even causing a supposedly dead individual to have life restored if it is cast upon the victim within a number of turns less than or equal to the level of experience of the cleric after the poisoning was suffered. i.e. a victim poisoned up to 10 turns previously could be temporarily saved by a 10th or higher level cleric who cast Slow Poison upon the victim. While this spell does not neutralize the venom, it does prevent it from substantially harming the individual for the duration of its magic, but each turn the poisoned creature will lose 1 hit point from the effect of the venom (although the victim will never go below 1 hit point while the Slow Poison spell's duration lasts). Thus, in the example above, the victim poisoned 10 turns previously has only 10 hit points, so when the 10th level cleric casts the spell, the victim remains with 1 hit point until the spell duration expires, and hopefully during that period a full cure can be accomplished. The material components of this spell are the cleric's holy/unholy symbol and a bud of garlic which must be crushed and smeared on the victim's bare feet."
    ),
    Spell('Snake Charm','C',2,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When this spell is cast, a hypnotic pattern is set up which causes one or more snakes to cease all activity except a semi-erect postured swaying movement. If the snakes are charmed while in a torpor, the duration of the spell is 3 to 6 turns (d4 + 2); if the snakes are not torpid, but are not aroused and angry, the charm lasts 1 to 3 turns; if the snakes are angry and/or attacking, the snake charm spell will last from 5 to 8 melee rounds (d4+4). The cleric casting the spell can charm snakes whose hit points are less than or equal to those of the cleric. On the average, a 1st level cleric could charm snakes with a total of 4 or 5 hit points; a 2nd level cleric 9 hit points, a 3rd level 13 or 14 hit points, etc. The hit points can represent a single snake or several of the reptiles, but the total hit points cannot exceed those of the cleric casting the spell."
    ),
    Spell('Speak With Animals','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By employing this spell, the cleric is empowered to comprehend and communicate with any warm or cold-blooded animal which is not mindless (such as an amoeba). The cleric is able to ask questions, receive answers, and generally be on amicable terms with the animal. This ability lasts for 2 melee rounds for each level of experience of the cleric employing the spell. Even if the bent of the animal is opposite to that of the cleric (evil/good, good/evil), it and any others of the same kind with it will not attack while the spell lasts. If the animal is neutral or of the some general bent as the cleric (evil/evil, good/good), there is a possibility that the animal, and its like associates, will do some favour or service for the cleric. This possibility will be determined by the referee by consulting a special reaction chart, using the charisma of the cleric and his actions as the major determinants. Note that this spell differs from speak with monsters (q.v.), for it allows conversation only with basically normal, non-fantastic creatures such as apes, bears, cats, dogs, elephants, and so on."
    ),
    Spell('Spiritual Hammer','C',2,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By calling upon his or her deity, the cleric casting a Spiritual Hammer spell brings into existence a field of force which is shaped vaguely like a hammer. This area of force is hammer-sized, and as long as the cleric who invoked it concentrates upon the hammer, it will strike at any opponent within its range as desired by the cleric. The force area strikes as a magical weapon equal to one plus per 3 levels of experience of the spell caster for purposes of being able to strike creatures, although it has no magical plusses whatsoever \"to hit\", and the damage it causes when it scores a hit is exactly the same as a normal war hammer, i.e. 1-6 versus opponents of man-sire or smaller, 1-4 upon larger opponents. Furthermore, the hammer strikes at exactly the same level as the cleric controlling it, just as if the cleric was personally wielding the weapon. As soon as the cleric ceases concentration, the Spiritual Hammer is dispelled. Note: If the cleric is behind an opponent, the force can strike from this position, thus gaining all bonuses for such an attack and negating defensive protections such as shield and dexterity. The material component of this spell is a normal war hammer which the cleric must hurl towards opponents whilst uttering a plea to his or her deity. The hammer disappears when the spell is cast."
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
        sourcebook=V,
        desc="This spell creates the lowest of the undead monsters, skeletons or zombies, from the bones or bodies of dead humans. The effect is to cause these remains to become animated and obey the commands of the cleric casting the spell. The skeletons or zombies will follow, remain in an area and attack any creature (or just a specific type of creature) entering the place, etc. The spell will animate the monsters until they are destroyed or until the magic is dispelled. (See Dispel Magic spell). The cleric is able to animate 1 skeleton or 1 zombie for each level of experience he or she has attained. Thus, a 2nd level cleric can animate 2 of these monsters, a 3rd level 3, etc. The act of animating dead is not basically a good one, and it must be used with careful consideration and good reason by clerics of good alignment. It requires a drop of blood, a piece of human flesh, and a pinch of bone powder or a bone shard to complete the spell."
    ),
    Spell('Cloudburst','C',3,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U
    ),
    Spell('Continual Light','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is similar to a Light spell, except that it lasts until negated (by a Continual Darkness or Dispel Magic spell) and its brightness is very great, being nearly as illuminating as full daylight. It can be cast into air, onto an object, or at a creature, In the third case, the Continual Light affects the space about one foot behind the creature if the latter makes its saving throw. Note that this spell will blind a creature if it is successfully cast upon the visual organs, for example. Its reverse causes complete absence of light."
    ),
    Spell('Create Food & Water','C',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast, the cleric causes food and/or water to appear. The food thus created is highly nourishing, and each cubic foot of the material will sustain three human-sized creatures or one horse-sized creature for a full day. For each level of experience the cleric has attained, 1 cubic foot of food and/or water is created by the spell, i.e. 2 cubic feet of food are created by a 2nd level cleric, 3 by a 3rd, 4 by a 4th, and so on; or the 2nd level cleric could create 1 cubic foot of food and 1 cubic foot of water, etc."
    ),
    Spell('Cure Blindness','C',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="By touching the creature afflicted, the cleric employing the spell can permanently cure most forms of blindness. Its reverse, Cause Blindness, requires a successful touch upon the victim, and if the victim then makes the saving throw, the effect is negated."
    ),
    Spell('Cure Disease','C',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="The cleric cures most diseases - including those of a parasitic, bacterial, or viral nature - by placing his or her hand upon the diseased creature. The affliction rapidly disappears thereafter, making the cured creature whole and well in from 1 turn to 1 week, depending on the kind of disease and the state of its advancement when the cure took place. The reverse of the Cure Disease spell is Cause Disease. To be effective. the cleric must touch the intended victim, and the victim must fail the saving throw. The disease caused will begin to affect the victim in 16 turns, causing the afflicted creature to lose 1 hit point per turn, and 1 point of strength per hour, until the creature is at 10% of original hit points and strength, at which time the afflicted is weak and virtually helpless."
    ),
    Spell('Death\'s Door','C',3,
        cast=tp(5,S),
        duration_lvl=tp(1,H),
        sourcebook=U
    ),
    Spell('Dispel Magic','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a cleric casts this spell, it neutralizes or negates the magic it comes in contact with as follows: A Dispel Magic will not affect a specially enchanted item such as a scroll, magic ring, wand, rod, staff, miscellaneous magic item, magic weapon, magic shield, or magic armour. It will destroy magic potions (they are treated as 12th level for purposes of this spell), remove spells cast upon persons or objects, or counter the casting of spells in the area of effect. The base chance for success of a Dispel Magic spell is 50%. For every level of experience of the character casting the Dispel Magic above that of the creature whose magic is to be dispelled (or above the efficiency level of the object from which the magic is issuing), the base chance increases by 5%, so that if there are 10 levels of difference, there is a 100% chance. For every level below the experience/efficiency level of the creature/object, the base chance is reduced by 2%. Note that this spell can be very effective when used upon charmed and similarly beguiled creatures. It is automatic in negating the spell caster's own magic."
    ),
    Spell('Feign Death','C',3,
        cast=tp(2,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level magic-user spell, Feign Death (q.v.). Note that a character of any level may be affected by the cleric casting this spell, and that the material components are a pinch of graveyard dirt and the cleric's holy/unholy symbol."
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
        sourcebook=V,
        desc="A Glyph of Warding is a powerful inscription magically drawn to prevent unauthorized or hostile creatures from passing, entering, or opening. It can be used to guard a small bridge, ward an entry, or as a trap on a chest or box. When the spell is cast, the cleric weaves a tracery of faintly glowing lines around the warding sigil. For every square foot of area to be protected, 1 segment of time is required to trace the warding lines from the glyph, plus the initial segment during which the sigil itself is traced. A maximum of a 5' X 5' area per level can be warded. When the spell is completed, the glyph and tracery become invisible, but any creature touching the protected area without first speaking the name of the glyph the cleric has used to serve as a ward will be subject to the magic it stores. Saving throws apply, and will either reduce effects by one-half or negate them according to the glyph employed. The cleric must use incense to trace this spell, and then sprinkle the area with powdered diamond (at least 2,000 g.p. worth) if it exceeds 50 square feet. Typical glyphs shock for 2 points of electrical damage per level of the spell caster, explode for a like amount of fire damage, paralyze, blind, or even drain a life energy level (if the cleric is of high enough level to cast this glyph)."
    ),
    Spell('Locate Object','C',3,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell aids in location of a known or familiar object. The cleric casts the spell, slowly turns, and knows when he or she is facing in the direction of the object to be located, provided the object is within range, i.e. 7\" for 1st level clerics, 8\" for 2nd, 9\" for 3rd, etc, The casting requires the use of a piece of lodestone, The spell will locate such objects as apparel, jewellery, furniture, tools, weapons, or even a ladder or stairway. By reversal (obscure object), the cleric is able to hide an object from location by spell, crystal ball, or similar means. Neither application of the spell will affect a living creature."
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
        sourcebook=V,
        desc="This spell exactly duplicates the effects of a Chant with regard to bonuses of +1 for friendly attacks and saving throws and -1 on like enemy dice. However, once the Prayer is uttered, the cleric can do other things, unlike a Chant which he or she must continue to make the spell effective. The cleric needs a silver holy symbol, prayer beads, or a similar device as the material component of this spell."
    ),
    Spell('Remove Curse','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Upon casting this spell, the cleric is usually able to remove a curse - whether it be on an object, a person, or in the form of some undesired sending or evil presence. Note that the Remove Curse spell will not affect a cursed shield, weapon or suit of armour, for example, although the spell will typically enable the person afflicted with any such cursed item to be rid of it. The reverse of the spell is not permanent; the Bestow Curse lasts for 1 turn for every level of experience of the cleric using the spell. It will lower one ability of the victim to 3 (your DM will determine which by random selection) 50% of the time; reduce the victim's \"to hit\" and saving throw probabilities by -4 25% of the time; or make the victim 50% likely per turn to drop whatever he, she, or it is holding (or simply do nothing in the case of creatures not using tools) 25% of the time. It is possible for a cleric to devise his or her own curse, and it should be similar in power to those shown. Consult your referee. The target of a Bestow Curse spell must be touched. If the victim is touched, a saving throw is still applicable; and if it is successful, the effect is negated."
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
        sourcebook=V,
        desc="This spell is a more potent version of the Cure Light Wounds spell (q.v.). Upon laying his or her hand upon a creature, the cleric causes from 3 to 17 (2d8+1) hit points of wound or other injury damage to the creature's body to be healed. This healing will affect only those creatures listed in the Cure Light Wounds spell explanation. Cause Serious Wounds, the reverse of the spell, operates similarly to the Cause Light Wounds spell, the victim having to be touched first, and if the touch is successful, it will inflict 3 to 17 hit points."
    ),
    Spell('Detect Lie','C',4,
        cast=tp(7,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When the cleric employs this spell, the recipient is immediately able to determine if truth is being spoken. The spell lasts one round for each level of experience of the cleric casting the Detect Lie. Gold dust is necessary for this spell. Its reverse, Undetectable Lie, makes bald-face untruths seem reasonable, or simply counters the Detect Lie spell powers. The reverse spell requires brass dust as its material component."
    ),
    Spell('Divination','C',4,
        cast=tp(1,T),
        duration=tp(0,R),
        sourcebook=V,
        desc="Similar to an Augury spell, a Divination spell is used to determine information regarding an area. The area can be a small woods, large building, or section of a dungeon level. In any case, its location must be known. The spell gives information regarding the relative strength of creatures in the area: whether a rich, moderate or poor treasure is there; and the relative chances for incurring the wrath of evil or good supernatural, super powerful beings if the area is invaded and attacked. The base chance for correct divination is 60%, plus 1% for each level of experience of the cleric casting the spell, i.e. 65% at 5th level, 66% at 6th, etc. The Dungeon Master will make adjustments to this base chance considering the facts regarding actual area being divined. If the result is not correct, inaccurate information will be obtained. The material components of the Divination are a sacrificial creature, incense, and the holy symbol of the cleric. If an unusually potent Divination is attempted, sacrifice of particularly valuable gems or jewellery and/or magic items may be required."
    ),
    Spell('Exorcise','C',4,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="The spell of Exorcism will negate possession of a creature or an object by any outside or supernatural force. This includes control of a creature by some force in an object, possession by Magic Jar (q.v.) spell, demonic possession, curse and even charm, for the Exorcise spell is similar to a Dispel Magic spell. Furthermore, it will affect a magical item if such is the object of the exorcism. Thus a soul object of any sort which comes under successful Exorcism will make the life force of the creature concerned wholly inhabit its nearest material body, wholly and completely. (Cf. ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL, Demon.) The Exorcise spell, once begun. cannot be interrupted, or else it is spoiled and useless. The base chance for success is a random 1% to 100%. Each turn of Exorcism the dice are rolled, and if the base chance number, or less, is rolled, the spell is successful. Base chance of success is modified by -1% for each level of difference between the cleric's level of experience and the level of the possessor or possessing magic, where the smaller number is the cleric's level. In the obverse, a +1% cumulative is added. The referee can determine base chance according to the existing circumstances if he or she so desires. Material components for this spell are the holy object of the cleric and holy water (or unholy, in the case of evil clerics, with respect to object and water). A religious artifact or relic can increase the chance of success by from 1% to 50%, according to the power of the artifact or relic."
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
        sourcebook=V,
        desc="The cleric casting a lower water spell causes water or similar fluid in the area of effect to sink away. Lowering is 5% of original effect for every level of experience of the cleric, i.e. 40% at 8th level, 45% at 9th, 50% at 10th, etc. The effect of the spell lasts for 1 turn for each level of experience of the cleric casting it. Likewise, the area of effect increases by level of experience, an 8th level cleric affecting an area of 8\" x 8\", a 9th level an area of 9\" x 9\", and so forth. Material components of this spell are the cleric's religious symbol and a pinch of dust. The reverse of the spell causes the water or similar fluid to return to its normal highest level, plus one foot for every level of experience of the cleric casting it."
    ),
    Spell('Neutralize Poison','C',4,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of a Neutralize Poison spell, the cleric detoxifies any sort of venom in the creature or substance touched. Note that an opponent, such as a poisonous reptile or snake (or even an envenomed weapon of an opponent) unwilling to be so touched requires the cleric to score a hit in melee combat. Effects of the spell are permanent only with respect to poison existing in the touched creature at the time of the touch, i.e. creatures (or objects) which generate new poison will not be permanently detoxified. The reversed spell, Poison, likewise requires an attack (a \"to hit\" touch which succeeds), and the victim is allowed a saving throw versus poison. If the latter is unsuccessful, the victim is killed by the poison."
    ),
    Spell('Protection From Evil 10\' Radius','C',4,
        cast=tp(7,S),
        duration=tp(0,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The globe of protection of this spell is identical in all respects to a Protection From Evil (q.v.) spell except that it encompasses a much larger area and the duration of the Protection From Evil, 10' Radius spell is greater. To complete this spell, the cleric must trace a circle 20' in diameter using holy water or blood, incense or smouldering dung as according to the Protection From Evil spell."
    ),
    Spell('Speak With Plants','C',4,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When cast, a Speak With Plants spell enables the cleric to converse, in very rudimentary terms, with all sorts of living vegetables. Thus, the cleric can question plants as to whether or not creatures have passed through them, cause thickets to part to enable easy passage, require vines to entangle pursuers, and similar things. The spell does not enable the cleric to animate non-ambulatory vegetation. The power of the spell lasts for 1 melee round for each level of experience of the cleric who cast it. All vegetation within the area of effect are under command of the spell. The material components for this spell are a drop of water, a pinch of dung, and a flame."
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
        sourcebook=V,
        desc="By means of this spell the cleric is able to change 1 stick to a snake for each level of experience he or she has attained, i.e. a 9th level cleric can change 9 sticks into 9 snakes. These snakes will attack as commanded by the cleric. There must, of course, be sticks or similar pieces of wood (such as torches, spears, etc.) to turn into snakes. Note that magical items such as staves and spears which are enchanted are not affected by the spell. Only sticks within the area of effect will be changed. The probability of a snake thus changed being venomous is 5% per level of experience of the spell caster, so that there is a 55% probability of any given snake created by the spell being poisonous when sticks are turned to snakes by an 11th level cleric, 60% at 12th level, etc. The effect lasts for 2 melee rounds for each level of experience of the spell caster. The material components of the spell are a small piece of bark and several snake scales. The reverse changes snakes to sticks for the duration appropriate, or it negates the Sticks To Snakes spell according to the level of the cleric countering the spell, i.e. a 10th level cleric casting the reverse spell can turn only 10 snakes back to sticks."
    ),
    Spell('Tongues','C',4,
        cast=tp(7,S),
        duration=tp(1,T),
        sourcebook=V,
        desc="This spell enables the cleric to speak the language of any creature inside the spell area, whether it is a racial tongue or an alignment language. The reverse of the spell cancels the effect of the Tongues spell or confuses verbal communication of any sort within the area of effect."
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
        sourcebook=V,
        desc="This spell is used by the cleric to remove the onus of unwilling or unknown deeds from the person who is the subject of the Atonement The spell will remove the effects of magical alignment change as well. The person for whom Atonement is being made must be either truly repentant or not in command of his or her own will so as to be able to be repentant. Your referee will judge this spell in this regard, noting any past instances of its use upon the person. Deliberate misdeeds and acts of knowing and wilful nature cannot be atoned for with this spell. The material components of this spell are the cleric's religious symbol, prayer beads or wheel or book, and burning incense."
    ),
    Spell('Commune','C',5,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V,
        desc="By use of a Commune spell the cleric is able to contact his or her divinity - or agents thereof - and request information in the form of questions which can be answered by a simple \"yes\" or \"no\". The cleric is allowed one such question for every level of experience he or she has attained. The answers given will be correct. It is probable that the referee will limit the use of Commune spells to one per adventure, one per week, or even one per month, for the \"gods\" dislike frequent interruptions. The material components necessary to a Commune spell are the cleric's religious symbol, holy/unholy water, and incense."
    ),
    Spell('Cure Critical Wounds','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The Cure Critical Wounds spell is a very potent version of the Cure Light Wounds spell (q.v.). The cleric lays his or her hand upon a creature and heals from 6 to 27 (3d8+3) hit points of damage from wounds or other damage. The spell does not affect creatures excluded in the Cure Light Wounds spell explanation. Its reverse, Cause Critical Wounds, operates in the same fashion as other Cause Wounds spells, requiring a successful touch to inflict the 6-27 hit points of damage. Caused wounds heal as do wounds of other sorts."
    ),
    Spell('Dispel Evil','C',5,
        cast=tp(8,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="The cleric using this spell causes summoned creatures of evil nature, or monsters enchanted and caused to perform evil deeds, to return to their own plane or place. Examples of such creatures are: aerial servants, demons, devils, djinn, efreet, elementals, and invisible stalkers. Note that this spell lasts for 1 melee round for each level of experience of the caster, and while the spell is in effect all creatures which could be affected by it attack at a -7 penalty' on their \"to hit\" dice when engaging the spell caster. The reverse of the spell, Dispel Good, functions against summoned or enchanted creatures of good alignment or sent to aid the cause of good. The material components for this spell are the cleric's religious object and holy/unholy water."
    ),
    Spell('Flame Strike','C',5,
        cast=tp(8,S),
        duration=tp(1,S),
        sourcebook=V,
        desc="When the cleric calls down a Flame Strike spell, a column of fire roars downward in the exact location called for by the caster. If any creature is within the area of effect of a Flame Strike, it must make a saving throw. Failure to make the save means the creature has sustained 6-48 (6d8) hit points of damage; otherwise, 3-24 (3d8) hit points of damage are taken. The material component of this spell is a pinch of sulphur."
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
        sourcebook=V,
        desc="When this spell is cast by the cleric, a horde of creeping, hopping, and flying insects swarm in a thick cloud. These insects obscure vision, limiting it to 3\". Creatures within the insect plague sustain 1 hit point of damage for each melee round they remain in it due to the bites and stings of the insects, regardless of armour class. The referee will cause all creatures with fewer than five hit dice to check morale. Creatures with two or fewer hit dice will automatically move at their fastest possible speed in a straight line in a random direction until they are not less than 24\" distant from the cloud of insects. Creatures with fewer than five hit dice which fail their morale check will behave likewise. Heavy smoke will drive off insects within its bounds. Fire will also drive insects away; a Wall of Fire in a ring shape will keep the Insect Plague outside its confines, but a Fireball will simply clear insects from its blast area for 1 turn. Lightning and cold/ice act likewise. The plague lasts for 1 turn for each level of experience of the cleric casting the spell, and thereafter the insects disperse. The insects swarm in an area which centres around a summoning point determined by the spell caster, which point can be up to 36\" distant from the cleric. The Insect Plague does not move thereafter for as long as it lasts. Note that the spell can be countered by casting a Dispel Magic upon the summoning point. A cube of force (a special magic item) would keep insects away from a character seeking the centre of the swarm, but invisibility would afford no protection. The material components of this spell area few grains of sugar, some kernels of grain, and a smear of fat."
    ),
    Spell('Magic Font','C',5,
        cast=tp(5,T),
        duration=tp(1,VA),
        sourcebook=U
    ),
    Spell('Plane Shift','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the Plane Shift spell is cast, the cleric moves himself or herself or some other creature to another plane of existence. The recipient of the spell will remain in the new plane until sent forth by some like means. If several persons link hands in a circle, up to seven can be affected by the Plane Shift at the same time. The material component of this spell is a small, forked metal rod - the exact size and metal type dictating to which plane of existence the spell will send the affected creature(s) to. (Your referee will determine specifics regarding how and what planes are reached.) An unwilling victim must be touched in order to be sent thusly: and in addition, the creature also is allowed a saving throw, and if the latter is successful the effect of the spell is negated."
    ),
    Spell('Quest','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The Quest is a spell by means of which the cleric requires the affected creature to perform a service and return to the cleric with proof that the deed was accomplished. The Quest can, for example, require the location and return of some important or valuable object, the rescue of a notable person, the release of some creature, the capture of a stronghold, the slaying of a person, the delivery of some item, and so forth. If the Quest is not properly followed due to disregard, delay, or perversion, the creature affected by the spell loses 1 from its saving throw dice for each day of such action, and this penalty will not be removed until the Quest is properly discharged or the cleric cancels it. (There are certain circumstances which will temporarily suspend a Quest, and other which will discharge or cancel it; your Dungeon Master will give you appropriate information as the need to know arises.) The material component of this spell is the cleric's religious symbol."
    ),
    Spell('Rainbow','C',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=U
    ),
    Spell('Raise Dead','C',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the cleric casts a raise dead spell, he or she can restore life to a dwarf, gnome, half-elf, halfling, or human. The length of time which the person has been dead is of importance, as the cleric can raise dead persons only up to a certain point, the limit being 1 day for each level of experience of the cleric, i.e. a 9th level cleric can raise a person dead for up to 9 days. Note that the body of the person must be whole, or otherwise missing parts will still be missing when the person is brought back to life. Also, the resurrected person must make a special saving throw to survive the ordeal (see CHARACTER ABILITIES, Constitution). Furthermore, the raised person is weak and helpless in any event, and he or she will need one full day of rest in bed for each day he or she was dead. The somatic component of the spell is a pointed finger. The reverse of the spell, Slay L living, allows the victim a saving throw, and if it is successful, the victim sustains damage equal only to that caused by a Cause Serious Wounds spell. i.e. 3-17 hit points. An evil cleric can freely use the reverse spell; a good cleric must exercise extreme caution in its employment, being absolutely certain that the victim of the Slay Living spell is evil and that his or her death is a matter of great necessity and for good, otherwise the alignment of the cleric will be sharply changed. Note that newly made undead, excluding skeletons, which fall within the days of being dead limit are affected by Raise Dead spells cast upon them. The effect of the spell is to cause them to become resurrected dead, providing the constitution permits survival; otherwise, they are simply dead."
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
        sourcebook=V,
        desc="When the cleric employs this spell, all things within the area of the True Seeing effect appear as they actually are. Secret doors become plain. The exact location of displaced things is obvious. Invisible things and those which are astral or ethereal become quite visible. Illusions and apparitions are seen through. Polymorphed, changed, or magicked things are apparent. Even the aura projected by creatures becomes visible, so that the cleric is able to know whether they are good or evil or between. The spell requires an ointment for the eyes. The ointment is made from very rare mushroom powder, saffron, and fat. The reverse of the spell, False Seeing, causes the person to see things as they are not, rich being poor, rough smooth, beautiful ugly. The ointment for the reverse spell is concocted of oil, poppy dust, and pink orchid essence. For both spells, the ointment must be aged for 1-6 months."
    ),
    Spell('Aerial Servant','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,D),
        sourcebook=V,
        desc="This spell summons an invisible Aerial Servant (see ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL) to do the bidding of the cleric who conjured it. The creature does not fight, but it obeys the command of the cleric with respect to finding and returning with whatever object or creature that is described to it. Of course, the object or creature must be such as to allow the aerial servant to physically bring it to the cleric or his or her assign. The spell caster should keep in mind the consequences of having an aerial servant prevented, for any reason, from completion of the assigned duty. The spell lasts for a maximum of 1 day for each level of experience of the cleric who cast it. The aerial servant returns to its own plane whenever the spell lapses, its duty is fulfilled, it is dispelled, the cleric releases it, or the cleric is slain. The cleric must have a Protection From Evil spell, or be within a magic circle, thaumaturgic triangle, or pentagram when summoning an aerial servant unless the cleric has his or her religious symbol or a religious artifact or relic to use to control the creature. Otherwise, the creature will slay its summoner and return from whence it came. The aerial servant will always attack by complete surprise when sent on a mission, and gain the benefit of 4 free melee rounds unless the creature involved is able to detect invisible objects, in which case a six-sided die is rolled, and 1 = 1 free round, 2 = 2 free rounds, 3 = 3 free rounds, 4 = 4 free rounds, and 5 or 6 = 0 free rounds (the opponent is not surprised at all). Each round the aerial servant must dice to score a hit, and when a hit is scored, it means the aerial servant has grabbed the item or creature it was sent to take and bring back to the cleric. If a creature is involved, the aerial servant's strength is compared to the strength of the creature to be brought. If the creature in question does not have a strength rating, roll the appropriate number of the correct type of hit dice for the aerial servant and for the creature it has grabbed. The higher total is the stronger."
    ),
    Spell('Animate Object','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This powerful spell enables the cleric casting it to imbue inanimate objects with mobility and a semblance of life. The animated object, or objects, then attack whomever or whatever the cleric first designates. The object can be of any material whatsoever - wood, metal, stone, fabric, leather, ceramic, glass, etc. The speed of movement of the object is dependent upon its means of propulsion and its weight. A large wooden table would be rather heavy, but its legs would give it speed. A rug could only slither along. A jar would roll. Thus a large stone pedestal would rock forward at 1\" per round, a stone statue would move at 4\" per round, a wooden statue 8\" per round, an ivory stool of light weight would move at 12\". Slithering movement is about 1\" to 2\" per round, rolling 3\" to 6\" per round. The damage caused by the attack of an animated object is dependent upon its form and composition. Light, supple objects can only obscure vision, obstruct movement, bind, trip. smother, etc. Light, hard objects can fall upon or otherwise strike for 1-2 hit points of damage or possibly obstruct and trip as do light, supple objects. Hard, medium weight objects can crush or strike for 2-8 hit points of damage, those larger and heavier doing 3-12, 4-16, or even 5-20 hit points of damage. The frequency of attack of animated objects is dependent upon their method of locomotion, appendages, and method of attack. This varies from as seldom as once every five melee rounds to as frequently as once per melee round. The armour class of the object animated is basically a function of material and movement ability with regard to hitting. Damage is dependent upon the type of weapon and the object struck. A sharp cutting weapon is effective against fabric, leather, wood and like substances. Heavy smashing and crushing weapons are useful against wood, stone, and metal objects. Your referee will determine all of these factors, as well as how much damage the animated object can sustain before being destroyed. The cleric can animate 1 cubic foot of material for each level of experience he or she has attained. Thus, a 14th level cleric could animate one or more objects whose solid volume did not exceed 14 cubic feet, i.e. a large statue, two rugs, three chairs, or a dozen average crocks."
    ),
    Spell('Blade Barrier','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(3,R),
        sourcebook=V,
        desc="The cleric employs this spell to set up a wall of circling, razor-sharp blades. These whirl and flash in endless movement around an immobile point. Any creature which attempts to pass through the Blade Barrier suffers 8-64 (8d8) hit points of damage in doing so. The barrier remains for 3 melee rounds for every level of experience of the cleric casting it. The barrier can cover any area from as small as 5' square to as large as 2\" square, i.e. 20'x20' under ground, 60'x60' outdoors."
    ),
    Spell('Conjure Animals','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="The Conjure Animals spell enables the cleric to summon a mammal, or several of them, to his locale in order that the creature(s) can attack the cleric's opponents. The conjured animal(s) remain in the cleric's locale for 2 melee rounds for each level of experience of the cleric conjuring it (them), or until slain. The spell caster can, by means of his incantation, call up one or more mammals with hit dice whose total does not exceed his or her level. Thus, a cleric of 12th level could conjure one mammal with 12 hit dice, two with 6 hit dice each, three with 4 hit dice each, 4 with a hit dice each, six with 2 hit dice each, or 12 with 1 hit die each. For every +1 (hit point) of a creature's hit dice, count 1/4 of a hit die, i.e. a creature with 4+3 hit dice equals a 4¾ hit dice creature. The creature(s) summoned by the spell will unfailingly attack the opponent(s) of the cleric by whom the spell was cast."
    ),
    Spell('Find The Path','C',6,
        cast=tp(3,R),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By use of this spell, the cleric is enabled to find the shortest, most direct route that he or she is seeking, be it the way to or from or out of a locale. The locale can be outdoors or underground, a trap or even a maze spell. The spell will enable the cleric to select the correct direction which will eventually lead him or her to egress, the exact path to follow (or actions to take), and this knowledge will persist as long as the spell lasts, i.e. 1 turn for each level of experience of the cleric casting find the path. The spell frees the cleric, and those with him or her from a Maze spell in a single melee round and will continue to do so as long as the spell lasts. The material component of this spell is a set of divination counters of the sort favoured by the cleric - bones, ivory counters, sticks, carved runes, or whatever. The reverse, Lose The Path, makes the creature touched totally lost and unable to find its way for the duration of the spell, although it can be led, of course."
    ),
    Spell('Forbiddance','C',6,
        cast=tp(6,R),
        duration=tp(1,P),
        sourcebook=U
    ),
    Spell('Heal','C',6,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="The very potent Heal spell enables the cleric to wipe away disease and injury in the creature who receives the benefits of the spell. It will completely cure any and all diseases and/or blindness of the recipient and heal all hit points of damage suffered due to wounds or injury, save 1 to 4 (d4). It dispels a Feeblemind spell. Naturally, the effects can be negated by later wounds, injuries, and diseases. The reverse, Harm, infects the victim with a disease and causes loss of all hit points, as damage, save 1 to 4 (d4), if a successful touch is inflicted. For creatures not affected by the Heal (or Harm) spell, see Cure Light Wounds."
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
        sourcebook=V,
        desc="By employing a Part Water spell, the cleric is able to cause water or similar liquid to move apart. thus forming a trough. The depth and length of the trough created by the spell is dependent upon the level of the cleric, and a trough 3' deep by 1' by 1\" (10' or 10 yards) is created per level, i.e. at 12th level the cleric would part water 36' deep by 12' wide by 24\" (240' or 240 yards) long. The trough will remain as long as the spell lasts or until the cleric who cast it opts to end its effects (cf. Dispel Magic). The material component of this spell is the cleric's religious symbol."
    ),
    Spell('Speak With Monsters','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When cast, the Speak With Monsters spell allows the cleric to converse with any type of creature which has any form of communicative ability. That is, the monster will understand the intent of what is said to it by the cleric. The creature or creatures thus spoken to will be checked by your referee in order to determine reaction. All creatures of the same type as that chosen by the cleric to speak to can likewise understand if they are within range. The spell lasts for 1 melee round per level of experience of the cleric casting it. and during its duration conversation can take place as the monster is able and desires."
    ),
    Spell('Stone Tell','C',6,
        cast=tp(1,T),
        duration=tp(1,T),
        sourcebook=V,
        desc="When the cleric casts a Stone Tell upon an area, the very stones will speak and relate to the caster who or what has touched them as well as telling what is covered, concealed, or simply behind the place they are. The stones will relate complete descriptions as required. The material components for this spell area drop of mercury and a bit of clay."
    ),
    Spell('Word of Recall','C',6,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="The Word Of Recall spell takes the cleric instantly back to his or her sanctuary when the word is uttered. The sanctuary must be specifically designated in advance by the cleric. It must be a well known place, but it can be any distance from the cleric, above or below ground. Transportation by the Word Of Recall spell is infallibly safe. The cleric is able to transport, in addition to himself or herself, 250 gold pieces weight cumulative per level of experience. Thus, a 15th level cleric could transport his or her person and 3,750 (375 pounds) gold pieces weight in addition; this extra matter can be equipment, treasure, or living material such as another person."
    ),
    Spell('Astral Spell','C',7,
        cast=tp(3,T),
        duration=tp(0),
        sourcebook=V,
        desc="By means of the Astral Spell a cleric is able to project his or her astral body into the Astral Plane, leaving his or her physical body and material possessions behind on the Prime Material Plane, (the plane on which the entire universe and all of its parallels have existence). Only certain magic items which have multi-planed existence can be brought into the Astral Plane. As the Astral Plane touches upon all of the first levels of the Outer Planes, the cleric can travel astrally to any of these Outer Planes as he or she wills. The cleric then leaves the Astral Plane, forming a body on the plane of existence he or she has chosen to enter. It is also possible to travel astrally anywhere in the Prime Material Plane by means of the Astral Spell, but a second body cannot be formed on the Prime Material Plane. As a general rule, a person astrally projected can be seen only by creatures on the Astral Plane. At all times the astral body is connected to the material by a silvery cord. If the cord is broken, the affected person is killed, astrally and materially, but generally only the psychic wind can normally cause the cord to break. When a second body is formed on a different plane. the silvery cord remains invisibly attached to the new body, and the cord simply returns to the latter where it rests on the Prime Material Plane, reviving it from its state of suspended animation. Although astrally projected persons are able to function on the Astral Plane, their actions do not affect creatures not existing on the Astral Plane. The spell lasts until the cleric desires to end it, or until it is terminated by some outside means (Dispel Magic or destruction of the cleric's body on the Prime Material Plane). The cleric can take up to five other creatures with him or her by means of the Astral Spell, providing the creatures are linked in a circle with the cleric. These fellow travellers are dependent upon the cleric and can be stranded. Travel in the Astral Plane can be slow or fast according to the cleric's desire. The ultimate destination arrived at is subject to the conceptualization of the cleric. (See APPENDIX IV, THE KNOWN PLANES OF EXISTENCE, for further information on the Astral Plane and astral projection.)"
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
        sourcebook=V,
        desc="The casting of a Gate spell has two effects: first, it causes an ultra-dimensional connection between the plane of existence the cleric is an and that plane on which dwells a specific being of great power, the result enabling the being to merely step through the gate or portal, from its plane to that of the cleric; second, the utterance of the spell attracts the attention of the dweller on the other plane. When casting the spell, the cleric must name the demon, devil, demi-god, god, or similar being he or she desires to make use of the Gate and come to the cleric's aid. There is a 100% certainty that something will step through the gate. The actions of the being which comes through will depend on many factors, including the alignment of the cleric, the nature of those in company with him or her, and who or what opposes or threatens the cleric. Your Dungeon Master will have a sure method of dealing with the variables of the situation. The being gated in will either return immediately (very unlikely) or remain to take action."
    ),
    Spell('Holy (Unholy) Word','C',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V
    ),
    Spell('Regenerate','C',7,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a Regenerate spell is cast, body members (fingers, toes, hands, feet, arms, legs, tails, or even the heads of multi-headed creatures), bones, or organs will grow back. The process of regeneration requires but 1 round if the member(s) severed is (are) present and touching the creature, 2-8 turns otherwise. The reverse, Wither, causes the member or organ touched to shrivel and cease functioning in 1 round, dropping off into dust in 2-8 turns. As is usual, creatures must be touched in order to have harmful effect occur. The material components of this spell are a prayer device and holy/unholy water."
    ),
    Spell('Restoration','C',7,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast, the life energy level of the recipient creature is raised upwards by one. This subsumes previous life energy level drain of the creature by some force or monster. Thus, if a 10th level character had been struck by a wight and drained to 9th level, the Restoration spell would bring the character up to exactly the number of experience points necessary to restore him or her to 10th level once again. and restoring additional hit dice (or hit points) and level functions accordingly. Restoration is only effective if the spell is cast within 1 day/level of experience of the cleric casting it of the recipient's loss of life energy. The reverse, Energy Drain, draws away a life energy level (cf. such \"undead\" as spectre, wight, vampire). The Energy Drain requires the victim to be touched. A Restoration spell will restore the intelligence of a creature affected by a Feeblemind spell (q.v.)."
    ),
    Spell('Resurrection','C',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="The cleric employing this spell is able to restore life and complete strength to the person he/she bestows the Resurrection upon. The person can have been dead up to 10 years cumulative per level of the cleric casting the spell, i.e. a 19th level cleric can resurrect the bones of a person dead up to 190 years. See raise dead for limitations on what persons can be raised. The reverse, Destruction, causes the victim of the spell to be instantly dead and turned to dust. Destruction requires a touch, either in combat or otherwise. The material components of the spell are the cleric's religious symbol and holy/unholy water. Employment of this spell makes it impossible for the cleric to cast further spells or engage in combat until he or she has had one day of bed rest for each level of experience of the person brought back to life or destroyed."
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
        sourcebook=V,
        desc=("The cleric casting this spell inscribes a symbol in the air or upon any surface, according to his or her wish. The symbol glows for 1 turn for each level of experience of the cleric casting it. The particular symbol used can be selected by the cleric at the time of casting, selection being limited to:\n"
            "HOPELESSNESS	- Creatures seeing it must turn back in dejection and/or surrender to capture or attack unless they save versus magic. Its effects last for 3 to 12 turns.\n"
            "PAIN	- Creatures affected suffer -4 on \"to hit\" dice and -2 on dexterity ability score due to wracking pains. The effects last for 2-20 turns.\n"
            "PERSUASION	- Creatures seeing the symbol become of the same alignment as and friendly to the cleric who scribed the symbol for from 1 to 20 turns unless a saving throw versus magic is made.\n"
            "The material components of this spell are mercury and phosphorus. (cf. eighth level magic-user symbol spell."
        )
    ),
    Spell('Wind Walk','C',7,
        cast=tp(1,R),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="This spell enables the cleric, and possibly one or two other persons. to alter the substance of his or her body to cloud-like vapours. A magical wind then wafts the cleric along at a speed of up to 60\" per turn, or as slow as 6\" per turn, as the spell caster wills. The Wind Walk spell lasts as long as the cleric desires, up to a maximum duration o 6 turns (one hour) per level of experience of the caster. For every 8 levels of experience the cleric has attained, up to 24, he or she is able to touch another and carry that person. or those two persons, along with the Wind Walk. Persons wind walking are not invisible but appear misty and are transparent. If fully clothed in white they are 80% likely to be mistaken for clouds, fog, vapours, etc. The material components of this spell are fire and holy/unholy water."
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
    Spell('Slow Poison','D',2,
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
        duration=tp(1,VA),
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
        cast=tp(Decimal(0.1),S),
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
        duration_lvl=tp(1,R),
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
        duration_lvl=tp(2,R),
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
        duration_lvl=tp(1,R),
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
    print(cleric_spells[0].sourcebook.value)


if __name__ == '__main__':
    test_module()


