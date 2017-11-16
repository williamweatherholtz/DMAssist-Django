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
        desc="Upon uttering the <i>bless</i> spell, the caster raises the morale of friendly creatures by +1. Furthermore, it raises their \"to hit\" dice rolls by +1. A blessing, however, will affect only those not already engaged in melee combat. This spell can be reversed by the cleric to a <i>curse</i> upon enemies which lowers morale and \"to hit\" by -1. The caster determines at what range (up to 6\") he or she will cast the spell, and it then affects all creatures in on area 5\" square centerd on the point the spell was cast upon. In addition to the verbal and somatic gesture components, the <i>bless</i> requires holy water, while the <i>curse</i> requires the sprinkling of specially polluted water."
    ),
    Spell('Ceremony','C',1,
        cast=tp(1,H),
        duration=tp(1,P),
        sourcebook=U,
        desc=("<i>Ceremony</i> has a number of applications in the religious organization, depending on the level of the cleric. The effect of a <i>ceremony</i> spell does not leave behind an aura of magic, although in some cases an aura of good or evil might be present (and thus detectable). The specific <i>ceremony</i> spells can vary from religion to religion, but usually encompass these:\n\n"
            "\t1st-level cleric: <i>coming of age, burial, marriage</i>\n"
            "\t3rd-level cleric: <i>dedication, investiture, consecrate item</i>\n"
            "\t5th-level cleric: <i>ordination, special vows</i>\n"
            "\t7th-level cleric: <i>consecrate ground</i>\n"
            "\t9th-level cleric: <i>anathematize</i>\n\n"
            "Each of these varieties of the <i>ceremony</i> spell requires a cleric of the indicated level or a higher one, with additional restrictions as described below. For all <i>ceremony</i> spells except <i>anathematize</i> (see below), no saving throw is called for, since the recipient is either inanimate or presumed to be willing to be affected by the magic, any version of the spell except for <i>anathematize</i> will simply fail if it is cast on a person who (for some reason) is unwilling to receive the benefit. Briefly, the <i>ceremonies</i> listed do the following things:\n\n"
            "<i>Coming of age</i> is a limited form of <a href=\"/spells/bless-cleric-lvl-1\"><i>bless</i></a> spell which is cast upon a young man (and in some cultures a young woman) at some point relatively early in life, often the age of 12. A young person who receives this spell gets a +1 bonus to any single saving throw, which can be taken at any time after the <i>coming of age ceremony</i> is completed. In some cultures, the <i>coming of age ceremony</i> has a symbolic significance, such that an adolescent must receive this blessing before he or she can enjoy the rights and privileges of adulthood.\n\n"
            "<i>Burial</i> magically protects a corpse, and bestows it with the blessing of the religious organization. The body is shielded for one week as if by a <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell, and anyone trying to disinter the corpse within that time must make a saving throw versus spell or stop and flee in fear for one turn.\n\n"
            "<i>Marriage</i> has no tangible after-effect (i.e., it does not guarantee happiness or harmony), but it usually carries a moral or legal significance, not dissimilar in nature to the various rites of marriage which are performed in our real world.\n\n"
            "<i>Dedication</i> allows the recipient of the spell to be taken into the ranks of the casting cleric's religion, making that person a sanctioned worshiper of the cleric's deity. The effect of a <i>dedication</i> is permanent, unless the worshiper demonstrates a desire to change allegiance to a different deity. In such a case, the earlier <i>dedication</i> can be overridden by a new <i>dedication</i> cast by a cleric of a higher level than the one who performed the previous <i>dedication</i>.\n\n"
            "The rite of <i>investiture</i> must be performed on any aspiring cleric before that character can achieve the status of a first-level cleric.\n\n"
            "<i>Consecrate item</i> must be performed on any object to be placed on an altar or some other location within a religious edifice. To prevent it from losing its potency, holy (or unholy) water must be kept in a properly <i>consecrated</i> container.\n\n"
            "<i>Ordination</i> must be performed on a cleric before the character can become the priest of a congregation or assume similar sorts of duties, and even an adventuring cleric must be <i>ordained</i> before he or she can gain followers and establish a following or other sort of group. In all cases, the cleric performing the <i>ordination</i> must be of higher level than the recipient; this <i>ceremony</i> is often conducted as part of the training a cleric receives in order to advance from second to third level.\n\n"
            "<i>Special vows</i> can be received by a would-be cavalier or paladin before that character embarks upon a career in the desired profession. The effects of this spell persist for as long as it takes the character to accumulate enough experience points to rise to the upper limit of his or her current level. The <i>special vows</i> can then be renewed as part of the character's training between levels, or at any time during advancement through the next higher level. A cavalier or paladin who has received <i>special vows</i> is immune to the effects of <a href=\"/spells/remove-curse-cleric-lvl-3/\"><i>bestow curse</i></a> spells (but not cursed items) for as long as the <i>special vows</i> remain in effect. Additionally, this <i>ceremony</i> renders the subject more susceptible (-4 on saving throw) to any <i>quest</i> spell cast upon him or her by a cleric of the same alignment as the caster of the <i>special vows</i>.\n\n"
            "<i>Consecrate ground</i> should be performed upon an area before any holy (unholy) structure is built on the site. A religious edifice constructed on ground that has not been <i>consecrated</i> will slowly but irrevocably fall into a state of disrepair and has a 1% chance per year, cumulative, of actually collapsing as a result of this oversight. This spell must be cast before the area in question is altered in any way (e.g., landscaping) and before any construction materials are brought to the site; it will have no effect if it is done as an afterthought. <i>Consecrate ground</i> can also be used on a plot of land destined for use as a graveyard, and in such case the graveyard itself automatically turns undead each round with the same effectiveness as a 3rd-level cleric. Or, if the <i>consecration</i> of a would-be graveyard is performed by an evil cleric, any undead creatures occupying the area are treated as if they were being protected and controlled by an evil cleric of 3rd level.\n\n"
            "<i>Anathematize</i> is a form of excommunication by means of which the offender is literally branded on the cheek, forehead, arm, or hand with a symbol, sigil, or sign that identifies the subject (to those who understand the symbol) as someone who has committed a serious offense in the eyes of his or her deity. An unwilling subject of this spell is allowed a saving throw versus spell, at -4, to escape its effects. If the recipient is not truly deserving of the telling brand, the spell fails when cast. A successful <a href=\"/spells/atonement-cleric-lvl-5/\"><i>atonement</i></a> causes the brand to fade, and possibly vanish. If the offending actions were caused magically or by some other external force, the brand utterly disappears. If the offending actions were natural, the brand cannot be completely removed.\n\n"
            "The components for the various <i>ceremony</i> spells vary from religion to religion, but the material component always involves the use of the cleric's holy symbol in one way or another. Standard costs for the casting of these spells are as follows: <i>coming of age</i>, 5-15 sp; <i>burial</i>, 5-50 gp; <i>marriage</i>, 1-20 gp; <i>dedication</i>, 1-10 sp (or sometimes free); <i>investiture</i>, 1-100 gp (or sometimes free); <i>item consecration</i>, usually free; <i>ordination</i>, usually free but possibly as much as 200 gp; <i>special vows</i>, 1-100 gp (or sometimes free); <i>consecrate groud</i>, 100-600 gp depending on the size of the area to be affected and the level of the cleric performing the spell; and <i>anathematize</i> is always performed at no charge, since the casting of this spell is always deemed to be in the best interests of the cleric's religion."
        )
    ),
    Spell('Combine','C',1,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("This spell enables three to five clerics to <i>combine</i> their abilities and thereby empower one of their number to cast a spell or turn undead with greater efficacy. The highest-level cleric of the group (or one of such, as applicable) stands, while the other clerics join hands in a surrounding circle. All the participating clerics then cast the combine spell together.\n"
            "The central cleric temporarily functions as if of higher level, gaining one level for each encircling cleric. The maximum gain is four levels, and the maximum duration is 3 turns. The increase applies to the cleric's effective level for determining the results of attempts to turn undead, and to spell details which vary by the level of the caster. The encircling clerics must concentrate on maintaining the <i>combine</i> effect. They gain no armor class bonuses from shield or dexterity, and their attackers gain a +4 bonus on all \"to hit\" rolls. The central cleric gains no additional spells, but may cast any previously memorized spell(s), often with bonus effects."
        )
    ),
    Spell('Command','C',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="This spell enables the cleric to issue a <i>command of a single word</i>. The <i>command</i> must be uttered in a language which the spell recipient is able to understand. The individual will obey to the best of his/her/its ability only so long as the <i>command</i> is absolutely clear and unequivocal, i.e. \"Suicide!\" could be a noun, so the creature would ignore the <i>command</i>. A <i>command</i> to \"Die!\" would cause the recipient to fall in a faint or cataleptic state for 1 round, but thereafter the creature would be alive and well. Typical <i>command words</i> are: back, halt, flee, run, stop, fall, fly, go, leave, surrender, sleep. rest, etc. Undead are not affected by a <i>command</i>. Creatures with intelligence of 13 or more, and creatures with 6 or more hit dice (or experience levels) are entitled to a saving throw versus magic. (Creatures with 13 or higher intelligence and 6 hit dice/levels do not get 2 saving throws!)"
    ),
    Spell('Create Water','C',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the cleric casts a <i>create water</i> spell, four gallons of water are generated for every level of experience of the caster, i.e. a 2nd level cleric creates eight gallons of water, a 3rd level twelve gallons, a 4th level sixteen gallons, etc. The water is clean and drinkable (it is just like rain water). Reversing the spell, <i>destroy water</i>, obliterates without trace (such as vapor, mist, fog or steam) a like quantity of water. Created water will last until normally used or evaporated, spilled, etc. Water can be created or destroyed in an area as small as will actually contain the liquid or in an area as large as 27 cubic feet (one cubic yard). The spell requires at least a drop of water to create, or a pinch of dust to destroy, water. Note that water cannot be created within a living thing."
    ),
    Spell('Cure Light Wounds','C',1,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Upon laying his or her hand upon a creature, the cleric causes from 1 to 8 hit points of wound or other injury damage to the creature's body to be healed. This healing will not affect creatures without corporeal bodies, nor will it cure wounds of creatures not living or those which can be harmed only by iron, silver, and/or magical weapons. Its reverse, <i>cause light wounds</i>, operates in the same manner; and if a person is avoiding this touch, a melee combat \"to hit\" die is rolled to determine if the cleric's hand strikes the opponent and causes such a wound. Note that cured wounds are permanent only insofar as the creature does not sustain further damage, and that caused wounds will heal — or can be cured — just as any normal injury will. Caused light wounds are 1 to 8 hit points of damage."
    ),
    Spell('Detect Evil','C',1,
        cast=tp(1,R),
        duration=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="This is a spell which discovers emanations of evil, or of good in the case of the reverse spell, from any creature or object. For example, evil alignment or an evilly cursed object will radiate evil, but a hidden trap or an unintelligent viper will not. The duration of a <i>detect evil</i> (or <i>detect good</i>) spell is 1 turn + ½ turn (5 rounds, or 5 minutes) per level of the cleric. Thus a cleric of 1st level of experience can cast a spell with a 1½ turn duration, at 2nd level a 2 turn duration, 2½ at 3rd, etc. The spell has a path of detection 1\" wide in the direction in which the cleric is facing. It requires the use of the cleric's holy (or unholy) symbol as its material component, with the cleric holding it before him or her."
    ),
    Spell('Detect Magic','C',1,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V,
        desc="When the <i>detect magic</i> spell is cast, the cleric detects magical radiations in a path 1\" wide, and up to 3\", long, in the direction he or she is facing. The caster can turn 60° per round. Note that stone walls of 1' or more thickness, solid metal of but 1/12' thickness, or 3' or more of solid wood will black the spell. The spell requires the use of the cleric's holy (or unholy) symbol."
    ),
    Spell('Endure Cold/Heat','C',1,
        cast=tp(1,R),
        duration_lvl=tp(9,T),
        sourcebook=U,
        desc="The recipient of this spell is provided with protection from normal extremes of cold or heat (depending on which application is used). He or she can stand unclothed in temperatures as low as -30°F or as high as 130°F (depending on application) with no ill effect. A temperature extreme beyond either of those limits will cause 1 hit point of exposure damage per hour for every degree above or below those limits. (Without the benefit of protection such as this, exposure damage is 1 hit point per turn for each degree of temperature.) The spell will last for the prescribed duration, or until the recipient is affected by any form of magical cold (including white dragon breath) or magical heat. The cancellation of the spell will occur regardless of which application was used and regardless of which type of magical effect hits the character (e.g. <i>endure cold</i> will be cancelled by magical heat or fire as well as by magical cold). The recipient of the spell will not suffer damage from the magical heat or cold during the round in which the spell is broken, but will be vulnerable to all such attacks starting on the following round. The spell will be cancelled instantly if either <a href=\"/spells/resist-fire-cleric-lvl-2/\"><i>resist fire</i></a> or <a href=\"/spells/resist-cold-cleric-lvl-1/\"><i>resist cold</i></a> is cast upon the recipient."
    ),
    Spell('Invisibility to Undead','C',1,
        cast=tp(4,S),
        duration=tp(6,R),
        sourcebook=U,
        desc=("This spell is quite similar to <a href=\"/spells/sanctuary-cleric-lvl-1/\"><i>sanctuary</i></a>, but only affects undead of 4 or fewer hit dice. A saving throw versus spell is made for each <i>type</i> of undead within 30 feet of the caster, and if failed, all undead of that type will ignore the caster completely for the duration of the spell. (Note that this negates subsequent attempts by the caster to turn those undead.) However, if the saving throw suceeds, all undead of that type will attack the spell caster in preference to any other possible targets.\n\n"
            "The effect of this spell ends if the caster attacks or attempts to cast any other spell. If the caster is of neutral morals (with respect to good and evil), the undead save at -2. The material component is the cleric's holy symbol."
        )
    ),
    Spell('Light','C',1,
        cast=tp(4,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="This spell causes excitation of molecules so as to make them brightly luminous. The <i>light</i> thus caused is equal to torch light in brightness, but its sphere is limited to 4\" in diameter. It lasts for the duration indicated (7 turns at 1st experience level, 8 at 2nd, 9 at 3rd, etc.) or until the caster utters a word to extinguish the light. The light spell is reversible, causing <i>darkness</i> in the same area and under the same conditions, except the blackness persists for only one half the duration that light would last. If this spell is cast upon a creature, the applicable magic resistance and saving throw dice rolls must be made. Success indicates that the spell affects the area immediately behind the creature, rather than the creature itself. In all other cases, the spell takes effect where the caster directs as long as he or she has a line of sight or unobstructed path for the spell; <i>light</i> can spring from air, rock, metal, wood, or almost any similar substance."
    ),
    Spell('Magic Stone','C',1,
        cast=tp(1,R),
        duration=tp(6,R),
        sourcebook=U,
        desc="To use this spell, the cleric picks up a small stone or pebble and then (via the casting process) places a magical aura on it. The spell cannot affect stones that are already magical. The <i>magic stone</i> can be thrown at a target up to 4\" distant (assuming no intervening obstacles and sufficient head room). It will act as a +1 weapon for \"to hit\" determination, and if a hit is scored the stone will do 1 point of damage. Ranges are 2\"/3\"/4\", with standard modifications. If the stone travels more than 4\" from the thrower or if it does not score a hit, the missile loses its dweomer and falls harmlessly to the ground. A <i>magic stone</i> must be thrown within 6 rounds after the casting of the spell is completed, or it turns back into an ordinary item. A hit from the stone will break the concentration of a spell caster only if the victim fails a saving throw versus spell. Any target with innate magic resistance cannot be affected by the stone. A <a href=\"/spells/shield-magic-user-lvl-1/\"><i>shield</i></a> spell will protect a target from a <i>magic stone</i>, as will a <i>brooch of shielding</i>, a <a href=\"/spells/protection-from-normal-missiles-magic-user-lvl-3/\"><i>protection from normal missiles</i></a> spell, a <a href=\"/spells/minor-globe-of-invulnerability-magic-user-lvl-4/\"><i>minor globe of invulnerability</i></a>, or any similar (more powerful) magic. A cleric of 6th through 10th level can enchant 2 stones with this spell, one of 11th through 15th level can use it on 3 stones, and an additional stone is allowed for every five levels of experience the caster has gained beyond the 11th (i.e., 4 stones at 16th level, 5 stones at 21st level, etc.). It is possible for a cleric to give the enchanted stone(s) to another character to throw. Note that some religious organizations forbid their clerics from using this spell, since it enables the cleric to use a missile weapon (of sorts)."
    ),
    Spell('Penetrate Disguise','C',1,
        cast=tp(2,R),
        duration=tp(1,R),
        sourcebook=U,
        desc="By means of this spell, the cleric is empowered to see through a disguise composed solely of makeup or altered clothing (i.e., non-magical in nature). The cleric cannot identify what class or profession the disguised figure actually belongs to, nor the true appearance of the figure; the spell merely points out that the target figure is posing as someone or something else. The spell doesn not detect actual rank or status and cannot reaveal an illusion for what it is, but it can detect whether a figure is the object of a <a href=\"/spells/friends-magic-user-lvl-1/\"><i>friends</i></a> spell. The spell cannot detect any deception involving alignment. The target of the spell is allowed a saving throw versus spell, and if this saving throw is made, the disguise will be enhanced in the eyes of the cleric, so that the caster becomes convinced that the target figure actually is what he claims to be. Being under the effect of a <a href=\"/spells/bless-cleric-lvl-1/\"><i>bless</i></a> spell, wearing magic armor, or using a magic item of protection (such as a cloak or ring) will give the target an appropriate bonus to the saving throw."
    ),
    Spell('Portent','C',1,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U,
        desc="This spell enables the cleric to tell something of his or another figure's future \"luck\". This \"luck\" takes the form of an improvement or reduction in a \"to hit\" roll or a saving throw at some point in the future unknown to the character who is the object of the <i>portent</i>. After this spell is cast, the Dungeon Master makes two die rolls in secret: First, 1d12, to determine at what point in the future the <i>portent</i> takes effect; second, 1d6 to determine the exact effect (roll of 1 = -3; 2 = -2; 3 = -1; 4 = +1; 5 = +2; 6 = +3). Based upon the result of the 1d6 roll, the DM should indicate to the player of the cleric character whether the <i>portent</i> is good, fair(which can be moderately good or moderately bad), or poor. The recipient of the spell will usually also be given this information. The result of the d12 roll represents the number of \"to hit\" rolls or saving throws that the target character must make before the roll to be affected by the <i>portent</i> occurs; e.g. if a 12 is rolled, then the 12th such roll thereafter will be the one to which the <i>portent</i> is applied. Die rolls only apply toward this count if they are taken in life-or-death (i.e., combat or peril) situations; the count is suspended if the character contrives to perform (for instance) saving throws against non-harmful effects in an effort to \"sidestep\" the <i>portent</i>. Die rolls that do apply toward this count include: Saving throws made in combat or against magical effects, \"to hit\" rolls made by an opponent against the character. When the die roll designated by the <i>portent</i> is made, the result will be adjusted upward or downward as indicated by the result of the d6 roll; thus, the character will be either more or less likely to succeed on a saving throw. The material component for this spell is either a numbered wheel or tea leaves."
    ),
    Spell('Precipitation','C',1,
        cast=tp(3,S),
        duration_lvl=tp(1,S),
        sourcebook=U,
        desc=("When this spell is cast, all water vapor in the atmosphere within the area of effect is precipitated in the form of a light rain. (Note that low-level spell casters will certainly be within the area of effect of the spell.) The rain will continue for only as many segments of time as the spell caster has levels of experience. Since only some 1/100 of an inch of precipitation falls during the course of a segment, the spell will have only the following general effects:\n\n"
            "Thin, light material will become damp in 1 segment and thoroughly wet thereafter.\n\n"
            "Twigs and heavy material such as canvas will be damp in 2 segments and wet thereafter.\n\n"
            "Flat, relatively non-porous surfaces such as stone floors, rock, painted wood, etc., will be damp in 1 segment and filmed with water thereafter.\n\n"
            "Semi-porous surfaces and materials will become damp on the surface in 2 segments, and thereafter the damp area will progress downward/inward, until after 5 segments the surface or material will be thoroughly wet.\n\n"
            "Porous surfaces and materials will simply absorb the rain up to the limit of their capacity — which probably extends well beyond the duration of the spell.\n\n"
            "Small flames, such as those of candles, will be extinguished by 1 segment of precipitation. Small fires will slow and become smoky for 1 round after precipitation has ceased. Large fires will not be materially affected by the spell.\n\n"
            "Note that if the temperature is above 90°F, the duration of the spell will be extended to double normal except in arid regions. Also, where the temperature ranges between 33° and 31°F, the precipitation will fall as rather thick snow, and most dampness/wetness effects will be negated or postponed until the snow melts. If magical heat of large area (i.e., a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a>, <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, <a href=\"/spells/flame-strike-cleric-lvl-5/\"><i>flame strike</i></a>, etc.) is applied to <i>precipitation</i>, a cloud of warm fog of double the area of the <i>precipitation</i> effect will be formed. If magical cold is applied to the spell or the water which remains thereafter, normal ice will be formed. The material component of the spell is a pinch of silver dust."
        )
    ),
    Spell('Protection From Evil','C',1,
        cast=tp(4,S),
        duration=tp(0,R),
        duration_lvl=tp(3,R),
        sourcebook=V,
        desc="When this spell is cast, it acts as if it were a magical armor upon the recipient. The protection encircles the recipient at a one foot distance, thus preventing bodily contact by creatures of an enchanted or conjured nature such as aerial servants, demons, devils, djinn, efreet, elementals, imps, invisible stalkers, night hags, quasits, salamanders, water weirds, wind walkers, and xorn. Summoned animals or monsters are similarly hedged from the protected creature. Furthermore, any and all attacks launched by evil creatures incur a penalty of -2 from dice rolls \"to hit\" the protected creature, and any saving throws caused by such attacks are made at +2 on the protected creature's dice. This spell can be reversed to become <i>protection from good</i>, although it still keeps out enchanted evil creatures as well. To complete this spell, the cleric must trace a 3' diameter circle upon the floor (or ground) with holy water for protection from evil, with blood for protection from good — or in the air using burning incense or smouldering dung with respect to evil/good."
    ),
    Spell('Purify Food & Drink','C',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When cast, the spell will make spoiled, rotten, poisonous or otherwise contaminated food and/or water pure and suitable for eating and/or drinking. Up to 1 cubic foot of food and/or drink can be thus made suitable for consumption. The reverse of the spell <i>putrefies food and drink</i>, even spoiling holy water. Unholy water is spoiled by <i>purify water</i>."
    ),
    Spell('Remove Fear','C',1,
        cast=tp(4,S),
        duration=tp(0),
        sourcebook=V,
        desc="By touch, the cleric instils courage in the spell recipient, raising the creature's saving throw against magical <i>fear</i> attacks by +4 on dice rolls for 1 turn. If the recipient has already been affected by fear, and failed the appropriate saving throw, the touch allows another saving throw to be made, with a bonus of +1 on the dice for every level of experience of the caster, i.e. a 2nd level cleric gives a +2 bonus, a 3rd level +3, etc. A \"to hit\" dice roll must be made to touch an unwilling recipient. The reverse of the spell, <i>cause fear</i>, causes the victim to flee in panic at maximum movement speed away from the caster for 1 round per level of the cleric causing such fear. Of course, <i>cause fear</i> can be countered by <i>remove fear</i> and vice versa."
    ),
    Spell('Resist Cold','C',1,
        cast=tp(1,R),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is placed on a creature by a cleric, the creature's body is inured to cold. The recipient can stand zero degrees Fahrenheit without discomfort, even totally nude. Greater cold, such as that produced by a sword of cold, <a href=\"/spells/ice-storm-magic-user-lvl-4/\"><i>ice storm</i></a>, cold wand, or white dragon's breath, must be saved against. All saving throws against cold are made with a bonus of +3, and damage sustained is one-half (if the saving throw is not made) or one-quarter (if the saving throw is made) of damage normal from that attack form. The resistance lasts for 1 turn per level of experience of the caster. A pinch of sulphur is necessary to complete this spell."
    ),
    Spell('Sanctuary','C',1,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When the cleric casts a <i>sanctuary</i> spell, any opponent must make a saving throw versus magic in order to strike or otherwise attack him or her. If the saving throw is not made, the creature will attack another and totally ignore the cleric protected by the spell. If the saving throw is made, the cleric is subject to normal attack process including dicing for weapons to hit, saving throws, damage. Note that this spell does not prevent the operation of area attacks (<a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, <a href=\"/spells/ice-storm-magic-user-lvl-4/\"><i>ice storm</i></a>, etc.). During the period of protection afforded by this spell, the cleric cannot take offensive action, but he or she may use non-attack spells or otherwise act in any way which does not violate the prohibition against offensive action, This allows the cleric to heal wounds, for example, or to <a href=\"/spells/bless-cleric-lvl-1\"><i>bless</i></a>, perform an <a href=\"/spells/augury-cleric-lvl-2/\"><i>augury</i></a>, <a href=\"/spells/chant-cleric-lvl-2/\"><i>chant</i></a>, cast a <a href=\"/spells/light-cleric-lvl-1\"><i>light</i></a> in the area (not upon on opponent!), and so on, The components of the spell include the cleric's holy/unholy symbol and a small silver mirror."
    ),
    Spell('Aid','C',2,
        cast=tp(4,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="The recipient of this spell gains the benefit of a <a href=\"/spells/bless-cleric-lvl-1/\"><i>bless</i></a> spell and a special benison of 1-8 additional hit points. The <a href=\"/spells/bless-cleric-lvl-1/\"><i>bless</i></a> lasts as long as the <i>aid</i> spell, as do the hit points thus gained. The <i>aid</i> allows a character to actually have more hit points than the character's full normal total. The added hit points last only for the duration of the <i>aid</i> spell. Any damage taken by the recipient while the <i>aid</i> spell is in effect is taken off the 1-8 additional hit points before regular ones are lost. Hit points bestowed by an <i>aid</i> spell and then lost cannot be regained by curative magic. <i>Example</i>: A 1st-level fighter has 8 hit points, takes 2 points of damage, and then recieves an <i>aid</> spell which gives 6 additional hit points. The fighter now has 12 hit points, 6 of which are temporary. If he is then hit for 7 points of damage, 1 regular point and all 6 of the temporary points are lost. The material components of this spell are a tiny strip of white cloth with a sticky substance (such as tree sap) on the ends, plus the cleric's holy symbol."
    ),
    Spell('Augury','C',2,
        cast=tp(2,R),
        duration=tp(0),
        sourcebook=V,
        desc="The cleric casting an <i>augury</i> spell seeks to divine whether an action in the immediate future (within 3 turns) will be for the benefit of, or harmful to, the party. The base chance for correctly divining the <i>augury</i> is 70%, plus 1% for each level of the cleric casting the spell, i.e. 71% at 1st level, 72% at 2nd, etc. Your referee will determine any adjustments due for the particular conditions of each <i>augury</i>. For example, assume that a party is considering the destruction of a weird seal which closes a portal. <i>Augury</i> is used to find if weal or woe will be the ultimate result to the party. The material component for <i>augury</i> is a set of gem-inlaid sticks, dragon bones, or similar tokens, or the wet leaves of an infusion which remain in the container after the infused brew is consumed. If the last method is used, a crushed pearl of at least 100 g.p. value must be added to the concoction before it is consumed."
    ),
    Spell('Chant','C',2,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V,
        desc="By means of the <i>chant</i>, the cleric brings into being a special favour upon himself or herself and his or her party, and causes harm to his or her enemies. Once the <i>chant</i> spell is completed, all attacks, damage and saving throws made by those in the area of effect who are friendly to the cleric are at +1, while those of the cleric's enemies are at -1. This bonus/penalty continues as long as the cleric continues to chant the mystic syllables and is stationary. An interruption, however, such as an attack which succeeds and causes damage, grappling the chanter, or a magical <a href=\"/spells/silence-15-radius-cleric-lvl-2/\"><i>silence</i></a>, will break the spell."
    ),
    Spell('Detect Charm','C',2,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V,
        desc="When used by a cleric, this spell will detect whether or not a person or monster is under the influence of a <i>charm</i> spell. Up to 10 creatures can be thus checked before the spell wanes. The reverse of the spell protects from such detection, but only a single creature can be so shielded."
    ),
    Spell('Detect Life','C',2,
        cast=tp(1,R),
        duration=tp(5,R),
        sourcebook=U,
        desc="By the use of this spell, a cleric can tell if a target creature is alive. The magic will <i>detect life</i> in the recipient of a <a href=\"/spells/feign-death-magic-user-lvl-3/\"><i>feign death</i></a> spell, or someone in a coma, deathlike trance, or state of <i>suspended animation</i>. If cast upon the body of a creature that is engaged in <a href=\"/spells/astral-spell-cleric-lvl-7/\"><i>astral travel</i></a>, it will reveal that the creature is alive. The spell works on plants and plant creatures as well as animals. The spell's range is diminished if more than a one-inch thickness of wood or stone lies between the cleric and the subject. Each inch of thickness of a wood or stone barrier is treated as 10 feet of open space. A barrier of metal of any thickness will cause the spell to fail and be ruined. Any form of mental protection, including those of psionic or magical nature, will likewise ruin the spell without anything being detected. The spell will detect the first living creature that lies along the cleric's line of sight (and within range), or else the first creature that crosses the line-of-sight path before the duration expires."
    ),
    Spell('Dust Devil','C',2,
        cast=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell enables a cleric to conjure up a weak air elemental — a <i>dust devil</i> of AC 4, 2 HD, MV 18\", 1 attack for 1-4 points of damage, which can be hit by normal weapons. Magic weapons of any type cause it double damage. The <i>dust devil</i> appears as a small whirlwind 5 feet in diameter at its base, 15 feet tall, and 10 feet across at the top. It will move as directed by the cleric, but will be dispelled if ordered to go farther than 3\" away from the spell caster. The winds of the <i>dust devil</i> can hold a gas cloud or a creature in <i>gaseous form</i> at bay or push it away from the caster (though it cannot damage or dispel such a cloud). Its winds are sufficient to put out torches, small campfires, exposed lanterns, and other small, open flames of non-magical origin. If skimming along the ground in an area of loose dust, sand or ash, the <i>dust devil</i> will pick up these particles and disperse them in a cloud 30 feet in diameter centered around the <i>dust devil</i>. Normal vision is not possible through the cloud, and creatures caught in the cloud will be effectively blinded until one round after they are free of it. Spell casting is virtually impossible for someone caught inside such a cloud or inside the <i>dust devil</i> itself; even if the creature fails to score damage on the victim from the buffeting of its winds, a spell caster must make a saving throw versus spell to keep his or her concentration (and the spell) from being ruined. Any creature native to the Elemental Plane of Air — even another creature of the same sort — can dismiss a <i>dust devil</i> at will from a distance of 3\" or less. Creatures not native to the plane occupied by the spell caster are not affected by the <i>dust devil</i>. It is automatically dispelled if it contacts any creature with innate magic resistance — but not until after it gets a chance to hit and do damage."
    ),
    Spell('Enthrall','C',2,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("A cleric who uses this spell can bind and <i>enthrall</i> an audience that can fully understand his or her language. Listeners of the same race as the cleric are allowed a saving throw versus spell; those of a different race which is generally unfriendly to the cleric's race save at +4. It is impossible to <i>enthrall</i> a character or creature with more than 4 levels or hit dice, or one with a wisdom score greater than 15.\n\n"
            "To effect the spell, the caster must speak without interruption for a full round. Thereafter, the enchantment lasts for as long as the cleric keeps speaking, to a maximum of 6 turns. Those who fail their saving throw will view the cleric as if he or she had a charisma of 21 (loyalty base +70%, reaction adjustment +50%). They will stand and listen to the cleric's words, but will not act on them as if a <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> had been cast. When the cleric stops talking, the spell is broken and the listeners regain control of their own minds. Any form of attack (i.e., a successful hit or the casting of a spell) against the cleric will instantly cancel the <i>enthrall</i> spell, as will any attempt by the cleric to cast a different spell or perform some other action. Members of the audience who make a successful saving throw will view the cleric as having a charisma of 3; they may (50% chance) hoot and jeer, allowing a new saving throw for others listening. If the cleric tries to take undue advantage of the spell by preaching about a religion or alignment opposed to that to which the members of the audience subscribe, each \"offended\" listener is allowed a new saving throw at +5."
        )
    ),
    Spell('Find Traps','C',2,
        cast=tp(5,S),
        duration=tp(3,T),
        sourcebook=V,
        desc="When a cleric casts a <i>find traps</i> spell, all traps — concealed normally or magically — of magical or mechanical <i>nature</i> become visible to him or her. Note that this spell is directional. and the caster must face the desired direction in order to determine if a trap is laid in that particular direction."
    ),
    Spell('Hold Person','C',2,
        cast=tp(5,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell holds immobile, and freezes in places, from 1-3 humans or humanoid creatures (see below) for 5 or more melee rounds. The level of the cleric casting the <i>hold person</i> spell dictates the length of time the effect will last. The basic duration is 5 melee rounds at 1st level, 6 rounds at 2nd level, 7 rounds at 3rd level, etc. If the spell is cast at three persons, each gets a saving throw at the normal score; if only two persons are being enspelled, each makes their saving throw at -1 on their die; if the spell is cast at but one person, the saving throw die is at -2. Persons making their saving throws are totally unaffected by the spell. Creatures affected by a <i>hold person</i> spell are: brownies, dryads, dwarves, elves, gnolls, gnomes, goblins, half-elves, halflings, half-orcs, hobgoblins, humans, kobolds, lizard men, nixies, orcs, pixies, sprites, and troglodytes. The spell caster needs a small, straight piece of iron as the material component of this spell."
    ),
    Spell('Holy Symbol','C',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=U,
        desc="This spell is used to prepare a cleric's holy symbol, or to create a new symbol to replace a lost or damaged one. The new symbol-to-be, which is the spell's material component (and obviously is not consumed in the casting), must be crafted of appropriate material depending on the religion/deity in question, and must be of the proper shape and design — a cleric cannot pick up just any item and make it into a holy symbol. A cleric may posess two holy symbols at one time, and this spell can be used to create a second one as a spare. No cleric can create a holy symbol related to a religion or deity other than the one that he or she worships. The holy symbol of a good or evil cleric will radiate a faint aura of good or evil, but it is not a magical item <i>per se</i>. The holy symbol of a cleric who is of neutral morals (with respect to good and evil) will have no such aura."
    ),
    Spell('Know Alignment','C',2,
        cast=tp(1,R),
        duration=tp(1,T),
        sourcebook=V,
        desc="A <i>know alignment</i> spell enables the cleric to exactly read the aura of a person — human, semi-human, or non-human. This will reveal the exact alignment of the person. Up to 10 persons can be examined with this spell. The reverse totally obscures alignment, even from this spell, of a single person for 1 turn, two persons for 5 rounds, etc. Certain magical devices will negate the ability to <i>know alignment</i>."
    ),
    Spell('Messenger','C',2,
        cast=tp(1,R),
        duration_lvl=tp(1,H),
        sourcebook=U,
        desc="This spell enables the cleric to call upon a small (size S) creature of at least <i>animal</i> intelligence to act as his or her <i>messenger</i>. The spell does not affect creatures that are \"giant\" types, and it will not work on creatures with an intelligence score of 4 or higher, or with a rating of <i>low</i> intelligence or better (whichever applies). If the creature is already within range, the cleric, using some type of food desirable to the animal as a lure, can call the animal to come. The animal is allowed a saving throw versus spell, and if this succeeds the spell fails. If the saving throw is failed, the animal will advance toward the cleric and await his or her bidding. The cleric can communicate with the animal in a crude fashion, telling it to go to a certain place, but directions must be simple. The spell caster can attach some small item or note to the animal. If so instructed, the animal will then wait at that location until the duration of the spell expires. (Note that unless the intended recipient of a message is expecting a <i>messenger</i> in the form of a small animal or bird, the carrier may be ignored.) When the spell's duration expires, the animal or bird will return to its normal activities. The intended reciever of a message gains no communication ability."
    ),
    Spell('Resist Fire','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is placed upon a creature by a cleric, the creature's body is toughened to withstand heat, and boiling temperature is comfortable. The recipient of the <i>resist fire</i> spell can even stand in the midst of very hot or magical fires such as those produced by red-hot charcoal, a large amount of burning oil, flaming swords, <a href=\"/spells/fire-storm-druid-lvl-7/\"><i>fire storms</i></a>, <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fire balls</i></a>, <a href=\"/spells/meteor-swarm-magic-user-lvl-9/\"><i>meteor swarms</i></a>. or red dragon's breath — but these will affect the creature, to some extent. The recipient of the spell gains a bonus of +3 on saving throws against such attack forms, and all damage sustained is reduced by 50%; therefore, if the saving throw is not made, the creature sustains one-half damage, and if the saving throw is made only one-quarter damage is sustained. Resistance to fire lasts for 1 turn for each level of experience of the cleric placing the spell. The caster needs a drop of mercury as the material component of this spell."
    ),
    Spell('Silence 15\' Radius','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Upon casting this spell, complete silence prevails in the area of its effect. All sound is stopped, so all conversation is impossible, spells cannot be cast and no noise whatsoever issues forth. The spell can be cast into the air or upon an object. The spell of <i>silence</i> lasts for 2 rounds for each level of experience of the cleric, i.e. 2 rounds at 1st level, 4 at 2nd, 6 at 3rd, 8 at 4th and so forth. The spell can be cast upon a creature, and the effect will then radiate from the creature and move as it moves. If the creature is unwilling, it saves against the spell, and if the saving throw is made, the spell effect locates about one foot behind the target creature."
    ),
    Spell('Slow Poison','C',2,
        cast=tp(1,S),
        duration=tp(0),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="When this spell is placed upon a poisoned individual it greatly slows the effects of any venom, even causing a supposedly dead individual to have life restored if it is cast upon the victim within a number of turns less than or equal to the level of experience of the cleric after the poisoning was suffered, i.e. a victim poisoned up to 10 turns previously could be temporarily saved by a 10th or higher level cleric who cast <i>slow poison</i> upon the victim. While this spell does not neutralize the venom, it does prevent it from substantially harming the individual for the duration of its magic, but each turn the poisoned creature will lose 1 hit point from the effect of the venom (although the victim will never go below 1 hit point while the <i>slow poison</i> spell's duration lasts). Thus, in the example above, the victim poisoned 10 turns previously has only 10 hit points, so when the 10th level cleric casts the spell, the victim remains with 1 hit point until the spell duration expires, and hopefully during that period a full cure can be accomplished. The material components of this spell are the cleric's holy/unholy symbol and a bud of garlic which must be crushed and smeared on the victim's bare feet."
    ),
    Spell('Snake Charm','C',2,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When this spell is cast, a hypnotic pattern is set up which causes one or more snakes to cease all activity except a semi-erect postured swaying movement. If the snakes are charmed while in a torpor, the duration of the spell is 3 to 6 turns (d4 + 2); if the snakes are not torpid, but are not aroused and angry, the charm lasts 1 to 3 turns; if the snakes are angry and/or attacking, the <i>snake charm</i> spell will last from 5 to 8 melee rounds (d4+4). The cleric casting the spell can charm snakes whose hit points are less than or equal to those of the cleric. On the average, a 1st level cleric could charm snakes with a total of 4 or 5 hit points; a 2nd level cleric 9 hit points, a 3rd level 13 or 14 hit points, etc. The hit points can represent a single snake or several of the reptiles, but the total hit points cannot exceed those of the cleric casting the spell."
    ),
    Spell('Speak With Animals','C',2,
        cast=tp(5,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By employing this spell, the cleric is empowered to comprehend and communicate with any warm or cold-blooded animal which is not mindless (such as an amoeba). The cleric is able to ask questions, receive answers, and generally be on amicable terms with the animal. This ability lasts for 2 melee rounds for each level of experience of the cleric employing the spell. Even if the bent of the animal is opposite to that of the cleric (evil/good, good/evil), it and any others of the same kind with it will not attack while the spell lasts. If the animal is neutral or of the some general bent as the cleric (evil/evil, good/good), there is a possibility that the animal, and its like associates, will do some favour or service for the cleric. This possibility will be determined by the referee by consulting a special reaction chart, using the charisma of the cleric and his actions as the major determinants. Note that this spell differs from <a href=\"/spells/speak-with-monsters-cleric-lvl-6/\"><i>speak with monsters</i></a>, for it allows conversation only with basically normal, non-fantastic creatures such as apes, bears, cats, dogs, elephants, and so on."
    ),
    Spell('Spiritual Hammer','C',2,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By calling upon his or her deity, the cleric casting a <i>spiritual hammer</i> spell brings into existence a field of force which is shaped vaguely like a hammer. This area of force is hammer-sized, and as long as the cleric who invoked it concentrates upon the <i>hammer</i>, it will strike at any opponent within its range as desired by the cleric. The force area strikes as a magical weapon equal to one plus per 3 levels of experience of the spell caster for purposes of being able to strike creatures, although it has no magical plusses whatsoever \"to hit\", and the damage it causes when it scores a hit is exactly the same as a normal war hammer, i.e. 1-6 versus opponents of man-size or smaller, 1-4 upon larger opponents. Furthermore, the hammer strikes at exactly the same level as the cleric controlling it, just as if the cleric was personally wielding the weapon. As soon as the cleric ceases concentration, the <i>spiritual hammer</i> is dispelled. <i>Note:</i> If the cleric is behind an opponent, the force can strike from this position, thus gaining all bonuses for such an attack and negating defensive protections such as shield and dexterity. The material component of this spell is a normal war hammer which the cleric must hurl towards opponents whilst uttering a plea to his or her deity. The hammer disappears when the spell is cast."
    ),
    Spell('Withdraw','C',2,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="By means of a <i>withdraw</i> spell, the cleric effectively alters the flow of time with regard to himself or herself. While but 1 segment of time passes for those not affected by the spell, the cleric is able to spend 1 round of time in contemplation. The base spell duration is 2 segments (2 rounds, from the cleric's point of view), and the cleric adds 1 additional increment of time for each level of experience he or she possesses. Thus, at 5th level of experience, the spell caster could spend up to 6 rounds cogitating on some matter while but 6 segments of time passed for all others. (The DM must allow the spell caster 1 minute of real time per segment to ponder some problem or question. No discussion with non-affected characters is permitted.) Note that while affected by a <i>withdraw</i> spell, the cleric can perform only these particular acts: the casting of an <a href=\"/spells/augury-cleric-lvl-2/\"><i>augury</i></a> spell, any curing or healing spells, or any informational spells — and all such spells can only be cast upon the cleric himself or herself. The casting of any of these spells in a different fashion (e.g. a <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> bestowed upon a companion) will cause the magic of the <i>withdraw</i> spell to cease. Similarly, the cleric who is affected by the <i>withdraw</i> spell cannot walk or run, become <i>invisible</i>, or otherwise engage in actions othen than thinking, reading, and the like. The <i>withdrawn</i> cleric can be affected by the actions of the others while under the influence of this spell, and any attack upon the cleric which succeeds will break the spell."
    ),
    Spell('Wyvern Watch','C',2,
        cast=tp(5,S),
        duration=tp(8,H),
        sourcebook=U,
        desc="This spell is known as <i>wyvern watch</i> because of the insubstantial haze brought forth by its casting, which vaguely resembles a wyvern. It is typically used to guard some area against intrusion. Any creature that approaches within 1\" of the area in question is subject to attack from the spell force. The \"wyvern\" will strike, and any creature so attacked must make its saving throw versus spell or else stand <i>paralyzed</i> for 1 round per level of the caster, or until freed by the spell caster, by a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell, or by a <a href=\"/spells/remove-paralysis-cleric-lvl-3/\"><i>remove paralysis</i></a> spell. A successful saving throw indicates that the target creature was missed by the attack of the wyvern-form and the spell remains in place. As soon as a target creature is successfully struck by the wyvern-form, the <i>paralysis</i> takes effect and the force of the spell itself is dissipated. The spell force will likewise dissipate if no intruder is struck by the wyvern-form for 8 hours after the spell is cast. Any creature approaching the space being guarded by the wyvern-form may be able to detect its presence before coming close enough to be attacked; this chance of detection is 90% in bright light, 30% in twilight conditions, and 0% in darkness. The material component is the cleric's holy/unholy symbol."
    ),
    Spell('Animate Dead','C',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell creates the lowest of the <i>undead</i> monsters, skeletons or zombies, from the bones or bodies of dead humans. The effect is to cause these remains to become animated and obey the commands of the cleric casting the spell. The skeletons or zombies will follow, remain in an area and attack any creature (or just a specific type of creature) entering the place, etc. The spell will animate the monsters until they are destroyed or until the magic is dispelled. (See <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell). The cleric is able to animate 1 skeleton or 1 zombie for each level of experience he or she has attained. Thus, a 2nd level cleric can animate 2 of these monsters, a 3rd level 3, etc. The act of animating dead is not basically a good one, and it must be used with careful consideration and good reason by clerics of good alignment. It requires a drop of blood, a piece of human flesh, and a pinch of bone powder or a bone shard to complete the spell."
    ),
    Spell('Cloudburst','C',3,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U,
        desc=("By means of this spell the caster causes the atmosphere to instantly precipitate all of its water vapor in the form of huge drops of rain, the resulting condensation not only causing a true downburst of rain but also sucking more vapor into the area to likewise be precipitated. The <i>cloudburst</i> will effectively drench everything in its area of effect within 1 segment, for its rain will fall at the rate of 1/10 inch per segment, or 1 inch rainfall in 1 round. All normal fires within the area of effect will be extinguished by a <i>cloudburst</i> — small ones instantly, medium-sized ones in 3-5 segments, and large-sized ones in 8-10 segments. Magical fires will also be extinguished by a <i>cloudburst</i>, with the following general rules applying:\n\n"
            "Permanent magical fires will re-light in 1-2 rounds. Small rekindlable magical fires such as that of a <i>flame tongue</i> sword will be affected only during the actual <i>cloudburst</i>.\n\n"
            "Spells such as <a href=\"/spells/produce-fire-druid-lvl-4/\"><i>produce fire</i></a> and <a href=\"/spells/burning-hands-magic-user-lvl-1/\"><i>burning hands</i></a> will be negated. Large-area spells such as <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, <a href=\"/spells/flame-strike-cleric-lvl-5/\"><i>flame strike</i></a>, <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a>, etc., will, in the course of being extinguished, vaporize the rain into a cloud of steam covering an area four times as large as the spell's area of effect (i.e., a cylinder of up to 12\" in diameter and as much as 24\" high). This steam will inflict 1-3 points of damage per round on normal creatures within its area, and will do twice that damage to cold-dwelling or cold-using creatures. The cloud of steam will persist for 2-5 rounds, half that if a breeze is blowing, or only 1 round if a strong wind is blowing.\n\n"
            "In arid regions, the <i>cloudburst</i> will act only as a double-strength <i>precipitation</i> spell. In hot and humid areas, the duration of the spell will be extended to 2 rounds. In areas with a temperature between 33° and 31°F inclusive, sleet rather than rain will fall, with ice and slush being formed when it accumulates. In temperatures of 30°F and lower, the <i>cloudburst</i> becomes a <i>snowburst</i>, with one inch of snow per segment falling. The material components for the spell are powdered silver and powdered iodine crystals, plus the cleric's holy symbol."
        )
    ),
    Spell('Continual Light','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is similar to a <a href=\"/spells/light-cleric-lvl-1/\"><i>light</i></a> spell, except that it lasts until negated (by a <i>continual darkness</i> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell) and its brightness is very great, being nearly as illuminating as full daylight. It can be cast into air, onto an object, or at a creature, In the third case, the <i>continual light</i> affects the space about one foot behind the creature if the latter makes its saving throw. Note that this spell will blind a creature if it is successfully cast upon the visual organs, for example. Its reverse causes complete absence of light."
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
        desc="By touching the creature afflicted, the cleric employing the spell can permanently cure most forms of blindness. Its reverse, <i>cause blindness</i>, requires a successful touch upon the victim, and if the victim then makes the saving throw, the effect is negated."
    ),
    Spell('Cure Disease','C',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="The cleric cures most diseases — including those of a parasitic, bacterial, or viral nature — by placing his or her hand upon the diseased creature. The affliction rapidly disappears thereafter, making the cured creature whole and well in from 1 turn to 1 week, depending on the kind of disease and the state of its advancement when the cure took place. The reverse of the <i>cure disease</i> spell is <i>cause disease</i>. To be effective. the cleric must touch the intended victim, and the victim must fail the saving throw. The disease caused will begin to affect the victim in 1-6 turns, causing the afflicted creature to lose 1 hit point per turn, and 1 point of strength per hour, until the creature is at 10% of original hit points and strength, at which time the afflicted is weak and virtually helpless."
    ),
    Spell('Death\'s Door','C',3,
        cast=tp(5,S),
        duration_lvl=tp(1,H),
        sourcebook=U,
        desc="When a cleric employs this spell, he or she touches a human or demi-human who is unconscious and \"at death's door\" (-1 to -9 hit points). The spell immediately brings the individual to 0 hit points. While the individual remains unconscious, bleeding and deterioration are stopped for the duration of the <i>death's door</i> spell. The subject, because of being treated by the spell and now being at 0 hit points, can be brought to consciousness, and have hit points restored, by means of <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a>, <a href=\"/spells/cure-serious-wounds-cleric-lvl-4/\"><i>cure serious wounds</i></a>, etc., potions such as <i>healing</i> or <i>extra-healing</i>, or clerical or other items which magically restore lost hit points. The material components of the spell are the cleric's holy/unholy symbol, a bit of white linen, and any form of unguent."
    ),
    Spell('Dispel Magic','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a cleric casts this spell, it neutralizes or negates the magic it comes in contact with as follows: A <i>dispel magic</i> will not affect a specially enchanted item such as a scroll, magic ring, wand, rod, staff, miscellaneous magic item, magic weapon, magic shield, or magic armor. It will destroy magic potions (they are treated as 12th level for purposes of this spell), remove spells cast upon persons or objects, or counter the casting of spells in the area of effect. The base chance for success of a <i>dispel magic</i> spell is 50%. For every level of experience of the character casting the <i>dispel magic</i> above that of the creature whose magic is to be dispelled (or above the efficiency level of the object from which the magic is issuing), the base chance increases by 5%, so that if there are 10 levels of difference, there is a 100% chance. For every level below the experience/efficiency level of the creature/object, the base chance is reduced by 2%. Note that this spell can be very effective when used upon <i>charmed</i> and similarly beguiled creatures. It is automatic in negating the spell caster's own magic."
    ),
    Spell('Feign Death','C',3,
        cast=tp(2,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level magic-user spell, <a href=\"/spells/feign-death-magic-user-lvl-3/\"><i>feign death</i></a>. Note that a character of any level may be affected by the cleric casting this spell, and that the material components are a pinch of graveyard dirt and the cleric's holy/unholy symbol."
    ),
    Spell('Flame Walk','C',3,
        cast=tp(5,S),
        duration=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="By means of this spell the caster is able to empower himself or herself, or another creature of man-size and comparable mass, to withstand non-magical fires up to temperatures of 2,000°F. It also confers a +2 bonus to saving throws against magical fires. For every level of experience above the minimum required to create the dweomer (5th), the caster can affect an additional man-sized creature. This growing power enables multiple individuals, or one or more of greater than man-size and mass, to be affected by the <i>flame walk</i> spell. For instance, an 11th-level caster could empower both himself or herself and a steed such as a horse to move in molten lava. (Consider a horse to be equivalent to 6 humans for purposes of this spell; conversely, halfling-sized creatures count as ½ human apiece, and pixie-sized creatures are considered equivalent to ¼ human each.) The material components of the spell are at least 500 gp of powdered ruby and the cleric's holy/unholy symbol."
    ),
    Spell('Glyph of Warding','C',3,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="A <i>glyph of warding</i> is a powerful inscription magically drawn to prevent unauthorized or hostile creatures from passing, entering, or opening. It can be used to guard a small bridge, ward an entry, or as a trap on a chest or box. When the spell is cast, the cleric weaves a tracery of faintly glowing lines around the warding sigil. For every square foot of area to be protected, 1 segment of time is required to trace the warding lines from the glyph, plus the initial segment during which the sigil itself is traced. A maximum of a 5' X 5' area per level can be warded. When the spell is completed, the glyph and tracery become invisible, but any creature touching the protected area without first speaking the name of the glyph the cleric has used to serve as a ward will be subject to the magic it stores. Saving throws apply, and will either reduce effects by one-half or negate them according to the glyph employed. The cleric must use incense to trace this spell, and then sprinkle the area with powdered diamond (at least 2,000 g.p. worth) if it exceeds 50 square feet. Typical glyphs shock for 2 points of electrical damage per level of the spell caster, explode for a like amount of fire damage, paralyze, blind, or even drain a life energy level (if the cleric is of high enough level to cast this glyph)."
    ),
    Spell('Locate Object','C',3,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell aids in location of a known or familiar object. The cleric casts the spell, slowly turns, and knows when he or she is facing in the direction of the object to be located, provided the object is within range, i.e. 7\" for 1st level clerics, 8\" for 2nd, 9\" for 3rd, etc. The casting requires the use of a piece of lodestone. The spell will locate such objects as apparel, jewellery, furniture, tools, weapons, or even a ladder or stairway. By reversal (<i>obscure object</i>), the cleric is able to hide an object from location by spell, crystal ball, or similar means. Neither application of the spell will affect a living creature."
    ),
    Spell('Magical Vestment','C',3,
        cast=tp(1,R),
        duration_lvl=tp(6,R),
        sourcebook=U,
        desc="This spell enchants the caster's vestment, providing protection equivalent to armor. It will only function while the cleric is on ground <i>consecrated</i> to his or her deity (cf. 1st-level <a href=\"/spells/ceremony-cleric-lvl-1/\"><i>ceremony</i></a> spell). If any armor or protective device is worn during the spell duration, the vestment protects as if normal chain mail armor. If no other protection is worn, the vestment also gains a +1 enchantment for each four levels of the cleric, to a maximum effect of chain mail +4 (base AC 1). The magic lasts for 6 rounds per level of the caster, or until the caster loses consciousness or leaves the <i>consecrated</i> area. The material components are the vestment to be enchanted and the cleric's holy symbol."
    ),
    Spell('Meld Into Stone','C',3,
        cast=tp(7,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="The magic of this spell, when properly cast, allows the cleric to meld his or her body and possessions worn or carried into a large stone. To effect the spell, the cleric stands next to the stone to be melded into (which must be large enough to accomodate the cleric's body in all three dimensions) while holding a small sample of the same type of stone. When casting is complete, the cleric and up to 100 pounds of his or her non-living gear blend into the stone. Magical artifacts and relics are not affected by the spell. If the dimensions of the stone are not sufficient, or if the cleric is wearing and carrying more than 100 pounds of gear, the spell will fail and be wasted. The magic lasts for 9-16 (1d8 + 8) rounds, the variable part of the duration rolled secretly by the DM. At any time before the duration expires, the cleric can step out of the stone along the same surface that he or she used to enter it (i.e., the spell does not allow movement through the stone such as would a <a href=\"/spells/passwall-magic-user-lvl-5/\"><i>passwall</i></a> or <a href=\"/spells/phase-door-magic-user-lvl-7/\"><i>phase door</i></a> spell). If the duration runs out before the cleric exits the stone, then he or she will be expelled from the stone and take 4-32 (4d8) points of damage — and each piece of gear affected must save versus petrification or turn to stone. While in the stone, the cleric is aware of the passage of time; however, he or she cannot see or hear anything that may be going on around the stone. The following spells will harm the cleric if cast upon the stone that he or she is occupying: <a href=\"/spells/stone-to-flesh-magic-user-lvl-6/\"><i>stone to flesh</i></a> will expel the cleric and inflict 4-32 points of damage, but items carried need not save. <a href=\"/spells/stone-shape-magic-user-lvl-5/\"><i>Stone shape</i></a> will cause 4-16 (4d4) points of damage, but will not expel the cleric. <a href=\"/spells/transmute-rock-to-mud-druid-lvl-5/\"><i>Transmute rock to mud</i></a> expels the cleric and will slay the victim instantly unless he or she makes a succussful saving throw versus spell."
    ),
    Spell('Negative Plane Protection','C',3,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="This spell enables the caster or any other eligible creature touched to be partially protected from an undead monster that has an existence on the Negative Material Plane (such as a shadow, wight, wraith, spectre, or vampire). The dweomer of the spell opens a channel to the Positive Material Plane, the energy from which helps to offset the effect of the undead creature's attack. The recipient is allowed a saving throw versus death magic if he or she is touched (attacked) by an undead creature. Success indicates that the recipient takes normal hit-point damage from the attack, but does not suffer the drain of experience that would otherwise take place. In addition, the undead creature takes 2-12 (2d6) hit points of damage from the Positive Plane energy. The magic is only proof against one such attack, and dissipates after that attack whether or not the saving throw is successful. If the saving throw versus death magic is failed, the recipient of the spell takes double the usual physical damage in addition to the loss of experience that normally occurs. The spell will also protect the recipient from the effect of a magic-user's <a href=\"/spells/energy-drain-magic-user-lvl-9/\"><i>energy drain</i></a> spell, but in such a case the magic-user is not affected. The contact between the Positive and Negative Planes that this spell brings about will cause a bright flash of light and sound like that of a thunderclap, but these phenomena do not cause damage in any event. The protection will last for 1 turn per level of the cleric casting the spell, or until the recipient is successfully attacked by an undead monster. This spell cannot be cast on the Negative Material Plane."
    ),
    Spell('Prayer','C',3,
        cast=tp(6,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell exactly duplicates the effects of a <a href=\"/spells/chant-cleric-lvl-2/\"><i>chant</i></a> with regard to bonuses of +1 for friendly attacks and saving throws and -1 on like enemy dice. However, once the <i>prayer</i> is uttered, the cleric can do other things, unlike a <a href=\"/spells/chant-cleric-lvl-2/\"><i>chant</i></a> which he or she must continue to make the spell effective. The cleric needs a silver holy symbol, prayer beads, or a similar device as the material component of this spell."
    ),
    Spell('Remove Curse','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Upon casting this spell, the cleric is usually able to remove a curse — whether it be on an object, a person, or in the form of some undesired sending or evil presence. Note that the <i>remove curse</i> spell will not affect a cursed shield, weapon or suit of armor, for example, although the spell will typically enable the person afflicted with any such cursed item to be rid of it. The reverse of the spell is <i>not</i> permanent; the <i>bestow curse</i> lasts for 1 turn for every level of experience of the cleric using the spell. It will lower one ability of the victim to 3 (your DM will determine which by random selection) 50% of the time; reduce the victim's \"to hit\" and saving throw probabilities by -4 25% of the time; or make the victim 50% likely per turn to drop whatever he, she, or it is holding (or simply do nothing in the case of creatures not using tools) 25% of the time. It is possible for a cleric to devise his or her own curse, and it should be similar in power to those shown. Consult your referee. The target of a <i>bestow curse</i> spell must be touched. If the victim is touched, a saving throw is still applicable; and if it is successful, the effect is negated."
    ),
    Spell('Remove Paralysis','C',3,
        cast=tp(6,S),
        duration=tp(1,P),
        duration_lvl=tp(0),
        sourcebook=U,
        desc=("By the use of this spell, the cleric can free the subject creature(s) from the effects of paralyzation or similar forces (such as a <a href=\"/spells/hold-monster-magic-user-lvl-5/\"><i>hold</i></a> spell). By casting this spell and then pointing his or her finger in the proper direction, the cleric can <i>remove paralysis</i> from as many as 4 creatures that are within range and within the area of affect. There must be no physical or magical barrier between the caster and the creature(s) to be affected, or else the spell will fail and be wasted. Each target of the spell obtains a new saving throw versus paralyzation, at a +3 bonus if only one creature is involved, +2 if two creatures are to be affected, and +1 if three or four creatures are the target.\n\n"
            "The reverse of the spell, <i>cause paralysis</i>, can affect only one target, which must be touched by the cleric (successful roll \"to hit\") using his or her holy/unholy symbol. If the victim fails a saving throw versus spell, paralyzation will set in for a duration of 1-6 rounds plus 1 round per level of the caster. Clerics of good alignment should be very discerning in their use of <i>cause paralysis</i>, and this spell might actually be prohibited to clerics belonging to certain good-aligned orders."
        )
    ),
    Spell('Speak With Dead','C',3,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("Upon casting a <i>speak with the dead</i> spell, the cleric is able to ask several questions of a dead creature in a set period of time and receive answers according to the knowledge of that creature. Of course, the cleric must be able to converse in the language which the dead creature once used. The length of time the creature has been dead is a factor, since only higher level clerics can converse with the long-dead. Likewise, the number of questions which can be answered and the length of time in which the questions can be asked are dependent upon the level of experience of the cleric. The cleric needs a holy symbol and burning incense in order to cast this spell upon the body, remains, or portion thereof.\n\n"
            "<table>"
            "<tr>"
            "<th>Level of Experience</th>"
            "<th>Maximum Length of Time Dead</th>"
            "<th>Time Questioned</th>"
            "<th>Number of Questions</th>"
            "</tr>"
            "<tr><td>up to 7th</td><td>1 week</td><td>1 round</td><td>2</td></tr>"
            "<tr><td>7th—8th</td><td>1 month</td><td>3 rounds</td><td>3</td></tr>"
            "<tr><td>9th—12th</td><td>1 year</td><td>1 turn</td><td>4</td></tr>"
            "<tr><td>13th—15th</td><td>10 years</td><td>2 turns</td><td>5</td></tr>"
            "<tr><td>16th—20th</td><td>100 years</td><td>3 turns</td><td>6</td></tr>"
            "<tr><td>21st and up</td><td>1,000 years</td><td>6 turns</td><td>7</td></tr>"
            "</table>"
        )
    ),
    Spell('Water Walk','C',3,
        cast=tp(7,S),
        duration=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="By means of this spell, the caster is able to empower himself or herself or another creature of man-size and comparable mass to tread upon water as if it were firm, grassy ground (cf. <i>ring of water walking</i>). For every level of the caster above the minimum required to create the dweomer (5th level), he or she can affect an additional man-sized creature. This growing power enables multiple individuals, or one or more of greater size and mass, to be affected by the <i>water walk</i> spell. For instance, an 11th-level caster could additionally affect a horse, so that he or she could move atop the waves while mounted. (Consider a horse to be equivalent to 6 humans for purposes of this spell.) The material components for this spell are a piece of cork and the cleric's holy/unholy symbol."
    ),
    Spell('Abjure','C',4,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U,
        desc=("When a cleric employs a spell of this sort, he or she is attempting to return a creature from another plane of existence to its own plane. The exact name of the type of creature to be affected by the <i>abjure</i> spell must be known. If the creature also has a specific (proper) name, then that too must be known and used. The naming cleric then compares his or her level against the level or hit dice of the creature under <i>abjuration</i>, in the same way that the success of a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell is determined (base 50% chance of success, plus or minus the level/HD difference between the caster and the creature to be affected). The percent chance for success is then compared to a percentile dice roll. If the roll is equal to or less than the chance to abjure, the creature is instantly sent back to its own plane. In all other cases the spell fails. (The creature might not wish to remain on the caster's plane, and in such a case it could be appreciative of the cleric's attempt to return it to its home.)\n\n"
            "The reverse of the spell, <i>implore</i>, entreats some like-aligned creature from another plane to come to the cleric casting the spell. Success must be determined just as if <i>abjure</i> had been cast. In like vein, the spell caster must know the exact name of the type of creature as well as its given name, if any. If the <i>implore</i> spell succeeds, the cleric has absolutely no guarantee that the creature summoned from another plane will be favorably disposed to him or her. Neither version of the spell will function upon deities, but might affect servants or minions thereof.\n\n"
            "The material components for an <i>abjure</i> spell are a holy/unholy symbol, holy or unholy water, and often some material inimical to the creature. In reversed form, the material components are the same except for the last, which must be something that the <i>implored</i> creature craves or respects."
        )
    ),
    Spell('Cloak of Fear','C',4,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc=("The casting of this spell empowers the cleric to radiate a personal aura of <i>fear</i> out to a 3' radius. Any character or creature that intrudes upon this aura must save versus spell or run away in fear for 6 rounds (cf. 4th-level magic-user spell <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a>). The spell will only remain in effect until one creature fails to save, whereupon the dweomer of the spell is dissipated. The spell has no effect upon creatures that themselves radiate <i>fear</i>, or upon undead creatures of any sort, and it is not dissipated upon contact by such creatures. It likewise remains in effect if an intruder makes a successful saving throw, but will expire after a duration of 1 turn per level of the cleric if not brought down earlier. Note that members of the cleric's party are not immune to the effects of the spell. The cleric may cancel the aura at any time before the duration ends if desired.\n\n"
            "The reverse of the spell, <i>cloak of bravery</i>, can be cast upon the cleric or upon another creature which is a willing recipient. A character or creature protected by a <i>cloak of bravery</i> gains a +3 bonus to the saving throw against any form of magical <i>fear</i> encountered. The magic of the <i>cloak of bravery</i> works only once and only upon a single figure, and is dispelled whether or not the recipient succeeds on his or her saving throw. The magic does not negate or otherwise affect the innate ability of a creature (such as a devil) to radiate <i>fear</i>, so that the creature can still affect others in the vicinity.\n\n"
            "The material components for a <i>cloak of fear</i> are a miniature quiver and a chicken feather; for a <i>cloak of bravery</i>, the necessary items are a drop of alcohol and the brain of a newt."
        )
    ),
    Spell('Cure Serious Wounds','C',4,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is a more potent version of the <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> spell. Upon laying his or her hand upon a creature, the cleric causes from 3 to 17 (2d8+1) hit points of wound or other injury damage to the creature's body to be healed. This healing will affect only those creatures listed in the <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> spell explanation. <i>Cause serious wounds</i>, the reverse of the spell, operates similarly to the <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cause light wounds</i></a> spell, the victim having to be touched first, and if the touch is successful, it will inflict 3 to 17 hit points."
    ),
    Spell('Detect Lie','C',4,
        cast=tp(7,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When the cleric employs this spell, the recipient is immediately able to determine if truth is being spoken. The spell lasts one round for each level of experience of the cleric casting the <i>detect lie</i>. Gold dust is necessary for this spell. Its reverse, <i>undetectable lie</i>, makes bald-face untruths seem reasonable, or simply counters the <i>detect lie</i> spell powers. The reverse spell requires brass dust as its material component."
    ),
    Spell('Divination','C',4,
        cast=tp(1,T),
        duration=tp(0,R),
        sourcebook=V,
        desc="Similar to an <a href=\"/spells/augury-cleric-lvl-2/\"><i>augury</i></a> spell, a <i>divination</i> spell is used to determine information regarding an area. The area can be a small woods, large building, or section of a dungeon level. In any case, its location must be known. The spell gives information regarding the relative strength of creatures in the area: whether a rich, moderate or poor treasure is there; and the relative chances for incurring the wrath of evil or good supernatural, super powerful beings if the area is invaded and attacked. The base chance for correct <i>divination</i> is 60%, plus 1% for each level of experience of the cleric casting the spell, i.e. 65% at 5th level, 66% at 6th, etc. The Dungeon Master will make adjustments to this base chance considering the facts regarding actual area being divined. If the result is not correct, inaccurate information will be obtained. The material components of the Divination are a sacrificial creature, incense, and the holy symbol of the cleric. If an unusually potent <i>divination</i> is attempted, sacrifice of particularly valuable gems or jewellery and/or magic items may be required."
    ),
    Spell('Exorcise','C',4,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="The spell of <i>exorcism</i> will negate possession of a creature or an object by any outside or supernatural force. This includes control of a creature by some force in an object, possession by <a href=\"/spells/magic-jar-magic-user-lvl-5/\"><i>magic jar</i></a> spell, demonic possession, curse and even charm, for the <i>exorcise</i> spell is similar to a <i>dispel magic</i> spell. Furthermore, it will affect a magical item if such is the object of the exorcism. Thus a soul object of any sort which comes under successful exorcism will make the life force of the creature concerned wholly inhabit its nearest material body, wholly and completely. (Cf. ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL, Demon.) The <i>exorcise</i> spell, once begun, cannot be interrupted, or else it is spoiled and useless. The base chance for success is a random 1% to 100%. Each turn of exorcism the dice are rolled, and if the base chance number, or less, is rolled, the spell is successful. Base chance of success is modified by -1% for each level of difference between the cleric's level of experience and the level of the possessor or possessing magic, where the smaller number is the cleric's level. In the obverse, a +1% cumulative is added. The referee can determine base chance according to the existing circumstances if he or she so desires. Material components for this spell are the holy object of the cleric and holy water (or unholy, in the case of evil clerics, with respect to object and water). A religious artifact or relic can increase the chance of success by from 1% to 50%, according to the power of the artifact or relic."
    ),
    Spell('Giant Insect','C',4,
        cast=tp(1,VA),
        duration_lvl=tp(2,R),
        sourcebook=U,
        desc=("By means of this spell, the cleric can turn one or more normal-sized insects into larger forms which resemble the \"giant\" forms of such creatures as described in the Monster Manual books or the FIEND FOLIO® Tome. The number of insects that can be affected is dependent upon the cleric's level: one at 7th-9th level, two at 10th or 11th level, three at 12th or 13th level, and four at 14th or higher level. The magic only works upon one type of insect at one time; i.e., a cleric cannot use the same casting of the spell to affect both an ant and a fly. The casting time for a <i>giant insect</i> spell is one round per hit die of the resulting giant creature(s); if the casting is interrupted for any reason, the subject insect(s) will die and the spell will be ruined. A monster created by this spell will have as many attacks per round as its namesake, but will not do full damage unless the created form has as many hit dice as the usual giant version of the same insect. Although it may have more hit dice than a standard giant form, the created insect can never exceed the damage figures given in the books. <i>Example</i>: A cleric of 14th level can use the <i>giant insect</i> spell to enlarge a normal wasp to one having 6 HD (instead of the usual 4 HD for a giant wasp; see Monster Manual), but the creature would still do damage of 2-8/1-4. Conversely, a 7th-level cleric can use this spell to create a giant wasp of 3 HD, and such a creature would have reduced damage figures of 2-6/1-3 — three-fourths of the damage potential of a \"real\" giant wasp, since it only has three-fourths of the usual number of hit dice for such a creature.\n\n"
            "The spell will only work on actual insects. Arachnids, crustaceans, and other types of small creatures are not affected. The <i>giant insects</i> created will not have any special attacks or defenses possessed by the standard giant forms; however, armor class, movement rate, and other physical characteristics are as described in the creature's book listing. Any <i>giant insects</i> created by this spell will not attempt to harm the cleric, but the cleric's control of such creatures is limited. He or she could give them simple commands such as \"attack\", \"defend\", \"guard\", and so forth, but could not instruct them to attack a certain creature or guard against a particular occurence. Unless commanded to do otherwise, the <i>giant insects</i> will attemp to attack whomever or whatever is near them.\n\n"
            "The reverse of the spell, <i>shrink insect</i>, will reduce the size of standard giant insects as well as those created by the unreversed form of the spell. The shrinking will be at a rate of 1 HD for every 4 levels of the casting cleric, with a maximum of 6 HD of reduction (to a minimum of ⅛ HD, or 1 hp). Special attacks possessed by a standard giant insect will be retained, but at a weaker level which allows a bonus to the saving throw versus the attack. For instance, a 9th-level cleric could cast <i>shrink insect</i> upon a standard giant wasp to reduce it form 4 HD to 1 HD. The resulting insect would still be able to use its poison string, but the saving throw against such an attack would be at a +3 bonus (or perhaps higher), and the hit-point damage from its normal attacks would be reduced to 1-2 for a bite and 1 point for a sting — one-fourth of the usual amounts, since the creature is only one-fourth of its original size. The material component for either version of the spell is the cleric's holy/unholy symbol."
        )
    ),
    Spell('Imbue With Spell Ability','C',4,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("By the use of this spell, the cleric can bestow the ability to cast a particular spell upon a character normally unable to cast spells. The magic is only effective on thieves, fighters, cavaliers, assassins, monks, rangers (of under 8th level), and paladins (of under 9th level) — it will not work on a member of any other character class or sub-class, nor will it function upon a monster or any individual with less than one full hit die. The spell or spells to be <i>imbued</i> in the subject must be ones the cleric presently carries (i.e., has prayed for), and they can only be spells of an informational or defensive nature, or a <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> spell. An attempt to transfer any other sort of spell will cause the magic to fail, and then no spells will be <i>imbued</i> in the recipient even if other allowable spells were also chosen. As many as three separate spells can be <i>imbued</i>, including one 2nd-level spell and one or two 1st-level spells. In order to recieve any spell, the subject character must have a wisdom score of 9 or higher. A single 1st-level spell can be <i>imbued</i> in any eligible recipient, but the recipient must be at least 3rd level to recieve two 1st-level spells, and must be at least 5th level to recieve a 2nd-level spell. If a transferred spell's characteristics (range, duration, area of effect, etc.) are variable according to the level of the caster, then the recipient will cast them at his or her own level. All other spell details (e.g., casting time, components, etc.) apply normally.\n\n"
            "When a cleric casts <i>imbue with spell ability</i> upon another character, the cleric loses that particular spell from his or her repertoire and cannot memorize more spells until the recipient uses all of the spells that were transferred. The material components for this spell are the cleric's holy/unholy symbol, plus some minor item \"borrowed\" from the intended recipient which is symbolic of his or her profession (a lockpick for a thief, a dagger for an assassin, etc.). The \"borrowed\" item is consumed in the casting of the spell."
        )
    ),
    Spell('Lower Water','C',4,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The cleric casting a <i>lower water</i> spell causes water or similar fluid in the area of effect to sink away. Lowering is 5% of original effect for every level of experience of the cleric, i.e. 40% at 8th level, 45% at 9th, 50% at 10th, etc. The effect of the spell lasts for 1 turn for each level of experience of the cleric casting it. Likewise, the area of effect increases by level of experience, an 8th level cleric affecting an area of 8\" x 8\", a 9th level an area of 9\" x 9\", and so forth. Material components of this spell are the cleric's religious symbol and a pinch of dust. The reverse of the spell causes the water or similar fluid to return to its normal highest level, plus one foot for every level of experience of the cleric casting it."
    ),
    Spell('Neutralize Poison','C',4,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of a <i>neutralize poison</i> spell, the cleric detoxifies any sort of venom in the creature or substance touched. Note that an opponent, such as a poisonous reptile or snake (or even an envenomed weapon of an opponent) unwilling to be so touched requires the cleric to score a hit in melee combat. Effects of the spell are permanent only with respect to poison existing in the touched creature at the time of the touch, i.e. creatures (or objects) which generate new poison will <i>not</i> be permanently detoxified. The reversed spell, <i>poison</i>, likewise requires an attack (a \"to hit\" touch which succeeds), and the victim is allowed a saving throw versus poison. If the latter is unsuccessful, the victim is killed by the poison."
    ),
    Spell('Protection From Evil 10\' Radius','C',4,
        cast=tp(7,S),
        duration=tp(0,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The globe of protection of this spell is identical in all respects to a <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell except that it encompasses a much larger area and the duration of the <i>protection from evil, 10' radius</i> spell is greater. To complete this spell, the cleric must trace a circle 20' in diameter using holy water or blood, incense or smouldering dung as according to the <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell."
    ),
    Spell('Speak With Plants','C',4,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When cast, a <i>speak with plants</i> spell enables the cleric to converse, in very rudimentary terms, with all sorts of living vegetables. Thus, the cleric can question plants as to whether or not creatures have passed through them, cause thickets to part to enable easy passage, require vines to entangle pursuers, and similar things. The spell does not enable the cleric to animate non-ambulatory vegetation. The power of the spell lasts for 1 melee round for each level of experience of the cleric who cast it. All vegetation within the area of effect are under command of the spell. The material components for this spell are a drop of water, a pinch of dung, and a flame."
    ),
    Spell('Spell Immunity','C',4,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="By means of this spell, the cleric or any creature touched is made immune to the effects of a specified spell of 4th level or lower that the cleric has directly experienced. For instance, if the cleric has been hit by a <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a> spell at some time, then this spell can be used to protect someone from the effect of a <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>. This spell cannot affect an intended recipient who is already magically protected by a spell or other temporary effect. The magic of this spell will only protect against actual cast spells, not against effects of magic items or a creature's innate spell-like abilities, but immunity lasts for the full duration of the spell. Only one <i>spell immunity</i> can be in effect upon a single creature at one time; any applications subsequent to the first have no effect until the first duration ends. The <i>spell immunity</i> does not extend to items carried by the recipient, which must still make saving throws (if applicable) to avoid damage. Only a particular spell can be protected against, not a certain class of spells or a group of spells which are similar in effect; thus, someone given immunity from <a href=\"/spells/lightning-bolt-magic-user-lvl-3/\"><i>lightning bolt</i></a> spells would still be vulnerable to a <a href=\"/spells/shocking-grasp-magic-user-lvl-1/\"><i>shocking grasp</i></a>. The material component for <i>spell immunity</i> is the same (if any) as for the spell to be protected against."
    ),
    Spell('Spike Growth','C',4,
        cast=tp(7,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="Wherever any sort of plant growth of moderate size or density is found, this spell is of service. It enables the caster to cause ground-covering vegetation and/or roots and rootlets to become very hard and sharply pointed. In effect the groud cover, while appearing to be unchanged, acts as if the area were strewn with caltrops. In areas of bare ground or earthen pits, roots and rootlets will act in the same way. Without the use of a spell such as <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a>, similar magical aids, or some other special means of detection (such as <a href=\"/spells/find-traps-cleric-lvl-2/\"><i>detect traps</i></a>), an area affected by <i>spike growth</i> is absolutely undetectable as such until a victim enters the area and takes damage. Even then, the creature will not be able to determine the extent of the perilous area unless some means of magical detection is used. For each 1\" of movement through the area, a victim will incur 2 \"attacks\" from the <i>spike growth</i>. Hit probability is as if the caster of the spell were making an attack, and any successful hit causes 1-4 points of damage. Spells which control or harm vegetation, or a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell, will negate the area of the dweomer. The components for this spell are the cleric's holy symbol plus either seven sharp thorns or seven small twigs, each sharpened to a point."
    ),
    Spell('Sticks to Snakes','C',4,
        cast=tp(7,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By means of this spell the cleric is able to change 1 stick to a snake for each level of experience he or she has attained, i.e. a 9th level cleric can change 9 sticks into 9 snakes. These snakes will attack as commanded by the cleric. There must, of course, be sticks or similar pieces of wood (such as torches, spears, etc.) to turn into snakes. Note that magical items such as staves and spears which are enchanted are not affected by the spell. Only sticks within the area of effect will be changed. The probability of a snake thus changed being venomous is 5% per level of experience of the spell caster, so that there is a 55% probability of any given snake created by the spell being poisonous when sticks are turned to snakes by an 11th level cleric, 60% at 12th level, etc. The effect lasts for 2 melee rounds for each level of experience of the spell caster. The material components of the spell are a small piece of bark and several snake scales. The reverse changes <i>snakes to sticks</i> for the duration appropriate, or it negates the <i>sticks to snakes</i> spell according to the level of the cleric countering the spell, i.e. a 10th level cleric casting the reverse spell can turn only 10 snakes back to sticks."
    ),
    Spell('Tongues','C',4,
        cast=tp(7,S),
        duration=tp(1,T),
        sourcebook=V,
        desc="This spell enables the cleric to speak the language of any creature inside the spell area, whether it is a racial tongue or an alignment language. The reverse of the spell cancels the effect of the <i>tongues</i> spell or confuses verbal communication of any sort within the area of effect."
    ),
    Spell('Air Walk','C',5,
        cast=tp(1,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="The spell enables the cleric to tread upon air just as if it were solid ground. Moving upward is similar to walking up a hill, and the more steep the ascent, the slower the rate of movement: Ascending at a 45° angle is done at one-half normal movement, a 60° angle reduces movement to one-fourth of normal, and traveling straight upward can be done at one-eighth the normal rate. Similarly, rapid descent is possible, almost as if the cleric were running downhill; invert the above proportions, so that traveling straight downward can be done at eight times the normal movement rate (or, of course, at any slower rate the traveller desires). An <i>air walking</i> creature is always in control of his or her own movement rate; someone traveling straight down at a rapid rate can \"stop on a copper piece\" to avoid crashing into the ground or some other solid object. Someone attempting to <i>air walk</i> while a <a href=\"/spells/gust-of-wind-magic-user-lvl-3/\"><i>gust of wind</i></a> spell is in effect in the same area will move at one-half the usual rate if going into the <i>gust</i>, or twice the usual rate if traveling in the same direction. The spell can be placed upon any creature touched, up to and including one of giant size. For example, the caster could place the spell upon a trained horse and ride it through the air. Of course, an animal not accustomed to such movement would panic, so the steed would certainly need careful and lengthy training. The material components for the spell are the cleric's holy/unholy symbol and a bit of thistledown."
    ),
    Spell('Animate Dead Monsters','C',5,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="This spell enables the caster to animate 1 humanoid or semi-humanoid skeleton or corpse for every 2 levels of experience which he or she has attained. The dweomer animates the remains and empowers the caster to give commands. Direct commands or instructions of up to about 12 words in length will be obeyed by the skeletons or zombies animated (cf. <a href=\"/spells/animate-dead-cleric-lvl-3/\"><i>animate dead</i></a> spell). Monster types which can be animated by this spell include but are not limited to: apes (carnivorous and giant), bugbears, ettins, giants (all varieties), ogres, and trolls (all varieties). In general, the remains must be of bipedal monsters of more than 3 hit dice and with endoskeletons similar to those of humans, except in size (which must be greater than 7' height). Corpses animated by this spell are treated either as monster zombies (see Monster Manual II), or else as normal (living) creatures of the same form if that creature type normally has less than 6 hit dice. Skeletons animated by this spell are treated as monsters of half the hit dice (rounded up) of the normal sort. Animated monsters of either type receive their normal physical attacks, but have no special attacks or defenses other than those typically possessed by monster zombies or skeletons. The material components for the spell are the cleric's holy/unholy symbol and a small specimen of the type of creature which is to be animated."
    ),
    Spell('Atonement','C',5,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is used by the cleric to remove the onus of unwilling or unknown deeds from the person who is the subject of the <i>atonement</i>. The spell will remove the effects of magical alignment change as well. The person for whom <i>atonement</i> is being made must be either truly repentant or not in command of his or her own will so as to be able to be repentant. Your referee will judge this spell in this regard, noting any past instances of its use upon the person. Deliberate misdeeds and acts of knowing and willful nature cannot be atoned for with this spell. The material components of this spell are the cleric's religious symbol, prayer beads or wheel or book, and burning incense."
    ),
    Spell('Commune','C',5,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V,
        desc="By use of a <i>commune</i> spell the cleric is able to contact his or her divinity — or agents thereof — and request information in the form of questions which can be answered by a simple \"yes\" or \"no\". The cleric is allowed one such question for every level of experience he or she has attained. The answers given will be correct. It is probable that the referee will limit the use of <i>commune</i> spells to one per adventure, one per week, or even one per month, for the \"gods\" dislike frequent interruptions. The material components necessary to a <i>commune</i> spell are the cleric's religious symbol, holy/unholy water, and incense."
    ),
    Spell('Cure Critical Wounds','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>cure critical wounds</i> spell is a very potent version of the <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> spell. The cleric lays his or her hand upon a creature and heals from 6 to 27 (3d8+3) hit points of damage from wounds or other damage. The spell does not affect creatures excluded in the <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> spell explanation. Its reverse, <i>cause critical wounds</i>, operates in the same fashion as other <i>cause wounds</i> spells, requiring a successful touch to inflict the 6-27 hit points of damage. Caused wounds heal as do wounds of other sorts."
    ),
    Spell('Dispel Evil','C',5,
        cast=tp(8,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="The cleric using this spell causes summoned creatures of evil nature, or monsters enchanted and caused to perform evil deeds, to return to their own plane or place. Examples of such creatures are: aerial servants, demons, devils, djinn, efreet, elementals, and invisible stalkers. Note that this spell lasts for 1 melee round for each level of experience of the caster, and while the spell is in effect all creatures which could be affected by it attack at a -7 penalty on their \"to hit\" dice when engaging the spell caster. The reverse of the spell, <i>dispel good</i>, functions against summoned or enchanted creatures of good alignment or sent to aid the cause of good. The material components for this spell are the cleric's religious object and holy/unholy water."
    ),
    Spell('Flame Strike','C',5,
        cast=tp(8,S),
        duration=tp(1,S),
        sourcebook=V,
        desc="When the cleric calls down a <i>flame strike</i> spell, a column of fire roars downward in the exact location called for by the caster. If any creature is within the area of effect of a <i>flame strike</i>, it must make a saving throw. Failure to make the save means the creature has sustained 6-48 (6d8) hit points of damage; otherwise, 3-24 (3d8) hit points of damage are taken. The material component of this spell is a pinch of sulphur."
    ),
    Spell('Golem','C',5,
        cast=tp(8,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("In order for this spell to operate, the cleric must first construct the form of the golem to be made. The cleric must do this personally and then place a prayer spell upon the construction. All golems must be man-shaped and approximately man-sized, although they can be as small as 3' or as large as 7' tall. The sort of golem that can be created depends on the material used and the level of the cleric:\n\n"
            "At 9th or higher level, the cleric can create a <i>straw golem</i>. Construction time is 1 hour, duration thereafter is 1 hour per level. The golem has AC 10, MV 12\", HD 2+4, hp 20, #AT 2, D 1-2/1-2, SD immune to piercing weapons, half damage from blunt weapons. Carrying capacity is 30 pounds. The golem is highly susceptible to flame (taking double normal damage).\n\n"
            "At 11th and higher level, the cleric can create a <i>rope golem</i>. Construction time is 3 hours, duration thereafter is 3 hours per level. The golem has AC 8, MV 9\", HD 3+6, hp 30, #AT 1, D 1-6 plus strangulation (6 points per round after scoring a hit until destroyed or caused to release its grip), SD immune to blunt weapons, half damage from piercing weapons. Carrying capacity is 40 pounds.\n\n"
            "At 13th and higher level, the cleric can create a <i>leather golem</i>. Construction time is 9 hours, duration thereafter is 6 hours per level. The golem has AC 6, MV 6\", HD 4+8, hp 40, #AT 2, D 1-6/1-6, SD +1 or better magic weapon to hit, half damage from blunt weapons. Carrying capacity is 50 pounds.\n\n"
            "At 15th or higher level, the cleric can create a <i>wood golem</i>. Construction time is 27 hours, duration thereafter is 12 hours per level. The golem has AC 4, MV 3\", HD 5+10, hp 50, #AT 1, D 3-12, SD +1 or better magic weapon to hit, immune to blunt and piercing weapons. Carrying capacity is 60 pounds.\n\n"
            "These creations are collectively known as <i>lesser golems</i> to distinguish them from the golems described in the Monster Manual. Similar to their namesakes, these golems have no minds, so spells such as <a href=\"/spells/charm-monster-magic-user-lvl-4/\"><i>charm</i></a>, <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a>, <a href=\"/spells/hold-monster-magic-user-lvl-5/\"><i>hold</i></a>, <a href=\"/spells/sleep-magic-user-lvl-1/\"><i>sleep</i></a>, and the like have no effect on them. The dweomer of the lesser golem enables it to save as if it were a cleric of the same experience level as the one who created it. These golems cannot speak, but they can comprehend and carry out simple instructions involving no more than a dozen words."
        )
    ),
    Spell('Insect Plague','C',5,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast by the cleric, a horde of creeping, hopping, and flying insects swarm in a thick cloud. These insects obscure vision, limiting it to 3\". Creatures within the <i>insect plague</i> sustain 1 hit point of damage for each melee round they remain in it due to the bites and stings of the insects, regardless of armor class. The referee will cause all creatures with fewer than five hit dice to check morale. Creatures with two or fewer hit dice will automatically move at their fastest possible speed in a straight line in a random direction until they are not less than 24\" distant from the cloud of insects. Creatures with fewer than five hit dice which fail their morale check will behave likewise. Heavy smoke will drive off insects within its bounds. Fire will also drive insects away; a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a> in a ring shape will keep the <i>insect plague</i> outside its confines, but a fire ball will simply clear insects from its blast area for 1 turn. Lightning and cold/ice act likewise. The plague lasts for 1 turn for each level of experience of the cleric casting the spell, and thereafter the insects disperse. The insects swarm in an area which centers around a summoning point determined by the spell caster, which point can be up to 36\" distant from the cleric. The <i>insect plague</i> does not move thereafter for as long as it lasts. Note that the spell can be countered by casting a <i>dispel magic</i> upon the summoning point. A <i>cube of force</i> (a special magic item) would keep insects away from a character seeking the center of the swarm, but invisibility would afford <i>no</i> protection. The material components of this spell are a few grains of sugar, some kernels of grain, and a smear of fat."
    ),
    Spell('Magic Font','C',5,
        cast=tp(5,T),
        duration=tp(1,VA),
        sourcebook=U,
        desc="This spell causes a holy/unholy water font to serve as a scrying device. The spell will not function unless the cleric is in good standing with his or her deity. The basin of holy/unholy water becomes similar to a <i>crystal ball</i> (see Dungeon Masters Guide, Miscellaneous Magic Treasure section, under <i>crystal ball</i>). For each vial of capacity of the basin of the font, the cleric may scry for 1 round; thus, the duration of the <i>magic font</i> spell is directly related to the size of the holy/unholy water receptacle. For the chances of a character being able to detect scrying, see the <i>crystal ball</i> description in the Dungeon Masters Guide and the text for the magic-user spell <a href=\"/spells/magic-mirror-magic-user-lvl-4/\"><i>magic mirror</i></a> herein. The material components for this spell, the cleric's holy/unholy symbol and the font and its trappings, are not exhausted by the use of the spell."
    ),
    Spell('Plane Shift','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the <i>plane shift</i> spell is cast, the cleric moves himself or herself or some other creature to another plane of existence. The recipient of the spell will remain in the new plane until sent forth by some like means. If several persons link hands in a circle, up to seven can be affected by the <i>plane shift</i> at the same time. The material component of this spell is a small, forked metal rod — the exact size and metal type dictating to which plane of existence the spell will send the affected creature(s) to. (Your referee will determine specifics regarding how and what planes are reached.) An unwilling victim must be <i>touched</i> in order to be sent thusly: and in addition, the creature also is allowed a saving throw, and if the latter is successful the effect of the spell is negated."
    ),
    Spell('Quest','C',5,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>quest</i> is a spell by means of which the cleric requires the affected creature to perform a service and return to the cleric with proof that the deed was accomplished. The quest can, for example, require the location and return of some important or valuable object, the rescue of a notable person, the release of some creature, the capture of a stronghold, the slaying of a person, the delivery of some item, and so forth. If the <i>quest</i> is not properly followed due to disregard, delay, or perversion, the creature affected by the spell loses 1 from its saving throw dice for each day of such action, and this penalty will not be removed until the <i>quest</i> is properly discharged or the cleric cancels it. (There are certain circumstances which will temporarily suspend a <i>quest</i>, and other which will discharge or cancel it; your Dungeon Master will give you appropriate information as the need to know arises.) The material component of this spell is the cleric's religious symbol."
    ),
    Spell('Rainbow','C',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc=("In order to effect this spell, the cleric must be in sight of a rainbow of any sort, or have a special component (see below). The <i>rainbow</i> spell has four applications, and the cleric is able to decide which one is desired at the time of casting. These applications are:\n\n"
            "<i>Bow</i>: The spell creates a shimmering, multi-layered bow of rainbow hues. It is light and easy to pull, so that anyone with a strength of 6 or better can use it. It is magic, each of its missiles being equal to a +3 weapon, and there is no non-proficiency penalty for its use. However, it can only be employed by a member of a character class permitted to use a bow. The bow will fire 7 missiles before disappearing. It fires once or twice per round, according to the user's desire. Each time a missile is fired, one hue leaves the bow, corresponding to the color of arrow that is released. Each color of arrow has the ability to cause double damage to certain creatures, as follows:\n"
            "   Red — fire dwellers/users\n"
            "   Orange — earth elementals\n"
            "   Yellow — vegetable targets (including fungus creatures, shambling mounds, treants, etc.)\n"
            "   Green — aquatic creatures and water elementals\n"
            "   Blue — aerial creatures, electricity-using creatures, and air elementals\n"
            "   Indigo — acid-usigng or poison-using creatures\n"
            "   Violet — metallic or regenerating creatures\n"
            "When the bow is drawn, an arrow of the appropriate color magically appears, nocked and ready. If no color is requested, or a color that has already been used is asked for, then the next arrow (in the order of the spectrum) will appear.\n\n"
            "<i>Bridge</i>: The caster causes the <i>rainbow</i> to form a seven-hued bridge. The bridge is as many feet wide as the cleric has levels of experience, and it can bear as much weight, in hundreds of pounds, as the cleric has levels of experience. It will be at least 20' long and can be as long as 120', according to the desire of the caster. If the bridge's weight limit is exceeded at any time, the bridge will simply disappear into nothingness; otherwise it will last for the length of the spell duration or until ordered out of existence by the caster.\n\n"
            "<i>Elevator</i>: When desired, the caster can cause the <i>rainbow</i> to life his or her person, and all those within a 10' radius, skyward. The effect is to carry the cleric and others, if any, in a path arching upward to as high an altitude as the cleric desires, and then down again if desired. Care must be taken to reach a place of safety before the spell duration expires, or the rainbow elevator will disappear, leaving those treading upon it with no means of support. Movement along the rainbow elevator is at a rate of 12\", and the arc of the rainbow trails out 12\" behind those traveling upon it.\n\n"
            "<i>Flagon</i>: When used in this form, the <i>rainbow</i> swirls and condenses into a seven-colored vessel which contains seven measures of pure water. Each time a measure of the water is poured out, one of the hues of the container mixes with it to produce a magical draught. Any measures of the liquid that remain unused at the expiration of the spell duration will disappear, along with the container itself, whether the contents have been poured from the <i>flagon</i> or not. The draughts and their effects are:\n"
            "   Red — <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a>\n"
            "   Orange — <a href=\"/spells/resist-fire-cleric-lvl-2/\"><i>resist fire</i></a>\n"
            "   Yellow — <a href=\"/spells/cure-blindness-cleric-lvl-3/\"><i>cure blindness</i></a>\n"
            "   Green — <a href=\"/spells/slow-poison-cleric-lvl-2/\"><i>slow poison</i></a>\n"
            "   Blue — <a href=\"/spells/cure-disease-cleric-lvl-3/\"><i>cure disease</i></a>\n"
            "   Indigo — <a href=\"/spells/resist-cold-cleric-lvl-1/\"><i>resist cold</i></a>\n"
            "   Violet — <a href=\"/spells/remove-paralysis-cleric-lvl-3/\"><i>remove paralysis</i></a>\n"
            "The effects of each draught consumed will be as if the appropriate spell had been cast by a cleric of 12th level, and these effects will persist after the duration of the spell expires.\n\n"
            "The components for this spell are the cleric's holy/unholy symbol and a vial of holy/unholy water. If no rainbow is in the vicinity, the cleric can substitute a diamond of not less than 1,000 gp value, specifically prepared by him or her when in sight of a rainbow by the casting of <a href=\"/spells/bless-cleric-lvl-1/\"><i>bless</i></a> and <a href=\"/spells/prayer-cleric-lvl-3/\"><i>prayer</i></a> spells upon the gem. Only the holy symbol remains after the spell is cast."
        )
    ),
    Spell('Raise Dead','C',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the cleric casts a <i>raise dead</i> spell, he or she can restore life to a dwarf, gnome, half-elf, halfling, or human. The length of time which the person has been dead is of importance, as the cleric can raise dead persons only up to a certain point, the limit being 1 day for each level of experience of the cleric, i.e. a 9th level cleric can raise a person dead for up to 9 days. Note that the body of the person must be whole, or otherwise missing parts will still be missing when the person is brought back to life. Also, the resurrected person must make a special saving throw to survive the ordeal (see CHARACTER ABILITIES, Constitution). Furthermore, the raised person is weak and helpless in any event, and he or she will need one full day of rest in bed for each day he or she was dead. The somatic component of the spell is a pointed finger. The reverse of the spell, <i>slay living</i>, allows the victim a saving throw, and if it is successful, the victim sustains damage equal only to that caused by a <a href=\"/spells/cure-serious-wounds-cleric-lvl-4/\"><i>cause serious wounds</i></a> spell, i.e. 3-17 hit points. An evil cleric can freely use the reverse spell; a good cleric must exercise extreme caution in its employment, being absolutely certain that the victim of the <i>slay living</i> spell is evil and that his or her death is a matter of great necessity and for good, otherwise the alignment of the cleric will be sharply changed. Note that newly made <i>undead</i>, excluding skeletons, which fall within the days of being dead limit are affected by <i>raise dead</i> spells cast upon them. The effect of the spell is to cause them to become resurrected dead, providing the constitution permits survival; otherwise, they are simply dead."
    ),
    Spell('Spike Stones','C',5,
        cast=tp(6,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="The <i>spike stones</i> spell causes rock to shape itself into long, sharp points which tend to blend into the background. It is effective on both natural rock and worked stone. The <i>spike stones</i> serve to impede progress through an area or actually inflict damage. If an area is carefully observed, each observer is 25% likely to notice the sharp points of rock. Otherwise, those entering the area of effect of the spell will suffer 1-4 points of damage from each <i>spike stone</i> that hits, success of such attacks determined as if the caster of the spell were actually engaging in combat. Those entering the area are subject to attack immediately upon setting foot in the area and upon each step taken therein afterward. The initial step will be sufficient to allow the individual to become aware of some problem only if the initial attack succeeds; otherwise movement will continue and the <i>spike stones</i> will remain unnoticed until damage occurs. Charging or running victims will suffer 2 attacks per 1\" of movement rate over the area of effect after initial damage is taken before being able to halt. Others will suffer but 1 additional attack-like check. Those falling into pits so affected by <i>spike stones</i> will suffer 6 such attack-like checks, each made at +2 probability \"to hit\" for each 10' of distance fallen, and +2 on damage inflicted per 10' distance fallen, spike damage being in addition to falling damage. The material component of this spell is four tiny stalactites."
    ),
    Spell('True Seeing','C',5,
        cast=tp(8,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When the cleric employs this spell, all things within the area of the <i>true seeing</i> effect appear as they actually are. Secret doors become plain. The exact location of displaced things is obvious. Invisible things and those which are astral or ethereal become quite visible. Illusions and apparitions are seen through. Polymorphed, changed, or magicked things are apparent. Even the aura projected by creatures becomes visible, so that the cleric is able to know whether they are good or evil or between. The spell requires an ointment for the eyes. The ointment is made from very rare mushroom powder, saffron, and fat. The reverse of the spell, <i>false seeing</i>, causes the person to see things as they are not, rich being poor, rough smooth, beautiful ugly. The ointment for the reverse spell is concocted of oil, poppy dust, and pink orchid essence. For both spells, the ointment must be aged for 1-6 months."
    ),
    Spell('Aerial Servant','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,D),
        sourcebook=V,
        desc="This spell summons an invisible <a href=\"/creatures/aerial-servant/\"><i>aerial servant</i></a> to do the bidding of the cleric who conjured it. The creature does not fight, but it obeys the command of the cleric with respect to finding and returning with whatever object or creature that is described to it. Of course, the object or creature must be such as to allow the <i>aerial servant</i> to physically bring it to the cleric or his or her assign. The spell caster should keep in mind the consequences of having an <i>aerial servant</i> prevented, for any reason, from completion of the assigned duty. The spell lasts for a maximum of 1 day for each level of experience of the cleric who cast it. The <i>aerial servant</i> returns to its own plane whenever the spell lapses, its duty is fulfilled, it is dispelled, the cleric releases it, or the cleric is slain. The cleric must have a <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell, or be within a magic circle, thaumaturgic triangle, or pentagram when summoning an <i>aerial servant</i> unless the cleric has his or her religious symbol or a religious artifact or relic to use to control the creature. Otherwise, the creature will slay its summoner and return from whence it came. The <i>aerial servant</i> will always attack by complete surprise when sent on a mission, and gain the benefit of 4 free melee rounds unless the creature involved is able to detect invisible objects, in which case a six-sided die is rolled, and 1 = 1 free round, 2 = 2 free rounds, 3 = 3 free rounds, 4 = 4 free rounds, and 5 or 6 = 0 free rounds (the opponent is not surprised at all). Each round the <i>aerial servant</i> must dice to score a hit, and when a hit is scored, it means the <i>aerial servant</i> has grabbed the item or creature it was sent to take and bring back to the cleric. If a creature is involved, the <i>aerial servant's</i> strength is compared to the strength of the creature to be brought. If the creature in question does not have a strength rating, roll the appropriate number of the correct type of hit dice for the <i>aerial servant</i> and for the creature it has grabbed. The higher total is the stronger."
    ),
    Spell('Animate Object','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This powerful spell enables the cleric casting it to imbue inanimate objects with mobility and a semblance of life. The animated object, or objects, then attack whomever or whatever the cleric first designates. The object can be of any material whatsoever — wood, metal, stone, fabric, leather, ceramic, glass, etc. The speed of movement of the object is dependent upon its means of propulsion and its weight. A large wooden table would be rather heavy, but its legs would give it speed. A rug could only slither along. A jar would roll. Thus a large stone pedestal would rock forward at 1\" per round, a stone statue would move at 4\" per round, a wooden statue 8\" per round, an ivory stool of light weight would move at 12\". Slithering movement is about 1\" to 2\" per round, rolling 3\" to 6\" per round. The damage caused by the attack of an animated object is dependent upon its form and composition. Light, supple objects can only obscure vision, obstruct movement, bind, trip. smother, etc. Light, hard objects can fall upon or otherwise strike for 1-2 hit points of damage or possibly obstruct and trip as do light, supple objects. Hard, medium weight objects can crush or strike for 2-8 hit points of damage, those larger and heavier doing 3-12, 4-16, or even 5-20 hit points of damage. The frequency of attack of animated objects is dependent upon their method of locomotion, appendages, and method of attack. This varies from as seldom as once every five melee rounds to as frequently as once per melee round. The armor class of the object animated is basically a function of material and movement ability with regard to hitting. Damage is dependent upon the type of weapon and the object struck. A sharp cutting weapon is effective against fabric, leather, wood and like substances. Heavy smashing and crushing weapons are useful against wood, stone, and metal objects. Your referee will determine all of these factors, as well as how much damage the animated object can sustain before being destroyed. The cleric can animate 1 cubic foot of material for each level of experience he or she has attained. Thus, a 14th level cleric could animate one or more objects whose solid volume did not exceed 14 cubic feet, i.e. a large statue, two rugs, three chairs, or a dozen average crocks."
    ),
    Spell('Blade Barrier','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(3,R),
        sourcebook=V,
        desc="The cleric employs this spell to set up a wall of circling, razor-sharp blades. These whirl and flash in endless movement around an immobile point. Any creature which attempts to pass through the <i>blade barrier</i> suffers 8-64 (8d8) hit points of damage in doing so. The barrier remains for 3 melee rounds for every level of experience of the cleric casting it. The barrier can cover any area from as small as 5' square to as large as 2\" square, i.e. 20'x20' under ground, 60'x60' outdoors."
    ),
    Spell('Conjure Animals','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="The <i>conjure animals</i> spell enables the cleric to summon a mammal, or several of them, to his locale in order that the creature(s) can attack the cleric's opponents. The conjured animal(s) remain in the cleric's locale for 2 melee rounds for each level of experience of the cleric conjuring it (them), or until slain. The spell caster can, by means of his incantation, call up one or more mammals with hit dice whose total does not exceed his or her level. Thus, a cleric of 12th level could conjure one mammal with 12 hit dice, two with 6 hit dice each, three with 4 hit dice each, 4 with a hit dice each, six with 2 hit dice each, or 12 with 1 hit die each. For every +1 (hit point) of a creature's hit dice, count 1/4 of a hit die, i.e. a creature with 4+3 hit dice equals a 4¾ hit dice creature. The creature(s) summoned by the spell will unfailingly attack the opponent(s) of the cleric by whom the spell was cast."
    ),
    Spell('Find The Path','C',6,
        cast=tp(3,R),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By use of this spell, the cleric is enabled to find the shortest, most direct route that he or she is seeking, be it the way to or from or out of a locale. The locale can be outdoors or underground, a trap or even a <a href=\"/spells/maze-magic-user-lvl-8/\"><i>maze</i></a> spell. The spell will enable the cleric to select the correct direction which will eventually lead him or her to egress, the exact path to follow (or actions to take), and this knowledge will persist as long as the spell lasts, i.e. 1 turn for each level of experience of the cleric casting <i>find the path</i>. The spell frees the cleric, and those with him or her from a <a href=\"/spells/maze-magic-user-lvl-8/\"><i>maze</i></a> spell in a single melee round and will continue to do so as long as the spell lasts. The material component of this spell is a set of divination counters of the sort favoured by the cleric — bones, ivory counters, sticks, carved runes, or whatever. The reverse, <i>lose the path</i>, makes the creature touched totally lost and unable to find its way for the duration of the spell, although it can be led, of course."
    ),
    Spell('Forbiddance','C',6,
        cast=tp(6,R),
        duration=tp(1,P),
        sourcebook=U,
        desc=("This spell can be used only to secure a <i>consecrated</i> area (cf. <a href=\"/spells/ceremony-cleric-lvl-1/\"><i>ceremony</i></a> spell). The effect on the enchanted area is based on the ethics (law/chaos) and morals (good/evil) of those trying to enter it, relative to the caster's.\n\n"
            "Identical morals and ethics: Cannot enter area unless password is known (no saving throw).\n\n"
            "Different ethics: Save versus spell to enter the area; if failed, take 2-12 points of damage.\n\n"
            "Different morals: Save versus spell to enter the area; if failed, take 4-24 points of damage.\n\n"
            "Once a saving throw is failed, a intruder can never enter the <i>forbidden</i> area until the dweomer ceases. Effects are cumulative, and multiple required saving throws are certainly possible. The caster is immune to the spell's effect. Intruders who enter by making saving throws will feel uneasy and tense, despite their success. In addition to the cleric's holy/unholy symbols, components include holy/unholy water, silver/dung, and iron/sulfur."
        )
    ),
    Spell('Heal','C',6,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="The very potent <i>heal</i> spell enables the cleric to wipe away disease and injury in the creature who receives the benefits of the spell. It will completely cure any and all diseases and/or blindness of the recipient and heal all hit points of damage suffered due to wounds or injury, save 1 to 4 (d4). It dispels a <a href=\"/spells/feeblemind-druid-lvl-6/\"><i>feeblemind</i></a> spell. Naturally, the effects can be negated by later wounds, injuries, and diseases. The reverse, <i>harm</i>, infects the victim with a disease and causes loss of all hit points, as damage, save 1 to 4 (d4), if a successful touch is inflicted. For creatures not affected by the <i>heal</i> (or <i>harm</i>) spell, see <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a>."
    ),
    Spell('Heroes\' Feast','C',6,
        cast=tp(1,T),
        duration=tp(1,H),
        sourcebook=U,
        desc="This special dweomer enables the cleric to bring forth a great feast which will serve as many creatures as the cleric has levels of experience. The spell creates a magnificent table, chairs, service, and all the necessary food and drink. Those partaking of the feast are cured of all diseases, are immune to poison for 12 hours, and healed of 5-8 points of damage after imbibing the nectar-like beverage which is part of the feast. The ambrosia-like food that is consumed is equal to a <a href=\"/spells/bless-cleric-lvl-1/\"><i>bless</i></a> spell that lasts for 12 hours. Also, during this period, the persons who consumed the feast are immune to <i>fear</i>, <i>hopelessness</i>, and <i>panic</i>. The feast takes one full hour to consume, and the beneficial effects do not set in until after this hour is over. If the feast is interrupted for any reason, the spell is ruined and all effects of the dweomer are negated. The material components of the spell are the cleric's holy/unholy symbol and specially fermented honey taken from the cells of bee larvae destined for royal status."
    ),
    Spell('Part Water','C',6,
        cast=tp(1,T),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By employing a <i>part water</i> spell, the cleric is able to cause water or similar liquid to move apart, thus forming a trough. The depth and length of the trough created by the spell is dependent upon the level of the cleric, and a trough 3' deep by 1' by 1\" (10' or 10 yards) is created per level, i.e. at 12th level the cleric would part water 36' deep by 12' wide by 24\" (240' or 240 yards) long. The trough will remain as long as the spell lasts or until the cleric who cast it opts to end its effects (cf. <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>). The material component of this spell is the cleric's religious symbol."
    ),
    Spell('Speak With Monsters','C',6,
        cast=tp(9,S),
        duration=tp(0),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When cast, the <i>speak with monsters</i> spell allows the cleric to converse with any type of creature which has any form of communicative ability. That is, the monster will understand the intent of what is said to it by the cleric. The creature or creatures thus spoken to will be checked by your referee in order to determine reaction. All creatures of the same type as that chosen by the cleric to speak to can likewise understand if they are within range. The spell lasts for 1 melee round per level of experience of the cleric casting it. and during its duration conversation can take place as the monster is able and desires."
    ),
    Spell('Stone Tell','C',6,
        cast=tp(1,T),
        duration=tp(1,T),
        sourcebook=V,
        desc="When the cleric casts a <i>stone tell</i> upon an area, the very stones will speak and relate to the caster who or what has touched them as well as telling what is covered, concealed, or simply behind the place they are. The stones will relate complete descriptions as required. The material components for this spell area drop of mercury and a bit of clay."
    ),
    Spell('Word of Recall','C',6,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="The <i>word of recall</i> spell takes the cleric instantly back to his or her sanctuary when the word is uttered. The sanctuary must be specifically designated in advance by the cleric. It must be a well known place, but it can be any distance from the cleric, above or below ground. Transportation by the <i>word of recall</i> spell is infallibly safe. The cleric is able to transport, in addition to himself or herself, 250 gold pieces weight cumulative per level of experience. Thus, a 15th level cleric could transport his or her person and 3,750 (375 pounds) gold pieces weight in addition; this extra matter can be equipment, treasure, or living material such as another person."
    ),
    Spell('Astral Spell','C',7,
        cast=tp(3,T),
        duration=tp(0),
        sourcebook=V,
        desc="By means of the <i>astral spell</i> a cleric is able to project his or her astral body into the <i>Astral Plane</i>, leaving his or her physical body and material possessions behind on the <i>Prime Material Plane</i>, (the plane on which the entire universe and all of its parallels have existence). Only certain magic items which have multi-planed existence can be brought into the <i>Astral Plane</i>. As the <i>Astral Plane</i> touches upon all of the first levels of the <i>Outer Planes</i>, the cleric can travel astrally to any of these <i>Outer Planes</i> as he or she wills. The cleric then leaves the <i>Astral Plane</i>, forming a body on the plane of existence he or she has chosen to enter. It is also possible to travel astrally anywhere in the <i>Prime Material Plane</i> by means of the <i>astral spell</i>, but a second body cannot be formed on the <i>Prime Material Plane</i>. As a general rule, a person astrally projected can be seen only by creatures on the <i>Astral Plane</i>. At all times the astral body is connected to the material by a silvery cord. If the cord is broken, the affected person is killed, astrally and materially, but generally only the psychic wind can normally cause the cord to break. When a second body is formed on a different plane, the silvery cord remains invisibly attached to the new body, and the cord simply returns to the latter where it rests on the <i>Prime Material Plane</i>, reviving it from its state of suspended animation. Although astrally projected persons are able to function on the <i>Astral Plane</i>, their actions do not affect creatures not existing on the <i>Astral Plane</i>. The spell lasts until the cleric desires to end it, or until it is terminated by some outside means (<a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> or destruction of the cleric's body on the <i>Prime Material Plane</i>). The cleric can take up to five other creatures with him or her by means of the <i>astral spell</i>, providing the creatures are linked in a circle with the cleric. These fellow travellers are dependent upon the cleric and can be stranded. Travel in the <i>Astral Plane</i> can be slow or fast according to the cleric's desire. The ultimate destination arrived at is subject to the conceptualization of the cleric. (See APPENDIX IV, THE KNOWN PLANES OF EXISTENCE, for further information on the <i>Astral Plane</i> and astral projection.)"
    ),
    Spell('Control Weather','C',7,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("The <i>control weather</i> spell allows a cleric to change the weather in the area he or she is in at the time the spell is cast. The spell will affect the weather for from 4 to 48 hours (4d12) in an area of from 4 to 16 square miles (4d4). It requires 1 turn to cast the spell, and an additional 1 to 4 (d4) turns for the effects of the weather to be felt. The <i>control weather</i> spell will not radically change the temperature, i.e. from below zero to a 100 degree temperature heat wave. The weather control possible depends upon the prevailing conditions:\n\n"
            "<table>"
            "<tr><th>CLEAR WEATHER</th><th>PARTLY CLOUDY WEATHER</th><th>CLOUDY WEATHER</th></tr>"
            "<tr><td>Very clear</td><td>Clear weather</td><td>Partly cloudy</td></tr>"
            "<tr><td>Light clouds or hazy</td><td>Cloudy</td><td>Deep clouds</td></tr>"
            "<tr><td></td><td>Mist/Light rain/Small hail</td><td>Fog</td></tr>"
            "<tr><td></td><td>Sleet/Light snow</td><td>Heavy rain/Large hail</td></tr>"
            "<tr><td></td><td></td><td>Driving sleet/Heavy snow</td></tr>"
            "</table>\n"
            "<table>"
            "<tr><th>HOT WEATHER</th><th>WARM WEATHER</th><th>COOL WEATHER</th><th>COLD WEATHER</th></tr>"
            "<tr><td>Warm weather</td><td>Hot weather</td><td>Warm weather</td><td>Cool weather</td></tr>"
            "<tr><td>Sweltering heat</td><td>Cool weather</td><td>Cold weather</td><td>Arctic cold</td></tr>"
            "</table>\n"
            "<table>"
            "<tr><th>CALM</th><th>LIGHT WIND</th><th>STRONG WIND</th><th>GALE</th><th>STORM</th></tr>"
            "<tr><td>Dead calm</td><td>Calm</td><td>Light wind</td><td>Strong wind</td><td>Gale</td></tr>"
            "<tr><td>Light breeze</td><td>Strong wind</td><td>Gale</td><td>Storm</td><td>Hurricane-Typhoon</td></tr>"
            "</table>\n\n"
            "All three aspects of the weather (clouds/precipitation, temperature, and wind) can be controlled, but only as shown. For example, a day which is <i>clear</i>, <i>warm</i>, and with <i>light wind</i> can be controlled to become <i>hazy</i>, <i>hot</i>, and <i>calm</i>. Contradictions are not possible — <i>fog</i> and <i>strong wind</i>, for example. Multiple <i>control weather</i> spells can be used only in succession. The material components for this spell are the cleric's religious symbol, incense, and prayer beads or similar prayer object. Obviously, this spell functions only in areas where there are appropriate climatic conditions."
        )
    ),
    Spell('Earthquake','C',7,
        cast=tp(1,T),
        duration=tp(1,R),
        sourcebook=V,
        desc=("When this spell is cast by a cleric, a local tremor of fairly high strength rips the ground. The shock is over in one melee round. The <i>earthquake</i> affects all terrain, vegetation, structures, and creatures in its locale. The area of effect of the <i>earthquake</i> spell is circular, the diameter being ½\" for every level of experience of the cleric casting it, i.e. a 20th level cleric casts an <i>earthquake</i> spell with a 10\" diameter area of effect. Effects are as follows:\n\n"
            "TERRAIN\n"
            "Cave or cavern — Collapses roof\n"
            "Cliffs — Crumble causing landslide\n"
            "Ground — Cracks open, causing creatures to fall in and be killed as follows:\n"
            "   — Size S — 1 in 4 (d4)\n"
            "   — Size M — 1 in 6 (d6)\n"
            "   — Size L — 1 in 8 (d8)\n"
            "Marsh — Drains water off to form muddy, rough ground\n"
            "Tunnel — Caves in\n\n"
            "VEGETATION\n"
            "Small growth — No effect\n"
            "Trees — 1 in 3 are uprooted and fall\n\n"
            "STRUCTURES\n"
            "All structures — Sustain from 5 to 60 points (5d12) of structural damage; those taking full damage are thrown down in rubble\n\n"
            "CREATURES\n"
            "See above\n\n"
            "The material components for this spell are a pinch of dirt, a piece of rock, and a lump of clay."
        )
    ),
    Spell('Exaction','C',7,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U,
        desc="When this spell is employed, the cleric confronts some powerful creature from another plane (including devas and powerful \"name\" demons, for instance, but not demigods or deities of any sort) and requires of it some duty or quest. The creature may not be one ethically or morally opposed to the cleric (i.e. not evil if the cleric is good, not chaotic if the cleric is lawful). Note that an absolute (true) neutral creature is in effect greatly opposed to both good and evil, and both law and chaos. The spell caster must know something about the creature to exact service from it, or else he or she must offer some fair trade in return for the service. That is, if the cleric is aware that the creature has received some favor from someone of the cleric's alignment, then the <i>exaction</i> can name this as cause; if no balancing reason for service is known, then some valuable gift or service must be pledged in return for the <i>exaction</i>. The service exacted must be reasonable with respect to the past or promised favor or reward. The spell then acts as a <a href=\"/spells/quest-cleric-lvl-5/\"><i>quest</i></a> upon the creature which is to perform the required service. Immediately upon completion of the service, the subject creature is transported to the vicinity of the cleric, and the cleric must then and there return the promised reward, whether it is irrevocable cancellation of a past debt or the giving of some service or other material reward. Upon so doing, the creature is instantly freed to return to its own plane. Failure to fulfill the promise to the letter results in the cleric being subject to <i>exaction</i> by the subject creature or by its master, liege, etc., at the very least. At worst, the creature may attack the reneging cleric without fear of any of his or her spells affecting it, for the failure to live up to the bargain gives the creature total immunity from the spell powers of the cleric so doing. The material components of this spell are the cleric's holy/unholy symbol, some matter or substance from the plane of the creature from whom an <i>exaction</a> is to be expected, and knowledge of the creature's nature and/or actions which is written out on a parchment leaf that is burned to seal the bargain."
    ),
    Spell('Gate','C',7,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The casting of a <i>gate</i> spell has two effects: first, it causes an ultra-dimensional connection between the plane of existence the cleric is an and that plane on which dwells a specific being of great power, the result enabling the being to merely step through the gate or portal, from its plane to that of the cleric; second, the utterance of the spell attracts the attention of the dweller on the other plane. When casting the spell, the cleric must name the demon, devil, demi-god, god, or similar being he or she desires to make use of the <i>gate</i> and come to the cleric's aid. There is a 100% certainty that something will step through the gate. The actions of the being which comes through will depend on many factors, including the alignment of the cleric, the nature of those in company with him or her, and who or what opposes or threatens the cleric. Your Dungeon Master will have a sure method of dealing with the variables of the situation. The being gated in will either return immediately (very unlikely) or remain to take action."
    ),
    Spell('Holy (Unholy) Word','C',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("The utterance of a <i>holy (unholy) word</i> has tremendous power. It drives off evil (good) creatures from other planes, forcing them to return to their own plane(s) of existence. It further affects other creatures of differing alignment as follows:\n\n"
            "<table>"
            "<tr><th>Creature's Hit Dice or Level</th><th>General</th><th>Move</th><th>Attack Dice</th><th>Spells</th></tr>"
            "<tr><td>less than 4</td><td>kills</td><td>-</td><td>-</td><td>-</td></tr>"
            "<tr><td>4 to 7+</td><td>paralyzes 1-4 turns</td><td>-</td><td>-</td><td>-</td></tr>"
            "<tr><td>8 to 11+</td><td>stuns 2-8 rounds</td><td>-50%</td><td>-4</td><td>-</td></tr>"
            "<tr><td>12 or more</td><td>defeans 1-4 rounds</td><td>-25%</td><td>-2</td><td>50% chance of failure</td></tr>"
            "</table>\n\n"
            "Affected creatures must be within the 6\" diameter area of effect centering on the cleric casting the spell."
        )
    ),
    Spell('Regenerate','C',7,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a <i>regenerate</i> spell is cast, body members (fingers, toes, hands, feet, arms, legs, tails, or even the heads of multi-headed creatures), bones, or organs will grow back. The process of regeneration requires but 1 round if the member(s) severed is (are) present and touching the creature, 2-8 turns otherwise. The reverse, <i>wither</i>, causes the member or organ touched to shrivel and cease functioning in 1 round, dropping off into dust in 2-8 turns. As is usual, creatures must be touched in order to have harmful effect occur. The material components of this spell are a prayer device and holy/unholy water."
    ),
    Spell('Restoration','C',7,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast, the life energy level of the recipient creature is raised upwards by one. This subsumes previous life energy level drain of the creature by some force or monster. Thus, if a 10th level character had been struck by a wight and drained to 9th level, the <i>restoration</i> spell would bring the character up to exactly the number of experience points necessary to restore him or her to 10th level once again, and restoring additional hit dice (or hit points) and level functions accordingly. <i>Restoration</i> is only effective if the spell is cast within 1 day/level of experience of the cleric casting it of the recipient's loss of life energy. The reverse, <i>energy drain</i>, draws away a life energy level (cf. such \"undead\" as <a href=\"/creatures/spectre/\">spectre</a>, <a href=\"/creatures/wight/\">wight</a>, <a href=\"/creatures/vampire/\">vampire</a>). The <i>energy drain</i> requires the victim to be touched. A <i>restoration</i> spell will restore the intelligence of a creature affected by a <a href=\"/spells/feeblemind-druid-lvl-6/\"><i>feeblemind</i></a> spell."
    ),
    Spell('Resurrection','C',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="The cleric employing this spell is able to restore life and complete strength to the person he/she bestows the <i>resurrection</i> upon. The person can have been dead up to 10 years cumulative per level of the cleric casting the spell, i.e. a 19th level cleric can resurrect the bones of a person dead up to 190 years. See <a href=\"/spells/raise-dead-cleric-lvl-5/\"><i>raise dead</i></a> for limitations on what persons can be raised. The reverse, <i>destruction</i>, causes the victim of the spell to be instantly dead and turned to dust. <i>Destruction</i> requires a touch, either in combat or otherwise. The material components of the spell are the cleric's religious symbol and holy/unholy water. Employment of this spell makes it impossible for the cleric to cast further spells or engage in combat until he or she has had one day of bed rest for each level of experience of the person brought back to life or destroyed."
    ),
    Spell('Succor','C',7,
        cast=tp(1,D),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("By casting this spell, the cleric creates a powerful dweomer in some specially prepared object — a string of prayer beads, a small clay tablet, an ivory baton, etc. This object will radiate magic, for it contains the power to instantaneously transport its possessor to the sanctuary of the cleric who created its dweomer. Once the item is magicked, the cleric must give it willingly to an individual, at the same time informing him or her of a command word to be spoken when the item is to be used. To make use of the item, the recipient must speak the command word at the same time that he or she rends or breaks the item. When this is done, the individual and all that he or she is wearing and carrying will be instantly transported to the sanctuary of the cleric just as if the individual were capable of speaking a <a href=\"/spells/word-of-recall-cleric-lvl-6/\"><i>word of recall</i></a> spell. No other creatures can be affected.\n\n"
            "The reversed application of the spell enables the cleric to be transported to the vicinity of the possessor of the dweomered item when it is broken and the command word said. The cleric can choose not to be affected by this \"summons\" by making that decision at the instant when the transportation is to take place, but if he or she so chooses, then the opportunity is gone forever and the spell is wasted. The cost of preparing the special item (for either version of the spell) varies from 2,000 to 5,000 gold pieces."
        )
    ),
    Spell('Symbol','C',7,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc=("The cleric casting this spell inscribes a <i>symbol</i> in the air or upon any surface, according to his or her wish. The symbol glows for 1 turn for each level of experience of the cleric casting it. The particular symbol used can be selected by the cleric at the time of casting, selection being limited to:\n\n"
            "HOPELESSNESS	- Creatures seeing it must turn back in dejection and/or surrender to capture or attack unless they save versus magic. Its effects last for 3 to 12 turns.\n"
            "PAIN	- Creatures affected suffer -4 on \"to hit\" dice and -2 on dexterity ability score due to wracking pains. The effects last for 2-20 turns.\n"
            "PERSUASION	- Creatures seeing the symbol become of the same alignment as and friendly to the cleric who scribed the symbol for from 1 to 20 turns unless a saving throw versus magic is made.\n\n"
            "The material components of this spell are mercury and phosphorus. (cf. eighth level magic-user <a href=\"/spells/symbol-magic-user-lvl-8/\"><i>symbol</i></a> spell."
        )
    ),
    Spell('Wind Walk','C',7,
        cast=tp(1,R),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="This spell enables the cleric, and possibly one or two other persons. to alter the substance of his or her body to cloud-like vapors. A magical wind then wafts the cleric along at a speed of up to 60\" per turn, or as slow as 6\" per turn, as the spell caster wills. The <i>wind walk</i> spell lasts as long as the cleric desires, up to a maximum duration of 6 turns (one hour) per level of experience of the caster. For every 8 levels of experience the cleric has attained, up to 24, he or she is able to touch another and carry that person, or those two persons, along with the <i>wind walk</i>. Persons wind walking are not invisible but appear misty and are transparent. If fully clothed in white they are 80% likely to be mistaken for clouds, fog, vapors, etc. The material components of this spell are fire and holy/unholy water."
    )
]

druid_spells = [
    Spell('Animal Friendship','D',1,
        cast=tp(6,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this spell the druid is able to show any animal which is of at least <i>animal</i> intelligence (but not above <i>semi</i>-intelligent rating) that the druid is disposed to be its friend. If the animal does not make its saving throw versus magic immediately when the spell is begun, it will stand quietly while the druid finishes the spell. Thereafter, it will follow the druid about, and he or she can teach it 3 specific \"tricks\" or tasks for each point of intelligence it possesses. (Typical tasks are those taught a dog or similar pet, i.e. they cannot be complex.) Training for each such \"trick\" must be done over a period of 1 week, and all must be done within 3 months of acquiring the creature. During the training period the animal will not harm the druid, but if the creature is left alone for more than 3 days it will revert to its natural state and act accordingly. The druid may use this spell to attract up to 2 hit dice of animal(s) per level of experience he or she possesses. This also means that the druid can never have more hit dice of animals so attracted and trained than are equal to or less than twice his or her levels of experience. Only <i>neutral</i> animals can be attracted, befriended, and trained. The material components of this spell ore mistletoe and a piece of food attractive to the animal subject."
    ),
    Spell('Ceremony','D',1,
        cast=tp(1,H),
        duration=tp(1,P),
        sourcebook=U,
        desc=("The druidic <i>ceremony</i> spell is similar to the <a href=\"/spells/ceremony-cleric-lvl-1/\">clerical spell of the same name</a>. It has a number of applications within the hierarchy of druids. The effect of a <i>ceremony</i> spell does not leave behind an aura of magic, although a <a href=\"/spells/know-alignment-cleric-lvl-2/\"><i>know alignment</i></a> spell or similar magic might reveal the force of true neutrality involved in the magic. Druidic <i>ceremonies</i> include the following, which can be cast by a druid of the indicated or higher level:\n\n"
            "   1st-level druid: <i>coming of age, rest eternal, marriage</i>\n"
            "   3rd-level druid: <i>dedication, investiture</i>\n"
            "   7th-level druid: <i>initiation, special vows</i>\n"
            "   9th-level druid: <i>hallowed ground</i>\n"
            "   12th-level druid: <i>cast out</i>\n\n"
            "The characteristics of the various types of druidic <i>ceremony</i> spells are as follows:\n\n"
            "<i>Coming of age</i> is performed upon young people in druidic societies, usually when they reach the age of 14, and is symbolic of the young man's or young woman's entrance into adulthood. Effects of the spell are the same as for the clerical version (+1 bonus to a single saving throw); see the cleric text for other details.\n\n"
            "<i>Rest eternal</i> is cast upon the body of a deceased being, by means of which the soul/spirit of the creature is hastened in its journey to its final resting place. The spells <a href=\"/spells/raise-dead-cleric-lvl-5/\"><i>raise dead</i></a> and <a href=\"/spells/resurrection-cleric-lvl-7/\"><i>resurrection</i></a> will not restore life to a character who has been the object of this spell, although a wish spell would serve that purpose.\n\n"
            "<i>Marriage</i> is essentially identical to the <a href=\"/spells/ceremony-cleric-lvl-1/\">clerical <i>ceremony</i></a> of the same name.\n\n"
            "<i>Dedication</i> allows the recipient of the spell to be taken into the ranks of the druid's followers/worshipers, provided that the character is true neutral in alignment. A recipient of this spell is charged, as are druids, with the responsibility to preserve and protect nature and the balance of forces in the world. In other respects it is similar to the <a href=\"/spells/ceremony-cleric-lvl-1/\">clerical <i>ceremony</i></a> of the same name.\n\n"
            "<i>Investiture</i> is a rite that must be performed upon a character before he or she can become an Aspirant (1st-level druid). It conveys no other benefit.\n\n"
            "<i>Initiation</i> imbues the druid with the shape-changing and immunity to woodland <i>charm</i> powers that become available to the character upon attaining 7th level. This <i>ceremony</i> must be performed upon a druid immediately after he or she begins to advance upward through the 7th level of experience; if cast earlier than this, it will not work, and the druid will not have the benefit of the above-mentioned special powers until receiving <i>initiation</i>. Usually a druid must seek out another druid of 7th or higher level to perform the rite, but in unusual cases a druid may cast it upon himself or herself.\n\n"
            "<i>Special vows</i> is a <i>ceremony</i> that operates in the same fashion as the clerical rite of the same name. It does not work upon paladins, but will function upon cavaliers of any alignment.\n\n"
            "<i>Hallowed ground</i> is cast by the druid on his or her permanent grove. This <i>ceremony</i> ensorcels the trees of the grove so that they will never be affected by disease or natural disasters. The ground remains <i>hallowed</i> for as long as the druid maintains this grove as his or her permanent base.\n\n"
            "<i>Cast out</i> is a form of excommunication or punishment that can be performed by a druid upon someone who has committed sacrilege upon the natural environment or in some other way violated the principles and standards of druidism. Its effects may be lessened at a later date by the casting of the reversed version of this <i>ceremony</i>, either by the same druid or another one of at least as high a level as the original caster, but the <i>casting out</i> can never be completely neutralized except by a Hierophant Druid of any level. A character who has been <i>cast out</i> exudes a powerful negative aura, causing any natural creature encountered to react negatively to the character. This includes all normal (non-magical) animals, monsters native to the woodlands, domesticated beasts such as horses and dogs, and all druids and their followers.\n\n"
            "<i>Casting out</i> is a very powerful form of punishment, and can only be performed by a druid who has received permission from his or her Archdruid to do so. Similarly, an Archdruid must get permission from the Great Druid, and the Great Druid from the Grand Druid. The Grand Druid does not need to obtain permission, but his or her actions may be reversed by a Hierophant Druid at any time.\n\n"
            "This ceremony is usually only used on occasions where the severity of an offense warrants an extreme punishment; a druid who asks for and is denied permission to perform it, or one who later has his or her actions offset by another druid, may be subject to punishment by higher-ranking members of the hierarchy. An intended recipient of this <i>ceremony</i> who is unwilling recieves a saving throw versus spell, at -4, to negate its effects.\n\n"
            "The components of a <i>ceremony</i> spell always include mistletoe, and the rite (of any sort) must be performed in a druid grove or some other natural, healthy patch of forest. Such <i>ceremonies</i> are normally conducted either at dawn or dusk, the times when night and day are in balance."
        )
    ),
    Spell('Detect Balance','D',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc=("This spell allows the druid to determine if non-neutral forces and alignments are at work in the area of effect (upon or in the object or creature being scanned). An alignment that is partly neutral (such as that of a neutral good cleric) will radiate a mild aura, while an alignment that has no neutral component (such as that of a chaotic good fighter) will give off a strong aura. The spell does not determine exact alignment, but only tells the druid if the object or creature being examined is something other than true neutral; a paladin and a chaotic evil thief, for instance, will radiate the same aura at the same strength.\n\n"
            "The spell will not function upon non-living items that do not have a natural aura (such as a vial of poison), but will work upon an object such as an aligned magical sword. Creatures that are under the effect of an <i>unknowable alignment</i> spell or similar magic will not radiate any aura when this spell is used upon them. If the magic is used upon something or someone that exudes a true neutral alignment (such as another druid), it will produce a smooth, well-balanced aura identifiable as one of neutrality."
        )
    ),
    Spell('Detect Magic','D',1,
        cast=tp(3,S),
        duration=tp(12,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the <a href=\"/spells/detect-evil-cleric-lvl-1/\">first level cleric spell</a> of the same name."
    ),
    Spell('Detect Poison','D',1,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc=("By means of this spell the druid is able to determine if some object, creature, or area contains poison or has been poisoned. In general, the area which can be perused by the dweomer of the spell is 1 cubic yard of space. Therefore, the druid cannot determine if an entire pond is poisoned, but he or she could tell if a portion — or something within the portion — scanned during the round contain poison. There is also a 5% chance per level of experience of the caster that the type of poison used or contained in the area scanned will also be discovered by the spell, i.e., contact poison (insinuative), ingestive, or respirative (gas).\n\n"
            "While more than one area can be scanned with a <i>detect poison</i> spell during the duration of the spell, it is almost fruitless to attempt to determine poison type for all of those areas; any single failure on the \"5% chance per level\" roll to detect poison type makes this spell useless for this purpose for the remainder of the duration of that particular casting. In addition to mistletoe, the druid needs a yew leaf as a material component for this spell. The latter item will turn brown if poison is present, so that several will possibly be needed to fully utilize the entire spell duration."
        )
    ),
    Spell('Detect Snares & Pits','D',1,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(4,R),
        sourcebook=V,
        desc='Upon casting this spell, the druid is able to <i>detect snares & pits</i> along the 1" wide by 4" long area of effect path and thus avoid such deadfalls. Note that in the underground only simple pits, not all forms of traps, would be detected by means of this spell. Outdoors, the spell detects all forms of traps — deadfalls, missile trips, snares, etc. The spell lasts 4 melee rounds for each level of experience of the druid casting it, i.e. 4 rounds at the 1st level, 8 at the 2nd, 12 (1 turn plus 2 rounds) at the 3rd, etc.'
    ),
    Spell('Entangle','D',1,
        cast=tp(3,S),
        duration=tp(1,T),
        sourcebook=V,
        desc="By means of this spell the druid is able to cause plants in the area of effect to <i>entangle</i> creatures within the area. The grasses, weeds, bushes, and even trees wrap, twist, and entwine about creatures, thus holding them fast for the duration of the spell. If any creature in the area of effect makes its saving throw, the effect of the spell is to slow its movement by 50% for the spell duration."
    ),
    Spell('Faerie Fire','D',1,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(4,R),
        sourcebook=V,
        desc="When the druid casts this spell, he or she outlines an object or creature with a pale glowing light. The completeness of the lining is dependent upon the number of linear feet the druid is able to affect, about 12' per level (i.e. one 6' man or two 3' kobolds). If there is sufficient power, several objects or creatures can be covered by the <i>faerie fire</i>, but one must be fully outlined before the next is begun, and all must be within the area of effect. Outlined objects or creatures (including those otherwise invisible) are visible at 8\" in the dark, 4\" if the viewer is near a bright light source. Outlined creatures are easier to strike, thus opponents gain +2 on \"to hit\" dice. The <i>faerie fire</i> can be blue, green, or violet according to the word of the druid at the time he or she casts the spell. The <i>faerie fire</i> does not itself cause any harm to the object or creature lined."
    ),
    Spell('Invisibility to Animals','D',1,
        cast=tp(4,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When an <i>invisibility to animals</i> spell is cast by a druid, the recipient of the magic becomes totally undetectable with respect to normal animals with intelligence under 6. Normal animals includes giant-sized varieties, but it excludes any with magical abilities or powers. The magicked individual is able to walk amongst animals or pass through them as if he or she did not exist. For example, this individual could stand before the hungriest of <a href=\"/creatures/lion/\">lions</a> or a <a href=\"/creatures/tyrannosaurus/\">tyrannosaurus rex</a> and not be molested or even noticed. However, a <a href=\"/creatures/nightmare/\">nightmare</a>, <a href=\"/creatures/hell-hound/\">hell hound</a>, or <a href=\"/creatures/winter-wolf/\">winter wolf</a> would certainly be aware of the individual. The material component of this spell is holly rubbed over the individual."
    ),
    Spell('Locate Animals','D',1,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc='The druid with a <i>locate animals</i> spell is able to determine the direction and distance of any of the desired animals within the area of effect. The sought after animal can be of any sort, but the druid must concentrate on the sort desired. The druid faces in a direction, thinks of the animal desired, and he or she then knows if any such animal is within spell range. During a round of spell effect duration, the druid must face in only one direction, i.e., only a 2" wide path can be known. The spell lasts 1 round per level of experience of the druid, while the length of the path is 2" per level of experience.'
    ),
    Spell('Pass Without Trace','D',1,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast, the recipient can move through any type of terrain — mud, snow, dust, etc. — and leave neither footprint nor scent. Thus, tracking a person or other creature covered by this dweomer is impossible. The material components of this spell are a leaf of mistletoe (which must be burned thereafter and the ashes powdered and scattered) and a sprig of pine or evergreen. <i>Note</i>: The area which is passed over will radiate a dweomer for 6-36 turns after the affected creature passes."
    ),
    Spell('Precipitation','D',1,
        cast=tp(3,S),
        duration_lvl=tp(1,S),
        sourcebook=U,
        desc="This spell is identical to the <a href=\"/spells/precipitation-cleric-lvl-1/\">1st-level clerical spell</a> of the same name, except that the druid needs mistletoe as an additional material component."
    ),
    Spell('Predict Weather','D',1,
        cast=tp(1,R),
        duration_lvl=tp(2,H),
        sourcebook=V,
        desc="When a <i>predict weather</i> spell is cast by a druid, he or she gains 100% accurate knowledge of the weather (sky, temperature, precipitation) in a nine square mile area centering on the druid. For each level of experience of the druid casting the spell, two hours advance weather can be forecast. Thus, at 1st level the druid knows what the weather will be for two hours; at second level he or she knows the weather for 4 hours in advance, etc."
    ),
    Spell('Purify Water','D',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell makes dirty, contaminated water clean and pure, suitable for consumption. Up to one cubic foot per level of the druid casting the spell can be thus purified. The reverse of the spell, <i>contaminate water</i>, works in exactly the same manner, and even holy/unholy water can be spoiled by its effects."
    ),
    Spell('Shillelagh','D',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell enables the druid to change his own oaken cudgel into a magical weapon which is +1 to hit and inflicts 2-8 hit points of damage on opponents up to man-sized, 2-5 hit points of damage on larger opponents. The druid must wield the <i>shillelagh</i>, of course. The material components of this spell are an oaken club, any mistletoe, and a shamrock leaf."
    ),
    Spell('Speak With Animals','D',1,
        cast=tp(3,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the <a href=\"/spells/speak-with-animals-cleric-lvl-2/\">second level cleric spell</a> of the same name."
    ),
    Spell('Barkskin','D',2,
        cast=tp(3,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When the druid casts the <i>barkskin</i> spell upon a creature, its armor class improves 1 place because the creature's skin becomes as tough as bark. In addition, saving throws versus all attack forms except magic increase by +1. This spell can be placed on the druid casting it or on any other creature he or she touches. In addition to mistletoe. the caster must have a handful of bark from an oak as the material component of the spell."
    ),
    Spell('Charm Person Or Mammal','D',2,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("This spell will affect any single person or mammal it is cast upon. The creature then will regard the druid who cast the spell as a trusted friend and ally to be heeded and protected. The spell does not enable the druid to control the charmed creature as if it were an automaton, but any word or action of the druid will be view in its most favorable way. Thus, a charmed creature would not obey a suicide command, but might believe the druid if assured that the only chance to save the druid's life is if the creature holds back an onrushing red dragon for \"just a round or two\". Note also that the spell does not empower the druid with linguistic capabilites beyond those he or she normally possesses. The duration of the spell is a function of the charmed creature's intelligence, and it is tied to the saving throw. The spell may be broken if a saving throw is made, and this saving throw is checked on a periodic basis according to the creature's intelligence:\n\n"
            "<table>"
            "<tr><th>Intelligence Score</th><th>Period Between Checks</th></tr>"
            "<tr><td>3 or less</td><td>3 months</td></tr>"
            "<tr><td>4 to 6</td><td>2 months</td></tr>"
            "<tr><td>7 to 9</td><td>1 month</td></tr>"
            "<tr><td>10 to 12</td><td>3 weeks</td></tr>"
            "<tr><td>13 to 14</td><td>2 weeks</td></tr>"
            "<tr><td>15 to 16</td><td>1 week</td></tr>"
            "<tr><td>17</td><td>3 days</td></tr>"
            "<tr><td>18</td><td>2 days</td></tr>"
            "<tr><td>19 or more</td><td>1 day</td></tr>\n\n"
            "If the druid harms, or attempts to harm, the charmed creature by some overt action, or if a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> is successfully cast upon the charmed creature, the <i>charm</i> will be broken automatically. The spell affects all mammalian animals and persons. The term <i>person</i> includes all bipedal human and humanoid creatures of approximately man-size, or less than man-size, including those affected by the <a href=\"/spells/hold-person-cleric-lvl-2/\"><i>hold person</i></a> spell. If the recipient of the <i>charm person/charm mammal</i> spell makes its saving throw versus the spell, its effect is negated."
        )
    ),
    Spell('Create Water','D',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="The druid can create pure, drinkable water by means of a <i>create water</i> spell. He or she creates 1 cubic foot of water for each level of experience attained. The water can be created at a maximum distance of 1\" from the druid."
    ),
    Spell('Cure Light Wounds','D',2,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="With the exception of the fact that the druid must have mistletoe (of any sort) to effect this spell, it is the same as the first level cleric <a href=\"/spells/cure-light-wounds-cleric-lvl-1/\"><i>cure light wounds</i></a> spell."
    ),
    Spell('Feign Death','D',2,
        cast=tp(3,S),
        duration=tp(4,R),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level magic-user <a href=\"/spells/feign-death-magic-user-lvl-3/\"><i>feign death</i></a> spell. The material component is a piece of dead oak leaf (in addition to mistletoe, of course)."
    ),
    Spell('Fire Trap','D',2,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the fourth level magic-user <a href=\"/spells/fire-trap-magic-user-lvl-4/\"><i>fire trap</i></a> spell except as shown above and for the fact that the material components are holly berries and a stick of charcoal to trace the outline of the closure."
    ),
    Spell('Flame Blade','D',2,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When a druid casts this spell, he or she causes a ray of red-hot fire to spring forth from his or her hand. This blade-like ray is actually wielded as if it were a scimitar, and if the druid scores a successful hit while employing the <i>flame blade</i>, the creature struck will take 5-8 points of damage — with a damage bonus of +2 if the creature is of the undead class or is especially vulnerable to fire, or a -2 penalty to damage if the creature is protected from fire. No damage can be inflicted upon a creature which is a fire-dweller or which uses fire as an attack form. The <i>flame blade</i> will ignite combustible materials such as parchment, straw, dry sticks, cloth, etc. However, it is not a magical weapon in the normal sense of the term except with respect to undead monsters, so creatures that can be struck only by magical weapons are not harmed by this spell unless they are of the undead class. In addition to mistletoe, the druid must have a leaf of sumac in order to cast the spell."
    ),
    Spell('Goodberry','D',2,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U,
        desc="When a druid casts a <i>goodberry</i> spell upon a handful or freshly picked berries, from 2 to 8 of them will become magical. The druid casting the spell (as well as any other druid of 3rd or higher level) will be able to immediately discern which berries were affected. A <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a> spell will discover this also. Berries with the dweomer will either enable a hungry creature of approximately man-size to eat one and be as well-nourished as if a full normal meal were eaten, or else the berry will cure 1 point of physical damage due to wounds or other similar causes, subject to a maximum of 8 points of such curing in any 24-hour period. The reverse of the spell, <i>badberry</i>, causes rotten berries to appear wholesome but each actually delivers 1 point of poison damage (no saving throw) if ingested. The material component of the spell is mistletoe passed over the freshly picked, edible berries to be enspelled (blueberries, blackberries, rapberries, currants, gooseberries, etc.)."
    ),
    Spell('Heat Metal','D',2,
        cast=tp(4,S),
        duration=tp(7,R),
        sourcebook=V,
        desc=("By means of the <i>heat metal</i> spell, the druid is able to excite the molecules of ferrous metal (iron, iron alloys, steel) and thus cause the affected metal to become hot. On the first round of the spell, the effect is merely to cause the metal to be very warm and uncomfortable to touch, and this is also the effect on the last melee round of the spell's duration. The second and sixth (next to last) round effect is to cause blisters and damage; the third, fourth, and fifth rounds the metal becomes searing hot, causing disability and damage to exposed flesh, as shown below:\n\n"
            "<table>"
            "<tr><th>Metal Temperature</th><th>Damage Per Round</th><th>Disability Per Round</th></tr>"
            "<tr><td>very warm</td><td>none</td><td>none</td></tr>"
            "<tr><td>hot</td><td>1-4 hit points</td><td>none</td></tr>"
            "<tr><td>searing</td><td>2-8 hit points</td><td>hands or feet\n2-8 days\n\nhead\n1-4 turns unconsciousness\n\nbody\n1-4 days</td></tr>\n\n"
            "</table>"
            "Note also that materials such as wood, leather, or flammable cloth will smoulder and burn if exposed to searing hot metal, and such materials will then cause searing damage to exposed flesh on the next round. <i>Fire resistance</i> (potion or ring) or a <a href=\"/spells/protection-from-fire-druid-lvl-3/\"><i>protection from fire</i></a> spell totally negates the effects of a <i>heat metal</i> spell, as will immersion in water or snow, or exposure to a <a href=\"/spells/cone-of-cold-magic-user-lvl-5/\"><i>cold</i></a> or <a href=\"/spells/ice-storm-magic-user-lvl-4/\"><i>ice storm</i></a> spell. For each level of experience of the druid casting the spell, he or she is able to affect the metal of one man-sized creature, i.e. amrs and armor, or a single mass of metal equal to 500 gold pieces in weight, cumulative. The reverse, <i>chill metal</i>, counters a <i>heat metal</i> spell or else causes metal to act as follows:\n\n"
            "<table>"
            "<tr><th>Metal Temperature</th><th>Damage Per Round</th><th>Disability</th></tr>"
            "<tr><td>cold</td><td>none</td><td>none</td></tr>"
            "<tr><td>icy</td><td>1-2 hit points</td><td>none</td></tr>"
            "<tr><td>freezing</td><td>1-4 hit points</td><td>amputation of fingers, toes, nose, or ears</td></tr>"
            "</table>\n\n"
            "The <i>chill metal</i> spell is countered by a <a href=\"/spells/resist-cold-cleric-lvl-1/\"><i>resist cold</i></a> spell, or by any great heat, i.e. proximity to a blazing fire (not a mere torch), a magical <i>flaming sword</i>, a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a>, etc."
        )
    ),
    Spell('Locate Plants','D',2,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is used by a druid, he or she is able to locate any desired type of plant within the area of effect. Note: the plant type must be singular and concentrated upon. The spell's area of effect centers on, and moves with, the druid."
    ),
    Spell('Obscurement','D',2,
        cast=tp(4,S),
        duration_lvl=tp(4,R),
        sourcebook=V,
        desc="This spell causes a misty vapor to arise around the druid. It persists in this locale for 4 rounds per level of experience of the druid casting the spell, and it reduces visibility of any sort (including infravision) to 2' to 8' (2d4). The area of effect is a cubic progression based on the druid's level of experience, a 1\" cube at 1st level, a 2\" cube at 2nd level, a 3\" cube at 3rd level, and so on. Underground, the height of the vapor is restricted to 1\", although the length and breadth of the cloud is not so limited. A strong wind will cut the duration of an <i>obscurement</i> spell by 75%."
    ),
    Spell('Produce Flame','D',2,
        cast=tp(4,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="A bright flame, equal in brightness to a torch, springs forth from the druid's palm when he or she casts a <i>produce flame</i> spell. This magical flame lasts for 2 melee rounds for each level of the druid casting the spell. The flame does not harm the druid's person. but it is hot, and it will cause combustion of inflammable materials (paper, cloth, dry wood, oil, etc.). The druid is capable of hurling the magical flame as a missile, with a range of 4\". The flame will flash on impact, igniting combustibles within a 3' diameter of its center of impact. and then extinguish itself. The druid can cause it to go out any time he or she desires, but fire caused by the flame cannot be so extinguished."
    ),
    Spell('Reflecting Pool','D',2,
        cast=tp(2,H),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc=("This spell enables the druid to cause a pool of normal water found in a natural setting to act as a scrying device. The pool can be no greater diameter than 2 feet per level of the spell caster. The effect is to create a scrying device similar to a <i>crystal ball</i>, in much the same fashion as the magic-user spell <a href=\"/spells/magic-mirror-magic-user-lvl-4/\"><i>magic mirror</i></a> and the clerical spell <a href=\"/spells/magic-font-cleric-lvl-5/\"><i>magic font</i></a>. The scrying can extend only to those planes of existence which are coexistent with or border upon the Prime Material Plane, i.e. the Inner Planes (including the Para-elemental Planes, Plane of Shadow, <i>et al.</i>). Penalties for attempting to scry beyond the druid's own plane, as given in the description for <i>crystal ball</i> (see Dungeon Masters Guide) are applicable.\n\n"
            "The following spells can be cast through a <i>reflecting pool</i>, with a 5% per level chance of operating correctly: <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a>, <a href=\"/spells/detect-snares-pits-druid-lvl-1/\"><i>detect snares and pits</i></a>, <a href=\"/spells/detect-poison-druid-lvl-1/\"><i>detect poison</i></a>. Infravision and ultravision will operate normally through the <i>reflecting pool</i>, as will the spells <a href=\"/spells/starshine-druid-lvl-3/\"><i>starshine</i></a> and <a href=\"/spells/moonbeam-druid-lvl-5/\"><i>moonbeam</i></a>. The druid must use both mistletoe and the oil extracted from such nuts as the hickory and the walnut, refined, and dropped in three measures upon the surface of the pool. (A measure need be no more than a single ounce of oil.)"
        )
    ),
    Spell('Slow Poison','D',2,
        cast=tp(0),
        duration=tp(0),
        duration_lvl=tp(0),
        sourcebook=U,
        desc=("This spell is identical to the 2nd-level clerical spell <a href=\"/spells/slow-poison-cleric-lvl-2/\"><i>slow poison</i></a>, except that if the druid is able to determine that the poison was one made from some living plant, he or she has a 5% chance per level of knowing an herbal antidote which will neutralize the poison. (If the actual type of poison is not given by the Dungeon Master, a successful casting of <a href=\"/spells/detect-poison-druid-lvl-1/\"><i>detect poison [type]</i></a> indicates an organic poison which can be countered.) A dice roll equal to or less than the druid's chance to find an antidote indicates neutralization.\n\n"
            "The druid uses mistletoe as a material component for this spell, and crushed garlic must be rubbed on the recipient's feet. Antidotes must be obtained from green vegetables outdoors, or from an herbalist or similar source of supply."
        )
    ),
    Spell('Trip','D',2,
        cast=tp(4,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The spell caster must use a length of vine, a stick, pole, rope, or similar object to cast this magic upon. The <i>trip</i> spell causes the object to rise slightly off the ground or floor it is resting on and trip creatures crossing it if they fail to make their saving throw versus magic. Note that only as many creatures can be tripped as are actually stepping across the magicked object, i.e. a 3' long piece of rope could trip only 1 man-sized creature. Creatures moving at a very rapid pace (running) when tripped will take 1-6 (d6) hit points of damage and be stunned for 2-5 (d4+1) rounds if the surface they full upon is very hard, but if it is turf or non-hard they will merely be stunned for 2-5 segments. Very large creatures such as elephants will not be at all affected by a <i>trip</i>. The object magicked will continue to trip all creatures passing over it, including the spell caster, for as long as the spell duration lasts. Creatures aware of the object and its potential add +4 to their saving throw when crossing it. The object is 80% undetectable without magical means of detection."
    ),
    Spell('Warp Wood','D',2,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast the druid causes a volume of wood to bend and warp, permanently destroying its straightness, form and strength. The range of a <i>warp wood</i> spell is 1\" for each level of experience of the druid casting it. It affects approximately a fifteen inch shaft of wood of up to one inch diameter per level of the druid. Thus, at 1st level, a druid might be able to warp a hand axe handle, or four crossbow bolts, at 5th level he or she could warp the shaft of a typical magic spear. Note that boards or planks can also be affected, causing a door to be sprung or a boat or ship to leak."
    ),
    Spell('Call Lightning','D',3,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When a <i>call lightning</i> spell is cast, there must be a storm of some sort in the area — a rain shower, clouds and wind, hot and cloudy conditions, or even a tornado. The druid is then able to call down belts of lightning from sky to ground. Each bolt will cause damage equal to 2 eight-sided dice (2d8) plus 1 like die (d8) for each level of experience of the druid casting the spell. Thus, a 4th level druid calls down a six-die (6d8) bolt. The bolt of lightning flashes down in a perpendicular stroke at whatever distance the spell caster decides, up to the 36\" radial distance maximum. Any creature within a 1\" radius of the path or the point where the lightning strikes will take full damage, unless a saving throw is made, in which case only one-half damage is taken. Full/half damage refers to the number of hit dice of the lightning bolt, i.e. if it is of eight dice strength, the victim will take either eight dice (8d8) or four dice (4d8), if the saving throw is made, of damage. The druid is able to call one bolt of lightning every 10 melee rounds (1 turn), to a maximum number of turns equal to the level of experience he or she has attained, i.e. 1 bolt/turn for each level of experience. Note: This spell is normally usable outdoors only."
    ),
    Spell('Cloudburst','D',3,
        cast=tp(5,S),
        duration=tp(1,R),
        sourcebook=U,
        desc="This spell is essentially the same as the <a href=\"/spells/cloudburst-cleric-lvl-3/\">3rd-level clerical spell of the same name</a>, with only the following special notations and additions: Lightning cannot be called by the use of a <i>cloudburst</i> spell, and a <a href=\"/spells/call-lightning-druid-lvl-3/\"><i>call lightning</i></a> spell cannot be used in the same area at the same time. Also, the druid must use mistletoe as an additional material component."
    ),
    Spell('Cure Disease','D',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the 3rd level cleric <a href=\"/spells/cure-disease-cleric-lvl-3/\"><i>cure disease</i></a> spell, with the exception that the druid must have mistletoe to effect it. It is reversible to <i>cause disease</i> also."
    ),
    Spell('Hold Animal','D',3,
        cast=tp(5,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By means of this spell the druid holds one to four animals rigid. Animals affected are normal or giant-sized mammals, birds, or reptiles, but not monsters such as centaurs, gorgons, harpies, naga, etc. That is, apes, bears, crocodiles, dogs, eagles, foxes, giant beavers, and similar animals are subject to this spell. The <i>hold</i> lasts for 2 melee rounds per level of experience of the druid casting it. It is up to the druid as to how many animals he or she wishes to <i>hold</i> with the spell, but the greater the number, the better chance each will have of not being affected by the spell. Note that a maximum body weight of 400 pounds (100 pounds with respect to non-mammals)/animal/level of experience of the druid can be affected, i.e. an 8th level druid can affect up to four 3,200 pound mammals or a like number of 800 pound non-mammals such as birds or reptiles. Each animal gets a saving throw: if only 1 is the subject of the spell, it has a penalty of -4 on its die roll to save; if 2 are subject, they each receive a penalty of -2 on their die rolls; if 3 are subject, they each receive a penalty of -1 on their die rolls; if 4 are subject, each makes a normal saving throw."
    ),
    Spell('Know Alignment','D',3,
        cast=tp(5,S),
        duration=tp(5,R),
        sourcebook=U,
        desc="This spell is essentially the same as the <a href=\"/spells/know-alignment-cleric-lvl-2/\">2nd-level clerical spell</a> of the same name, except as noted above, and with the following additional difference. Because of the shorter duration, only five creatures (maximum) can be examined by this spell, and it cannot be reversed."
    ),
    Spell('Neutralize Poison','D',3,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the 4th level cleric <a href=\"/spells/neutralize-poison-cleric-lvl-4/\"><i>neutralize poison</i></a> spell (q.v.)."
    ),
    Spell('Plant Growth','D',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a <i>plant growth</i> spell is cast by the druid, he or she causes normal vegetation to grow, entwine, and entangle to form a thicket or jungle which creatures must hack or force a way through at a movement rate of 1\" per, or 2\" per with respect to larger than man-sized creatures. Note that the area must have brush and trees in it in order to allow this spell to go into effect. Briars, bushes, creepers, lianas, roots, saplings, thistles, thorn, trees, vines, and weeds become so thick and overgrown in the area of effect as to form a barrier. The area of effect is 2\" x 2\" square per level of experience of the druid, in any square or rectangular shape that the druid decides upon at the time of the spell casting. Thus an 8th level druid can affect a maximum area of 16\" x 16\" square, a 32\" x 8\" rectangle, a 64\" X 4\" rectangle, 128\" x 2\" rectangle, etc. The spell's effects persist in the area until it is cleared by labor, fire, or such magical means as a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell."
    ),
    Spell('Protection From Fire','D',3,
        cast=tp(5,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The effect of a <i>protection from fire</i> spell differs according to the recipient of the magic — the druid or some other creature. If the spell is cast upon the druid, it confers complete invulnerability to normal fires (torches, bonfires, oil fires, and the like) and to exposure to magical fires such as demon fire, <a href=\"/spells/burning-hands-magic-user-lvl-1/\"><i>burning hands</i></a>, fiery dragon breath, <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fire ball</i></a>, <a href=\"/spells/fire-seeds-druid-lvl-6/\"><i>fire seeds</i></a>, <a href=\"/spells/fire-storm-druid-lvl-7/\"><i>fire storm</i></a>, <a href=\"/spells/flame-strike-cleric-lvl-5/\"><i>flame strike</i></a>, hell hound breath, <a href=\"/spells/meteor-swarm-magic-user-lvl-9/\"><i>meteor swarm</i></a>, pyrohydra breath, etc. until an accumulation of 12 hit points of potential damage per level of experience of the druid has been absorbed by the <i>protection from fire</i> spell, at which time the spell is negated. Otherwise the spell lasts for 1 turn per level of experience of the druid. If the spell is cast upon another creature, it gives invulnerability to normal fire, gives a bonus of +4 on saving throw die rolls made versus fire attacks, and reduces damage sustained from magical fires by 50%."
    ),
    Spell('Pyrotechnics','D',3,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="A <i>pyrotechnics</i> spell can have either of two effects. It produces a flashing and fiery burst of glowing, colored aerial <i>fireworks</i> which lasts 1 segment per experience level of the druid casting the spell and temporarily blinds those creatures in the area of effect or under it or within 12\" of the area (and in any event in unobstructed line of sight); or it causes a thick writhing stream of <i>smoke</i> to arise from the fire source of the spell and form a choking cloud which lasts for 1 round per experience level of the druid casting it, covering a roughly globular area from the ground or floor up (or conforming to the shape of a confined area), which totally obscures vision beyond 2'. The spell requires a fire of some sort in range. The area of <i>pyrotechnics</i> effect is 10 times the volume of the fire source with respect to <i>fireworks</i>, 100 times with respect to <i>smoke</i>. In either case, the fire source is immediately extinguished by the employment of the spell."
    ),
    Spell('Snare','D',3,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell enables the druid to make a <i>snare</i> which is 90% undetectable without magical aid. The <i>snare</i> can be made from any supple vine, a thong, or a rope. When the <i>snare</i> spell is cast upon it, the cordlike object blends with the background of its location. One end of the <i>snare</i> is tied in a loop which will contract about 1 or more of the limbs of any creature stepping inside the circle (note that the head of a worm or snake could also be thus ensnared). If a strong and supple tree is nearby, the snare will be fastened to it, and the dweomer of the spell will cause it to bend and then straighten when the loop is triggered, thus causing 1-6 hit points of damage to the creature trapped, and lifting it off the ground by the trapped member(s) (or strangling it if the head/neck triggered the <i>snare</i>). If no such sapling or tree is available, the cord-like object will tighten upon the member(s) and then enwrap the entire creature, doing no damage, but tightly binding it. The snare is magical, so for 1 hour it is breakable only by storm giant or greater strength (23); each hour thereafter, the snare material loses magic so as to become 1 point more breakable per hour — 22 after 2 hours, 21 after 3, 20 after 4 — until 6 full hours have elapsed. At that time, 18 strength will break the bonds. After 12 hours have elapsed, the materials of the <i>snare</i> lose all of the magical properties, and the loop opens, freeing anything it had held. The druid must have a snake skin and a piece of sinew from a strong animal to weave into the cord-like object from which he or she will make the <i>snare</i>. Only mistletoe is otherwise needed."
    ),
    Spell('Spike Growth','D',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="This spell is essentially the same as the <a href=\"/spells/spike-growth-cleric-lvl-4/\">4th-level clerical spell</a> of the same name, except as noted above, and with the following additional differences: The affected area will radiate an aura of magic, and a <a href=\"/spells/detect-snares-pits-druid-lvl-1/\"><i>detect snares and pits</i></a> spell will reveal the location of the <i>spike growth</i>. The druid must use mistletoe as a material component (in place of the cleric's holy symbol) in addition to the seven small twigs or thorns."
    ),
    Spell('Starshine','D',3,
        cast=tp(5,S),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="A <i>starshine</i> spell enables the druid to softly illuminate an area as if it were exposed to a clear night sky filled with stars. Regardless of the height of the open area in which the spell is cast, the area immediately beneath it will be lit by <i>starshine</i>. Vision will be clear at up to 30', indistinct out to 60', and beyond that only gleams and glitters will be discernible. The <i>starshine</i> allows shadows. It enhances ultravision to its full potential but does not affect infravision. The spell makes the area of effect actually appear to be a night sky, but disbelief of the illusion merely allows the disbeliever to note that the \"stars\" are actually evoked lights. The material components are several stalks from an amaryllis (especially Hypoxis) and several holly berries."
    ),
    Spell('Stone Shape','D',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is exactly the same as the fifth level magic-user spell, <a href=\"/spells/stone-shape-magic-user-lvl-5/\"><i>stone shape</i></a>, except as noted above and for the requirement of mistletoe as an additional component to enable a druid to cast the spell."
    ),
    Spell('Summon Insects','D',3,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When a <i>summon insects</i> spell is cast by a druid, he or she attracts flying insects 70% of the time. The exact insects called will be bees, biting flies, hornets, or wasps if flying insects are indicated, or biting ants or pinching beetles if non-flying insects are determined. A cloud of the flying type, or a swarm of the crawling sort, will appear after the spell is cast. They will attack any creature the druid points to. The attacked creature will sustain 2 hit points of damage per melee round, and it can do nothing but attempt to fend off these insects during the time it is so attacked. The summoned insects can be caused to attack another opponent, but there will be at least a 1 round delay while they leave the former recipient and attack the new victim, and crawling insects can travel only about 12' per round (maximum speed over smooth ground). It is possible in underground situations that the druid could summon 1-4 giant ants by means of the spell, but the possibility is only 30% unless giant ants are nearby. The materials needed for this spell are mistletoe, a flower and a bit of mud or wet clay."
    ),
    Spell('Tree','D',3,
        cast=tp(5,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By means of this spell the druid is able to assume the form of a small living tree or shrub or that of a large dead tree trunk with but a few limbs. Although the closest inspection will not reveal that this plant is actually a druid, and for all normal tests he or she is, in fact, a tree or shrub, the druid is able to observe all that goes on around his or her person just as if he or she were in human form. The spell caster may remove the dweomer at any time he or she desires, instantly changing from plant to human form, and having full capability of undertaking any action normally possible to the druid. Note that all clothing and gear worn/carried change with the druid. The material components of this spell are mistletoe and a twig from a tree."
    ),
    Spell('Water Breathing','D',3,
        cast=tp(5,S),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="The recipient of a <i>water breathing</i> spell is able to freely breathe underwater for the duration of the spell, i.e. 6 turns for each level of experience of the druid casting the spell. The reverse, <i>air breathing</i>, allows water breathing creatures to comfortably survive in the atmosphere for an equal duration."
    ),
    Spell('Animal Summoning I','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this spell, the druid calls up to eight animals of whatever sort the druid names when the summoning is made, if such type are within spell range. These animals can have no more than four hit dice each. The animals summoned will aid the druid by whatever means they possess, staying until a fight is over, a specific mission is finished, the druid is safe, he or she sends them away, etc. The druid may try three times to summon three different sorts of animals, i.e. suppose that wild dogs are first summoned to no avail, then hawks are unsuccessfully called, and finally the druid calls for wild horses which may or may not be within summoning range. Your referee will determine probabilities if the presence of a summoned animal type is not known. Other than various sorts of giant animals, fantastic animals or monsters cannot be summoned lay this spell, i.e. no chimerae, dragons, gorgons, manticores, etc."
    ),
    Spell('Call Woodland Beings','D',4,
        cast=tp(2,T),
        duration=tp(1,P),
        sourcebook=V,
        desc=("By means of this spell the druid is able to summon certain woodland creatures to his or her location. Naturally, this spell will only work outdoors, but not necessarily only in wooded areas. The druid begins the incantation, and the spell must be continued uninterrupted until some called creature appears or 2 turns have elapsed. (The verbalization and somatic gesturing are easy, so this is not particularly exhausting to the spell caster.) Only 1 type of the following sorts of beings can be summoned by the spell, and they will come only if they are within the range of the call:\n\n"
            "<table>"
            "<tr><th>Creature</th><th>Quantity</th></tr>"
            "<tr><td>Brownie</td><td>2-8</td></tr>"
            "<tr><td>Centaur</td><td>1-4</td></tr>"
            "<tr><td>Dryad</td><td>1-4</td></tr>"
            "<tr><td>Pixie</td><td>1-8</td></tr>"
            "<tr><td>Satyr</td><td>1-4</td></tr>"
            "<tr><td>Sprite</td><td>1-6</td></tr>"
            "<tr><td>Treant</td><td>1</td></tr>"
            "<tr><td>Unicorn</td><td>1</td></tr>"
            "</table>\n\n"
            "(Your referee will consult his outdoor map or base the probability of any such creature being within spell range upon the nature of the area the druid is in at the time of spell casting.)\n\n"
            "The creature(s) called by the spell are entitled to a saving throw versus magic (at -4) to avoid the summons. Any woodland being answering the <i>call</i> will be favorably disposed to the spell caster and give whatever aid it is capable of. However, if the caller or members of the caller's party are of evil alignment, the creatures are entitled to another saving throw versus magic (this time at +4) when they come within 1\" of the druid or other evil character with him or her, and these beings will seek immediately to escape if the saving throw is successful. In any event, if the druid requests that the summoned creatures engage in combat on behalf of the druid, they are required to make a loyalty reaction score based on the druid's charisma and whatever dealings he or she has has with the called creature(s). The material components of this spell are a pinecone and 8 holly berries."
        )
    ),
    Spell('Control Temperature, 10\' Radius','D',4,
        cast=tp(6,S),
        duration=tp(4,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast by the druid, the temperature surrounding the druid can be altered by 9 degrees Fahrenheit (5ºC) per level of experience of the spell caster, either upwards or downwards. Thus, a 10th level druid could raise the surrounding temperature from 1 to 90 degrees (1-50ºC) or lower it by from 1 to 90 degrees (1-50ºC). The spell lasts for a number of turns equal to 4 plus the level of experience of the druid, i.e. when cast by a 10th level druid the spell persists for 14 turns."
    ),
    Spell('Cure Serious Wounds','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the 4th level cleric <a href=\"/spells/cure-serious-wounds-cleric-lvl-4/\"><i>cure serious wounds</i></a> spell (q.v.), with the exception of the fact that the spell requires the use of any sort of mistletoe."
    ),
    Spell('Dispel Magic','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the 3rd level cleric <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell."
    ),
    Spell('Hallucinatory Forest','D',4,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By casting this spell the druid causes the appearance of an <i>hallucinatory forest</i> to come into existence. The illusionary forest appears to be perfectly natural and is indistinguishable from a real forest. Other druids — as well as such creatures as centaurs, dryads, green dragons, nymphs, satyrs, and treants — will recognize the forest for what it is. All other creatures will believe it is there, and movement and order of march will be affected accordingly. The <i>hallucinatory forest</i> will remain until it is magically dispelled by a reverse of the spell or a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>. The area shape is either rectangular or square, in general, at least 4\" deep, and in whatever location the druid casting the spell desires. The forest can be of less than maximum area if the druid wishes. One of its edges will appear up to 8\" away from the druid, according to the desire of the spell caster."
    ),
    Spell('Hold Plant','D',4,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="The <i>hold plant</i> spell affects vegetable matter as follows: 1) it causes ambulatory vegetation to cease moving; 2) it prevents vegetable matter from entwining, grasping, closing, or growing; 3) it prevents vegetable matter from making any sound or movement which is not caused by wind. The spell effects apply to all forms of vegetation, including parasitic and fungoid types, and those magically animated or otherwise magically empowered. It affects such monsters as green slime, moulds of any sort, shambling mounds, shriekers, treants, etc. The duration of a <i>hold plant</i> spell is 1 melee round per level of experience of the druid casting the spell. It affects from 1 to 4 plants — or from 4 to 16 square yards of small ground growth such as grass or mould. If but one plant (or 4 square yards) is chosen as the target for the spell by the druid, the saving throw of the plant (or area of plant growth) is made at a -4 on the die; if two plants (or 8 square yards) are the target, saving throws are at -2; if three plants (or 12 square yards) are the target, saving throws are at -1; and if the maximum of 4 plants (or 16 square yards of area) are the target, saving throws are normal."
    ),
    Spell('Plant Door','D',4,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>plant door</i> spell opens a magical portal or passageway through trees, undergrowth, thickets, or any similar growth — even growth of a magical nature. The <i>plant door</i> is open only to the druid who cast the spell, druids of a higher level, or dryads. The <i>door</i> even enables the druid to enter into a solid tree trunk and remain hidden there until the spell ends. If the tree is cut down or burned, the druid must leave before the tree falls or is consumed, or else he or she is killed also. The duration of the spell is 1 turn per level of experience of the druid casting it. If the druid opts to stay within an oak, the spell lasts 9 times longer, if an ash tree it lasts 3 times as long. The path created by the spell is up to 4' wide, 8' high and 12' per level of experience of the druid long."
    ),
    Spell('Produce Fire','D',4,
        cast=tp(6,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="By means of this spell the druid causes a common-type fire of up to 12' per side in area boundary. While it lasts but a single round, the fire produced by the spell will cause 1-4 hit points of damage on creatures within its area; and it will ignite combustible materials such as cloth, oil, paper, parchment, wood and the like so as to cause continued burning. The reverse, <i>quench fire</i> will extinguish any normal fire (coals, oil, tallow, wax, wood, etc.) within the area of effect."
    ),
    Spell('Protection From Lightning','D',4,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="This spell is exactly the same as the 3rd level <a href=\"/spells/protection-from-fire-druid-lvl-3/\"><i>protection from fire</i></a> spell (q.v.) except that it applies to electrical/lightning attacks."
    ),
    Spell('Repel Insects','D',4,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast the druid creates an invisible barrier to all sorts of insects, and normal sorts will not approach within 10' of the druid while the spell is in effect, although any giant insects with 2 or more hit dice will do so if they make a saving throw versus magic, and even those which do so will sustain 1-6 hit points of damage from the passing of the magical barrier. Note that the spell does not in any way affect arachnids, myriapods, and similar creatures — it affects only true insects. The material components of the <i>repel insects</i> spell are mistletoe and one of the following: several crushed marigold flowers, a whole crushed leek, 7 crushed stinging nettle leaves or a small lump of resin from a camphor tree."
    ),
    Spell('Speak With Plants','D',4,
        cast=tp(1,T),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Except as noted above, and that the material component is that typically druidic (mistletoe, et al.), the spell is the same as the 4th level cleric spell <a href=\"/spells/speak-with-plants-cleric-lvl-4/\"><i>speak with plants</i></a>."
    ),
    Spell('Animal Growth','D',5,
        cast=tp(7,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="When this spell is cast, the druid causes all animals, up to a maximum of 8, within a 2\" square area to grow to twice their normal size. The effects of this growth are doubled hit dice (with resultant improvement in attack potential) and doubled damage in combat. The spell lasts for 2 melee rounds for each level of experience of the druid casting the spell. Note that the spell is particularly useful in conjunction with a <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charm person or mammal</i></a> or a <a href=\"/spells/speak-with-animals-cleric-lvl-2/\"><i>speak with animals</i> spell. The reverse reduces animal size by one half, and likewise reduces hit dice, attack damage, etc."
    ),
    Spell('Animal Summoning II','D',5,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same in duration and effect as the 4th level <a href=\"/spells/animal-summoning-i-druid-lvl-4/\"><i>animal summoning I</i></a> spell, except that up to six animals of no more than eight hit dice each can be called, or 12 animals of no more than four hit dice each can be called."
    ),
    Spell('Anti-Plant Shell','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>anti-plant shell</i> spell creates an invisible barrier which keeps out all creatures or missiles of living vegetable material. Thus, the druid (and any creatures within the shell) is protected from attacking plants or vegetable creatures such as shambling mounds or treants. The spell lasts for one turn per level of experience of the druid."
    ),
    Spell('Commune With Nature','D',5,
        cast=tp(1,T),
        duration=tp(0),
        sourcebook=V,
        desc="This spell enables the druid to become one with nature in the area, thus being empowered with knowledge of the surrounding territory. For each level of experience of the druid, he or she may \"know\" one fact, i.e. the ground ahead, left or right, the plants ahead, left or right, the minerals ahead, left or right, the water courses/bodies of water ahead, left or right, the people dwelling ahead, left or right, etc. The spell is effective only in outdoors settings, and operates in a radius of one half mile for each level of experience of the druid casting the <i>commune with nature</i> spell."
    ),
    Spell('Control Winds','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By means of a <i>control winds</i> spell the druid is able to alter wind force in the area of effect. For every level of his or her experience, the druid is able to increase or decrease wind force by 3 miles per hour. Winds in excess of 30 miles per hour drive small flying creatures (those eagle-sized and under) from the skies and severely inhibit missile discharge. Winds in excess of 45 miles per hour drive even man-sized flying creatures from the skies. Winds in excess of 60 miles per hour drive all flying creatures from the skies and uproot trees of small size, knock down wooden structures, tear off roofs, etc. Winds in excess of 75 miles per hour are of hurricane force and cause devastation to all save the strongest stone constructions. A wind above 30 miles per hour makes sailing difficult, above 45 miles per hour causes minor ship damage, above 60 miles per hour endangers ships, and above 75 miles per hour sinks ships. There is an \"eye\" of 4\" radius around the druid where the wind is calm. A higher level druid can use a <i>control winds</i> spell to counter the effects of a like spell cast by a lower level druid (cf. <a href=\"/spells/control-weather-cleric-lvl-7/\"><i>control weather</i></a>). The spell remains in force for 1 turn for each level of experience of the druid casting it. Once the spell is cast, the wind force increases by 3 miles per hour per round until maximum speed is attained. When the spell is exhausted, the force of the wind diminishes at the same rate. Note that while the spell can be used in underground places, the \"eye\" will shrink in direct proportion to any confinement of the wind effect, i.e. if the area of effect is a 48\" radius, and the confined space allows only a 46\" radius, the \"eye\" will be 2\" radius; and any space under 44\" radius will completely eliminate the \"eye\" and subject the spell caster to the effects of the wind."
    ),
    Spell('Insect Plague','D',5,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="Except as noted above, and other than the fact that the material component needed for the spell is mistletoe or the holly or oak leaves substitute, the spell is the same as the 5th level cleric <a href=\"/spells/insect-plague-cleric-lvl-5/\"><i>insect plague</i></a> spell."
    ),
    Spell('Moonbeam','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="By means of this spell the druid is able to cause a beam of soft, pale light to strike downward from overhead and illuminate whatever area he or she is pointing at. The light is exactly the same as moonlight, so that colors other than shades of black, gray, or white will not be determinable. The spell caster can easily cause the <i>moonbeam</i> to move to any area that he or she can see and point to. This makes the spell an effective way to spotlight something, for example an opponent. While the <i>moonbeam</i> allows shadows, a creature centered in a <i>moonbeam</i> spell is most certainly under observation. The reflected light from this spell allows dim visual perception 1\" beyond the area of affect. The light does not adversely affect infravision, and enhances ultravision to its greatest potential. The material components are several seeds of any moonseed plant and a piece of opalescent feldspar (moonstone)."
    ),
    Spell('Pass Plant','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("By using this spell, a druid is able to enter a tree and move from inside it to another of the same type which lies in approximately the direction desired by the spell user and is within the range shown below:\n\n"
            "<table>"
            "<tr><th>Type of Tree</th><th>Range of Area of Effect</th></tr>"
            "<tr><td>Oak</td><td>60\"</td></tr>"
            '<tr><td>Ash</td><td>54"</td></tr>'
            '<tr><td>Yew</td><td>48"</td></tr>'
            '<tr><td>Elm</td><td>42"</td></tr>'
            '<tr><td>Linden</td><td>36"</td></tr>'
            '<tr><td>deciduous</td><td>30"</td></tr>'
            '<tr><td>coniferous</td><td>24"</td></tr>'
            '<tr><td>other</td><td>18"</td></tr>'
            '</table>\n\n'
            "The tree entered and that receiving the druid must be of the same type, living, and of girth at least equal to the druid. Note that if the druid enters a tree, suppose an ash, and wishes to pass north as far as possible (54\"), but the only appropriate ash in range is south, the druid will pass to the ash in the south. The <i>pass plant</i> spell functions so that the movement takes only one segment (6 seconds) of a round. The druid may, at his or her option, remain within the receiving tree for a maximum of 1 round per level of experience. Otherwise, he or she may step forth immediately. Should no like tree be in range, the druid simply remains within the tree, does not pass elsewhere, and must step forth in the applicable number of rounds. (See <a href=\"/spells/plant-door-druid-lvl-4/\"><i>plant door</i></a> for effects of chopping or burning such a tree.)"
        )
    ),
    Spell('Spike Stones','D',5,
        cast=tp(6,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell is the same as the <a href=\"/spells/spike-stones-cleric-lvl-5/\">5th-level clerical spell</a> of the same name."
    ),
    Spell('Sticks To Snakes','D',5,
        cast=tp(7,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Except as noted above, and for the fact that the material component of the spell is typical for druids, this is the same as the 4th level cleric <a href=\"/spells/sticks-to-snakes-cleric-lvl-4/\"><i>sticks to snakes</i></a> spell."
    ),
    Spell('Transmute Rock To Mud','D',5,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell turns natural rock of any sort into an equal volume of mud. The depth of the mud can never exceed one-half its length and/or breadth. If it is cast upon a rock, for example, the rock affected will collapse into mud. Creatures unable to levitate, fly, or otherwise free themselves from the mud will sink and suffocate, save for lightweight creatures which could normally pass across such ground. The mud will remain until a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell or a reverse of this spell, <i>mud to rock</i>, restores its substance — but not necessarily its form. Evaporation will turn the mud to normal dirt, from 1 to 6 days per cubic 1\" being required. The exact time depends on exposure to sun, wind and normal drainage. The <i>mud to rock</i> reverse will harden normal mud into soft stone (sandstone or similar mineral) permanently unless magically changed."
    ),
    Spell('Wall of Fire','D',5,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="The <i>wall of fire</i> spell brings forth a blazing curtain of magical fire of shimmering color — yellow-green or amber in case of druidical magic. The <i>wall of fire</i> inflicts 4 to 16 hit points of damage, plus 1 hit point of damage per level of the spell caster, upon any creature passing through it. Creatures within 1\" of the wall take 2-8 hit points of damage, those within 2\", take 1-4 hit points of damage. Creatures especially subject to fire may take additional damage, and undead always take twice normal damage. Only the side of the wall away from the spell caster will inflict damage. The opaque <i>wall of fire</i> lasts for as long as the druid concentrates on maintaining it, or 1 round per level of experience of the druid in the event he or she does not wish to concentrate upon it. The spell creates a sheet of flame up to 2\" square per level of the spell caster, or as a ring with a radius of up to ½\" per level of experience from the druid to its flames, and a height of 2\". The former is stationary, while the latter moves as the druid moves."
    ),
    Spell('Animal Summoning III','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same in duration and effect as the 4th level <a href=\"/spells/animal-summoning-i-druid-lvl-4/\"><i>animal summoning I</i></a> spell except that up to 4 animals of no more than 16 hit dice each can be summoned, or eight of no more than 8 hit dice, or 16 creatures of no more than 4 hit dice each can be summoned."
    ),
    Spell('Anti-Animal Shell','D',6,
        cast=tp(1,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By casting this spell the druid brings into being a hemispherical force field which prevents the entrance of any sort of animal matter of normal (not magical) nature. Thus, a giant would be kept out, but undead could pass through the shell of force, as could such monsters as aerial servants, demons, devils, etc. The <i>anti-animal shell</i> lasts for 1 turn for each level of experience the druid has attained."
    ),
    Spell('Conjure Fire Elemental','D',6,
        cast=tp(6,R),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="Upon casting a <i>conjure fire elemental</i> spell, the druid opens a special gate to the Elemental Plane of Fire, and a strong <a href=\"/creatures/fire-elemental/\">fire elemental</a> is summoned to the vicinity of the spell caster. It is 85% likely that a 16 die elemental will appear, 9% likely that 2 to 4 <a href=\"/creatures/salamander/\"><i>salamanders</i></a> will come, a 4% chance exists that an <a href=\"/creatures/efreeti/\"><i>efreeti</i></a> will come, and a 2% chance exists that a huge fire elemental of 21 to 24 hit dice (d4 + 20) will appear. Because of the relationship of druids to natural and elemental forces, the conjuring druid need not fear that the elemental force summoned will turn on him or her, so concentration upon the activities of the fire elemental (or other creature, summoned) or the protection of a magic circle is not necessary. The elemental summoned will help the druid however possible, including attacking opponents of the druid. The fire elemental or other creature summoned remains for a maximum of 1 turn per level of the druid casting the spell — or until it is sent back by attack, a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell or the reverse of the spell (<i>dismiss fire elemental</i>). Only a druid can dismiss summoned salamanders, efreeti, or ultra-powerful elemental."
    ),
    Spell('Cure Critical Wounds','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the 5th level cleric <a href=\"/spells/cure-critical-wounds-cleric-lvl-5/\"><i>cure critical wounds</i></a> spell (q.v.), with the exception of the fact that the spell requires the use of any sort of mistletoe."
    ),
    Spell('Feeblemind','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc=("A spell which is solely for employment against those persons or creatures who use magic spells, <i>feeblemind</i> causes the victim's brain to become that of a moronic child. The victim remains in this state until a <i>heal</i>, <i>restoration</i> or <i>wish</i> spell is used to do away with the effects. The spell is of such a nature that the probability of it affecting the target creature is generally enhanced, i.e. saving throws are lowered.\n\n"
            "<table>"
            "<tr><th>Type of Spells Used by Target Creature</th><th>Saving Throw Adjustment</th></tr"
            "<tr><td>Cleric</td><td>+1</td></tr>"
            "<tr><td>Druid</td><td>-1</td></tr>"
            "<tr><td>Magic-user (human)</td><td>-4</td></tr>"
            "<tr><td>Illusionist</td><td>-5</td></tr>"
            "<tr><td>Combination or non-human</td><td>-2</td></tr>"
            "</table>\n\n"
            "Note that this spell has no material component."
        )
    ),
    Spell('Fire Seeds','D',6,
        cast=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The spell of <i>fire seeds</i> creates special missiles or timed incendiaries which burn with great heat. The druid may hurl these seeds up to 4\" or place them to ignite upon a command word. Acorns become <i>fire seed</i> missiles, while holly berries are used as the timed incendiaries. The spell creates up to four acorn <i>fire seeds</i> or eight holly berry <i>fire seeds</i>. The acorns burst upon striking their target, causing 2 to 16 hit points (2d8) of damage and igniting any combustible materials within a 1\" diameter of the point of impact. Although the holly berries are too light to make effective missiles, they can be placed, or tossed up to 6' away, to burst into flame upon a word of command. The berries ignite causing 1 to 8 hit points (d8) of damage to any creature in a ½\" diameter burst area, and their fire ignites combustibles in the burst area. The command range for holly berry <i>fire seeds</i> is 4\". All <i>fire seeds</i> lose their power after the expiration of 1 turn per level of experience of the druid casting the spell, i.e. a 13th level druid has <i>fire seeds</i> which will remain potent for a maximum of 13 turns after their creation. Targets of acorn <i>fire seeds</i> must be struck by the missile. If a saving throw is made, creatures within the burst area take only one-half damage, but creatures struck directly always take full damage. Note that no mistletoe or other material components beyond acorns or holly berries are needed for this spell."
    ),
    Spell('Liveoak','D',6,
        cast=tp(1,T),
        duration_lvl=tp(1,D),
        sourcebook=U,
        desc="This spell enables the druid to select a healthy oak tree and cast a dweomer upon it so as to cause it to serve as a protector. The spell can be cast on but a single tree at a time, and while a <i>liveoak</a> cast by a particular druid is in effect, he or she cannot cast another such spell. The tree upon which the dweomer is cast must be within 10 feet of the druid's dwelling place, within a place sacred to the druid, or within 10' of something the druid wishes to guard or protect. The <i>liveoak</i> spell can be cast upon a healthy tree of small, medium, or large size according to desire and availability. A \"triggering\" phrase of up to a maximum of one word per level of the spell caster is then placed upon the dweomered oak; for instance \"Attack any persons who come near without first saying 'sacred mistletoe'\" is an 11-word trigger phrase that could be used by a druid of 11th or higher level casting the spell. The <i>liveoak</i> triggers the tree into becoming a treant of appropriate size and attack capability, matching the specifications of the Monster Manual description, but with only a 3\" movement rate. An oak enchanted by this spell will radiate a magic aura, and can be returned to normal by a successful casting of <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> or upon the desire of the druid who enchanted it. The druid needs mistletoe to cast this spell."
    ),
    Spell('Transmute Water To Dust','D',6,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=U,
        desc=("When this spell is cast, the subject area instantly undergoes a change from liquid to powdery dust. Note that if the water is already muddy, the area of effect will be expanded to double normal, while if wet mud is concerned the area of effect will be quadrupled. If water remains in contact with the transmuted dust, the former will quickly permeate the latter, turning dust into silty mud if a sufficient quantity of water exists to do so, otherwise soaking or dampening the dust accordingly."
            "Only liquid actually existing in the area of effect at the moment of spell casting is affected. Liquids which are only partially water will be affected insofar as the actual water is concerned, except that potions which contain water as a component part will be rendered useless. Living creatures are unaffected, except for those native to the Elemental Plane of Water. Such creatures receive a saving throw versus spell to escape the effect, and only one such creature can be affected by any single casting of this spell, regardless of the creature's size or the size of the spell's area of effect. The reverse of the spell is simply a very high-powered <a href=\"/spells/create-water-cleric-lvl-1/\"><i>create water</i></a> spell which requires a pinch of normal dust as an additional material component. For either usage of the spell, other components required are diamond dust of at least 500 gp value, a bit of seashell, and the druid's mistletoe."
        )
    ),
    Spell('Transport Via Plants','D',6,
        cast=tp(3,S),
        duration=tp(1,D),
        sourcebook=V,
        desc="By means of this spell, the druid is able to enter any large plant and pass any distance to a plant of the same species in a single round regardless of the distance separating the two. The entry plant must be alive. The destination plant need not be familiar to the druid, but it also must be alive. If the druid is uncertain of the destination plant, he or she need merely determine direction and distance, and the <i>transport via plants</i> spell will move him or her as near as possible to the desired location. There is a basic 20% chance, reduced 1% per level of experience of the druid, that the transport will deliver the druid to an allied species of plant from 1 to 100 miles removed from the desired destination plant. If a particular destination plant is desired, but the plant is not living, the spell fails, and the druid must come forth from the entrance plant within 24 hours. Harm to a plant housing a druid can affect the druid (cf. <a href=\"/plant-door-druid-lvl-4/\"><i>plant door</i></a>)."
    ),
    Spell('Turn Wood','D',6,
        cast=tp(8,S),
        duration_lvl=tp(4,R),
        sourcebook=V,
        desc="When this spell is cast, waves of force roll forth from the druid, moving in the direction he or she faces, and causing all wooden objects in the path of the spell to be pushed away from the druid to the limit of the area of effect. Wooden objects above three inches diameter which are fixed firmly will not be affected, but loose objects (movable mantlets, siege towers, etc.) will move back. Objects under 3 inches diameter which are fixed will splinter and break and the pieces will move with the wave of force. Thus, objects such as wooden shields, spears, wooden weapon shafts and hafts, and arrows and bolts will be pushed back, dragging those carrying them with them; and if a spear is planted in order to prevent this forced movement, it will splinter. The <i>turn wood</i> spell lasts for 4 rounds per level of experience of the druid casting it, and the waves of force will continue to sweep down the set path for this period. The wooden objects in the area of effect are pushed back at a rate of 4\" per melee round. The length of the path is 2\" per level of the druid, i.e. a 14th level druid casts a <i>turn wood</i> spell with an area of effect 12\" wide by 28\" long, and the spell would last for 56 rounds (5.6 turns). As usual, the above assumes the druid is using greater mistletoe when casting the spell. Note that after casting the spell the path is set, and the druid may then do other things or go elsewhere without affecting the spell's power."
    ),
    Spell('Wall of Thorns','D',6,
        cast=tp(8,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>wall of thorns</i> spell creates a barrier of very tough, pliable green angled brush bearing needle-sharp thorns as long as a person's finger. Any creature breaking through (or merely impacting upon) the <i>wall of thorns</i> takes 8 hit points of damage plus an additional amount of hit points equal to the creature's armor class, i.e. 10 or fewer additional hit points of damage, with negative armor classes subtracting from the base 8 hit points of damage. Any creature within the area of effect of the spell when it is cast is considered to have impacted on the <i>wall of thorns</i> and in addition must break through to gain movement space. The damage is based on each 1\" thickness of the barrier. If the <i>wall of thorns</i> is chopped at, it will take at least 4 turns to cut a path through a 1\" thickness. Normal fire will not harm the barrier, but magical fires will burn away the barrier in 2 turns with the effect of creating a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a> while doing so. The nearest edge of the <i>wall of thorns</i> appears up to 8\" distant from the druid, as he or she desires. The spell lasts for 1 turn for each level of experience of the druid casting it, and covers an area of ten cubic inches per level of the caster in whatever form the caster desires. Thus a 14th level druid could create a <i>wall of thorns</i> 7\" long by 2\" high (or deep) by)\" deep (or high), a 1\" high by 1\" wide by 14\" long wall to block a dungeon passage, or any other sort of shape that suited his or her needs."
    ),
    Spell('Weather Summoning','D',6,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The druidic <i>weather summoning</i> spell is similar to the <a href=\"/spells/control-weather-cleric-lvl-7/\"><i>control weather</i></a> spell of clerical nature. By casting the spell, the druid calls forth weather commensurate with the climate and season of the area he or she is in at the time. Thus, in spring a tornado, thunderstorm, cold, sleet storm, or hot weather could be summoned. In summer a torrential rain, heat wave, hail storm, etc. can be called for. In autumn, hot or cold weather, fog, sleet, etc. could be summoned. Winter allows great cold, blizzard, or thaw conditions to be summoned. Hurricane-force winds can be summoned near coastal regions in the late winter or early spring. The summoned weather is not under the control of the druid. It might last but a single turn in the case of a tornado, or for hours or even days in other cases. The area of effect likewise varies from about 1 square mile to 100 or more square miles. Note that several druids can act in concert to greatly affect weather, controlling winds and/or working jointly to summon very extreme weather conditions. Within 4 turns after the spell is cast, the trend of the weather to come will be apparent, i.e., clearing skies, gusts of warm or hot air, a chill breeze, overcast skies, etc. Summoned weather will arrive 6 to 17 turns (d12 + 5) after the spell is cast. Anything less than <i>greater mistletoe</i> as the material component will sharply curtail the weather extremes desired."
    ),
    Spell('Animate Rock','D',7,
        cast=tp(9,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By employing an <i>animate rock</i> spell, the druid causes a lithic object of a size up to that indicated to move (see <a=href=\"/spells/animate-object-cleric-lvl-6/\"><i>animate object</i></a>, the sixth level cleric spell.) The animated stone object must be separate, i.e. not a piece of a huge boulder or the like. It will follow the desire of the druid casting the spell — attacking, breaking objects, blocking — while the magic lasts. It has no intelligence nor volition of its own, but it follows instructions exactly as spoken. Note that only one set of instructions for one single action (the whole being simply worded and very brief — 12 words or so), can be given to the rock animated. The rock remains animated for 1 melee round per level of experience of the spell caster, and the volume of rock which can be animated is also based on the experience level of the druid — 2 cubic feet of stone per level, i.e. 24 cubic feet at the 12th level."
    ),
    Spell('Changestaff','D',7,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc=("By means of this spell, the druid is able to change his or her staff from a pole of dead wood into a <a href=\"/creatures/treant/\">treant</a> of largest size. In order to cast the dweomer, the druid must first have located a tree struck by lightning within the past 24 hours (1%-5% chance for any given tree, depending on the severity of the storm). He or she must then select a sound limb, remove it from the tree, and prepare a specially cured section. This section must be shaped and carved so as to be ready to accept the magic which the druid will then place upon it. The staff must be of ash, oak, or yew wood. Curing by sun drying and special smoke requires 28 days. Shaping, carving, smoothing, and polishing require another 28 days. The druid cannot adventure or engage in other strenuous activity during either of these periods. The finished staff, engraved with scenes of woodland life, is then rubbed with the juice of holly berries, and the end of it is thrust into the earth of the druid's grove while he or she <a href=\"/spells/speak-with-plants-cleric-lvl-4/\"><i>speaks with plants</i></a>, calling upon the staff to assist in time of need. The item is then charged with a dweomer which will last for many changes from staff to treant and back again.\n\n"
            "While the staff/treant will initially be of largest size and greatest number of hit points, each 8 points of damage it accumulates actually reduces it by 1 hit die. The staff begins at 12 hit dice and 96 hit points, goes to 11 and 88, 10 and 80, 9 and 72, etc. As it loses hit dice, it becomes smaller in size, thus losing attack power as well. If and when the staff/treant is brought below 7 hit dice, the thing crumbles to sawdust-like powder and is lost. The staff cannot ever be brought upwards in hit dice or hit points, except by a <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> (which restores it completely). Of course, a new staff can always be sought out, seasoned, as so forth, to begin the process anew.\n\n"
            "When the druid plants the end of the staff in the ground and speaks a special command prayer and invocation, the staff turns into a treant. It can and will defend the druid, or obey him or her in any way. However, it is by no means a true treant, and it cannot converse with actual treants. The transformation lasts for as many turns as the druid has levels of experience, until the druid commands the thing to return to its true form, or until the thing is destroyed, whichever first occurs. In order to cast a <i>changestaff</i> spell, the druid must have either mistletoe or leaves (ash, oak, or yew) of the same sort as the staff."
        )
    ),
    Spell('Chariot of Sustarre','D',7,
        cast=tp(1,T),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast by a druid, it brings forth a large flaming chariot pulled by two fiery horses which appear in a clap of thunder amidst cloud-like smoke. This vehicle moves at 24\" on the ground, 48\" flying, and it can carry the druid and up to 8 other man-sized creatures whom he or she first touches so as to enable these creatures to be able to ride aboard this burning transport. Creatures other than the druid and his or her designated passengers will sustain damage equal to that of a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a> spell if they are within 5' of the horses or chariot, voluntarily or involuntarily. The druid controls the chariot by verbal command, causing the flaming steeds to stop or go, walk, trot, run or fly, turning left or right as he or she desires. Note that the <i>Chariot of Sustarre</i> is a physical manifestation, and can sustain damage. The vehicle and steeds are struck only by magical weapons or by water (one quart of which will cause 1 hit point of damage), they are armor class 2, and each requires 30 hit points of damage to dispel. Naturally, fire has absolutely no effect upon either the vehicle or its steeds, but magical fires will affect the riders if they are exposed to them (other than those of the chariot itself). In addition to mistletoe, the druid casting this spell must have a small piece of wood, 2 holly berries, and a fire source at least equal too torch."
    ),
    Spell('Confusion','D',7,
        cast=tp(9,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("This spell causes <i>confusion</i> in one or more creatures within spell range. Confused creatures will react as follow:\n\n"
            "<table>"
            "<tr><th>Die Roll</th><th>Action</th></tr>"
            "<tr><td>01-10</td><td>Wander away for 1 turn</td></tr>"
            "<tr><td>11-60</td><td>Stand confused for 1 round</td></tr>"
            "<tr><td>61-80</td><td>Attack nearest creature for 1 round</td></tr>"
            "<tr><td>81-00</td><td>Attack druid or his party for 1 round</td></tr>"
            "</table>\n\n"
            "The spell lasts for 1 melee round for each level of experience of the spell caster. It will affect 2 to 8 creatures, plus a possible additional number of creatures determined by subtracting the level or number of hit dice of the strongest opponent creature within the spell range and area of affect from the level of the druid who cast the spell of <i>confusion</i>. If a positive number results, it is added to the random die roll result for number of creatures affected; a negative number is ignored. All creatures affected will be those closest to the druid within the area of effect. Each affected creature must make a saving throw each round, unless they are caused to \"wander away for 1 turn\" in which case they will go as far away from the druid as is possible in one turn of normal movement, as conditions permit. All saving throws are at -2. Confused creatures act according to the table of actions shown above, but saving throws and actions are checked at the beginning of each round."
        )
    ),
    Spell('Conjure Earth Elemental','D',7,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When a druid casts a <i>conjure earth elemental</i> spell, he or she summons an <a href=\"/creatures/earth-elemental/\">earth elemental</a> of 16 hit dice to do the druid's bidding. Furthermore, the druid need but command it, and then do as he or she desires, for the elemental does not regard the druid who conjured it with enmity. The elemental remains until destroyed, dispelled, or sent away by dismissal (cf. <a href=\"/spells/conjure-fire-elemental-druid-lvl-6/\"><i>conjure fire elemental</i></a>)."
    ),
    Spell('Control Weather','D',7,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The druidic <i>control weather</i> spell is more powerful than the <a href=\"/spells/control-weather-cleric-lvl-7/\">clerical spell of the same name</a>. The spell caster is able to change weather by two places from the prevailing conditions if <i>greater mistletoe</i> is used. It otherwise is the same as the 7th level cleric <a href=\"/spells/control-weather-cleric-lvl-7/\"><i>control weather</i></a> spell."
    ),
    Spell('Creeping Doom','D',7,
        cast=tp(9,S),
        duration_lvl=tp(4,R),
        sourcebook=V,
        desc="When the druid utters the spell of <i>creeping doom</i>, he or she calls forth a mass of from 500 to 1000 (d6 + 4) venomous, biting and stinging arachnids, insects and myriapods. This carpet-like mass will swarm in an area of 2\" square, and upon command from the druid will creep forth at 1\" per round towards any prey within 8\", moving in the direction in which the druid commanded. The <i>creeping doom</i> will slay any creature subject to normal attacks, each of the small horrors inflicting 1 hit point of damage (each then dies after their attack), to that up to 1,000 hit points of damage can be inflicted on creatures within the path of the <i>creeping doom</i>. If the <i>creeping doom</i> goes beyond 8\" of the summoner, it loses 50 of its number for each 1\" beyond 8\", i.e. at 10\" its number has shrunk by 100. There are a number of ways to thwart or destroy the creatures forming the swarm, all of which methods should be obvious."
    ),
    Spell('Finger of Death','D',7,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>finger of death</i> spell causes the victim's heart to stop. The druid utters the incantation, points his or her index finger at the creature to be slain, and unless the victim succeeds in making the appropriate saving throw, death occurs. A successful saving throw negates the spell."
    ),
    Spell('Fire Storm','D',7,
        cast=tp(9,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="When a <i>fire storm</i> spell is cast by a druid, a whole area is shot through with sheets of roaring flame which are equal to a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a> in effect. Creatures within the area of fire and 1\" or less from the edge of the affected area receive 2 to 16 hit points of damage plus additional hit points equal to the number of levels of experience of the druid unless they make a saving throw, in which case they take only one-half damage. The area of effect is equal to 2 cubic\" per level of the druid, i.e. a 13th level druid can cast a <i>fire storm</i> which measures 13\" by 2\" by 1\". The height of the storm is 1\" or 2\"; the balance of its area must be in length and width. The reverse spell, <i>fire quench</i>, smothers double the area of effect of a <i>fire storm</i> with respect to normal fires, and with respect to magical fires it has a 5% chance per level of the caster of extinguishing a magical fire (such as a <i>fire storm</i>) of proportions up to the normal area of effect of the non-reversed spell."
    ),
    Spell('Reincarnate','D',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc=("Druids have the capability of bringing back the dead in another body if death occured no more than a week before the casting of the spell. The person reincarnated will recall the majority of his or her former life and form, but the class they have, if any, in their new incarnation might be different indeed. Abilities and speech are likewise often changed. The table below gives the reincarnation possibilities of this spell:\n\n"
            "<table>"
            "<tr><th>Die Roll</th><th>Incarnation</th></tr>"
            "<tr><td>01-03</td><td>badger</td></tr>"
            "<tr><td>04-08</td><td>bear, black</td></tr>"
            "<tr><td>09-12</td><td>bear, brown</td></tr>"
            "<tr><td>13-16</td><td>boar, wild</td></tr>"
            "<tr><td>17-19</td><td>centaur</td></tr>"
            "<tr><td>20-23</td><td>dryad</td></tr>"
            "<tr><td>24-28</td><td>eagle</td></tr>"
            "<tr><td>29-31</td><td>elf</td></tr>"
            "<tr><td>32-34</td><td>faun</td></tr>"
            "<tr><td>35-36</td><td>fox</td></tr>"
            "<tr><td>37-40</td><td>gnome</td></tr>"
            "<tr><td>41-44</td><td>hawk</td></tr>"
            "<tr><td>45-58</td><td>human</td></tr>"
            "<tr><td>59-61</td><td>lynx</td></tr>"
            "<tr><td>62-64</td><td>owl</td></tr>"
            "<tr><td>65-68</td><td>pixie</td></tr>"
            "<tr><td>69-70</td><td>raccoon</td></tr>"
            "<tr><td>71-75</td><td>stag</td></tr>"
            "<tr><td>76-80</td><td>wolf</td></tr>"
            "<tr><td>81-85</td><td>wolverine</td></tr>"
            "<tr><td>86-00</td><td>use magic-user <i>reincarnation</i> table</td></tr>"
            "</table>\n\n"
            "Any sort of player character can be reincarnated. If an elf, gnome or human is indicated, the character must be created. When the corpse is touched, the new incarnation will appear in the area within 1 to 6 turns. (Cf. sixth level magic-user spell <a href=\"/spells/reincarnation-magic-user-lvl-6/\"><i>reincarnation</i></a>.)"
        )
    ),
    Spell('Sunray','D',7,
        cast=tp(3,S),
        duration=tp(1,R),
        sourcebook=U,
        desc=("When a <i>sunray</i> spell is cast, the druid evokes a burning beam of light which is similar to a ray of actual sunlight in all important aspects. It inflicts blindness for 1-3 rounds upon all creatures within its area of effect unless a successful saving throw versus spell is made. Creatures using ultravision at the time may be blinded for 2-8 rounds, while those to whom sunlight is harmful or unnatural will suffer permanent blindness unless the save is made, in which case blindness lasts for 2-12 rounds. Those within its area of effect, as well as creatures within 2\" of its perimeter, will have no infravisual capabilites for 2-5 rounds.\n\n"
            "Undead (including vampires) caught within its main area of effect must save versus spell, taking 8-48 points of damage or half damage if a save is made. Those within the secondary area of effect (up to 2\" from the perimeter) take 3-18 points of damage or no damage if save is made. The ultraviolet light generated by the spell will inflict damage on fungoid creatures and subterranean fungi just as if they were undead, but no saving throw is possible. The material components are an aster seed and a piece of aventurine feldspar (sunstone)."
        )
    ),
    Spell('Transmute Metal To Wood','D',7,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>transmute metal to wood</i> spell allows the druid casting it to change an object from metal to wood. The volume of metal is equal to a maximum weight of 80 gold pieces per level of experience. Magical objects of metal are only 10% likely to be affected by the spell. Note that even a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell will not reverse the spell effects. Thus, a metal door changed to wood would be forevermore a wooden door."
    ),
]

mu_spells = [
    Spell('Affect Normal Fires','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell enables the magic-user to cause small fires — from as small as a torch or lantern to as large as a normal bonfire of 3' maximum diameter — to reduce in size and light to become match-like or increase in light so as to become as bright as a <a href=\"/spells/light-cleric-lvl-1/\"><i>light</i></a> spell. Reducing the fire will cut fuel consumption to half normal, and increasing the fire will double consumption. Note that heat output is not altered in either case!"
    ),
    Spell('Alarm','M',1,
        cast=tp(1,R),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="When an <i>alarm</i> spell is cast, the magic-user causes a selected area to react to the presence of any living creature larger than a normal rat, i.e. anything larger than about one-half cubic foot in volume or more than about 3 pounds in weight. The area of effect can be a portal, a section of floor, stairs, etc. As soon as any living creature sets foot upon the area, touches it, or otherwise contacts it, the <i>alarm</i> spell will evoke a loud ringing which will be clearly heard within a 60' radius. (Reduce the radius by 10' for interposing doors, by 20' for substantial interposing walls.) The sound will last for 1 segment and then cease. While undead creatures will <i>not</i> cause the spell to function, invisible creatures, as well as those from other planes who are otherwise alive, will do so. Ethereal or astrally projected creatures will not trigger an <i>alarm</i>, but flying and levitating creatures will. The material components of this spell are a tiny bell and a piece of very fine silver wire."
    ),
    Spell('Armor','M',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U,
        desc=("By means of this spell, the caster creates a magical field of force which serves as if it were leather armor (AC 8). If the spell is cast upon a person already armored, it has no effect. However, if it is cast upon a creature with an armor class normally better than 9 (due to its size, speed, skin, etc.) it will benefit the normal armor class by one step, i.e. AC 8 becomes 7, AC 7 becomes 6, and so on. The magic <i>armor</i> spell does not slow or hinder movement, adds no weight or encumbrance, nor does it prevent spell casting. It lasts until dispelled or until the wearer sustains cumulative damage totaling greater than 8 points + 1 per level of the caster. Thus, the wearer might take 8 points from an attack, then several turns later sustain an additional 1 point of damage. Unless the spell were cast by a magic-user of 2nd level or higher, it would be dispelled at this time. Until it is dispelled, the <i>armor</i> spell allows the wearer full benefits of the armor class gained due to the dweomer.\n\n"
            "Note: This spell will not function in conjunction with protective magic devices other than a <i>ring of protection</i>. The material component is a piece of finely cured leather which has been <a href=\"/spells/bless-cleric-lvl-1/\"><i>blessed</i></a> by a cleric."
        )
    ),
    Spell('Burning Hands','M',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="When the magic-user casts this spell, jets of searing flame shoot from his or her fingertips. Hands can only be held so as to send forth a fan-like sheet of flames, as the magic-user's thumbs must touch each other and fingers must be spread. The <i>burning hands</i> send out flame jets of 3' length in a horizontal arc of about 120° in front of the magic-user. Any creature in the area of flames takes 1 hit point of damage for each level of experience of the spellcaster, and no saving throw is possible. Inflammable materials touched by the fire will burn, i.e. cloth, paper, parchment, thin wood, etc."
    ),
    Spell('Charm Person','M',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as shown above, this spell is the same as the second level druid spell, <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charm person or mammal</i></a>, but the magic-user can charm only persons, i.e. brownies, dwarves, elves, gnolls, gnomes, goblins, half-elves, halflings, half-orcs, hobgoblins, humans, kobolds, lizard men, nixies, orcs, pixies, sprites, and troglodytes. All other comments regarding spell effects apply with respect to persons."
    ),
    Spell('Comprehend Languages','M',1,
        cast=tp(1,R),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="When this spell is cast, the magic-user is able to read an otherwise incomprehensible written message such as a treasure map (but not a magical writing, other than to know it is \"magic\") or understand the language of a speaking creature. In either case, the magic-user must touch the object to be read or the creature to be understood, and the spell does not enable the spell caster to write or speak the language. The material components of this spell are a pinch of soot and a few grains of salt. The reverse, <i>confuse languages</i>, prevents comprehension or cancels a <i>comprehend languages</i> spell."
    ),
    Spell('Dancing Lights','M',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="When a <i>dancing lights</i> spell is cast, the magic-user creates, at his or her option, from 1 to 4 lights which resemble either A) torches and/or lanterns (and cast that amount of light), B) glowing spheres of light (such as evidenced by <a href=\"/creatures/will-o-wisp/\">will-o-wisps</a>), or C) one faintly glowing, vaguely man-like shape, somewhat similar to that of a creature from the Elemental Plane of Fire. The <i>dancing lights</i> move as the spell caster desires, forward or back, straight or turning corners, without concentration upon such movement by the magic-user. The spell will wink out if the range or duration is exceeded. Range is a base of 4\" plus 1\" for each level of the magic-user who cast the spell. Duration is 2 melee rounds per level of the spell caster. The material component of this spell is either a bit of phosphorus or wytchwood or a glowworm."
    ),
    Spell('Detect Magic','M',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="The only differences between this spell and the first level cleric <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a> spell are noted above (duration, area of effect, and no material component)."
    ),
    Spell('Enlarge','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="This spell causes instant growth of a creature or object. <i>Enlargement</i> causes increase in both size and weight. It can be cast upon only a single creature or object. Spell range is ½\" for each level of experience of the magic-user, and its duration is 1 turn per level of power experience of the spell caster. The effect of the <i>enlargement</i> spell is to increase the size of a living creature (or a symbiotic or community entity) by 20% per level of experience of the magic-user, with a maximum additional growth of 200%. The effect on objects is one-half that of creatures, i.e. 10% per level to a 100% maximum additional <i>enlargement</i>. The creature or object must be seen in order to effect the spell. The maximum volume of living material which can be initially affected is 10 cubic feet — for non-living matter, 5 cubic feet — per level of the magic-user. While magical properties are not increased by this spell — a huge +1 sword is still only +1, a staff-sized wand is still only capable of its normal functions, a giant-sized potion merely requires a greater fluid intake to make its magical effects operate, etc. — weight, mass and strength are. Thus, a table blocking a door would be heavier and more effective; a hurled stone would have more mass (and be more hurtful providing <i>enlargement</i> took place just prior to impact); chains would be more massive; doors thicker; a thin line turned to a sizable, longer rope; and so on. Likewise, a person 12' tall would be as an ogre, while an 18' tall person would actually be a giant for the duration of the spell. The reverse spell, <i>reduce</i>, will negate the effects or actually make creatures or objects smaller in the tame ratios as the regular spell application functions. Unwilling victims of the spell, or its reverse, are entitled to a saving throw, which, if successful, indicates the magic does not function, and the spell is wasted. The material component of this spell is a pinch of powdered iron. "
    ),
    Spell('Erase','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>erase</i> spell removes writings of either magical or mundane nature from a scroll or one or two pages or sheets of paper, parchment or similar surfaces. It will not remove <a href=\"/spells/explosive-runes-magic-user-lvl-3/\"><i>explosive runes</i></a> or a <a href=\"/spells/symbol-cleric-lvl-7/\"><i>symbol</i></a> (see these spells hereafter), however. There is a basic chance of 50%, plus 2% per level of experience of the spell caster with respect to magical writings, plus 4% per level for mundane writing, that the spell will take effect. This represents the saving throw, and any percentile dice score in excess of the adjusted percentage chance means the spell fails."
    ),
    Spell('Feather Fall','M',1,
        cast=tp(Decimal(0.1),S),
        duration_lvl=tp(1,S),
        sourcebook=V,
        desc="When this spell is cast, the creature(s) or object(s) affected immediately assumes the mass of a feathery piece of down. Rate of falling is thus instantly changed to a mere constant 2' per second or 12' per segment, and no damage is incurred when landing when the spell is in effect. However, when the spell duration ceases, normal rate of fall occurs. The spell can be cast upon the magic-user or some other creature or object up to the maximum range of 1\" per level of experience of the spell caster. It lasts for 1 segment for each level of the magic-user. The <i>feather fall</i> affects an area of 1 cubic inch, and the maximum weight of creatures and/or objects cannot exceed a combined total equal to a base 2,000 gold pieces weight plus 2,000 gold pieces weight per level of the spell caster. Example: a 2nd level magic-user has a range of 2\", a duration of 2 segments, a weight maximum of 6,000 gold pieces (600 pounds) when employing the spell. The spell works only upon free-falling or propelled objects. It will not affect a sword blow or a charging creature, but it will affect a missile. The material component is a small feather or a piece of down somewhere on the person of the spell caster."
    ),
    Spell('Find Familiar','M',1,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc=("A familiar is of certain benefit to a magic-user, as the creature adds to the spell caster's hit points, it conveys its sensory powers to its master, and it can converse with and will serve as a guard/scout/spy as well. However, the magic-user has no control over what sort of creature will answer the summoning, or if any at all will come, and the power of the conjuration is such that it can by attempted but once per year. At such time as the magic-user determines to find a familiar, he or she must stoke up a brass brazier with charcoal, and when this is burning well, add 100 g.p. worth of incense, herbs (basil, savory, and catnip for sure), and fat. When these items are burning, the spell caster begins his or her incantation, and it must be continued until the familiar comes or the casting time is finished. Your referee will secretly determine all results. The magic-user has absolutely no control over what sort of a creature appears to become his or her familiar. This will be determined on the table below:\n\n"
            "<table>"
            "<tr><th>Die Roll (d20)</th><th>Familiar</th><th>Sensory Powers</th></tr>"
            "<tr><td>1-4</td><td>cat, black</td><td>excellent night vision & superior hearing</td></tr>"
            "<tr><td>5-6</td><td>crow</td><td>excellent vision</td></tr>"
            "<tr><td>7-8</td><td>hawk</td><td>very superior distance vision</td></tr>"
            "<tr><td>9-10</td><td>owl, screech</td><td>night vision equal human daylight visual ability, superior hearing</td></tr>"
            "<tr><td>11-12</td><td>toad</td><td>wide angle vision</td></tr>"
            "<tr><td>13-14</td><td>weasel</td><td>superior hearing & very superior olfactory power</td></tr>"
            "<tr><td>15</td><td>special — see sub-table below for details</td><td></td></tr>"
            "<tr><td>16-20*</td><td>no familiar available within spell range</td><td></td></tr>"
            "</table>\n\n"
            "*Subtract 1 from the die score for each 3 levels of experience of the spell caster, and if the score is 15 or less roll again using d16, and if a 16 is rolled then the result is final.\n\n"
            "If a score of 15 is rolled, use the table below for a special familiar:\n\n"
            "<table>"
            "<tr><th>Alignment of Magic-User</th><th>Result of Special Familiar</th></tr>"
            "<tr><td>chaotic evil or neutral chaotic</td><td><a href=\"/creatures/quasit/\">quasit</a></td></tr>"
            "<tr><td>chaotic good, neutral, or neutral good</td><td><a href=\"/creatures/pseudo-dragon/\">pseudo-dragon</a></td></tr>"
            "<tr><td>lawful neutral or lawful good</td><td><a href=\"/creatures/brownie/\">brownie</a></td></tr>"
            "<tr><td>lawful evil or neutral evil</td><td><a href=\"/creatures/imp/\">imp</a></td></tr>"
            "</table>\n\n"
            "Normal familiars have 2-4 hit points and armor class of 7 (due to size, speed, etc.). Each is abnormally intelligent and totally faithful to the magic-user whose familiar it becomes. The number of the familiar's hit points is added to the hit point total of the magic-user when it is within 12\" of its master, but if the familiar should ever be killed, the magic-user will permanently lose double that number of hit points.\n\n"
            "If a special familiar is indicated, details of the powers it conveys are given in ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL for all except the brownie. This creature becomes a friend and companion to the magic-user, and he or she will gain dexterity equal to the brownie's (18) and the advantage of never being surprised, as well as +2 on all saving throws. Note that special familiars are entitled to a saving throw versus magic when summoned by the spell, and if they succeed, they will ignore the spell, and NO familiar will be available that year to the caster.\n\n"
            "A familiar will fight for the life of the magic-user it serves only in a life-and-death situation, and imps and quasits will be 90% likely not to do so at the risk of their own life."
        )
    ),
    Spell('Firewater','M',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=U,
        desc="By means of this spell, the magic-user changes a volume of water to a volative, flammable substance similar to alcohol and likewise lighter than water. If this substance is exposed to flame, fire, or even a spark, it will burst into flames and burn with a hot fire. Each creature subject to <i>firewater</i> flame will suffer 2-12 hit points of damage. The <i>firewater</i> created will evaporate and be useless within 1 round, even if it is securely contained and sealed, so it must be utilized (ignited) within 10 segments of its creation. The material components of this spell are a few grains of sugar and a raisin."
    ),
    Spell('Friends','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="A <i>friends</i> spell causes the magic-user to gain a temporary increase of 2-8 points in charisma — or a temporary lowering of charisma by 1-4 points — depending on whether creatures within the area of effect of the spell make — or fail — their saving throw versus magic. Those that fail their saving throw will be very impressed with the spell caster and desire greatly to be his or her friend and help. Those that do not fail will be uneasy in the spell caster's presence and tend to find him or her irritating. Note that this spell has absolutely no effect on creatures of <i>animal</i> intelligence or lower. The components for this spell are chalk (or white flour), lampblack (or soot), and vermilion applied to the face before casting the spell."
    ),
    Spell('Grease','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="A <i>grease</i> spell creates an area covered by a slippery substance of a fatty, greasy nature. Any creature stepping upon this area will have to save versus petrification or slip, skid, and fall. Of course, if a creature is aware of the area, it can possibly be avoided. The spell can also be used to cause a greasy coating on some surface other than underfoot — a rope, ladder rungs, weapon handle, etc. Lone material objects will always be subject to such a spell use, but if the magic is cast upon an object wielded or employed by a creature, the creature must fail a saving throw versus spell for the grease to be effective. A single saving throw will negate the effects. The material component of the spell is a bit of pork rind, butter, or other greasy material."
    ),
    Spell('Hold Portal','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell magically bars a door, gate or valve of wood, metal or stone. The magical closure holds the portal fast just as if it were securely stopped and locked. The range of the spell is 2' per level of experience of the caster, and it lasts for 1 round per level. Note that any extra-dimensional creature (demon, devil, elemental, etc.) will shatter such a held portal. A magic-user of four or more experience levels higher than the spell caster can open the held portal at will. A <a href=\"/spells/knock-magic-user-lvl-2/\"><i>knock</i></a> spell or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell will negate the <i>hold portal</i>. Held portals can be broken or battered down."
    ),
    Spell('Identify','M',1,
        cast=tp(1,T),
        duration_lvl=tp(1,S),
        sourcebook=V,
        desc="When an <i>identify</i> spell is cast, one item may be touched and handled by the magic-user in order that he or she may possibly find what dweomer it possesses. The item in question must be held or worn as would be normal for any such object, i.e. a bracelet must be placed on the spell caster's wrist, a helm on his or her head, boots on the feet, a cloak worn, a dagger held, and so on. Note that any consequences of this use of the item fall fully upon the magic-user, although any saving throw normally allowed is still the privilege of the magic-user. For each segment the spell is in force, it is 15% + 5% per level of the magic-user probable that 1 property of the object touched can become known — possibly that the item has no properties and is merely a ruse (the presence of <a href=\"/spells/nystuls-magic-aura-magic-user-lvl-1/\"><i>Nystul's Magic Aura</i></a> or a <a href=\"/spells/magic-mouth-magic-user-lvl-2/\"><i>magic mouth</i></a> being detected). Each time a property can be known, the referee will secretly roll to see if the magic-user made his or her saving throw versus magic. If the save was successful, the property is known; if it is 1 point short, a false power will be revealed; and if it is lower than 1 under the required score no information will be gained. The item will never reveal its exact plusses to hit or its damage bonuses, although the fact that it has few or many such plusses can be discovered. If it has charges, the object will never reveal the exact number, but it will give information which is +/-25% of actual i.e. a wand with 40 charges could feel as if it had 30, or 50, or any number in between. The item to be <i>identified</i> must be examined by the magic-user within 1 hour per level of experience of the examiner after it has been discovered, or all readable impressions will have been blended into those of the characters who have possessed it since. After casting the spell and determining what can be learned from it, the magic-user loses 8 points of constitution. He or she must rest for 6 turns per 1 point in order to regain them. If the 8 point loss drops the spell caster below a constitution of 3, he or she will fall unconscious, and consciousness will not be regained until full constitution is restored 24 hours later. The material components of this spell are a pearl (of at least 100g.p. value) and an owl feather steeped in wine, with the infusion drunk and a live miniature carp swallowed whole prior to spell casting. If a <i>luckstone</i> is powdered and added to the infusion, probability increases 25% and all saving throws are made at +4."
    ),
    Spell('Jump','M',1,
        cast=tp(1,S),
        duration=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast, the individual is empowered to leap up to 30' forward or 10' backward or straight upward. Horizontal leaps forward or backward are in only a slight arc — about 2'/10' of distance travelled. The <i>jump</i> spell does not insure any safety in landing or grasping at the end of the leap. For every 3 additional levels of experience of the magic-user beyond the 1st, he or she is able to empower 1 additional leap, so a 4th level magic-user can cast a <i>jump</i> spell which enables the recipient to make 2 leaps, 3 leaps at 7th level, etc. All leaps must be completed within 1 turn after the spell is cast, for after that period has elapsed the spell wears off. The material component of this spell is a grasshopper's hind leg, one for each leap, to be broken when the leap is made."
    ),
    Spell('Light','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="With the exceptions noted above, this spell is the same as the first level cleric <a href=\"/spells/light-cleric-lvl-1/\"><i>light</i></a> spell."
    ),
    Spell('Magic Missile','M',1,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="Use of the <i>magic missile</i> spell creates one or more magical missiles which dart forth from the magic-user's fingertip and unerringly strike their target. Each missile does 2 to 5 hit points (d4+1) of damage. If the magic-user has multiple missile capability, he or she can have them strike a single target creature or several creatures, as desired. For each level of experience of the magic-user, the range of his or her <i>magic missile</i> extends 1\" beyond the 6\" base range. For every 2 levels of experience, the magic-user gains an additional missile, i.e. 2 at 3rd level, 3 at 5th level, 4 at 7th level, etc."
    ),
    Spell('Melt','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When a <i>melt</i> spell is cast, the magic-user effectively raises the temperature in the area of effect. This sudden increase in warmth will melt ice in 1 round, so that a 1st level magic-user can melt a cube of solid ice, 1 yard on a side, in 1 round after the spell is cast, so that the ice becomes water. Twice this volume of snow can be affected, so that the spell will melt 1 cubic yard of snow in ½ round, or will turn 2 cubic yards (1 yd. x 1 yd. x 2 yds.) of snow to water in 1 round. Against monsters such as white dragons, winter wolves, yeti, woolly rhinos, those composed of para-elemental ice, and the like, a <i>melt</i> spell will inflict 2 points of damage per level of the spell caster, or 1 point per level if the subject creature makes its saving throw versus spell. The <i>melt</i> spell is generally ineffective against types of creatures other than those enumerated above. The material components for a <i>melt</i> spell are a few crystals or rock salt and a pinch of soot."
    ),
    Spell('Mending','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell repairs small breaks in objects. It will weld a broken ring, chain link, medallion or slender dagger, providing but one break exists. Ceramic or wooden objects with multiple breaks can be invisibly rejoined to be as strong as new. A hole in a leather sack or wineskin is completely healed over by a <i>mending</i> spell. This spell will not repair magic items of any kind. The material components of this spell are two small magnets of any type (lodestone in all likelihood) or two burrs."
    ),
    Spell('Message','M',1,
        cast=tp(1,S),
        duration=tp(5,S),
        duration_lvl=tp(1,S),
        sourcebook=V,
        desc="When this spell is cast, the magic-user can whisper a message and secretly, or openly, point his or her finger while so doing, and the whispered <i>message</i> will travel in a straight line and be audible to the creature pointed at. The <i>message</i> must fit spell duration, and if there is time remaining, the creature who received the <i>message</i> can whisper a reply and be heard by the spell caster. Note that there must be an open and unobstructed path between the spell caster and the recipient of the spell. The material component of the spell is a short piece of copper drawn fine."
    ),
    Spell('Mount','M',1,
        cast=tp(1,R),
        duration=tp(12,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc=("By means of this spell, the caster calls a normal animal to serve him or her as a mount. The animal will serve willingly and well, but at the expiration of the spell duration it will disappear, returning to its own place. The type of mount gained by this spell depends on the level of the caster; of course, a caster of sufficiently high level to qualify for a camel (for instance) can choose a \"lower level\" <i>mount</i> if he or she so desires. Available <i>mounts</i> are these:\n"
            "   1st through 3rd level: mule or light horse\n"
            "   4th through 7th level: draft horse or warhorse\n"
            "   8th through 12 level: camel\n"
            "   13th level & up: elephant (and houda at 18th level)\n\n"
            "The <i>mount</i> will not come with any riding gear, unless it is of a class lower than the caster would normally be entitled to gain, i.e. a 4th level magic-user can gain a warhorse <i>without</i> saddle and harness or a light horse <i>with</i> saddle and harness. The statistics of the animal gained are typical of all creatures of the same class. The material component of the spell is a bit of hair or dung from the type of animal to be conjured."
        )
    ),
    Spell('Nystul\'s Magic Aura','M',1,
        cast=tp(1,R),
        duration_lvl=tp(1,D),
        sourcebook=V,
        desc="By means of this spell any one item of a weight of 50 g.p. per level of experience of the spell caster can be given an aura which will be noticed if detection of magic is exercised upon the object. If the object bearing the <i>Nystul's Magic Aura</i> is actually held by the creature detecting for a dweomer, he, she or it is entitled to a saving throw versus magic, and if this throw is successful, the creature knows that the aura has been placed to mislead the unwary. Otherwise, the aura is simply magical, but no amount of testing will reveal what the magic is. The component for this spell is a small square of silk which must be passed over the object to bear the aura."
    ),
    Spell('Precipitation','M',1,
        cast=tp(1,S),
        duration_lvl=tp(1,S),
        sourcebook=U,
        desc="This spell is identical to the <a href=\"/spells/precipitation-cleric-lvl-1/\">1st-level clerical spell</a> of the same name, except that a holy symbol is not part of the material component."
    ),
    Spell('Protection From Evil','M',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="With the differences shown above, and the requirement of powdered iron and silver as the material components for tracing the magic circle for <i>protection from evil</i>, the spell is the same as the first level cleric <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell. "
    ),
    Spell('Push','M',1,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="Upon pronouncing the syllables of this spell, the magic-user causes an invisible force to strike against whatever object he or she is pointing at. The force of the <i>push</i> is not great, being 1 foot- pound per level of the magic-user casting the spell, but it can move small objects up to 1' in a direction directly away from the caster, topple an object under the proper conditions, or cause a creature to lose its balance. An example of the latter use is causing a creature attacking to lose its balance when it is attacking, for if the creature fails its saving throw, it will not be able to attack that round. Of course, the mass of the creature attacking cannot exceed the force of the <i>push</i> by more than a factor of 50, i.e. a 1st level magic-user cannot effectively <i>push</i> a creature weighing more than 50 pounds. A <i>push</i> spell employed against an object held by a creature will cause it to subtract the force of the spell in foot- pounds (1,2,3, etc.) from its chance to hit or add to opponent saving throws as applicable if the creature fails to make its saving throw against magic when the spell is cast. The material component of this spell is a small pinch of powdered brass which must be blown from the palm prior to pointing at the object of the spell."
    ),
    Spell('Read Magic','M',1,
        cast=tp(1,R),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By means of a <i>read magic</i> spell, the magic-user is able to read magical inscriptions on objects — books, scrolls weapons and the like — which would otherwise be totally unintelligible to him or her. (The personal books of the magic-user, and works already magically read, are intelligible.) This deciphering does not normally invoke the magic contained in the writing, although it may do so in the case of a <i>curse scroll</i>. Furthermore, once the spell is cast and the magic-user has read the magical inscription, he or she is thereafter able to read that particular writing without recourse to the use of the <i>read magic</i> spell. The duration of the spell is 2 rounds per level of experience of the spell caster. The material component for the spell is a clear crystal or mineral prism. Note that the material is not expended by use. The reverse of the spell, <i>unreadable magic</i>, makes such writing completely unreadable to any creature, even with the aid of a <i>read magic</i>, until the spell wears off or the magic is dispelled. The material components for the reverse spell are a pinch of dirt and a drop of water."
    ),
    Spell('Run','M',1,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U,
        desc="The <i>run</i> spell enables the recipient to run at full speed (twice normal speed) for from 5-8 hours without tiring. However, after so running the individual must spend a like number of hours resting, as well as drinking plenty of liquids and eating heartily. For every 2 levels of experience of the spell caster, another individual can be affected, i.e. at 4th level, 2 individuals can be touched and empowered to <i>run</i>; at 6th level, 3 individuals; etc. Only humans and demi-humans in their natural forms are affected by this spell, and barbarians having the special running ability of that class are immune to the spell's effects. The material component of this spell is an elixir made from the juice of dried plums boiled in spring water and the oil of 5-8 beans of a spurge (castor) plant."
    ),
    Spell('Shield','M',1,
        cast=tp(1,S),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="When this spell is cast, an invisible barrier before the front of the magic-user comes into being. This <i>shield</i> will totally negate <a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>magic missile</i></a> attacks. It provides the equivalent protection of armor class 2 against hand hurled missiles (axes, darts, javelins, spears, etc.), armor class 3 against small device-propelled missiles (arrows, bolts, bullets, manticore spikes, sling stones, etc.), and armor class 4 against all other forms of attack. The <i>shield</i> also adds +1 to the magic-user's saving throw dice vs. attacks which are basically frontal. Note that all benefits of the spell accrue only to attacks originating from the front facing the magic-user, where the Shield can move to interpose itself properly."
    ),
    Spell('Shocking Grasp','M',1,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="When the magic-user casts this spell, he or she develops a powerful electrical charge which gives a jolt to the creature touched. The <i>shocking grasp</i> delivers from 1 to 8 hit points damage (d8), plus 1 hit point per level of the magic-user, i.e. a 2nd level magic-user would discharge a shock causing 3 to 10 hit points of damage. While the magic-user must only come close enough to his or her opponent to lay a hand on the opponent's body or upon an electrical conductor which touches the opponent's body, a like touch from the opponent does not discharge the spell."
    ),
    Spell('Sleep','M',1,
        cast=tp(1,S),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc=("When a magic-user casts a <i>sleep</i> spell, he or she usually cause a comatose slumber to come upon one or more creatures [other than <i>undead</i> and certain other creatures specifically excluded (see ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL) from the spell's effects]. All creatures to be affected by the <i>sleep</i> spell must be within a 3\" diameter circle. The number of creatures which can be affected is a function of their life energy levels, expressed as hit dice and hit points:\n\n"
            "<table>"
            "<tr><th>Creatures Hit Dice</th><th>Number Affected by Sleep Spell</th></tr>"
            "<tr><td>up to 1</td><td>4-16 (4d4)</td></tr>"
            "<tr><td>1+1 to 2</td><td>2-8 (2d4)</td></tr>"
            "<tr><td>2+1 to 3</td><td>1-4 (1d4)</td></tr>"
            "<tr><td>3+1 to 4</td><td>1-2 (½d4, round off)</td></tr>"
            "<tr><td>4+1 to 4+4</td><td>0-1 (d4, 3 or 4)</td></tr>"
            "</table>\n\n"
            "The area of effect is determined by the range and area center decided upon by the spell caster. Slapping or wounding will awaken affected creatures, but noise will not do so. Awakening requires 1 complete melee round. Note that sleeping creatures can be slain automatically at a rate of 1 per slayer per melee round. The material component for this spell is a pinch of fine sand, rose petals, or a live cricket."
        )
    ),
    Spell('Spider Climb','M',1,
        cast=tp(1,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="A <i>spider climb</i> spell enables the recipient to climb and travel upon vertical surfaces just as a giant spider is able to do, i.e. at 3\" movement rate, or even hang upside down from ceilings. Note that the affected creature must have bare hands and feet in order to climb in this manner. During the course of the spell the recipient cannot handle objects which weigh less than 50 g.p., for such objects will stick to the creature's hands/feet, so a magic-user will find it virtually impossible to cast spells if under a <i>spider climb</i> dweomer. The material components of this spell are a drop of bitumen and a live spider, both of which must be eaten by the spell recipient."
    ),
    Spell('Taunt','M',1,
        cast=tp(1,R),
        duration=tp(0),
        sourcebook=U,
        desc="A <i>taunt</i> spell enables the caster to jape and jeer effectively with respect to any creature with an intelligence of 2 or greater. The spell's dweomer gives the magic-user's words and sounds real meaning to the subject creature or creatures. These words and sounds will challenge the subject(s), be insulting, and in general cause irritation and anger. If the subject creature or creatures fail to save versus spell, the <i>taunt</i> spell will cause them to rush forth in fury to do battle with the spell caster, and each and every affected creature so coming will certainly attack the spell caster if physically capable of doing so, i.e. they will seek to use body weapons and hand-held weapons rather than attacking from a distance. Separation by an impenetrable or uncrossable boundary (a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of flame</i></a>, a deep chasm) will cause the spell to break. Only one sort of creature can be affected by a single <i>taunt</i> spell; in a mixed group of orcs and goblins (for instance) the caster would be able to affect either the orcs or the goblins (caster's choice), but not both at once. The magic affects creatures closest to the spell caster first, regardless of maximum range. Thus, if a group of gnolls were being <i>taunted</i> by a 10th-level magic-user, the nearest ten creatures would be subject to the spell first, even though the spell caster might prefer to affect the gnollish shaman at the rear of the group. Troops under a strong leader would gain a saving throw bonus of +1 to +4, at the DM's discretion."
    ),
    Spell('Tenser\'s Floating Disc','M',1,
        cast=tp(1,S),
        duration=tp(3,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="With this spell, the caster creates the circular plane of null-gravity known as <i>Tenser's Floating Disc</i> after the famed wizard of that appellation (whose ability to locate treasure and his greed to recover every copper found are well known). The <i>disc</i> is concave, 3' in diameter, and holds 1,000 g.p. weight per level of the magic-user casting the spell. The <i>disc</i> floats at approximately 3' above the ground at all times and remains level likewise. It maintains a constant interval of 6' between itself and the magic-user if unbidden. It will otherwise move within its range, as well as along with him at a rate of 6\", at the command of the magic-user. If the spell caster moves beyond range, or if the spell duration expires, the <i>floating disc</i> winks out of existence and whatever it was supporting is precipitated to the surface beneath it. The material component of the spell is a drop of mercury."
    ),
    Spell('Unseen Servant','M',1,
        cast=tp(1,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>unseen servant</i> is a non-visible valet, a butler to step and fetch, open doors and hold chairs, as well as to clean and mend. The spell creates a force which is not strong, but which obeys the command of the magic-user. It can carry only light-weight items — a maximum of 200 gold pieces weight suspended, twice that amount moving across a relatively friction-free surface such as a smooth stone or wood floor. It can only open normal doors, drawers, lids, etc. The <i>unseen servant</i> cannot fight nor can it be killed, as it is a force rather than a creature. It can be magically dispelled, or eliminated after taking 6 hit points of magical damage. The material components of the spell are a piece of string and a bit of wood."
    ),
    Spell('Ventriloquism','M',1,
        cast=tp(1,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell enables the magic-user to make it sound as if his or her voice — or someone's voice or similar sound — is issuing from someplace else, such as from another creature, a statue, from behind a door, down a passage, etc. The spell caster is able to make his or her voice sound as if a different creature were speaking or making the noise; of course, in a language known by him or her, or a sound which the caster can normally make. With respect to such voices and sounds, there is a 10% chance per point of intelligence above 12 of the hearer that the ruse will be recognized. The material component of the spell is a small cone of parchment."
    ),
    Spell('Wizard Mark','M',1,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="When this spell is cast, the magic-user is able to inscribe, visibly or invisibly, his or her personal rune or mark, as well as up to six additional characters of smaller size. A <i>wizard mark</i> spell allows the caster to etch the rune upon stone, metal, or any softer substance without harm to the material upon which the mark is placed. If an invisible mark is made, <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a> will cause it to glow and be readable (which does not necessarily imply understandability). <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>Detect invisibility</i></a>, <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a>, <a href=\"/spells/true-sight-illusionist-lvl-6/\"><i>true sight</i></a>, a <i>gem of seeing</i>, or a <i>robe of eyes</i> will likewise note an invisible <i>wizard mark</i>. A <a href=\"/spells/read-magic-magic-user-lvl-1/\"><i>read magic</i></a> spell will reveal the maker's intent, and an <a href=\"/spells/erase-magic-user-lvl-1/\"><i>erase</i></a> spell will wipe clean a <i>wizard marked</i> surface. The material components for the casting of this spell are a pinch of diamond dust (about 50 gp worth) and a pigment or pigments for coloration of the mark. If the mark is to be invisible, the pigments are still needed, but the caster uses a stylus of some sort rather than his or her digit."
    ),
    Spell('Write','M',1,
        cast=tp(1,R),
        duration_lvl=tp(1,H),
        sourcebook=V,
        desc="By means of this spell a magic-user might be able to inscribe a spell to make a magical scroll he or she cannot understand at the time (due to level or lack of sufficient intelligence) into the tome or other compilation he or she employs to maintain a library of spells. The magic-user must make a saving throw versus magic to attempt the writing of any spell, +2 if it is only up to 1 level greater than he or she currently uses, 0 at 2 levels higher, and -1 per level from 3 levels higher onwards. If this throw fails, the magic user is subject to 1d4 of damage for every level of the spell he or she was attempting to transcribe into his or her magic book, and furthermore be knocked unconscious for a like number of turns. This damage, if not fatal, can only be healed at the rate of 1-4 points per day, as it is damage to psyche and body. Furthermore, a spell will take 1 hour per level to transcribe in this fashion, and during this period, the magic-user is in a trance state and can always be surprised by any foe. In addition to the writing surface upon which the spell is to be transcribed, the spell caster needs a fine ink composed of rare substances (minimum cost 200 g.p. per bottle, if available at all without manufacture by the magic user)."
    ),
    Spell('Audible Glamer','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="When the <i>audible glamer</i> spell is cast, the magic-user causes a volume of sound to arise, at whatever distance he or she desires (within range), and seeming to recede, close, or remain in a fixed place as desired. The volume of sound caused, however, is directly related to the level of the spell caster. The relative noise is based upon the lowest level at which the spell can be cast, 3rd level. The noise of the <i>audible glamer</i> at this level is that of 4 men, maximum. Each additional experience level adds a like volume, so at 4th level the magic-user can have the spell cause sound equal to that of 8 men, maximum. Thus, talking, singing, or shouting, and/or walking, marching or running sounds can be caused. The auditory illusion created by an <i>audible glamer</i> spell can be virtually any type of sound, but the relative volume must be commensurate with the level of the magic-user casting the spell. A horde of rats running and squeaking is about the some volume as 8 men running and shouting. A roaring lion is equal to the noise volume of 16 men, while a roaring dragon is equal to the noise volume of no fewer than 24 men. If a character states that he or she does not believe the sound, a saving throw is made, and if it succeeds, the character then hears nothing, or possibly just a faint sound. Note that this spell is particularly effective when cast in conjunction with <a href=\"/spells/phantasmal-force-magic-user-lvl-3/\"><i>phantasmal force</i></a>. The material component of the spell is a bit of wool or a small lump of wax."
    ),
    Spell('Bind','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When this spell is employed, the magic-user causes any ropelike object of non-living material to behave as he or she orders. The subject can be string, yarn, cord, line, rope, or even a cable. About 50' of normal rope (1 inch diameter), plus 5' per level of the spell caster, can be affected. Reduce length proportionally when diameter increases, and increase length by 50% when diameter is halved. The commands possible to give under a <i>bind</i> spell are: <i>Coil</i> (form a neat, coiled stack); <i>Coil & Knot<; Loop; Loop & Knot; Tie & Knot;</i> and the reverses of all of the above (<i>Uncoil</i>, etc.). The rope or other ropelike object must be within about 1 foot of any object in order for it to respond properly, so it must usually be thrown or hurled nearby. Any creature affected by the ropelike object can, of course, interact with it as if it were a normal object. The creature's hold overrides the dweomer on the rope, and the rope takes 2 points of slashing damage before breaking. The rope cannot be used as a garrot, but can be used as a trip line or to <a href=\"/spells/entangle-druid-lvl-1/\"><i>entangle</i></a> (as the druid spell) a single opponent. The dweomer does not cause the rope to have magical properties beyond its ability to obey commands (cf. <i>rope of climbing, rope of entanglement</i>)."
    ),
    Spell('Continual Light','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the third level cleric spell <a href=\"/spells/continual-light-cleric-lvl-3/\"><i>continual light</i></a> except that the range is only 6\", not 12\", and it cannot be reversed by the caster."
    ),
    Spell('Darkness 15\' Radius','M',2,
        cast=tp(2,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell causes total, impenetrable darkness in the area of its effect. Infravision or ultravision are useless. Neither normal nor magical light will work unless a <a href=\"/spells/light-cleric-lvl-1/\"><i>light</i></a> or <a href=\"/spells/continual-light-cleric-lvl-3/\"><i>continual light</i></a> spell is used. In the former event, the <i>darkness</i> spell is negated by the <i>light</i> spell and vice versa. The material components of this spell area bit of bat fur and either a drop of pitch or a piece of coal."
    ),
    Spell('Deeppockets','M',2,
        cast=tp(1,T),
        duration=tp(24,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc="This spell allows the magic-user to specially prepare a garment so as to hold far more than it normally could. A finely sewn gown or robe of high-quality material (at least 300 gp value) is fashioned so as to contain numerous hand-sized pockets. One dozen is the minimum number. The <i>deeppockets</i> spell then makes one of these pockets able to hold 1,000 gp worth of weight (5 cubic feet volume) as if it were only 100 gp of weight. Furthermore, there will be no discernible bulge where the special pocket is. The spell can be changed to allow 10 pockets each of 100 gp weight capability (½ cubic foot volume each). If a robe or like garment is sewn with 100 or more pockets (1,000 gp minimum cost), then 100 pockets can be dweomered to contain 10 gp weight each and hold ⅙ cubic foot volume each. If the spell duration expires while there is material within the enchanted pockets, or a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> is cast upon the enchanted garment, the wearer must make a saving throw versus spell. Failure indicates the material in those pockets has gone from extra-dimensional space to astral space — lost forever. Success indicates the material suddenly and totally appears around the wearer and immediately falls to the ground. In addition to the garment, the material components of this spell are a tiny golden needle and a strip of fine cloth given a half-twist and fastened at the ends."
    ),
    Spell('Detect Evil','M',2,
        cast=tp(2,S),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the first level cleric <a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect evil</i></a>."
    ),
    Spell('Detect Invisibility','M',2,
        cast=tp(2,S),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="When the magic-user casts a <i>detect invisibility</i> spell, he or she is able to clearly see any objects which are invisible, as well as astral, ethereal, hidden, invisible or out of phase creatures. Detection is in the magic-user's line of sight along a 1\" wide path to the range limit. The material components of this spell are a pinch of talc and a small sprinkling of powdered silver."
    ),
    Spell('ESP','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When an <i>ESP</i> spell is used, the caster is able to detect the surface thoughts of any creatures in range — except creatures with no mind (as we know it), such as all of the <i>undead</i>. The <i>ESP</i> is stopped by 2 or more feet of rock, 2 or more inches of any metal other than lead, or a thin sheet of lead foil. The magic-user employing the spell is able to probe the surface thoughts of 1 creature per turn, getting simple instinctual thoughts from lower order creatures. Probes can continue on the same creature from round to round. The caster can use the spell to help determine if some creature lurks behind a door, for example, but the <i>ESP</i> will not always reveal what sort of creature it is. The material component of this spell is a copper piece."
    ),
    Spell('Flaming Sphere','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="A <i>flaming sphere</i> spell causes a burning globe of normal-type fire to come into being up to 1\" distant from the spell caster. This sphere will then begin rolling in the direction in which the magic-user points, even though it might be uphill. It will roll over low barriers such as walls, furniture, etc., as long as these barriers are not over 4' tall. Flammable substances will be set afire by contact with the sphere. Creatures struck will suffer 2-8 points of damage. All creatures within a 5' radius of the sphere's center must save versus spell or else take the indicated damage. A successful save negates the <i>flaming sphere</i>. The <i>flaming sphere</i> moves at a rate of 1\" per round as long as the spell caster points in the direction it is to move, for it otherwise merely stays at rest and flames. It can be extinguished by the same means as any normal fire of its size. The material components are a bit of tallow, a pinch of sulphur, and a dusting of powdered iron."
    ),
    Spell('Fools Gold','M',2,
        cast=tp(1,R),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="Copper coins can temporarily be changed to gold pieces, or brass items turned to solid gold for the spell duration by means of this dweomer. Note that a huge amount of copper or brass can be turned to gold by the spell — assume 4,000 g.p. are equal to a cubic foot for purposes of this spell. Any creature viewing <i>fools gold</i> is entitled to a saving throw which must be equal to or less than its intelligence score, but for every level of the magic-user the creature must add 1 to his dice score, so it becomes unlikely that <i>fools gold</i> will be detected if it was created by a high level caster. If the \"gold\" is struck hard by an object of cold-wrought iron, there is a slight chance it will revert to its natural state, depending on the material component used to create the \"gold\": if a 50 g.p. citrine is powdered and sprinkled over the metal to be changed, the chance that cold iron will return it to its true nature is 30%; if a 100 g.p. amber stone is powdered, there is a 25% chance that iron will dispel the dweomer; if a 500 g.p. topaz is powdered, the chance drops to 10%; and if a 1,000 g.p. oriental (corundum) topaz is powdered, there is only a 1% chance that the cold iron will reveal that it is <i>fools gold</i>."
    ),
    Spell('Forget','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this dweomer the spell caster causes creatures within the area of effect to forget the events of the previous round (1 minute of time from the utterance of the spell back). For every 3 levels of experience of the spell caster another minute of past time is forgotten. Naturally, <i>forget</i> in no way negates any <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charm</i></a>, <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestions</i></a>, <a href=\"/spells/geas-magic-user-lvl-6/\"><i>geases</i></a>, <a href=\"/spells/quest-cleric-lvl-5/\"><i>quests</i></a>, or similar spells, but it is possible that the creature who caused such magic to be placed upon the victim of a <i>forget</i> spell could be forgotten by this means. From 1-4 individual creatures can be affected by the spell, at the discretion of the caster. If only 1 is to be affected, the recipient saves versus magic at -2 on the dice; if 2 are spell objects, they save at -1; and if 3 or 4 are to be made to <i>forget</i> by this dweomer, they save normally. A clerical <a href=\"/spells/heal-cleric-lvl-6/\"><i>heal</i></a> or <a href=\"/spells/restoration-cleric-lvl-7/\"><i>restoration</i></a> spell, specially cast for this purpose, will restore the lost memories, as will a <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a>, but other means will not serve to do so."
    ),
    Spell('Invisibility','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell causes the recipient to vanish from sight and not be detectable by normal vision or even infravision. Of course, the invisible creature is not magically silenced with respect to noises normal to it. The spell remains in effect until it is magically broken or dispelled, or the magic-user or the other recipient cancels it or until he, she or it attacks any creature. Thus, the spell caster or recipient could open doors, talk, eat, climb stairs, etc., but if any form of attack is made, the invisible creature immediately becomes visible, although this will allow the first attack by the creature because of the former <i>invisibility</i>. Even the allies of the spell recipient cannot see the invisible creature, or his, her or its gear, unless these allies can normally see invisible things or employ magic to do so. Note that all <i>highly intelligent</i> creatures with 10 or more hit dice, or levels of experience, or the equivalent in intelligence/dice/levels have a chance to automatically detect invisible objects. The material components of the <i>invisibility</i> spell are an eyelash and a bit of gum arabic, the former encased in the latter."
    ),
    Spell('Irritation','M',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("An <i>irritation</i> spell affects the epidermis of the subject creature. Creatures having very thick or insensitive skins (such as buffalo, elephants, scaled creatures, etc.) are basically unaffected by the dweomer. There are two versions of the spell, either of which can be cast from the standard preparation:\n\n"
            "<i>Itching</i> — When cast, this causes the subject to feel an instant itching sensation on some portion of its body. If 5-8 segments are not immediately spent scratching this <i>irritated</i> area, the subject creature will be so affected that the next 3 rounds will be spent squirming and twisting, effectively lowering the subject's armor class by 4 and its \"to hit\" probability by 2 during this time. Spells are ruined for the initial round this spell is in effect, but not for the following three rounds.\n\n"
            "<i>Rash</i> — When a <i>rash</i> version of the spell is cast, the subject creature will notice nothing for 1-4 rounds, but thereafter its entire skin will begin to break out in red welts which faintly itch. The <i>rash</i> will persist until either a <a href=\"/spells/cure-disease-cleric-lvl-3/\"><i>cure disease</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> is cast upon it. It lowers comeliness by 1 point per day until four days have passed, i.e. maximum loss of comeliness is 4 points. After one week, the subject's dexterity is lowered by 1 point also. Symptoms vanish immediately upon the removal of the <i>rash</i>, all statistics returning to normal.\n\n"
            "The material component for this spell is powdered leaf from poison ivy, oak, or sumac."
        )
    ),
    Spell('Knock','M',2,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The <i>knock</i> spell will open stuck or <a href=\"/spells/hold-person-cleric-lvl-2/\"><i>held</i></a> or <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard-locked</i></a> doors. It will also open barred or otherwise locked doors. It causes secret doors to open. The <i>knock</i> spell will also open locked or trick-opening boxes or chests. It will loose shackles or chains as well. If it is used to open a <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard-locked</i></a> door, the <i>knock</i> does not remove the former spell, but it simply suspends its functioning for 1 turn. In all other cases, the <i>knock</i> will permanently open locks or welds — although the former could be closed and locked again thereafter. It will not raise bars or similar impediments (such as a portcullis). The spell will perform <i>two</i> functions, but if a door is locked, barred, <i>and held</i>, opening it will require two <i>knock</i> spells."
    ),
    Spell('Know Alignment','M',2,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="Except as noted above, this spell is the same as the <a href=\"/spells/know-alignment-cleric-lvl-2/\">2nd-level clerical spell</a> of the same name. If a target creature is scried for only one round, only its alignment ethic (law/chaos) will be discerned."
    ),
    Spell('Leomund\'s Trap','M',2,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="This false trap is designed to fool the dwarf and/or thief attempting to pilfer or otherwise steal the spell caster's goods. It enables the magic-user to place a dweomer upon any small mechanism or device such as a lock, hinge, hasp, screw-on cap, ratchet, etc. Any examination by a character able to detect traps will be 80% likely to note the <i>Leomund's Trap</i> and believe it to be real. This probability reduces by 4% for each level of experience of the examiner beyond the first. If the supposed \"trap\" is then to be removed, it is only 20% likely that the creature attempting it will believe he or she has succeeded, +4% probability per level of experience of the remover. Of course, the spell is illusory, nothing will happen if the trap is ignored, and its primary purpose is to frighten away thieves or make them waste precious time. The material component of the spell is a piece of iron pyrite touched to the object to be \"trapped\". Only one <i>Leomund's Trap</i> may be placed within a 50' by 50' area"
    ),
    Spell('Levitate','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When a <i>levitate</i> spell is cast, the magic-user can place it upon his or her person, or upon some other creature, subject to a maximum weight limit of 1,000 gold pieces equivalence per level of experience, i.e., a third level magic user can <i>levitate</i> up to 300 pounds (3,000 g.p.) maximum. If the spell is cast upon the person of the magic-user, he or she can move vertically at a rate of 20' per round. If cast upon another creature, the magic-user can <i>levitate</i> it at a maximum vertical movement of 10' per round. Horizontal movement is not empowered by this spell, but the recipient could push along the face of a cliff, far example, to move laterally. The spell caster can cancel the spell as desired. If the recipient of the spell is unwilling, that creature is entitled to a saving throw to determine if the <i>levitate</i> spell affects it. The material component of this spell is either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end."
    ),
    Spell('Locate Object','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is the same as the third level cleric <a href=\"/spells/locate-object-cleric-lvl-3/\"><i>locate object</i></a> except that its range differs."
    ),
    Spell('Magic Mouth','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast, the magic-user empowers the chosen object with an enchanted mouth which suddenly appears and speaks the message which the spell caster imparted upon the occurrence of a specified event. The <i>magic mouth</i> can speak any message of 25 words or less in a language known by the spell caster, over a 1 turn period from start to finish. It cannot speak magic spells. The <i>mouth</i> moves to the words articulated, so if it is placed upon a statue, for example, the mouth of the statue would actually move and appear to speak. Of course, the <i>magic mouth</i> can be placed upon a tree, rock, door or any other object excluding intelligent members of the animal or vegetable kingdoms. The spell will function upon specific occurrence according to the command of the spell caster, i.e. speak to the first creature that touches you — or to the first creature that passes within 30'. Command can be as general or specific and detailed as desired, such as the following: \"Speak only when an octogenerian female human carrying a sack of great clusters sits cross legged within 1'.\" Command range is ½\" per level of the magic-user, so a 6th level magic-user can command the <i>magic mouth</i> to speak at a maximum encounter range of 3\", i.e. \"Speak when a winged creature comes within 3\" \". Until the speak command can be fulfilled, the <i>magic mouth</i> will remain in effect, thus spell duration is variable. A <i>magic mouth</i> cannot distinguish invisible creatures, alignments, level or hit dice, nor class, except by external garb. The material component of this spell is a small bit of honeycomb."
    ),
    Spell('Melf\'s Acid Arrow','M',2,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="By means of this spell, the magic-user creates a magic \"arrow\" which speeds itself to its target as if fired from the bow of a fighter of the same level as the magic-user casting the spell. The arrow is equal to a +1 weapon for hit determination purposes. The effect of a hit might inflict damage on the target even if it would not normally be harmed by an arrow or magic weapon of only +1 value. This is due to the acid. The arrow itself does 2-5 points of damage. The acid which gushes forth when it hits is equal to an acid missile of 8-ounce volume (1' diam. area of effect, 2-8 hit points damage, plus item saving throw; splash does not apply). The acid's strength increases by one round's worth of damage for every 3 levels of experience of the spell caster above the 3rd, so that damage will occur over two rounds if the spell cast is from a 4th-6th level magic-user, unless the target can have the acid neutralized. The material components of the spell are a dart and powdered rhubarb leaf and adder stomach."
    ),
    Spell('Mirror Image','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="When a <i>mirror image</i> spell is invoked, the spell caster causes from 1 to 4 exact duplicates of himself or herself to come into being around his or her person. These images do exactly what the magic-user does, and as the spell causes a blurring and slight distortion when it is effected, it is impossible for opponents to be certain which are the phantasms and which is the actual magic-user. When an image is struck by a weapon, magical or otherwise, it disappears, but any other existing images remain intact until struck. The images seem to shift from round to round, so that if the actual magic-user is struck during one round, he or she cannot be picked out from amongst his or her images the next. To determine the number of images which appear, roll percentile dice, and add 1 to the resulting score for each level of experience of the magic-user: 25 or less = 1 <i>mirror image</i>, 26-50 = 2, 51-75 = 3, 75 or more = 4. At the expiration of the spell duration all images wink out."
    ),
    Spell('Preserve','M',2,
        cast=tp(2,R),
        duration=tp(1,P),
        sourcebook=U,
        desc=("A <i>preserve</i> spell enables the caster to retain some item fresh and whole until some later time when it is needed in a spell. Of course, the dweomer is ineffective in retaining the potency of material such as mistletoe, holly berries, and similar stuffs which must be gathered periodically. It is likewise ineffective in preserving the deceased for later resurrection. It is otherwise effectual. The sort of material which can be treated by a <i>preserve</i> spell depends upon the level of the caster:\n"
            "   Hard, relatively dry material: 2nd-4th level\n"
            "   Soft, relatively wet material: 5th-7th level\n"
            "   Semi-liquid and liquid materials: 8th level & up\n\n"
            "A container is necessary only in cases where a relatively high degree of moisture is concerned. The material components of the spell are a pinch of dust, a bit of resin (or amber), and a drop of brandy."
        )
    ),
    Spell('Protection From Cantrips','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,D),
        sourcebook=U,
        desc="By casting this spell, the magic-user provides immunity to the effects of cantrips cast by other magic-users, apprentices, or creatures that use cantrip magic. The spell will protect the caster, or one item or person that he or she touches (such as a spell book or a drawer containing spell components). Any cantrip that is cast against the person or item in question dissipates with an audible popping sound. This spell is often used by a magic-user with mischievous apprentices, or one who wishes apprentices to clean or shine an area using elbow grease instead of magic. Any unwilling target of this spell must be touched (via a roll \"to hit\") and is allowed a saving throw versus spell to escape the effect."
    ),
    Spell('Pyrotechnics','M',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="With the exception of the differences noted above, this spell is the same as the third level druid spell <a href=\"/spells/pyrotechnics-druid-lvl-3/\"><i>pyrotechnics</i></a>."
    ),
    Spell('Ray of Enfeeblement','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of a <i>ray of enfeeblement</i>, a magic-user weakens an opponent, reducing strength — and attacks which rely upon it — by 25% or more. For every level of experience beyond the third of the magic-user casting the spell, there is an additional 2% strength reduction, so that at 4th level, strength loss is 27%. Range and duration of the spell are also dependent upon the level of experience of the spell caster. For example, if a creature is struck by a <i>ray of enfeeblement</i>, it will lose the appropriate percentage of hit points of damage it scores on physical attacks (missiles, thrusting/cutting/crushing weapons, biting, clawing, goring, kicking, constriction, etc.). Your referee will determine any other reductions appropriate to the affected creature. If the target creature makes its saving throw, the spell has no effect."
    ),
    Spell('Rope Trick','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,T),
        sourcebook=V,
        desc="When this spell is cast upon a piece of rope from 5' to 30' in length, one end of the rope rises into the air until the whole is hanging perpendicular, as if affixed at the upper end. The upper end is, in fact, fastened in an extra-dimensional space, and the spell caster and up to five others can climb up the rope and disappear into this place of safety where no creature can find them. The rope cannot be taken into the extra-dimensional space if six persons have climbed it, but otherwise it can be pulled up. Otherwise, the rope simply hangs in air, and will stay there unless removed by some creature. The persons in the extra-dimensional space must climb down the rope <i>prior</i> to the expiration of the spell duration, or else they are dropped from the height to which they originally climbed when the effect of the spell wears out. The rope can be climbed by only one person at a time. Note that the <i>rope trick</i> spell allows climbers to reach a normal place if they do not climb all the way to the rope's upper end, which is in an extra-dimensional space. The material components of this spell are powdered corn extract and a twisted loop of parchment."
    ),
    Spell('Scare','M',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When this spell is directed at any creature with fewer than 6 levels of experience/hit dice, it must save versus magic or fall into a fit of trembling and shaking. The frightened creature will not drop any items held unless it is encumbered. If cornered, the spell recipient will fight, but at -1 on \"to hit\" and damage dice rolls and all saving throws as well. Note that this spell does not have any effect on elves, half-elves, the <i>undead</i> (skeletons, zombies, ghouls, shadows, ghosts, wights, wraiths), larvae, lemures, manes, or clerics of any sort. The material component used for this spell is a bit of bone from an <i>undead</i> skeleton, zombie, ghoul, ghost or mummy."
    ),
    Spell('Shatter','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>shatter</i> spell affects non-magical objects of crystal, glass, ceramic, or porcelain such as vials, bottles, flasks, jugs, windows, mirrors, etc. Such objects are shivered into dozens of pieces by the spell. Objects above 100 gold pieces weight equivalence per level of the spell caster are not affected, but all other objects of the appropriate composition must save versus a <i>\"crushing blow\"</i> or be shattered. The material component of this spell is a chip of mica."
    ),
    Spell('Stinking Cloud','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When a <i>stinking cloud</i> is cast, the magic-user causes a billowing mass of nauseous vapors to come into being up to 3\" distant from his or her position. Any creature caught within the cloud must save versus poison or be helpless due to nausea from 2 to 5 turns (d4 + 1). Those which make successful saving throws are helpless only for as long as they remain within the <i>cloud</i>, and for the round after they emerge, because of its irritating effects on visual and olfactory organs. The material component of the spell is a rotten egg or several skunk cabbage leaves."
    ),
    Spell('Strength','M',2,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc=("Application of this spell increases the strength of the character by a number of points — or tenths of points after 18 strength is attained and the character is in the fighter class. Benefits of the <i>strength</i> spell last for the duration of the magic. The amount of additional strength accruing to a character upon whom this spell is cast depends upon his or her class and is subject to all restrictions on strength due to race, sex or class.\n\n"
            "<table>"
            "<tr><th>Class</th><th>Strength Gain</th></tr>"
            "<tr><th>CLERIC</th><th>1-6 (d6)</th></tr>"
            "<tr><th>FIGHTER</th><th>1-8 (d8)</th></tr>"
            "<tr><th>MAGIC-USER</th><th>1-4 (d4)</th></tr>"
            "<tr><th>THIEF</th><th>1-6 (d6)</th></tr>"
            "<tr><th>MONK</th><th>1-4 (d4)</th></tr>"
            "</table>\n\n"
            "If a fighter (paladin or ranger as well) has an 18 strength already, from 10% to 80% is added to his extraordinary strength roll. All Strength addition scores above 18 are likewise treated as 1 equalling an extra 10% on the extraordinary strength rating. The material component of this spell is a few hairs or a pinch of dung from a particularly strong animal — ape, bear, ox, etc."
        )
    ),
    Spell('Tasha\'s Uncontrollable Hideous Laughter','M',2,
        cast=tp(2,S),
        duration=tp(1,R),
        sourcebook=U,
        desc="This spell enables the caster to cause the subject to perceive everything as hilariously funny. The effect is not immediate, and the subject creature will feel only a slight tingling on the round the dweomer is placed, but on the round immediately following, it will begin smiling, then giggling, chuckling, tittering, snickering, guffawing, and finally collapsing into gales of <i>uncontrollable hideous laughter</i>. Although this magic mirth lasts only a single round, the affected creature must spend the next round regaining its feet, and it will be at -2 from its strength (or -2 \"to hit\" and damage) on the 3rd and 4th rounds following the spell casting. A successful save versus spell negates the effect. The saving throw depends on the intelligence of the creature. Creatures with intelligence of 3 or less are totally unaffected. Those with intelligence of 4-8 save at -6; those with intelligence of 9-12 save at -4; those with intelligence of 13-15 save at -2; and those with intelligence of 16 or greater have normal saving throw probability. The material components of the spell are a small feather, a tiny wooden paddle, and a minute tort. The tort is hurled at the subject, while the feather is waved in one hand and the paddle is tapped against the posterior of the spell caster."
    ),
    Spell('Vocalize','M',2,
        cast=tp(1,R),
        duration=tp(5,R),
        sourcebook=U,
        desc="This spell allows the recipient to cast spells that normally require a verbal component without having to make a sound, so long as the casting of the subsequent spell(s) takes place entirely within the duration of the <i>vocalize</i> spell. This spell is of great use in situations where quiet is desired, or when the recipient is under the influence of a <a href=\"/spells/silence-15-radius-cleric-lvl-2/\"><i>silence</i></a> spell. The <i>vocalize</i> spell does not negate possible effects upon other vocal communication (a <a href=\"/spells/message-magic-user-lvl-1/\"><i>message</i></a> spell could be cast from within an area of magical <i>silence</i>, but no information would be transmitted back to the caster). The spell does not negate the effect of <i>silence</i>, but merely offsets it for the purpose of subsequent spell casting. If a spell cast by means of a <i>vocalize</i> spell has some audible effect, that sound will be masked for as long as the <i>silence</i> remains in force. The material component of this spell is a bell without a clapper, or else a jailbird's tongue."
    ),
    Spell('Web','M',2,
        cast=tp(2,S),
        duration_lvl=tp(2,T),
        sourcebook=V,
        desc="A <i>web</i> spell creates a many-layered mass of strong, sticky strands similar to spider webs, but far larger and tougher. These masses must be anchored to two or more points — floor and ceiling, opposite walls, etc. — diametrically opposed.\n\n"
            "The <i>web</i> spell covers a maximum area of 8 cubic inches, and the webs must be at least 1\" thick, so a mass 4\" high, 2\" wide, and 1\" deep may be cast. Creatures caught within webs, or simply touching them, become stuck amongst the gluey fibers. Creatures with less than 13 strength must remain fast until freed by another or until the spell wears off. For every full turn entrapped by a <i>web</i>, a creature has a 5% cumulative chance of suffocating to death. Creatures with strength between 13 and 17 can break through 1' of webs per turn. Creatures with 18 or greater strength break through 1' of webs per round. (N.B. Sufficient mass equates to great strength in this case, and great mass will hardly notice webs.) Strong and huge creatures will break through 1' of webs per segment. It is important to note that the strands of a <i>web</i> spell are flammable. A magic <i>flaming sword</i> will slash them away as easily as a hand brushes away cobwebs. Any fire — torch, flaming oil, flaming sword, etc. — will set them alight and burn them away in a single round. All creatures <i>within</i> the webs will take 2-8 hit points of damage from the flames, but those freed of the strands will not be harmed. Saving throw is made at -2. If the saving throw versus <i>web</i> is made, two results may have occurred. If the creature has room to escape then he is assumed to have jumped free. If there is no room to escape then the webs are only ½ strength. The material component of this spell is a bit of spider web."
    ),
    Spell('Whip','M',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="By means of this spell, the magic-user creates a material, whip-like substance up to 1\" distant from his or her person. The spell caster can then wield this <i>whip</i> by moving his or her hand as if it held an actual one, for the magical one will respond to movements made by its evoker. The lash can be used so as to make both a whistling crack and an actual strike each turn. The sound alone is sufficient to keep animals at bay unless they save versus spell. Any animal actually struck (as indicated by a normal \"to hit\" die roll) must save versus spell at -1 to -4 or else slink away and not return for at least an hour. Note that the <i>whip</i> does not do actual damage to the creature struck. Creatures with intelligence above 3 are not affected, nor are giant-sized animals above bear-size, nor are monsters. The <i>whip</i> can also be used in melee combat, a successful \"to hit\" roll indicating that the lash has struck and wrapped around an opponent's weapon. If that weapon is an edged one, the <i>whip</i> must make a saving throw versus <i>crushing blow</i> (13 or better); if the weapon is non-edged, the <i>whip</i> must save versus <i>normal blow</i> (6 or better). Success on this saving throw indicates that the <i>whip</i> has torn the weapon from the opponent's hand — unless the opponent succeeds on a saving throw versus spell. An affected weapon will be cast to the ground, and the opponent must take 1 round to recover it. The magic bonus of a target weapon applies as a penalty to the <i>whip's</i> saving throw versus <i>crushing blow</i> or <i>normal blow</i>, and the magic resistance of an intended target opponent must fail for a \"to hit\" roll to be possible in the first place. The material component for the spell is a small bit of silk braided so as to form a miniature whip."
    ),
    Spell('Wizard Lock','M',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a <i>wizard lock</i> spell is cast upon a door, chest or portal, it magically locks it. The wizard-locked door or object can be opened only by breaking, a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>, a <a href=\"/spells/knock-magic-user-lvl-2/\"><i>knock</i></a> spell, or by a magic-user 4 or more levels higher than the one casting the spell. Note that the last two methods do <i>not remove the wizard lock</i>, they only negate it for a brief duration. Creatures of extra-dimensional nature do not affect a <i>wizard lock</i> as they do a held portal (see <a href=\"/spells/hold-portal-magic-user-lvl-1/\"><i>hold portal</i></a>)."
    ),
    Spell('Zephyr','M',2,
        cast=tp(2,S),
        duration=tp(1,S),
        sourcebook=U,
        desc="By means of this spell, a gentle draft of air moves from the spell caster and travels in the direction that he or she is facing. It continues until the maximum area of effect is reached. The force of the <i>zephyr</i> is sufficient to cause small flames to waver and dance. It fans flames and fires of larger size, making them hotter (+1 on damage dice, if applicable). It will hold back moving clouds of vapors (such as <a href=\"/spells/cloudkill-magic-user-lvl-5/\"><i>cloudkill</i></a>) for 1 round. It will weaken such vapors as <a href=\"/spells/fog-cloud-illusionist-lvl-2/\"><i>fog cloud</i></a> and <a href=\"/spells/wall-of-fog-illusionist-lvl-1/\"><i>wall of fog</i></a> so as to reduce their duration by half. It will move stagnant air, vapors, or even poisonous gases backwards by 1\", and this force likewise reduces their duration and potency by half, unless the vapor or gas is renewed by some source. The material component for this spell is a piece of fine parchment, accordion-folded and tacked near the bottom with a pin of ivory or silver."
    ),
    Spell('Blink','M',3,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell, the magic-user causes his or her material form to \"blink\" out and back to this plane once again in random period and direction during the duration of each minute the spell is in effect. (Cf. <a href=\"/creatures/blink-dog/\"><i>Blink Dog</i></a>.) The segment of the round that the spell caster \"blinks out\" is determined by random roll with 2d4, and during this same segment he or she will appear again 2' distant from his or her previous position. (Direction is determined by roll of d8: 1 = right ahead, 2 = right, 3 = right behind, 4 = behind, 5 = left behind, 6 = left, 7 = left ahead, 8 = ahead.) If some object is already occupying the space where the spell caster is indicated as \"blinking\" into, his or her form is displaced in a direction away from original (round starting) position for any distance necessary to appear in empty space, but never in excess of an additional 10'. If that extra distance still dictates the magic-user and another solid object are to occupy the same space, the spell caster is then trapped on the ethereal plane. During and after the <i>blink</i> segment of a round, the spell caster can be attacked only by opponents able to strike both locations at once, e.g. a breath weapon, <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, and similar wide area attack forms. Those not so able can only strike the magic-user if they managed to attack prior to the \"blink\" segment. The spell caster is only 75% likely to be able to perform any acts other than physical attack with a hand-held stabbing or striking weapon during the course of this spell. That is, use of any spell, device, or item might not be accomplished or accomplished in an incorrect manner or in the wrong direction. Your referee will determine success/failure and the results thereof according to the particular action being performed."
    ),
    Spell('Clairaudience','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="The <i>clairaudience</i> spell enables the magic-user to concentrate upon some locale and hear in his or her mind whatever noise is within a 6\" radius of his or her determined <i>clairaudience</i> locale center. Distance is not a factor, but the locale must be known, i.e. a place familiar to the spell caster or an obvious one (such as behind a door, around a corner, in a copse of woods, etc.). Only sounds which are normally detectable by the magic-user can be heard by use of this spell. Only metal sheeting or magical protections will prevent the operation of the spell. Note that it will function only on the plane of existence an which the magic-user is at the time of casting. The material component of the spell is a small silver horn of at least 100 g.p. value, and casting the spell causes it to disappear."
    ),
    Spell('Clairvoyance','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Similar to the <a href=\"/spells/clairaudience-magic-user-lvl-3/\"><i>clairaudience</i></a> spell, the <i>clairvoyance</i> spell empowers the magic-user to see in his or her mind whatever is within sight range from the spell locale chosen. Distance is not a factor, but the locale must be known — familiar or obvious. Furthermore, light is a factor whether or not the spell caster has the ability to see into the infrared or ultraviolet spectrums. If the area is dark, only a 1\" radius from the center of the locale of the spell's area of effect can be clairvoyed; otherwise, the seeing extends to normal vision range. Metal sheeting or magical protections will foil a <i>clairvoyance</i> spell. The spell functions only on the plane on which the magic-user is at the time of casting. The material component of the spell is a pinch of powdered pineal gland from a human or humanoid creature."
    ),
    Spell('Cloudburst','M',3,
        cast=tp(3,S),
        duration=tp(1,R),
        sourcebook=U,
        desc="This spell is identical to the <a href=\"/spells/cloudburst-cleric-lvl-3/\">3rd-level clerical spell of the same name</a>, except that a holy symbol is not part of the material component."
    ),
    Spell('Detect Illusion','M',3,
        cast=tp(3,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell is the same as the 1st-level illusionist spell <a href=\"/spells/detect-illusion-illusionist-lvl-1/\"><i>detect illusion</i></a>, except as noted above."
    ),
    Spell('Dispel Magic','M',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level cleric spell <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>."
    ),
    Spell('Explosive Runes','M',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By tracing the mystic runes upon a book, map, scroll, or similar instrument bearing written information, the magic-user prevents unauthorized reading of such. The <i>explosive runes</i> are difficult to detect, 5% per level of magic use experience of the reader, thieves having only a 5% chance in any event. When read, the <i>explosive runes</i> detonate, delivering a full 12 to 30 (6d4 + 6) hit points of damage upon the reader, who gets <i>no</i> saving throw, and either a like amount, or half that if saving throws are made, on creatures within the blast radius. The magic-user who cast the spell, as well as any other magic-users he or she instructs, can use the instrument without triggering the runes. Likewise, the magic-user can totally remove them whenever desired. They can otherwise be removed only by a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell, and the <i>explosive runes</i> last until the spell is triggered. The instrument upon which the runes are placed will be destroyed when the explosion takes place unless it is not normally subject to destruction by magical fire."
    ),
    Spell('Feign Death','M',3,
        cast=tp(1,S),
        duration=tp(6,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell, the caster or any other creature whose levels of experience/hit dice do not exceed the magic-user's own level can be put into a cataleptic state which is impossible to distinguish from actual death. Although the person/creature affected by the <i>feign death</i> spell can smell, hear, and know what is going on, no feeling or sight of any sort is possible; thus, any wounding or mistreatment of the body will not be felt and no reaction will occur and damage will be only one-half normal. In addition, paralysis, poison, or energy level drain will not affect the individual/creature under the influence of this spell, but poison injected or otherwise introduced into the body will become effective when the spell recipient is no longer under the influence of this spell, although a saving throw is permitted. Note that only a willing individual can be affected by <i>feign death</i>. The spell caster is able to end the spell effects at any time desired, but it requires 1 full round for bodily functions to begin again."
    ),
    Spell('Fireball','M',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V,
        desc="A <i>fireball</i> is an explosive burst of flame, which detonates with a low roar, and delivers damage proportionate to the level of the magic-user who cast it, i.e. 1 six-sided die (d6) for each level of experience of the spell caster. <i>Exception</i>: Magic fireball wands deliver 6 die fireballs (6d6), magic staves with this capability deliver 8 die fireballs, and scroll spells of this type deliver a fireball of from 5 to 10 dice (d6 + 4) of damage. The burst of the <i>fireball</i> does not expend a considerable amount of pressure, and the burst will generally conform to the shape of the area in which it occurs, thus covering an area equal to its normal spherical volume. [The area which is covered by the <i>fireball</i> is a total volume of roughly 33,000 cubic feet (or yards)]. Besides causing damage to creatures, the <i>fireball</i> ignites all combustible materials within its burst radius, and the heat of the <i>fireball</i> will melt soft metals such as gold, copper, silver, etc. Items exposed to the spell's effects must be rolled for to determine if they are affected. Items with a creature which makes its saving throw are considered as unaffected. The magic-user points his or her finger and speaks the range (distance and height) at which the <i>fireball</i> is to burst. A streak flashes from the pointing digit and, unless it impacts upon a material body prior to attaining the prescribed range, flowers into the <i>fireball</i>. If creatures fail their saving throws, they all take full hit point damage from the blast. Those who make saving throws manage to dodge, fall flat or roll aside, taking ½ the full hit point damage — each and every one within the blast area. The material component of this spell is a tiny ball composed of bat guano and sulphur."
    ),
    Spell('Flame Arrow','M',3,
        cast=tp(3,S),
        duration=tp(0),
        duration_lvl=tp(1,S),
        sourcebook=V,
        desc="Once the magic-user has cast this spell, he or she is able to touch one arrow or crossbow bolt (quarrel) per segment for the duration of the <i>flame arrow</i>. Each such missile so touched becomes magic, although it gains no bonuses \"to hit\". Each such missile must be discharged within 1 round, for after that period flame consumes it entirely, and the magic is lost. Fiery missiles will certainly have normal probabilities of causing combustion. and any creature subject to additional fire damage will suffer +1 hit point of damage from any <i>flame arrow</i> which hits it. The material components for this spell are a drop of oil and a small piece of flint."
    ),
    Spell('Fly','M',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="This spell enables the magic-user to bestow the power of magical flight. The creature affected is able to move vertically and/or horizontally at a rate of 12\" per move (half that if ascending, twice that if descending in a dive). The exact duration of the spell is always unknown to the spell caster, as the 1-6 turns variable addition is determined by the Dungeon Master secretly. The material component of the <i>fly</i> spell is a wing feather of any bird."
    ),
    Spell('Gust of Wind','M',3,
        cast=tp(3,S),
        duration=tp(1,S),
        sourcebook=V,
        desc="When this spell is cast, a strong puff of air originates from the magic-user and moves in the direction he or she is facing. The force of this <i>gust of wind</i> is sufficient to extinguish candles, torches, and similar unprotected flames. It will cause protected flames — such as those of lanterns — to wildly dance and has a 5% chance per level of experience of the spell caster to extinguish even such lights. It will also fan large fires outwards 1' to 6' in the direction of the wind's movement. It will force back small flying creatures 1\" to 6\" and cause man-sized ones to be held motionless if attempting to move into its force, and similarly slow large flying creatures by 50% for 1 round. It will blow over light objects. Its path is 1\" wide by 1\" of length per level of experience of the magic-user casting the <i>gust of wind</i> spell i.e. an 8th level magic-user causes a gust of wind which travels 8\". The material component of the spell is a legume seed."
    ),
    Spell('Haste','M',3,
        cast=tp(3,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When this spell is cast, affected creatures function at double their normal movement and attack rates. Thus, a creature moving at 6\" and attacking 1 time per round would move at 12\" and attack 2 times per round. Spell casting is not more rapid. The number of creatures which can be affected is equal to the level of experience of the magic-user, those creatures closest to the spell caster being affected in preference to those farther away, and all affected by haste must be in the designated area of effect. Note that this spell negates the effects of a <a href=\"/spells/slow-magic-user-lvl-3/\"><i>slow</i></a> spell. Additionally, this spell ages the recipients due to speeded metabolic processes. Its material component is a shaving of licorice root."
    ),
    Spell('Hold Person','M',3,
        cast=tp(3,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="Similar to the second level cleric <a href=\"/spells/hold-person-cleric-lvl-2/\"><i>hold person</i></a>, this spell immobilizes creatures, within range, as designated by the magic-user. If three or four persons are attacked, their saving throws are normal; but if two are attacked, their saving throws are made at -1 and if only one creature is attacked, the saving throw versus the <i>hold person</i> spell is made at -3 on the die. Partial negation of a <i>hold person</i> spell, such as would be possible by a <i>ring of spell turning</i>, causes the spell to function as a <a href=\"/spells/slow-magic-user-lvl-3/\"><i>slow</i></a> spell unless the saving throw is successful. Creatures affected by the spell are: brownies, dryads, dwarves, elves, gnolls, gnomes, goblins, half-elves, halflings, half-orcs, hobgoblins, humans, kobolds, lizard men, nixies, orcs, pixies, sprites, and troglodytes."
    ),
    Spell('Infravision','M',3,
        cast=tp(1,R),
        duration=tp(12,R),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="By means of this spell the magic-user enables the recipient of <i>infravision</i> to see light in the infrared spectrum. Thus, differences in heat wave radiations can be seen up to 6\". Note that strong sources of infrared radiation (fire, lanterns, torches, etc.) tend to blind or cast \"shadows\" just as such light does with respect to normal vision, so the infravision is affected and does not function efficiently in the presence of such heat sources. (Invisible creatures are not usually detectable by <i>infravision</i>, as the infrared light waves are affected by invisibility, just as those of the ultraviolet and normal spectrums are.) The material component of this spell is either a pinch of dried carrot or an agate."
    ),
    Spell('Invisibility 10\' Radius','M',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is essentially the same as <a href=\"/spells/invisibility-magic-user-lvl-2/\"><i>invisibility</i></a>. Those affected by it cannot see each other. Those affected creatures which attack negate the invisibility only with respect to themselves, not others made invisible, unless the spell recipient causes the spell to be broken."
    ),
    Spell('Item','M',3,
        cast=tp(3,S),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc="By means of this spell, the magic-user is able to touch any normal, non-magical item of a size appropriate to the allowable area of effect and cause it to shrink to one-twelfth of its normal size. Optionally, the caster can also change its now-shrunken composition to a cloth-like one. Only living things are entitled to a saving throw versus spell, but each save is at +4. Objects and creatures transformed to cloth make saving throws normally (as if not altered) against subsequent attacks. Objects changed by an <i>item</i> spell can be returned to normal composition and size merely by tossing them onto any solid surface or by word of command from the original spell caster. It is possible to affect a fire and its fuel with this spell."
    ),
    Spell('Leomund\'s Tiny Hut','M',3,
        cast=tp(3,S),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="When this spell is cast, the magic-user causes an opaque sphere of force to come into being around his or her person, half of the sphere projecting above the ground or floor surface, the lower hemisphere passing through the surface. This field causes the interior of the sphere to maintain at 70°F temperature in cold to 0°F, and heat up to 105°F. Cold below 0° lowers inside temperature on a 1° for 1° basis, heat above 105° raises the inside temperature likewise. The <i>tiny hut</i> will withstand winds up to 50 m.p.h. without being harmed, but wind force greater than that will destroy it. The interior of the <i>tiny hut</i> is a hemisphere, and the spell caster can illuminate it dimly upon command, or extinguish the light as desired. Note that although the force field is opaque from positions outside, it is transparent from within. In no way will <i>Leomund's Tiny Hut</i> provide protection from missiles, weapons, spells, and the like. Up to 6 other man-sized creatures can fit into the field with its creator, and these others can freely pass in and out of the <i>tiny hut</i> without harming it, but if the spell caster removes himself from it, the spell will dissipate. The material component for this spell is a small crystal bead which will shatter when spell duration expires or the hut is otherwise dispelled."
    ),
    Spell('Lightning Bolt','M',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V,
        desc="Upon casting this spell, the magic user releases a powerful stroke of electrical energy which causes damage equal to 1 six-sided die (d6) for each level of experience of the spell caster to creatures within its area of effect, or 50% of such damage to such creatures which successfully save versus the attack form. The range of the bolt is the location of the commencement of the stroke, i.e. if shot to 6\", the bolt would extend from this point to <i>n</i> inches further distance. The <i>lightning bolt</i> will set fire to combustibles, sunder wooden doors, splinter up to 1' thickness of stone, and melt metals with a low melting point (lead, gold, copper, silver, bronze). Saving throws must be made for objects which withstand the full force of a stroke (cf. <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>). The area of the <i>lightning bolt</i>'s effect is determined by the spell caster, just as its distance is. The stroke can be either a forking bolt 1\" wide and 4\" long. or a single bolt ½\" wide and 8\" long. If a 12th level magic-user cast the spell at its maximum range, 16\" in this case, the stroke would begin at 16\" and flash outward from there, as a forked bolt ending at 20\" or a single one ending at 24\". If the full length of the stroke is not possible due to the interposition of a non-conducting barrier (such as a stone wall), the <i>lightning bolt</i> will double and rebound towards its caster, its length being the normal total from beginning to end of stroke, damage caused to interposing barriers notwithstanding. Example: An 8\" stroke is begun at a range of 4\", but the possible space in the desired direction is only 3½\"; so the bolt begins at the 3½\" maximum, and it rebounds 8\" in the direction of its creator. The material components of the spell are a bit of fur and an amber, crystal or glass rod."
    ),
    Spell('Material','M',3,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U,
        desc="A <i>material</i> spell allows the magic-user to actually bring into being certain common things. There is no difficulty in causing common basic materials such as stone, earth (soil), or wood to appear. These sorts of materials in raw, unworked form are easily gained by means of this spell. Similarly, other inorganic or non-living materials such as water, air, dung, straw, etc., can be conjured. When simple plants are concerned, such as when the caster attempts to bring into being an area of grass, there is a base 100% chance of total failure, modified downward by 1% per level of the spell caster. Animal life can never be affected by this spell. In no event can worked, refined, or fabricated items be brought into being by a <i>material</i> spell, nor can rough gems or precious metals. The spell essentially enables the magic-user to create common things of a basic nature."
    ),
    Spell('Melf\'s Minute Meteors','M',3,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("This spell is unusual in two respects. First, the dweomer enables the caster to cast small globes of fire, each of which bursts into a 1 ft. diameter sphere upon impact, inflicting 1-4 points of damage upon the target creature — or otherwise igniting combustible materials (even solid planks). These meteors are missile weapons thrown by the mage, with misses being treated as grenade-like missiles. This ability continues from round to round until the caster has fired off as many as these \"meteors\" as he or she has levels of experience, until he or she decides to forego casting any additional missiles still remaining, or until a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel</i></a> magic spell is successfully cast upon the magic-user. Second, once <i>Melf's Minute Meteors</i> is cast, the magic-user has the option to discharge the available missiles at the rate of 1 every 2 segments, as desired, or 1 every round (beginning with the initial round of casting). The magic-user may not switch between these options once one of them is chosen.\n\n"
            "In the first option, the caster must point at the desired target on the second segment after the spell is cast, and a missile will be discharged. This process is repeated every 2 segments thereafter until all of the missiles are so released. Naturally, this usually will mean that the spell actually carries over into at least the following round.\n\n"
            "If the second option is chosen, the magic-user can withhold or discharge missiles as he or she sees fit, so long as one missile is let go during each subsequent round. This option has the benefit of enabling the spell caster to actually discharge one of the \"meteors\" and conjure some other spell as well in the same round. The other spell must be of such nature as to not require the continuing concentration of the spell caster, or else he or she will involuntarily forego the casting of any further missiles from the original spell. However, the magic-user's opportunity to discharge a missile and cast a spell in the same round is of such benefit that the potential loss is not of concern. If the magic-user fails to maintain an exact <i>mental</i> count of the number of missiles remaining, this is an unfailing indication that he or she has involuntarily foregone the remaining portion of the spell.\n\n"
            "The components necessary for the casting of this dweomer are nitre and sulphur formed into a bead by the admixture or pine tar, and a small hollow tube of minute proportion, fashioned from gold. The tube costs no less than 1,000 gp to construct, so fine is its workmanship and magical engraving, but it remains potent throughout numerous castings of this spell — unless damaged by accident or abuse."
        )
    ),
    Spell('Monster Summoning I','M',3,
        cast=tp(3,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Within 1-4 rounds of casting this spell, the magic-user will cause the appearance of from 2-8 first level monsters (selected at random by the referee, but whose number may be either randomly determined or selected personally by the referee, according to the strength of the monster randomly determined). These monsters will appear in the spot, within spell range, desired by the magic-user, and they will attack the spell user's opponents to the best of their ability until he or she commands that attack cease, or the spell duration expires, or the monsters ore slain. Note that if no opponent exists to fight, summoned monsters can, if communication is possible, and if they are physically capable, perform other services for the summoning magic-user. The material components of this spell are a tiny bag and a small (not necessarily lit) candle."
    ),
    Spell('Phantasmal Force','M',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V,
        desc="When this spell is cast, the magic-user creates a visual illusion which will affect all believing creatures which view the <i>phantasmal force</i>, even to the extent of suffering damage from phantasmal missiles or from falling into an illusory pit full of sharp spikes. Note that audial illusion is not a component of the spell. The illusion lasts until struck by an opponent — unless the spell caster causes the illusion to react appropriately — or until the magic-user ceases concentration upon the spell (due to desire, moving, or successful attack which causes damage). Creatures which disbelieve the <i>phantasmal force</i> gain a saving throw versus the spell, and if they succeed, they see it for what it is and add +4 to associates' saving throws if this knowledge can be communicated effectively. Creatures not observing the spell effect are immune until they view it. The spell can create the illusion of any object, or creature, or force, as long as it is within the boundaries of the spell's area of effect. This area can move within the limits of the range. The material component of the spell is a bit of fleece."
    ),
    Spell('Protection From Evil 10\' Radius','M',3,
        cast=tp(3,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="This spell is the same as the first level <a href=\"/spells/protection-from-evil-magic-user-lvl-1/\"><i>protection from evil</i></a> spell except with respect to its area of effect. See also the first level cleric <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell for general information."
    ),
    Spell('Protection From Normal Missiles','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By means of this spell, the magic-user bestows total invulnerability to hurled and projected missiles such as arrows, axes, bolts, javelins, small stones and spears. Furthermore, it causes a reduction of 1 from each die of damage inflicted by large and/or magical missiles such as ballista missiles, catapult stones, and magical arrows, bolts, javelins, etc. Note, however that this spell does not convey any protection from such magical attacks as <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireballs</i></a>, <a href=\"/spells/lightning-bolt-magic-user-lvl-3/\"><i>lightning bolts</i></a>, or <a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>magic missiles</i></a>. The material component of this spell is a piece of tortoise or turtle shell."
    ),
    Spell('Secret Page','M',3,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=U,
        desc="When cast, a <i>secret page</i> spell alters the actual contents of a page to appear to be something entirely different. Thus, a map can be changed to become a treatise on burnishing ebony walking sticks; the text of a spell can be altered to show a ledger page or even another form of spell, etc. <a href=\"/spells/comprehend-languages-magic-user-lvl-1/\"><i>Confuse languages</i></a> and <a href=\"/spells/explosive-runes-magic-user-lvl-3/\"><i>explosive runes</i></a> may be cast upon the <i>secret page</i>, but <a href=\"/spells/comprehend-languages-magic-user-lvl-1/\"><i>comprehend languages</i></a> will not reveal the actual contents of the <i>secret page</i>. The caster is able to reverse the effect of the spell by the mere utterance of a command word, then peruse the actual page, and return it to its <i>secret page</i> form thereafter. The caster can also remove the spell by double repetition of the command word. Others noting the dim magic of a page with this spell cloaking its true contents can attempt a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>, but if it fails, the page will be destroyed. Short of an <a href=\"/spells/alter-reality-illusionist-lvl-7/\"><i>alter reality</i></a> or <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> spell, only will-o-wisp or boggart essence will reveal the true nature of the subject of a <i>secret page</i> spell, if that page is not subjected to <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>. The material component of the spell is powdered herring scales."
    ),
    Spell('Sepia Snake Sigil','M',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="There are three forms of this spell, but each eventually causes the conjuration of a deep brown snake-like force. This so-called <i>sepia snake</i> springs into being and strikes at the nearest living creature (but the <i>sepia snake</i> will not attack the magic-user who cast the spell). Its attack is made as if it were a monster with hit dice equal to the level of the magic-user who cast the dweomer. If it is successful in striking, the victim is engulfed in a shimmering amber field of force, frozen and immobilized until the caster releases the dweomer or until a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell does so. Until then, nothing can get at the victim, move the shimmering force surrounding him or her, or otherwise affect the field or the victim. The victim does not age, grow hungry, sleep or regain spells while in this state, and is not aware of his or her surroundings. If the <i>sepia snake</i> misses its target, it dissipates in a flash of brown light, with a loud noise and a puff of dun-colored smoke which is 1\" in diameter and lasts for 1 round. The three applications are: 1) as a glowing sigil in the air drawn by the spell caster and pointed at the intended target; 2) as a glyph of umber marked on some surface that is touched or gazed upon; and 3) as a small character written into some magic work to protect it. The components for the spell are 100 gp worth of powdered amber, a scale from any snake, and a pinch of mushroom spores."
    ),
    Spell('Slow','M',3,
        cast=tp(3,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="A <i>slow</i> spell causes affected creatures to move and attack at one half of the normal or current rate. Thus, it negates a <a href=\"/spells/haste-magic-user-lvl-3/\"><i>haste</i></a> spell, has cumulative effect if cast upon creatures already slowed, and otherwise affects magically speeded or slowed creatures. The magic will affect as many creatures as the spell caster has levels of experience, providing these creatures are within the area of effect determined by the magic-user, i.e. the 4\" x 4\" area which centers in the direction and at the range called for by the caster. The material component of this spell is a drop of treacle."
    ),
    Spell('Suggestion','M',3,
        cast=tp(3,S),
        duration=tp(6,T),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="When this spell is cast by the magic-user, he or she influences the actions of the chosen recipient by utterance of a few words — phrases, or a sentence or two — suggesting a course of action desirable to the spell caster. The creature to be influenced must, of course, be able to understand the magic-user's <i>suggestion</i>, i.e., it must be spoken in a language which the spell recipient understands. The <i>suggestion</i> must be worded in such a manner as to make the action sound reasonable; a request asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act will automatically negate the effect of the spell. However, a <i>suggestion</i> that a pool of acid was actually pure water, and a quick dip would be refreshing, is another matter; or the urging that a cessation of attack upon the magic-user's party would benefit a red dragon, for the group could loot a rich treasure elsewhere through co-operative action, is likewise a reasonable use of the spell's power. The course of action of a <i>suggestion</i> can continue in effect for a considerable duration, such as in the case of the red dragon mentioned above. If the recipient creature makes its saving throw, the spell has no effect. Note that a very reasonable <i>suggestion</i> will cause the saving throw to be made at a penalty (such as -1, -2, etc.) at the discretion of your Dungeon Master. Undead are not subject to <i>suggestion</i>. The material components of this spell are a snake's tongue and either a bit of honeycomb or a drop of sweet oil."
    ),
    Spell('Tongues','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the fourth level cleric spell, <a href=\"/spells/tongues-cleric-lvl-4/\"><i>tongues</i></a>. Also, the material component is a small clay model of a ziggurat, which shatters when the spell is pronounced."
    ),
    Spell('Water Breathing','M',3,
        cast=tp(3,S),
        duration_lvl=tp(3,T),
        sourcebook=V,
        desc="Except as noted above, and that the material component of the spell is a short reed or piece of straw, this is the same as the third level druid spell, <a href=\"/spells/water-breathing-druid-lvl-3/\"><i>water breathing</i></a>."
    ),
    Spell('Wind Wall','M',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell brings forth an invisible curtain of wind of considerable strength — sufficient to blow birds as large as crows upward, or to tear papers and like materials from unsuspecting hands. (If in doubt, a saving throw versus spell determines whether the subject maintains its grasp.) Normal insects cannot pass such a barrier. Loose material, even cloth garments, caught in a <i>wind wall</i> will fly upward. The material components are a tiny fan and a feather of exotic origin."
    ),
    Spell('Charm Monster','M',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("This spell is similar to a <a href=\"/spells/charm-person-magic-user-lvl-1/\"><i>charm person</i></a> spell, but it will affect any living creature — or several creatures of lesser level as explained hereafter. The magic-user casts the <i>charm monster</i> spell, and any affected creature regards the spell caster as friendly, an ally or companion to be treated well or guarded from harm. If communication is possible, the charmed creature will follow reasonable requests, instructions, or oders most faithfully (cf. <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> spell). Affected creatures will eventually come out from under the influence of the spell, and the probability of such breaking of a <i>charm monster</i> spell is a function of the creature's level, i.e. its number of hit dice:\n\n"
            "<table>"
            "<tr><th>Monster Level or Hit Dice</th><th>Percent Chance/Week of Breaking Spell</th></tr>"
            "<tr><td>1st or up to 2</td><td>5%</td></tr>"
            "<tr><td>2nd or up to 3+2</td><td>10%</td></tr>"
            "<tr><td>3rd or up to 4+4</td><td>15%</td></tr>"
            "<tr><td>4th or up to 6</td><td>25%</td></tr>"
            "<tr><td>5th or up to 7+2</td><td>35%</td></tr>"
            "<tr><td>6th or up to 8+4</td><td>45%</td></tr>"
            "<tr><td>7th or up to 10</td><td>60%</td></tr>"
            "<tr><td>8th or up to 12</td><td>75%</td></tr>"
            "<tr><td>9th or over 12</td><td>90%</td></tr>"
            "</table>\n\n"
            "Naturally, overtly hostile acts by the person charming the monster will automatically break the spell, or at the very least allow the monster a new saving throw versus the charm. The spell will affect from 2-8 1st level creatures, 1-4 2nd level creatures, 1 or 2 3rd level, or 1 creature of 4th or higher level."
        )
    ),
    Spell('Confusion','M',4,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, this spell is identical to the seventh level druid spell, <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a>. However, it affects a basic 2-16 creatures. Its material component is a set of three nut shells."
    ),
    Spell('Dig','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="A <i>dig</i> spell enables the caster to excavate 125 cubic feet of earth, sand, or mud per round. The hole thus dug is a cube 5' per side. The material thrown from the excavation scatters evenly around the pit. If the magic-user continues downward beyond 5', there is a chance that the pit will collapse: 15%/additional 5' in depth in earth, 35%/additional 5' depth in sand, and 55%/additional 5' depth in mud. Any creature at the edge (1') of such a pit uses its dexterity score as a saving throw to avoid falling into the hole with a score equal to or less than the dexterity meaning that a fall was avoided. Any creature moving rapidly towards a pit area will fall in unless it saves versus magic. Any creature caught in the center of a pit just dug will always fall in. The spell caster uses a miniature shovel and tiny bucket to activate a <i>dig</i> spell and must continue to hold these material components while each pit is excavated."
    ),
    Spell('Dimension Door','M',4,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="By means of a <i>dimension door</i> spell, the magic-user instantly transfers himself or herself up to 3\" distance per level of experience of the spell caster. This special form of teleportation allows for no error, and the magic-user always arrives at exactly the spot desired — whether by simply visualizing the area (within spell transfer distance, of course) or by stating direction such as \"30 inches straight downwards,\" or \"upwards to the northwest, 45 degree angle, 42 inches.\" If the magic-user arrives in a place which is already occupied by a solid body, he or she remains in the <i>Astral Plane</i> until located by some helpful creature willing to cast a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> upon the person, for he or she is stunned and cannot successfully perform any spell casting. If distances are stated and the spell caster arrives with no support below his or her feet (i.e. in mid-air), falling and damage will result unless further magical means are employed. All that the magic-user wears or carries, subject to a maximum weight equal to 5,000 gold pieces of non-living matter, or half that amount of living matter, is transferred with the spell caster. Recovery from use of a <i>dimension door</i> spell requires 7 segments."
    ),
    Spell('Dispel Illusion','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="This spell is similar to the <a href=\"/spells/dispel-illusion-illusionist-lvl-3/\">3rd-level illusionist spell</a> of the same name. A magic-user attempting to dispel an illusion is considered at <i>two</i> levels below his actual level with respect to <i>illusion/phantasm</i> spells cast by an illusionist."
    ),
    Spell('Enchanted Weapon','M',4,
        cast=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="This spell turns an ordinary weapon into a magical one. The weapon is the equivalent of a +1 weapon but has <i>no</i> bonuses whatsoever. Thus, arrows, axes, bolts, bows, daggers, hammers, maces, spears, swords, etc. can be made into <i>enchanted</i> weapons. Two small (arrows, bolts, daggers, etc.) or one large (axe, bow, hammer, mace, etc.) weapon can be affected by the spell. Note that successful hits by enchanted missile weapons cause the spell to be broken, but that otherwise the spell duration lasts until the time limit based on the level of experience of the magic-user casting it expires, i.e. 40 rounds (4 turns) in the case of an 8th level magic-user. The material components of this spell are powdered lime and carbon."
    ),
    Spell('Evard\'s Black Tentacles','M',4,
        cast=tp(8,S),
        duration=tp(1,R),
        sourcebook=U,
        desc="By means of this spell the caster creates many rubbery, black tentacles in the area of effect of the dweomer. These waving members seem to spring forth from the earth, floor, or whatever surface is underfoot — including water. Each tentacle is 10' long, AC 4, and takes as many points of damage to destroy as the magic-user who cast the spell has levels of experience. Furthermore, there will be one such tentacle for each of the levels of experience of the spell caster. Any creature within range of the writhing tentacles is subject to attack. If more than one target is within range of a tentacle, the probability of attack on each is determined and the result found by die roll. A victim of a tentacle attack must make a saving throw versus spell. If this succeeds, the victim takes 1-4 hit points of damage from initial contact with the tentacle, and it then is destroyed. Failure to save indicates that the damage inflicted will be 2-8 points, the ebon member is wrapped around its victim, and damage will be 3-12 points on the second and succeeding rounds. Since these tentacles have no intelligence to guide them, there is a possibility that they will entwine any object — a tree, post, pillar — or continue to squeeze a dead opponent. Once grasped, a tentacle remains wrapped around its chosen target until the tentacle is destroyed by some form of attack or it disappears due to the expiration of the dweomer's duration. The component for this spell is a piece of tentacle from a giant octopus or giant squid."
    ),
    Spell('Extension I','M',4,
        cast=tp(2,S),
        duration=tp(0),
        sourcebook=V,
        desc="By use of an <i>extension I</i> spell the magic-user prolongs the <i>duration</i> of a previously cast first, second, or third level spell by 50%. Thus, a <a href=\"/spells/levitate-magic-user-lvl-2/\"><i>levitation</i></a> spell can be made to function 1½ turns/level, a <a href=\"/spells/hold-person-magic-user-lvl-3/\"><i>hold person</i></a> spell made to work for 3 rounds/level, etc. Naturally, the spell has effect only on such spells where <i>duration</i> is meaningful."
    ),
    Spell('Fear','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When a <i>fear</i> spell is cast, the magic-user sends forth an invisible ray which causes creatures within its area of effect to turn away from the spell caster and flee in panic. Affected creatures are likely to drop whatever they are holding when struck by the spell; the base chance of this is 60% at 1st level (or at 1 hit die), and each level (or hit die) above this reduces the probability by 5%, i.e. at 10th level there is only a 15% chance, and at 13th level 0% chance. Creatures affected by <i>fear</i> flee at their fastest rate for the number of melee rounds equal to the level of experience of the spell caster. The panic takes effect on the melee round following the spell casting, but dropping of items in hand will take place immediately. Of course, creatures which make their saving throws versus the spell are not affected. The material component of this spell is either the heart of a hen or a white feather."
    ),
    Spell('Fire Charm','M',4,
        cast=tp(4,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By means of this spell the magic-user causes a normal fire source such as a brazier, flambeau, or bonfire to serve as a magical agent, for from this source he or she causes a gossamer veil of multi-hued flame to circle the fire at 5' distance. Any creatures observing the fire or the dancing circle of flame around it must save versus magic or be <i>charmed</i> into remaining motionless and gazing, transfixed at the flames. While so <i>charmed</i>, creatures are subject to <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> spells of 12 or fewer words, saving against their influence at -3. The <i>fire charm</i> is broken by any physical attack upon the <i>charmed</i> creature, if a solid object is interposed between the creature and the veil of flames so as to obstruct vision, or when the duration of the spell is at an end. Note that the veil of flame is not a magical fire, and passing through it incurs the same type and amount of damage as would be sustained from passing through its original fire source. The material component for this spell is a small piece of multicolored silk of exceptional thinness which the dweomercrafter must throw into the fire source."
    ),
    Spell('Fire Shield','M',4,
        cast=tp(4,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("By casting this spell the magic-user appears to immolate himself or herself, but the flames are thin and wispy shedding light equal only to half that of a normal torch (15' radius of dim light), and colored blue or green if variation <i>A</i> is cast, violet or blue if variation <i>B</i> is employed. Any creature striking the spell caster with body or hand-held weapons will inflict normal damage upon the magic-user, but the attacker will take double the amount of damage so inflicted! The other spell powers depend on the variation of the spell used:\n\n"
            "A)	The flames are hot, and any cold-based attacks will be saved against at +2 on the dice, and either half normal damage or no damage will be sustained, fire-based attacks are normal, but if the magic-user fails to make the required saving throw (if any) against them, he or she will sustain double normal damage. The material component for this variation is a bit of phosphorous.\n\n"
            "B)	The flames are cold, and any fire-based attack will be saved against at +2 on the dice, and either half normal damage or no damage will be sustained; cold-based attacks are normal, but if the magic-user fails to make the required saving throw (if any) against them, he or she will sustain double normal damage. The material component for this variation is a live firefly or glow worm or the tail portions of 4 dead ones.")
    ),
    Spell('Fire Trap','M',4,
        cast=tp(3,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="Any closable item (book, box, bottle. chest, coffer, coffin, door, drawer, and so forth) is affected by a <i>fire trap</i> spell, but the item so trapped cannot have a second spell such as <a href=\"/spells/hold-portal-magic-user-lvl-1/\"><i>hold portal</i></a> or <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard lock</i></a> placed upon it except as follows: if a <i>fire trap</i>/<a href=\"/spells/hold-portal-magic-user-lvl-1/\"><i>hold portal</i> is attempted, only the spell first cast will work, and the other will be negated (both negated if cast simultaneously). If a <i>fire trap</i> is cast after a <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard lock</i></a>, the former is negated, if both are cast simultaneously both are negated, and if a <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard lock</i></a> is cast after placement of a <i>fire trap</i> there is a 50% chance that both spells will be negated. A <a href=\"/spells/knock-magic-user-lvl-2/\"><i>knock</i></a> spell will not affect a <i>fire trap</i> in any way — as soon as the offending party enters/touches, the trap will discharge. The caster can use the trapped object without discharging it. When the trap is discharged there will be an explosion of 5' radius, and all creatures within this area must make saving throws versus magic. Damage is 1-4 hit points plus 1 hit point per level of the magic-user who cast the spell, or one-half the total amount for creatures successfully saving versus magic. The item trapped is NOT harmed by this explosion. There is only 50% of the normal chance to detect a <i>fire trap</i>, and failure to remove it when such action is attempted detonates it immediately. To place this spell, the caster must trace the outline of the closure with a bit of sulphur or saltpetre."
    ),
    Spell('Fumble','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When a <i>fumble</i> spell is cast, the magic-user causes the recipient of the magic to suddenly become clumsy and awkward. Running creatures will trip and fall, those reaching for an item will <i>fumble</i> and drop it, those employing weapons will likewise awkwardly drop them. Recovery from a fall or of a fumbled object will typically require the whole of the next melee round. Note that breakable items might suffer damage when dropped. If the victim makes his or her saving throw, the <i>fumble</i> will simply make him or her effectively operate at one-half normal efficiency (cf. <a href=\"/spells/slow-magic-user-lvl-3/\"><i>slow</i></a> spell). The material component of this spell is a dab of solidified milk fat."
    ),
    Spell('Hallucinatory Terrain','M',4,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this spell the magic-user causes an illusion which hides the actual terrain within the area of the spell's effect. Thus, open fields or a road can be made to look as if a swamp or hill or crevasse or same other difficult or impassable terrain existed there. Also, a pond can be made to appear as a grassy meadow, a precipice look as if it were a gentle slope, or a rock-strewn gully made to look as if it were a wide and smooth road. The <i>hallucinatory terrain</i> persists until a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell is cast upon the area or until it is contacted by an intelligent creature. Each level of experience of the magic-user enables him or her to affect a larger area. At 10th level, a magic-user can affect an area up to 10\" x 10\" square, while at 12th level the spell caster affects a 12\" x 12\" square area. The material components of this spell are a stone, a twig, and a bit of green plant — leaf or grass blade."
    ),
    Spell('Ice Storm','M',4,
        cast=tp(4,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="When this spell is cast, the magic-user causes either great hail stones to pound down in an area of 4\" diameter and inflict from 3 to 30 (3d10) hit points of damage on any creatures within the area of effect; or the <i>ice storm</i> can be made to cause driving sleet to fall in an area of 8\" diameter and both blind creatures within its area of effect for the duration of the spell and cause the ground in the area to be icy, thus slowing movement within by 50% and making it 50% probable that a moving creature will slip and fall when trying to move. The material components for this spell are a pinch of dust and a few drops of water. (Note that this spell will negate a <a href=\"/spells/heat-metal-druid-lvl-2/\"><i>heat metal</i></a> spell, but its first application will also cause damage in the process)."
    ),
    Spell('Leomund\'s Secure Shelter','M',4,
        cast=tp(4,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc=("This spell enables the magic-user to magically call into being a sturdy cottage or lodge, made of material which is common in the area where the spell is cast — stone, timber, or (at worst) sod. The floor area of lodging will be 30 square feet per level of the spell caster, and the surface will be level, clean, and dry. In all respects the lodging will resemble a normal cottage, with a sturdy door, two or more shuttered windows, and a small fireplace.\n\n"
            "While the lodging will be secure against winds of up to 70 miles per hour, it has no heating or cooling source (other than natural insulation qualities). Therefore, it must be heated as a normal dwelling, and extreme heat will certainly affect it, and its occupants, adversely. The dwelling does, however, provide considerable security otherwise, as it will be as strong as a normal stone building regardless of its material composition, will resist flames and fire as if it were stone, and will be generally impervious to normal missiles (but not the sort cast by siege machinery or giants). The door, shutters, and even chimney are secure against intrusion, the two former being <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard locked</i></a> and the latter being secured by a top grate of iron and a narrow flue. In addition, these three areas are protected by an <a href=\"/spells/alarm-magic-user-lvl-1/\"><i>alarm</i></a> spell. Lastly, an <a href=\"/spells/unseen-servant-magic-user-lvl-1/\"><i>unseen servant</i></a> is called up to provide service to the spell caster.\n\n"
            "The inside of a <i>Leomund's Secure Shelter</i> will contain crude furnishings as desired by the spell caster — up to 8 bunks, a trestle table and benches, as many as 4 chairs or 8 stools, and a writing desk. The material components of this spell are a square chip of stone, crushed lime, a few grains of sand, a sprinkling of water, and several splinters of wood. These must be augmented by the components of the <a href=\"/spells/alarm-magic-user-lvl-1/\"><i>alarm</i></a> and <a href=\"/spells/unseen-servant-magic-user-lvl-1/\"><i>unseen servant</i></a> spells if these are to be included in the spell; i.e. string and silver wire and a small bell."
        )
    ),
    Spell('Magic Mirror','M',4,
        cast=tp(1,H),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="By means of this spell, the magic-user changes a normal mirror into a scrying device similar to a crystal ball. The details of the use of a scrying device are found on p. 141 of the DMG under the description for the <i>crystal ball</i>. The mirror used must be of finely wrought and highly polished silver of a minimum cost of 1,000 gp. This mirror is not harmed by casting of the spell as are the other material components — the eye of a hawk, an eagle, or even a roc, and nitric acid, copper and zinc (cf. 5th-level cleric spell <a href=\"/spells/magic-font-cleric-lvl-5/\"><i>magic font</i></a> and 2nd-level druid spell <a href=\"/spells/reflecting-pool-druid-lvl-2/\"><i>reflecting pool</i></a>). The following spells can be cast through a <a href=\"/spells/magic-mirror-magic-user-lvl-4/\"><i>magic mirror</i></a>: <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a>, <a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect good/evil</i></a>, <a href=\"/spells/message-magic-user-lvl-1/\"><i>message</i></a>, and <a href=\"/spells/detect-illusion-illusionist-lvl-1/\"><i>detect illusion</i></a>. There is a chance of the target realizing he or she is being watched. The base chance for a target to detect any <i>crystal ball</i>-like spell is listed in the <i>crystal ball</i> item description, with the following additions: A cavalier has a base 5% chance of detecting scrying and a barbarian has a base 1% chance."
    ),
    Spell('Massmorph','M',4,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast upon willing creatures of man-size or smaller, up to 10 such creatures per level of experience of the magic-user can be made to appear as normal trees of any sort. Thus, a company of creatures can be made to appear as a copse, grove, or orchard. Furthermore, these <i>massmorphed</i> creatures can be passed through — and even touched — by other creatures without revealing the illusion. Note, however, that blows to the creature-trees will reveal their nature, as damage will be sustained by the creatures struck and blood will be seen. Creatures <i>massmorphed</i> must be within the spell's area of effect. Unwilling creatures are not affected. The spell persists until the caster commands it to cease or until a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> is cast upon the creatures. The material component of this spell is a handful of bark chips."
    ),
    Spell('Minor Globe of Invulnerability','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell creates a magical sphere around the caster which prevents any first, second or third level spells from penetrating, i.e. the area of effect of any such spells does not include the area of the <i>minor globe of invulnerability</i>. However, any sort of spells can be cast <i>out</i> of the magical sphere, and they pass from the caster of the <i>globe</i>, through its area of effect, and to their target without effect upon the <i>minor globe of invulnerability</i>. Fourth and higher level spells are not affected by the globe. It can be brought down by a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell. The material component of the spell is a glass or crystal bead."
    ),
    Spell('Monster Summoning II','M',4,
        cast=tp(4,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is similar to the third level <a href=\"/spells/monster-summoning-i-magic-user-lvl-3/\"><i>monster summoning I</i></a> spell. Its major difference is that 1-6 second level monsters are conjured up. The material components are the same as those of the lesser spell. There is also a 1-4 round delay."
    ),
    Spell('Otiluke\'s Resilient Sphere','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When this spell is cast, the result is a globe of shimmering force which encapsulates the subject creature — if it is small enough to fit within the diameter of the sphere and it fails to successfully save versus spell. The <i>resilient sphere</i> will contain its subject for as long as the dweomer persists, and it is not subject to damage of any sort except from a <i>rod of cancellation</i>, a <i>wand of negation</i>, or a <a href=\"/spells/disintegrate-magic-user-lvl-6/\"><i>disintegrate</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell. These will cause it to be destroyed without harm to the subject. Nothing can pass through the sphere, inside or out, and the target can breathe normally. The subject may struggle, but all that will occur is a movement of the sphere. The globe can be physically moved either by people outside the globe, or by the struggles of those within. The material components of the spell are a hemispherical piece of diamond (or similar hard, clear gem material) and a matching hemispherical piece of gum arabic."
    ),
    Spell('Plant Growth','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as a third level druid spell, <a href=\"/spells/plant-growth-druid-lvl-3/\"><i>plant growth</i></a>."
    ),
    Spell('Polymorph Other','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>polymorph other</i> spell is a powerful magic which completely alters the form and ability, and possibly the personality and mentality, of the recipient. Of course, creatures with a lower intelligence cannot be polymorphed into something with a higher intelligence, but the reverse is possible. The creature polymorphed must make a \"system shock\" (cf. CONSTITUTION) roll to see if it survives the change. If it is successful, it then acquires all of the form and abilities of the creature it has been polymorphed into. There is a base 100% chance that this change will also change its personality and mentality into that of the creature whose form it now possesses. For each 1 point of intelligence of the creature polymorphed, subtract 5% from the base chance. Additionally, for every hit die of difference between the original form and the form it is changed into by the spell, the polymorphed creature must adjust the base chance percentage by +/-5% per hit die below or above its own number (or <i>level</i> in the case of characters). The chance for assumption of the personality and mentality of the new form must be checked daily until the change takes place. (Note that all creatures generally prefer their own form and will not <i>willingly</i> stand the risk of being subjected to this spell!) If a one hit die orc of 8 intelligence is <i>polymorphed</i> into a white dragon with 6 hit dice, for example, it is 85% (100% - [5% x 8 intelligence + [(6 - 1) x 5%] = 85%) likely to actually become one in all respects, but in any case it will have the dragon's physical and mental capabilities; and if it does not assume the personality and mentality of a white dragon, it will know what it formerly knew as well. Another example: an 8th level fighter successfully <i>polymorphed</i> into a blue dragon would know combat with weapons and be able to employ them with prehensile dragon forepaws if the fighter did not take on dragon personality and mentality. However, the new form of the <i>polymorphed</i> creature may be <i>stronger</i> than it looks, i.e. a mummy changed to a puppy dog would be very tough, or a brontosaurus changed to an ant would be impossible to squash merely from being stepped on by a small creature or even a man-sized one. The magic-user must use a <a href=\"/spells/dispel-magic-magic-user-lvl-3/\"><i>dispel magic</i></a> spell to change the <i>polymorphed</i> creature back to its original form, and this too requires a \"system shock\" saving throw. The material component of this spell is a caterpillar cocoon."
    ),
    Spell('Polymorph Self','M',4,
        cast=tp(3,S),
        duration_lvl=tp(2,T),
        sourcebook=V,
        desc="When this spell is cast, the magic-user is able to assume the form of any creature — from as small as a wren to as large as a hippopotamus — and its form of locomotion as well. The spell does <i>not</i> give the other abilities (attack, magic, etc.), nor does it run the risk of changing personality and mentality. No \"system shock\" check is required. Thus, a magic-user changed to an owl could fly, but his or her vision would be human; a change to a black pudding would enable movement under doors or along halls and ceilings, but not the pudding's offensive or defensive capabilities. Naturally, the strength of the new form must be sufficient to allow normal movement. The spell caster can change his or her form as often as desired, the change requiring only 5 segments. Damage to the <i>polymorphed</i> form is computed as if it were inflicted upon the magic-user, but when the magic-user returns to his or her own form, from 1 to 12 (d12) points of damage are restored."
    ),
    Spell('Rary\'s Mnemonic Enhancer','M',4,
        cast=tp(1,T),
        duration=tp(1,D),
        sourcebook=V,
        desc="By means of this spell the magic-user is able to memorize, or retain the memory of, three additional spell levels, i.e. three spells of the first level, or one first and one second, or one third level spell. The magic-user can elect to immediately memorize additional spells or he or she may opt to retain memory of a spell cast by means of the <i>Enhancer</i>. The material components of the spell are a piece of string, an ivory plaque of at least 100 g.p. value, and an ink composed of squid secretion and either black dragon's blood or giant slug digestive juice. All components disappear when the spell is cast."
    ),
    Spell('Remove Curse','M',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level cleric spell, <a href=\"/spells/remove-curse-cleric-lvl-3/\"><i>remove curse</i></a>."
    ),
    Spell('Shout','M',4,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="When a <i>shout</i> spell is cast, the magic-user empowers himself or herself with tremendous vocal powers. Via the dweomer of the spell, the caster releases an ear-splitting noise which has a principal effect in a cone shape radiating from the mouth of the caster to a 3\" terminus. Any creature within this area will be deafened for 2-12 rounds and take a like amount (2-12 points) of damage (unless a saving throw is made). Any exposed brittle or similar substance subject to sonic vibrations will be shattered by a <i>shout</i>, e.g. a <a href=\"/spells/wall-of-ice-magic-user-lvl-4/\"><i>wall of ice</i></a>. A spell of this nature can be employed but once per day, for otherwise the caster might permanently deafen himself or herself. The material components for casting the <i>shout</i> spell are a drop of honey, a drop of citric acid, and a small cone made from a bull's or ram's horn."
    ),
    Spell('Stoneskin','M',4,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="When this spell is cast, the affected creature gains a virtual immunity to any attack by cut, blow, projectile or the like. Thus, even a <i>sword of sharpness</i> would not affect a creature protected by <a href=\"/spells/stoneskin-magic-user-lvl-4/\"><i>stoneskin</i></a>, nor would a rock hurled by a giant, a snake's strike, etc. However, magic attacks from such spells as <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, <a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>magic missile</i></a>, <a href=\"/spells/lightning-bolt-magic-user-lvl-3/\"><i>lightning bolt</i></a>, and so forth would have normal effect. Any attack or attack sequence from a single opponent dispels the dweomer, although it makes the creature immune to that single attack or attack sequence. Attacks with relatively soft weapons, such as a monk's hands, an ogrillon's first, etc, will inflict 1-2 points of damage on the attacker for each such attack while the attacked creature is protected by the <a href=\"/spells/stoneskin-magic-user-lvl-4/\"><i>stoneskin</i></a> spell, but will not dispel the dweomer. The material components of the spell are granite and diamond dust sprinkled on the recipient's skin."
    ),
    Spell('Ultravision','M',4,
        cast=tp(4,S),
        duration=tp(6,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc="By means of this spell the magic-user empowers the recipient to see radiation in the ultraviolet spectrum. In night conditions this means that vision will be clear, as if it were daylight, to a range of 100 yards, and shadowy and indistinct from beyond 100 yards to about 300 yards distance. If the night is very dark, with thick clouds overhead, reduction of ultravisual sight is 50%. Where more than about 6 feet of earth or 3 feet of stone interpose between the sky and the individual, such as in virtually any underground area, ultravision allows only vision of the dimmest sort in about a 3-foot radius, since the ultraviolet rays are screened out. (Of course, if an emission source is nearby, the visual capabilities improve accordingly.) Nearby light, including the radiance shed by magic items, tends to spoil ultravision, the brightness of the rays \"blinding\" the eyes to dimmer areas more distant. The material component for this spell is a crushed amethyst of at least 500 gp value."
    ),
    Spell('Wall of Fire','M',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell differs from the fifth level druid spell, <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a> only as indicated above and as stated below: the flame color is either violet or reddish blue, base damage is 2-12 hit points (plus 1 hit point per level), the radius of the ring-shaped <i>wall of fire</i> is 1\" + 1/4\" per level of experience of the magic user casting it, and the material component of the spell is phosphorus. "
    ),
    Spell('Wall of Ice','M',4,
        cast=tp(4,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="When this spell is cast, a sheet of strong, flexible ice is created. The wall is primarily defensive, stopping pursuers and the like. The wall is one inch thick per level of experience of the magic-user. It covers a 1\" square area per level, i.e. a 10th level magic-user would cause a <i>wall of ice</i> up to 10\" long and 1\" high, or 5\" long and 2\" high, and so forth. Any creature breaking through the ice will suffer 2 hit points of damage per inch of thickness of the wall, fire-using creatures will suffer 3 hit points, cold-using creatures only 1 hit point when breaking through. If this spell is cast to form a horizontal sheet to fall upon opponents, it has the same effect as an <a href=\"/spells/ice-storm-magic-user-lvl-4/\"><i>ice storm's</i></a> hail stones in the area over which it falls. Magical fires such as Fireballs and fiery dragon breath will melt a wall of ice in 1 round, though they will cause a great cloud of steamy fog which will last 1 turn, but normal fires or lesser magical ones will not hasten its melting. The material component of this spell is a small piece of quartz or similar rock crystal."
    ),
    Spell('Wizard Eye','M',4,
        cast=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When this spell is employed, the magic-user creates an invisible sensory organ which sends visual information to him or her. The <i>wizard eye</i> travels at 3\" per round, viewing an area ahead as a human would or 1\" per round examining the ceiling and walls as well as the floor ahead and casually viewing the walls ahead. The <i>wizard eye</i> can \"see\" with infravision at 10', or it \"sees\" up to 60' distant in brightly lit areas. The <i>wizard eye</i> can travel in any direction as long as the spell lasts. The material component of the spell is a bit of bat fur."
    ),
    Spell('Airy Water','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>airy water</i> spell turns normal liquid such as water or water based infusions or solutions to a less dense, breathable substance. Thus, if the magic-user were desirous of entering an underwater place, he or she would step into the water, cast the spell and sink downwards in a globe of bubbling water which he or she and any companions in the spell's area of effect could move freely in and breathe just as if it were air rather than water. The globe will move with the spell caster. Note that water breathing creatures will avoid a sphere (or hemisphere) of <i>airy water</i>, although intelligent ones can enter it if they are able to move by means other than swimming, but no water-breathers will be able to breathe in an area affected by this spell. There is only one word which needs to be spoken to actuate the magic, and the material component of the spell is a small handful of alkaline or bromine salts."
    ),
    Spell('Animal Growth','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, and for the fact that the material component of the spell is a pinch of powdered bone, this is the same as the fifth level druid spell <a href=\"/spells/animal-growth-druid-lvl-5/\"><i>animal growth</i></a>."
    ),
    Spell('Animate Dead','M',5,
        cast=tp(5,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level cleric spell <a href=\"/spells/animate-dead-cleric-lvl-3/\"><i>animate dead</i></a>."
    ),
    Spell('Avoidance','M',5,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="By means of this spell, the caster sets up a natural repulsion between the affected object and any living things. Thus, any living creature attempting to touch the affected object will be repulsed (unable to come closer than 1'), or will repulse the affected object, depending on the relative mass of the two; i.e., a lone halfling attempting to touch an iron chest with an <i>avoidance</i> spell upon it will be thrown back; a dozen such halflings would find themselves unable to come within 1' of the chest, while the chest would skitter away from a giant-sized creature as the creature approached. The material component for the spell is a magnetized needle. Because the spell cannot be cast upon living things, any attempt to cast <i>avoidance</i> upon the apparel or possessions borne by a living creature entitle the subject creature to make a saving throw. The reverse of this spell, <i>attraction</i>, uses the same material components, and sets up a natural attraction between the affected object and all living things. The creature will be drawn to the object if the creature is smaller, or the object will slide toward the creature if the creature is of greater mass than the object. A successful <i>bend bars</i> roll must be made to remove an object once it has adhered to another object or creature in this fashion."
    ),
    Spell('Bigby\'s Interposing Hand','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="<i>Bigby's Interposing Hand</i> is a large to huge-sized magic member which appears and places itself between the spell caster and his or her chosen opponent. This disembodied hand then remains between the two, regardless of what the spell caster does subsequently or how the opponent tries to get around it. The size of the <i>Hand</i> is determined by the magic-user, and it can be human-sized all the way up to titan-sized. It takes as many hit points of damage to destroy as the magic-user who cast it. Any creature weighing less than 2,000 pounds trying to push past it will be slowed to one-half normal movement. The material component of the spell is a glove."
    ),
    Spell('Cloudkill','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell generates a billowing cloud of ghastly yellowish green vapors which is so toxic as to slay any creature with fewer than 4 + 1 hit dice, cause creatures with 4 + 1 to 5 + 1 hit dice to save versus poison at -4 on the dice roll, and creatures up to 6 hit dice (inclusive) to save versus poison normally or be slain by the <i>cloud</i>. The cloudkill moves away from the spell caster at 1\" per round, rolling along the surface of the ground. A wind will cause it to alter course, but it will not move back towards its caster. A strong wind will break it up in 4 rounds, and a greater wind force prevents the use of the spell. Very thick vegetation will disperse the <i>cloud</i> in two rounds, i.e. moving through such vegetation for 2\". As the vapors are heavier than air, they will sink to the lowest level of the land, even pour down den or sinkhole openings; thus, it is ideal for slaying nests of giant ants, for example."
    ),
    Spell('Conjure Elemental','M',5,
        cast=tp(1,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc=("There are actually four spells in one as respects <i>conjure elemental</i>. The magic-user is able to conjure an air, earth, fire or water elemental with this spell — assuming he or she has the material component for the particular elemental. A considerable fire source must be in range to conjure that type of elemental; a large amount of water must be likewise available for conjuration of a water elemental. Conjured elementals are very strong — see ADVANCED DUNGEONS & DRAGONS, MONSTER MANUAL — typically having 16 hit dice (16d8). It is possible to conjure up successive elementals of different type if the spell caster has memorized two or more of these spells. The type of elemental to be conjured must be decided upon before memorizing the spell. The elemental conjured up must be controlled by the magic-user, i.e. the spell caster must concentrate on the elemental doing his or her commands, or it will turn on the magic-user and attack. The elemental, however, will not cease a combat to do so, but it will avoid creatures when seeking its conjurer. If the magic-user is wounded or grappled, his or her concentration is broken. There is always a 5% chance that the elemental will turn on its conjurer regardless of concentration, and this check is made at the end of the second and each succeeding round. The elemental can be controlled up to 3\" distant per level of the spell caster. The elemental remains until its form on this plane is destroyed due to damage or the spell's duration expires. Note that water elementals are destroyed if they move beyond 6\" of a body of water. The material component of this spell (besides the quantity of the element at hand) is a small amount of:\n\n"
            "   Air Elemental — burning incense\n"
            "   Earth Elemental — soft clay\n"
            "   Fire Elemental — sulphur and phosphorus\n"
            "   Water Elemental — water and sand\n\n"
            "N.B. Special protection from uncontrolled elementals is available by means of a pentacle, pentagram, thaumaturgic triangle, magic circle, or <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a> spell."
        )
    ),
    Spell('Cone of Cold','M',5,
        cast=tp(5,S),
        duration=tp(0),
        sourcebook=V,
        desc="When this spell is cast, it causes a cone-shaped area originating at the magic-user's hand and extending outwards in a cone ½\" long per level of the caster. It drains heat and causes 1 four-sided die, plus 1 hit point of damage (1d4 +1), per level of experience of the magic-user. For example, a 10th level magic-user would cast a <i>cone of cold</i> causing 10d4 + 10 hit points of damage. Its material component is a crystal or glass cone of very small size."
    ),
    Spell('Contact Other Plane','M',5,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("When this spell is cast, the magic-user sends his or her mind to another plane of existence in order to receive advice and information from powers there. As these powers are located at random, and resent such contact in any case, only brief answers will be given. (Your DM will answer all questions with a \"yes\", \"no\", \"maybe\", \"never\", \"irrelevant\", etc.) The character can contact an elemental plane or some plane further removed. For every 2 levels of experience of the magic-user one question may be asked. Contact with minds far removed from the plane of the magic-user increases the probability of the spell caster going insane or dying, but the chance of the power knowing the answer, as well as the probability of the being telling the correct answer, are likewise increased by moving to distant planes:\n\n"
            "<table>"
            "<tr><th>Plane</th><th>Likelihood of Insanity*</th><th>Likelihood of Knowledge</th><th>Probability of Veracity**</th></tr>"
            "<tr><td>Elemental</td><td>20%</td><td>90%***</td><td>75%</td></tr>"
            "<tr><td>1 removed</td><td>5%</td><td>60%</td><td>65%</td></tr>"
            "<tr><td>2 removed</td><td>10%</td><td>65%</td><td>67%</td></tr>"
            "<tr><td>3 removed</td><td>15%</td><td>70%</td><td>70%</td></tr>"
            "<tr><td>4 removed</td><td>20%</td><td>75%</td><td>73%</td></tr>"
            "<tr><td>5 removed</td><td>25%</td><td>80%</td><td>75%</td></tr>"
            "<tr><td>6 removed</td><td>30%</td><td>85%</td><td>78%</td></tr>"
            "<tr><td>7 removed</td><td>35%</td><td>90%</td><td>81%</td></tr>"
            "<tr><td>8 removed</td><td>40%</td><td>95%</td><td>85%</td></tr>"
            "<tr><td>9 or more removed</td><td>50%</td><td>98%</td><td>90%</td></tr>"
            "</table>\n\n"
            "* For every 1 point of intelligence over 15, the magic user reduces probability of insanity by 5%.\n\n"
            "** If the answer is unknown, and the answer is not true, the being will answer definitely. If truth is indicated, it will answer \"unknown\".\n\n"
            "*** Assumes knowledge of questions pertaining to the appropriate elemental plane.\n\n"
            "Insanity will strike as soon as 1 question is asked. It will last for 1 week for each removal of the plane contacted, 10 weeks maximum. There is a 1% chance per plane that the magic-user will die before recovering unless a <a href=\"/spells/remove-curse-cleric-lvl-3/\"><i>remove curse</i></a> spell is cast upon him or her."
        )
    ),
    Spell('Dismissal','M',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U,
        desc=("By means of this spell, a magic-user on the Prime Material Plane seeks to force or allow some creature from another plane of existence to return to its proper plane (cf. 4th-level cleric spell <a href=\"/spells/abjure-cleric-lvl-4/\"><i>abjure</i></a>). The name of the type of creature to be returned must be known and used in the spell. Magic resistance, if any, is checked for effect immediately. Then, the level of the spell caster is compared to the level or number of hit dice of the creature being dismissed. If the magic-user has a higher number, the difference between his or her level is subtracted from the saving throw score of the creature to be affected by the <i>dismissal</i>. If the creature has a higher level or higher number of hit dice than the level of the caster, then that difference is added to its saving throw score. <i>Exception</i>: If the creature desires to be dismissed, then only an unmodified saving throw is needed. Certain arcane works are reputed to allow greatly enhanced chances for spell success. If the spell is successful, the creature is instantly whisked away, but the spell has a 20% chance of actually sending the subject to a plane other than its own.\n\n"
            "The reverse of the spell, <i>beckon</i>, attempts to conjure up a known and named (if applicable) creature from another plane. Success or failure is determined in the same manner as for a <i>dismissal</i> spell, but in this case magic resistance is only checked if the creature has no known proper name. If the spell succeeds, the creature is instantly transported from wherever it was to the plane of the spell caster. This does not guarantee that the beckoned creature will be kindly disposed to the magic-user, nor will it in any way be subject to his or her wishes or commands without some additional constraint. Because of this, various sorts of protective measures are generally taken when using this form of the spell, and even with careful preparation, the results might be unwholesome.\n\n"
            "This spell does not work on creatures that are native to the Prime Material Plane but travel to other planes (such as shedu), nor against creatures that have part of their ancestry in the Prime Material Plane (such as cambions).\n\n"
            "The material components of the spell vary with the type of creature to be dismissed or called. In general, items which are inimical and distasteful to the subject creature are used for <i>dismissal</i>, and for a <i>beckon</i> spell materials which are pleasing, desirable, and rewarding must be used."
        )
    ),
    Spell('Distance Distortion','M',5,
        cast=tp(6,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="This spell can only be cast when the magic-user has an earth elemental conjured up, but the elemental will not react hostilely to co-operation with the spell caster when he or she announces that his or her intent is to cast a <i>distance distortion</i> spell. The magic places the earth elemental in the area of effect, and the elemental then causes the area's dimensions to be distorted in either of two ways: 1) the area will effectively be one-half the distance to those travelling over it, or 2) the area will be twice the distance to those travelling across it. Thus a 10' X 100' corridor could seem as if it was but 5' wide and 50' long, or it could appear to be 20' wide and 200' long. When the spell duration has elapsed, the elemental returns to its own plane. The true nature of an area affected by <i>distance distortion</i> is absolutely undetectable to any creatures travelling along it, although the area will radiate a dim dweomer, and a <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a> spell will reveal that an earth elemental is spread within the area. Material needed for this spell is a small lump of soft clay."
    ),
    Spell('Dolor','M',5,
        cast=tp(5,S),
        duration=tp(2,R),
        sourcebook=U,
        desc=("By means of this spell, the magic-user attempts to force compliance or obedience from some oppositely aligned or hostile creature from a plane foreign to that of the spell caster. The dweomer causes <i>unease</i> in the creature in question during its mere reading, and on the round thereafter, the subject becomes <i>nervous</i> and filled with <i>doubts</i>, while on the last round of effect the creature actually feels a dull, all-encompassing <i>dolor</i>. The initial effects cause the subject creature to make all saving throws versus commands and non-offensive spells (including <i>charms</i>) at -1 on the dice rolled to determine whether or not it resists, the adjustment favoring compliance. The secondary effects cause the adjustment to go to -2. The tertiary effect brings with it an adjustment of -3. Thereafter, the creature is no longer affected and it makes further saving throws without adjustment.\n\n"
            "The verbal component of the spell must deal with the class of creature in question, containing as much information as possible about the subject creature.\n\n"
            "When uttering the spell, the magic-user can be mentally assailed by the creature if the subject has a higher intelligence than the spell caster. In such a case, the creature has a 5% chance per point of superior intelligence of effectively <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charming</i></a> and <i>dominating</i> the magic-user. In the case of such control, the creature will then do with the spell caster as its alignment dictates. If the spell caster is distracted or interrupted during the casting of the spell, the subject creature is able to automatically effect the <i>charm</i> and <i>domination</i>."
        )
    ),
    Spell('Extension II','M',5,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell is the same as the fourth level <a href=\"/spells/extension-i-magic-user-lvl-4/\"><i>extension I</i></a> spell, except it extends the duration of first through fourth level spells by 50%."
    ),
    Spell('Fabricate','M',5,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=U,
        desc=("By means of this spell, the magic-user is able to convert material of one sort into a product of desired nature which is of basically the same material as was initially used when the <i>fabricate</i> was cast. Thus, the spell caster can fabricate a wooden bridge from a clump of trees, a rope from a patch of hemp, clothes from flax or wool, and so forth. Magical or living things cannot be created or altered by a fabricate spell. The quality of items made by means of the spell is commensurate with the quality of material used as the basis for the new fabrication. If mineral material is worked with, the area of effect is reduced by a factor of nine; i.e., 1 cubic yard becomes 1 cubic foot.\n\n"
            "Articles requiring a high degree of craftsmanship (jewlery, swords, glass, crystal, etc.) cannot be <i>fabricated</i> unless the magic-user actually has great skill in the craft considered. Casting requires 1 full round per cubic yard (or foot) of material to be affected."
        )
    ),
    Spell('Feeblemind','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the sixth level druid spell, <a href=\"/spells/feeblemind-druid-lvl-6/\"><i>feeblemind</i></a>. The material component of this spell is a handful of small clay, crystal, glass or mineral spheres."
    ),
    Spell('Hold Monster','M',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell immobilizes from one to four creatures of any type within spell range and in sight of the spell caster. He or she can opt to <i>hold</i> one, two, three or four monsters. If three or four are attacked, each saving throw is at normal; if two are attacked, each saving throw is at -1 on the die; and if but one is attacked, the saving throw is at -3 on the die. (Partially-negated <i>hold monster</i> spell effects equal those of a <a href=\"/spells/slow-magic-user-lvl-3/\"><i>slow</i></a> spell.) The material component for this spell is one hard metal bar or rod for each monster to be held. The bar or rod can be small, i.e. the size of a three-penny nail."
    ),
    Spell('Leomund\'s Lamentable Belabourment','M',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("By means of this spell, the magic-user causes a combination of <a href=\"/spells/fascinate-illusionist-lvl-2/\"><i>fascination</i></a>, <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a>, and <i>rage</i> upon one or more creatures able to understand the language in which the spell caster speaks. Upon casting the spell, the magic-user begins discussion of some topic germane to the creature or creatures to be affected. Those not saving versus spell will immediately begin to converse with the spell caster, agreeing or disagreeing, all most politely. As long as the spell caster chooses, he or she can maintain the spell by conversing with the subject(s). As long as there is no attack made upon them, they will ignore all else going on around them, instead \"choosing\" to spend their time exclusively talking and arguing. This saving throw, and all saving throws in this spell, is modified by the target's intelligence as follows: Creatures with intelligence of 2 or lower are not affected by the spell, but those with intelligence of 3-7 save at -1. Beings with intelligence of 8-10 save normally, those with intelligence of 11-14 at +1, and those with intelligence scores of 15 or higher at +2.\n\n"
            "If the spell is maintained for more than 3 rounds, each subject creature must attempt another save versus spell. Those failing to save this time will wander off in <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> for 3-12 rounds, avoiding the proximity of the spell caster in any event. Those who make the <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> save are still kept in <a href=\"/spells/fascinate-illusionist-lvl-2/\"><i>fascination</i></a> and must also save in the 4th, 5th, and 6th rounds (or as long as the caster continues the dweomer) to avoid the <i>confusion</i> effect. If the spell is maintained for more than 6 rounds, each subject must save versus spell to avoid going into a <i>rage</i> — either at oneself, if one is the sole object of the spell, or at all other subjects of the spell — and attacking (regular \"to hit\" probability) against one's own person, or falling upon the nearest other subject of the dweomer with intent to kill. This <i>rage</i> will last for 2-5 rounds. Those subjects who save versus spell on the <i>rage</i> check will realize that they have fallen prey to the spell and will collapse on the ground, lamenting their foolishness, for 1-4 rounds unless they are attacked or otherwise disturbed.\n\n"
            "If during the course of the maintenance of the spell the caster is attacked or otherwise distracted, he or she is still protected, for the subject or subjects will not notice. The magic-user can leave at any time after the casting and the subject(s) will continue on for 1 full round as if he or she were still there to converse with. In these cases, however, saving throws for continuance of the spell are not applicable, even if, for instance, the subject(s) would otherwise have had to save to avoid <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> or <i>rage</i>. Note that the spell is entirely verbal."
        )
    ),
    Spell('Leomund\'s Secret Chest','M',5,
        cast=tp(1,T),
        duration=tp(60,D),
        sourcebook=V,
        desc=("In order to cast this spell the magic-user must have an exceptionally well-crafted and expensive chest constructed for him by master craftsmen. If made principally of wood, it must be of ebony, rosewood, sandalwood, teak or the like, and all of its corner fittings, nails, and hardware must be of platinum. If constructed of ivory, the metal fittings of the chest may be of gold; and if the chest is fashioned from bronze, copper, or silver, its fittings may be of electrum or silver. The cost of such a chest will never be less than 5,000 g.p. Once constructed, the magic-user must have a tiny replica (of the same materials and perfect in every detail) made, so that the miniature of the <i>chest</i> appears to be a perfect copy. One magic-user can have but one pair of these <i>chests</i> at any given time, and even <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> spells will not allow exceptions.\n\n"
            "While touching the <i>chest</i> and holding the tiny replica, the caster chants the spell. This will cause the large chest to vanish into the ethereal plane. The chest can contain one cubic foot of material per level of the magic-user no matter what its apparent size. Living matter makes it 75% likely that the spell will fail, so the <i>chest</i> is typically used for securing valuable spell books, magic items, gems, etc. As long as the spell caster has the small duplicate of the magic chest, he or she can recall the large one from the ethereal plane to the locale he or she is in when the chest is desired. If the miniature of the chest is lost or destroyed, there is no way, including a <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a>, that the large chest will return.\n\n"
            "While on the ethereal plane, there is a 1% cumulative chance per week that some creature/being will find the <i>chest</i>. If this occurs there is 10% likelihood that the chest will be ignored, 10% possibility that something will be added to the contents, 30% possibility that the contents will be exchanged for something else, 30% chance that something will be stolen from it, and 20% probability that it will be emptied. In addition, when the <i>secret chest</i> is brought back to the Prime Material Plane, an ethereal window is opened and remains open for 5 hours, slowly diminishing in size. As this hole opens between the planes there is a 5% chance that some ethereal monster will be drawn through, with a 1% cumulative reduction in probability each hour thereafter until the window is gone. However, no creature on the Prime Material Plane can locate the <i>chest</i>, even with a <i>gem of seeing</i>, <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a>, etc.\n\n"
            "If <i>Leomund's Secret Chest</i> is not retrieved before spell duration lapses, there is a cumulative chance of 5% per day that the <i>chest</i> will be lost forever, i.e. 5% chance for loss at 61 days, 10% at 62 days, and so forth."
        )
    ),
    Spell('Magic Jar','M',5,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("<i>Magic jar</i> is a very unusual spell. It enables the magic user to take over the mind of the victim and thus control the creature's body. In fact, if the body is human or humanoid, the magic-user can even use the spells he or she knows. The possessor can call upon rudimentary knowledge of the possessed, but not upon the real knowledge, i.e. a possessor will not know the language or spells of the possessed. The spell caster transfers his or her life force to a special container (a large gem or crystal), and from this <i>magic jar</i> the life force can sense and attack any creature within the spell range radius, but what the creature is, is not determinable from the <i>magic jar</i>. The special life force receptacle must be within spell range of the magic-user's body at the time of spell casting. Possession takes place only if the victim fails to make the required saving throw. Failure to possess a victim leaves the life force of the magic-user in the <i>magic jar</i>. Possession attempts require 1 round each. If the body of the spell caster is destroyed, the life force in the <i>magic jar</i> is not harmed. If the <i>magic jar</i> is destroyed, the life force is snuffed out. Returning to the real body requires 1 round, and can only be done from a <i>magic jar</i> in spell range of the body. The saving throw versus a <i>magic jar</i> spell is modified by comparing combined intelligence and wisdom scores (intelligence only in non-human or non-humanoid creatures) of the magic-user and victim.\n\n"
            "<table>"
            "<tr><th>Difference</th><th>Die Adjustment</th></tr>"
            "<tr><td>Negative 9 or +</td><td>+4</td></tr>"
            "<tr><td>Negative 8 to 6</td><td>+3</td></tr>"
            "<tr><td>Negative 5 to 3</td><td>+2</td></tr>"
            "<tr><td>Negative 2 to 0</td><td>+1</td></tr>"
            "<tr><td>Positive 1 to 4</td><td>0</td></tr>"
            "<tr><td>Positive 5 to 8</td><td>-1</td></tr>"
            "<tr><td>Positive 9 to 12</td><td>-2</td></tr>"
            "<tr><td>Positive 13 or +</td><td>-3</td></tr>"
            "</table>\n\n"
            "A <i>negative</i> score indicates the magic-user has a lower score than does his or her intended victim; thus, the victim has a saving throw bonus. The <i>magic jar</i> is the spell's material component. Note that a possessed creature with any negative difference or a positive difference less than 5 is entitled to a saving throw each round to determine if it is able to displace the possessor's mind, a positive difference of 5 to 8 gains a saving throw each turn, a positive difference of 9 to 12 gains a saving throw each day, and a positive difference of 13 or better gains a saving throw each week. If the <i>magic jarred</i> creature regains control of its mind, the magic-user is trapped until he or she can take over the mind for control or escape."
        )
    ),
    Spell('Monster Summoning III','M',5,
        cast=tp(5,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When this spell is cast, 1-4 third level monsters are summoned, coming within 1-4 rounds. See <a href=\"/spells/monster-summoning-i-magic-user-lvl-3/\"><i>monster summoning I</i></a> for other details."
    ),
    Spell('Mordenkainen\'s Faithful Hound','M',5,
        cast=tp(5,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By means of this spell the magic-user summons up a phantom watchdog which only he or she can see. He or she may then command it to perform as guardian of a passage, room, door, or similar space or portal. The phantom watchdog will immediately commence a loud barking if any creature larger than a cat approaches the place it guards. As the <i>Faithful Hound</i> is able to detect invisible, astral, ethereal, out of phase, duo-dimensional, or similarly non-visible creatures, it is an excellent guardian. In addition, if the intruding creature or creatures allow their backs to be exposed to the phantom watchdog, it will deliver a vicious attack as if it were a 10 hit dice monster, striking for 3-18 hit points of damage, and being able to hit opponents of all sorts, even those normally subject only to magical weapons of +3 or greater. The <i>Faithful Hound</i> cannot be attacked, but it can be dispelled. Note, however, that the spell caster can never be more than 3\" distant from the area that the phantom watchdog is guarding, or the magic is automatically dispelled. The material components of this spell are a tiny silver whistle, a piece of bone, and a thread."
    ),
    Spell('Passwall','M',5,
        cast=tp(5,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="A <i>passwall</i> enables the spell caster to open a passage through wooden, plaster, or stone walls; thus he or she and any associates can simply walk through. The spell causes a 5' wide by 8' high by 10' deep opening. Note several of these spells will form a continuing passage so that very thick walls can be pierced. The material component of this spell is a pinch of sesame seeds."
    ),
    Spell('Sending','M',5,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("By means of this spell, the caster is empowered to contact a single creature with whom he or she is familiar and whose name and appearance are well known. If the creature in question is not on the same plane of existence as the spell caster, there is a 5% chance per plane removed that the <i>sending</i> will not arrive; i.e., if the subject were two planes removed there would be a 10% chance of failure. The magic-user can send one word per level of experience, with articles not considered; e.g. <i>a, an,</i> and <i>the</i> are not treated as words with respect to the message sent. Although the <i>sending</i> is received, the subject creature is not obligated to act upon it in any manner. The <i>sending</i>, if successful, will be understood even though the creature has an intelligence of as little as 1 factor (1 point, or <i>animal</i> intelligence).\n\n"
            "The material component for this spell consists of two tiny cylinders, each with one open end, connected by a short piece of copper wire."
        )
    ),
    Spell('Stone Shape','M',5,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this spell the magic-user can form an existing piece of stone into a shape which will suit his or her purposes. For example, a stone weapon can be made, a special trapdoor fashioned, or an idol sculpted. By the same token, it would allow the spell caster to reshape a stone door, perhaps, so as to escape imprisonment, providing the volume of stone involved was within the limits of the area of effect. While stone coffers can be thus formed, secret doors made, etc., the fineness of detail is not great. The material component of this spell is soft clay which must be worked into roughly the desired shape of the stone object and then touched to the stone when the spell is uttered."
    ),
    Spell('Telekinesis','M',5,
        cast=tp(5,S),
        duration=tp(2,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell the magic-user is able to move objects by will force, by concentrating on moving them mentally. The <i>telekinesis</i> spell causes the desired object to move vertically or horizontally. Movement is 2\" the first round, 4\" the second, 8\" the third, 16\" the fourth, and so on, doubling each round until a maximum telekinetic movement of 1,024\" per round is reached. (Heavy objects travelling at high speed can be deadly weapons!) Note that <i>telekinesis</i> can be used to move opponents who fall within the weight capacity of the spell, but if they are able to employ as simple a counter-measure as an <a href=\"/spells/enlarge-magic-user-lvl-1/\"><i>enlarge</i></a> spell, for example (thus making the body weight go over the maximum spell limit), it is easily countered. Likewise, ambulation or some other form of motive power if the recipient of the spell is not able to ambulate, counters the effect of <i>telekinesis</i>, provided the velocity has not reached 16\" per round. The various <i>Bigby's ... Hand</i> spells will also counter this spell, as will many other magics."
    ),
    Spell('Teleport','M',5,
        cast=tp(2,S),
        duration=tp(0),
        sourcebook=V,
        desc=("When this spell is used, the magic-user instantly transports himself or herself, along with a certain amount of additional weight which is upon, or being touched by, the spell caster, to a well-known destination. Distance is not a factor, but inter-plane travel is not possible by means of a <i>teleport</i> spell. The spell caster is able to <i>teleport</i> a maximum weight of 2,500 g.p. equivalence, plus an additional 1,500 g.p. weight for each level of experience above the 10th, i.e. a 13th level magic-user <i>teleports</i> a maximum weight of 7,000 g.p. (700 pounds). If the destination area is very familiar to the magic-user (he or she has a clear mental picture through actual proximity to and studying of the area) it is unlikely that there will be any error in arriving exactly in the place desired. Lesser known areas (those seen only magically or from a distance) increase the probability of error. Unfamiliar areas present considerable peril. This is demonstrated below:\n\n"
            "<table>"
            "<tr><th>Destination Area Is</th><th>Teleport High</th><th>On Target</th><th>Teleport Low</th></tr>"
            "<tr><td>Very familiar</td><td>01-02</td><td>03-99</td><td>00</td></tr>"
            "<tr><td>Studied carefully</td><td>01-04</td><td>05-98</td><td>99-00</td></tr>"
            "<tr><td>Seen casually</td><td>01-08</td><td>09-96</td><td>97-00</td></tr>"
            "<tr><td>Viewed once</td><td>01-16</td><td>17-92</td><td>93-00</td</tr>"
            "<tr><td>Never seen</td><td>01-32</td><td>33-84</td><td>85-00</td></tr>"
            "</table>\n\n"
            "<i>Teleporting high</i> means the magic-user will arrive 1\" above ground for every 1% he or she is below the lowest \"On Target\" probability — only 2\" when the destination is <i>very familiar</i>, and as high as 32\" if the destination area was <i>never seen</i>. Any <i>low</i> result means the instant death of the magic-user if the area into which he or she teleports to is solid. Note that there is no possibility of teleporting to an area of empty space, i.e. a substantial area of surface must be there, whether a wooden floor, a stone floor, natural ground, etc."
        )
    ),
    Spell('Transmute Rock To Mud','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, and that the material components for the spell are clay and water (or sand, lime and water for the reverse), this spell is the same as the fifth level druid spell, <a href=\"/spells/transmute-rock-to-mud-druid-lvl-5/\"><i>transmute rock to mud</i></a>."
    ),
    Spell('Wall of Force','M',5,
        cast=tp(5,S),
        duration=tp(1,T),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="A <i>wall of force</i> spell creates an invisible barrier in the locale desired by the caster, up to the spell's range. The <i>wall of force</i> will not move and is totally unaffected by any other spells, including <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>, save a <a href=\"/spells/disintegrate-magic-user-lvl-6/\"><i>disintegrate</i></a> spell, which will immediately destroy it. Likewise, the <i>wall of force</i> is not affected by blows, missiles, cold, heat electricity, or any similar things. Spells or breath weapons will not pass through it in either direction. The magic-user can, if desired, shape the wall to a hemispherical or spherical shape with an area equal to his or her ability, maximum of 20 square feet per level of experience. The material component for this spell is a pinch of powdered diamond."
    ),
    Spell('Wall of Iron','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast, the magic-user causes a vertical iron wall to spring into being. Typically, this wall is used to seal off a passage or close a breach, for the wall inserts itself into any surrounding material if its area is sufficient to do so. The <i>wall of iron</i> is one quarter of an inch thick per level of experience of the spell caster. The magic-user is able to evoke an area of iron wall 15 square feet for each of his or her experience levels, so at 12th level a wall of iron 180 square feet in area can be created. If the wall is created in a location where it is not supported, it will fall and crush any creature beneath it. The wall is permanent, unless attacked by a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell, but subject to all forces a normal iron wall is subject to. i.e. rust, perforation, etc. The material component of this spell is a small piece of sheet iron."
    ),
    Spell('Wall of Stone','M',5,
        cast=tp(5,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell creates a wall of granite rock which merges into adjoining rock surfaces if the area is sufficient to allow it. It is typically employed to close passages, portals, and breaches against opponents. The <i>wall of stone</i> is ¼' thick and 20' square in area per level of experience of the magic-user casting the spell. Thus, a 12th level magic-user creates a <i>wall of stone</i> 3' thick and 240 square feet in surface area (a 12' wide and 20' high wall, for example, to completely close a 10' x 16' passage). The wall created need not be vertical nor rest upon any firm foundation (cf. <a href=\"/spells/wall-of-iron-magic-user-lvl-5/\"><i>wall of iron</i></a>); however, it must merge with an existing stone formation. It can be used to bridge a chasm, for instance, or as a ramp. The wall is permanent unless destroyed by a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell or by normal means such as breaking, chipping or a <a href=\"/spells/disintegrate-magic-user-lvl-6/\"><i>disintegrate</i></a> spell. The material component is a small block of granite."
    ),
    Spell('Anti-Magic Shell','M',6,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By means of an <i>anti-magic shell</i>, the magic-user causes an invisible barrier to surround his or her person, and this moves with the spell caster. This barrier is totally impervious to all magic and magic spell effects (this includes such attack forms as breath weapons, gaze weapons, and voice weapons). It thus prevents the entrance of spells or their effects, and it likewise prevents the function of any magical items or spells within its confines. It prevents the entrance of charmed, summoned, and conjured creatures. However, normal creatures (assume a normal troll rather than one conjured up, for instance) can pass through the <i>shell</i>, as can normal missiles. While a magic sword would not function magically within the <i>shell</i>, it would still be a sword."
    ),
    Spell('Bigby\'s Forceful Hand','M',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="<i>Bigby's Forceful Hand</i> is a more powerful version of <a href=\"/spells/bigbys-interposing-hand-magic-user-lvl-5/\"><i>Bigby's Interposing Hand</i></a>. It exerts a force in addition to interposing itself, and this force is sufficient to push a creature away from the spell caster if the creature weighs 500 pounds or less, to push so as to slow movement to 1\" per round if the creature weighs between 500 and 2,000 pounds, and to slow movement by 50% of creatures weighing up to 8,000 pounds. It takes as many hit points to destroy as its creator has. Its material component is a glove."
    ),
    Spell('Chain Lightning','M',6,
        cast=tp(6,S),
        duration=tp(0),
        sourcebook=U,
        desc=("When this spell is cast, the electrical discharge begins as a single stroke of lightning, ¼\" wide, commencing from the fingertips of the caster and extending to the primary target, which must lie within the maximum range of the spell as dictated by the level of the caster.\n\n"
            "<i>Chain lightning</i> differs sharply from a <a href=\"/spells/lightning-bolt-magic-user-lvl-3/\"><i>lightning bolt</i></a> spell in that it has a primary target as opposed to an area effect. If the primary target makes a successful saving throw versus spell, one-half damage from the bolt of <i>chain lightning</i> is taken; otherwise full damage (1d6 points per level of the spell caster) will be inflicted.\n\n"
            "In addition, after striking the initial target, the bolt arcs to the nearest other object, be it animal, vegetable, or mineral. This chain of striking continues from one object to another object nearest it, possibly setting up an oscillation between two (presumably stationary or immobilized) objects, or a regular pattern involving three or more objects. If two or more possible targets are equidistant, the <i>chain lightning</i> will arc to metal first, then to the one with the most fluid, otherwise at random. The chain keeps building up to as many \"links\" (including the initial target) as the spell caster has levels. Thus, a 12th-level magic-user casting the spell would hit 12 targets: the primary target first, then 11 other (not necessarily different) targets. After the initial strike, each object subsequently struck is entitled to a saving throw versus spell, if applicable. Success on the save indicates that the stroke actually arced to the <i>next</i> nearest target, and the target that saved takes <i>no</i> damage.\n\n"
            "The arcing bolt will continue until it has struck the appropriate number of objects, as indicated by a target's failure to save or lack of the opportunity to do so (as for an inanimate object of non-magical nature), until the stroke fades out or strikes a target that grounds it. Direction is never a consideration in plotting the path of the arcing <i>chain lightning</i>. Distance is a factor, though; a single arc can never be longer than the range limit. If, in order to arc, the bolt must travel a greater distance than its maximum range, the stroke fades into nothing. A tree or a substantial piece of conductive metal — such as interconnecting iron bars of a large cell or cage — will ground the lightning stroke and prevent further arcing.\n\n"
            "The lightning inflicts one less d6 of damage on each target it hits after striking the primary target for the first time; if the initial target was struck by a 12d6 bolt, the next target struck takes an 11d6 bolt, then 10d6, 9d6, 8d6, 7d6, and so on all the way down to 1d6 — the last spurt of energy from the bolt. (A saving throw for half damage applies on each strike, different from the save versus spell to see if the lightning actually hits a secondary target.) The caster can be struck by an arc from his or her own spell. The material components are a bit of fur; an amber, glass or crystal rod; and as many silver pins as the spell caster has levels of experience."
        )
    ),
    Spell('Contingency','M',6,
        cast=tp(1,T),
        duration_lvl=tp(1,D),
        sourcebook=U,
        desc=("By means of this spell, the magic-user is able to place another spell upon his or her person so that the latter spell will come into effect upon occurrence of the situation dictated during the casting of the <i>contingency</i> spell. The <i>contingency</i> spell and the spell it is to bring into effect — the \"companion\" spell — are, in effect, cast at the same time (the 1-turn casting time indicated above is a total for both castings). The spell to be brought into effect by the prescribed contingency must be one which affects the magic-user's person (<a href=\"/spells/feather-fall-magic-user-lvl-1/\"><i>feather fall</i></a>, <a href=\"/spells/levitate-magic-user-lvl-2/\"><i>levitation</i></a>, <a href=\"/spells/fly-magic-user-lvl-3/\"><i>fly</i></a>, <a href=\"/spells/statue-magic-user-lvl-7/\"><i>statue</i></a>, <a href=\"/spells/feign-death-magic-user-lvl-3/\"><i>feign death</i></a>, etc.) and of a level no higher than one-third of the experience level of the caster (rounded down), to an upper limit of the 6th level spell: a 4th level \"companion spell\" maximum at 12th, 13th or 14th level of experience; a 5th level maximum at 15th, 16th, or 17th level of experience, and a 6th level maximum at 18th level of experience and beyond. Only one <i>contingency</i> spell can be in effect upon the spell caster at any one time; if a second is used, the first one (if still active) is cancelled.\n\n"
            "The situation prescribed to bring the spell into effect must be clear, although it can be rather general. For example, a <i>contingency</i> cast with an <a href=\"/spells/airy-water-magic-user-lvl-5/\"><i>airy water</i></a> \"companion spell\" might prescribe that any time the magic-user is plunged into or otherwise engulfed in water or similar liquid, the <a href=\"/spells/airy-water-magic-user-lvl-5/\"><i>airy water</i></a> spell will instantly come into effect. Likewise, the <i>contingency</i> could bring a <a href=\"/spells/feather-fall-magic-user-lvl-1/\"><i>feather fall</i></a> into effect anytime the magic-user falls over 2' distance. In all cases, the <i>contingency</i> immediately brings into effect the second spell, the latter being \"cast\" instantaneously when the prescribed circumstances occur. Note that complex, complicated, and/or convoluted prescribed conditions for effecting the play of the dweomer are likely to cause the whole spell complex (the <i>contingency</i> spell and the companion magic) to simply fail when called upon.\n\n"
            "The material components of this spell are (in addition to those of the companion spell) 100 gp worth of quicksilver, an elephant ivory statuette of the magic-user, and an eyelash of an ogre magi, ki-rin or similar spell-using creature. Note that the ivory statuette is not destroyed by the spell casting (although it might be subject to wear and tear), and it must be carried on the person of the spell caster for the <i>contingency</i> spell to perform its function when called upon."
        )
    ),
    Spell('Control Weather','M',6,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, and for the differing material components, this spell is the same as the seventh level cleric <a href=\"/spells/control-weather-cleric-lvl-7/\"><i>control weather spell</i></a>. The material components of this spell are burning incense, and bits of earth and wood mixed in water."
    ),
    Spell('Death Spell','M',6,
        cast=tp(6,S),
        duration=tp(0),
        sourcebook=V,
        desc=("When a <i>death spell</i> is cast, it slays creatures in the area of effect instantly and irrevocably. The number of creatures which can be so slain is a function of their hit dice:\n\n"
            "<table>"
            "<tr><th>Victim's Hit Dice</th><th>Maximum Number of Creatures Affected</th></tr>"
            "<tr><td>less than 2</td><td>4-80 4d20</td></tr>"
            "<tr><td>2 to 4</td><td>3-30</td></tr>"
            "<tr><td>4+1 to 6+3</td><td>2-8</td></tr>"
            "<tr><td>6+4 to 8+3</td><td>1-4</td></tr>"
            "</table>\n\n"
            "If a mixed group of creatures is attacked with a <i>death spell</i>, use the following conversion:\n\n"
            "<table>"
            "<tr><th>Creature's Hit Dice:</th><th>less than 2</th><th>2 to 4</th><th>4+1 to 6+3</th><th>6+4 to 8+3</th></tr>"
            "<tr><td>6+4 to 8+3</td><td>10</td><td>5</td><td>2</td><td>-</td></tr>"
            "<tr><td>4+1 to 6+3</td><td>8</td><td>3</td><td>-</td><td>0.5</td></tr>"
            "<tr><td>2 to 4</td><td>4</td><td>-</td><td>0.125</td><td>0.05</td></tr>"
            "</table>\n\n"
            "First, simply roll the dice to see how many creatures of less than 2 hit dice are affected, kill all these, then use the conversion to kill all 2 to 4 hit dice monsters, etc. If not enough of the number remains to kill the higher levels, they remain. This system can be reversed by applying it to higher hit dice victims first. Example: The 4d20 when rolled indicate a total of 53, 20 of this is used to kill one 6+4 to 8+3 die creature (20 x .05 = 1), 16 are used to kill two 4+1 to 6+3 hit dice creatures (16 x .125 = 2), 12 are used to kill three 2 to 4 die creatures (3 x 4 = 12), and 5 remainder can be used to kill off 5 less-than-2 dice creatures (5 x 1 = 5), i.e. 20 + 16 + 12 + 5 = 53. A <i>death spell</i> does not affect lycanthropes, undead creatures, or creatures from other than the Prime Material Plane. The material component of this spell is a crushed black pearl with a minimum value of 1000 g.p."
        )
    ),
    Spell('Disintegrate','M',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell causes matter to vanish. It will affect even matter (or energy) of a magical nature, such as <a href=\"/spells/bigbys-forceful-hand-magic-user-lvl-6/\"><i>Bigby's Forceful Hand</i></a>, but not a <a href=\"/spells/globe-of-invulnerability-magic-user-lvl-6/\"><i>globe of invulnerability</i></a> or an <a href=\"/spells/anti-magic-shell-magic-user-lvl-6/\"><i>anti-magic shell</i></a>. Disintegration is instantaneous, and its effects are permanent. Any living thing can be affected, even undead, and non-living matter up to 1\" cubic volume can be obliterated by the spell. Creatures, and magical material with a saving throw, which successfully save versus the spell are not affected. Only 1 creature or object can be the target of the spell. Its material components are a lodestone and a pinch of dust."
    ),
    Spell('Enchant An Item','M',6,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("This is a spell which must be used by a magic-user planning to create a magic item. The <i>enchant an item</i> spell prepares the object to accept the magic to be placed upon or within it. The item to be magicked must meet the following tests: 1) it must be in sound and undamaged condition; 2) the item must be the finest possible, considering its nature, i.e. crafted of the highest quality material and with the finest workmanship; and 3) its cost or value must reflect the second test, and in most cases the item must have a raw materials cost in excess of 100 g.p. With respect to requirement 3), it is not possible to apply this test to items such as ropes, leather goods, cloth, and pottery not normally embroidered, bejeweled, tooled, carved, and/or engraved; however, if such work or materials can be added to an item without weakening or harming its normal functions, these are required for the item to be magicked.\n\n"
            "The item to be prepared must be touched manually by the spell caster. This touching must be constant and continual during the casting time which is a base 16 hours plus an additional 8-64 hours (as the magic-user may never work over 8 hours per day, and <a href=\"/spells/haste-magic-user-lvl-3/\"><i>haste</i></a> or any other spells will not alter time required in any way, this effectively means that casting time for this spell is 2 days + 1-8 days). All work must be uninterrupted, and during rest periods the item being enchanted must never be more than 1' distant from the spell caster, for if it is, the whole spell is spoiled and must be begun again. (Note that during rest periods absolutely no other form of magic may be performed, and the magic-user must remain quiet and in isolation.) At the end of the spell, the caster will \"know\" that the item is ready for the final test. He or she will then pronounce the final magical syllable, and if the item makes a saving throw (which is exactly the same as that of the magic-user who magicked it) versus magic, the spell is completed. (Note that the spell caster's saving throw bonuses also apply to the item, up to but not exceeding +3.) A result of 1 on the die (d20) always results in failure, regardless of modifications. Once the spell is finished, the magic-user may begin to place the desired dweomer upon the item, and the spell he or she plans to place on or within the item must be cast within 24 hours or the preparatory spell fades, and the item must again be enchanted.\n\n"
            "Each spell subsequently cast upon an object bearing an <i>enchant an item</i> spell requires 4 hours + 4-8 additional hours per spell level of the magic being cast. Again, during casting the item must be touched by the magic-user, and during rest periods it must always be within 1' of his or her person. This procedure holds true for any additional spells placed upon the item, and each successive dweomer must be begun within 24 hours of the last, even if any prior spell failed.\n\n"
            "No magic placed on or into an item is permanent unless a <i>permanency</i> spell is used as a finishing touch, and this always runs a risk of draining a point of constitution from the magic-user casting the spell. It is also necessary to point out that while it is possible to tell when the basic (<i>enchant an item</i>) spell succeeds, it is not possible to tell if successive castings actually take, for each must make the same sort of saving throw as the item itself made. Naturally, items that are charged — rods, staves, wands, <i>javelins of lightning</i>, <i>ring of wishes</i>, etc. — can never be made permanent. Scrolls or magic devices can never be used to <i>enchant an item</i> or cast magic upon an object so prepared.\n\n"
            "The material component(s) for this spell vary according to both the nature of the item being magicked and successive magicks to be cast upon it. For example, a <i>cloak of displacement</i> might require the hides of 1 or more displacer beasts, a sword meant to slay dragons could require the blood and some other part of the type(s) of dragon(s) it will be effective against, and a <i>ring of shooting stars</i> might require pieces of meteorites and the horn of a ki-rin. These specifics, as well as other information pertaining to this spell, are known by your Dungeon Master."
        )
    ),
    Spell('Ensnarement','M',6,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("The casting of this spell attempts a dangerous act — the luring of a powerful creature from another plane to a specially prepared trap where it will be held until it agrees to perform one service in return for freedom from the <i>ensnarement</i> spell. The spell causes an awareness of a <a href=\"/spells/gate-cleric-lvl-7/\"><i>gate</i></a>-like opening on the plane of the creature to be ensnared. A special saving throw is then made to determine if the creature detects the nature of the planar opening as a trap or believes it to be a <i>gate</i>. To save, the creature must roll equal to or less than its intelligence score on 3d6. The score modified by the difference between the creature's intelligence and that of the spell caster's. If the creature has a higher score, the difference is subtracted from its dice roll to save. If the spell caster has a higher score, the difference is added to the total of the 3d6.\n\n"
            "If the saving throw succeeds the creature merely ignores the spell-created opening, and the dweomer fails. If the saving throw is not made, the creature steps into the opening and is <i>ensnared</i>. The type of creature to be ensnared must be known and stated, and if it has a specific, proper, or given name, this also must be used in casting of the <i>ensnarement</i> spell.\n\n"
            "When actually ensnared, the creature coming from another plane to that of the spell caster is not constrained from harming the one who trapped it. Therefore, the caster uses a magic circle (for creatures from the upper planes or the Astral Plane), a thaumatugic triangle (for creatures from the Ethereal, Elemental, or Concordant Opposition planes), or a pentagram (for creatures from the lower and infernal planes). Regardless of such protection, there is a chance that the entrapped creature will be able to break free and wreak its vengeance upon the spell caster. The base chance for an ensnared creature to break free depends on the manner in which the confining design was made. A hand-done one has a base chance of 20% of being broken, one inlaid or carved has only a base of 10%. and that for the first time only (which indicates whether or not the job was done properly). This base chance is modified by the total score of the magic-user's combined intelligence and experience level compared to the intelligence and the experience level or number of hit dice of the creature summoned. If the spell caster has a higher total, that difference is subtracted from the percentage chance for the creature to break free. If the creature has a higher total, that difference is added to its chance to break free.\n\n"
            "The chance may be further modified by care in preparation of the protective symbol. If the hand-made protection is inscribed over a long period of time, using specially prepared pigments (1,000 gp per turn of application), the chance of an <i>ensnared</i> creature breaking free is reduced by 1% for every turn spent so preparing; i.e. an expenditure of 1 turn and 1,000 gp reduces the chance of breaking free by 1%. This can bring the base chance to 0%, but the further modifications for intelligence and level/hit dice still must be made thereafter, and no amount of special preparation can negate that risk. Similarly, an inlaid or inscribed design can be brought to 0% chance of being broken by inlaying it with various metals, minerals, etc. This effort will require a minimum of one full month of time and add not less than 50,000 gp to the basic cost of having the protection inlaid or inscribed into stone. Any breaking of the lines of protection or blurring of the glyphs, runes, and sigils which guard the magical barrier will spoil the efficacy of the dweomer and allow the creature to break free automatically. Even a straw droppped across the lines of a circle destroy its power. Fortunately, the creature within cannot so much as place a straw upon any portion of the inscribed protective device, for the magic of the barrier absolutely prevents it.\n\n"
            "Once safely <i>ensnared</i>, the creature can be kept for as long as the spell caster dares. (Remember the danger of something breaking the inscription!) The caster can offer bribes, use promises, or make threats in order to exact one service from the captive creature. The DM will then assign a value to what the magic-user has said to the ensnared creature, rating it from 0 to 6. This rating is then subtracted from the intelligence score of the creature. If the creature makes its saving throw, a score equal to or less than its adjusted intelligence, it will refuse service. New offers, bribes, etc. can be made, or the old ones re-offered 24 hours later, when the creature's intelligence has dropped by 1 point due to confinement. This can be repeated until the creature promises to serve, until it breaks free, or until the caster decides to release it by means of some riddance spell. It need not be stressed that certain other spells can be used to force a captive creature into submission.\n\n"
            "Once the single service is completed, the creature need only so inform the spell caster to be instantly teleported from whence it came. Revenge can be sought (cf. <a href=\"/creatures/efreeti/\">efreeti</a>, <a href=\"/creatures/aerial-servant/\">aerial servant</a>, and <a href=\"invisible-stalker/\">invisible stalker</a>). Impossible commands or unreasonable commands will never be agreed to."
        )
    ),
    Spell('Extension III','M',6,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell is the same as the fourth level <a href=\"/spells/extension-i-magic-user-lvl-4/\"><i>extension I</i></a> except that it will extend first through third level spells to double duration and will extend the duration of fourth or fifth level spells by 50% of the indicated duration."
    ),
    Spell('Eyebite','M',6,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("An <i>eyebite</i> spell enables the caster to merely meet the gaze of his or her subject and speak a single word to cause the dweomer to be effectuated. With this single spell, the caster can choose which particular effect is to strike the subject, but the <i>eyebite</i> spell is then dissipated, even though only one of its four possible effects were used. The four effects of the spell to be chosen from are these:\n\n"
            "<i>Charm</i>: The magic-user can charm a person or monster by gaze and vocalization of a single word. The effect is to make the <i>charmed</i> subject absolutely loyal and docile with respect to the charmer, even to the point of personal danger. It is otherwise the same as a <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charm person</i></a> or <a href=\"/spells/charm-monster-magic-user-lvl-4/\"><i>charm monster</i></a> spell. A successful saving throw versus spell negates this effect.\n\n"
            "<i>Fear</i>: The magic-user can cause fear by gaze and vocalization of a single word. The subject will act as if struck by a <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a> spell unless a saving throw versus spell is successful.\n\n"
            "<i>Sicken</i>: This power enables the caster to merely gaze at the subject, speak a word, and cause sudden nausea and sickness to sweep over the subject's body. The victim will be at one-half normal abilities (strength, intelligence, etc.) from the pain and fever (creatures without ability scores are not affected). Movement will be at one-half normal rate also, and the victim will have to rest half of each turn in order to be able to move at all. A saving throw versus spell will negate the power of the dweomer. Otherwise, the victim will remain struck by the <i>sickness</i>, losing one actual point of constitution per day until death occurs at zero consitution points. The effects are negated by a successful <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell or <a href=\"/spells/heal-cleric-lvl-6/\"><i>heal</i></a> spell. <a href=\"/spells/alter-reality-illusionist-lvl-7/\"><i>Alter reality</i></a>, <a href=\"/spells/limited-wish-magic-user-lvl-7/\"><i>limited wish</i></a>, and <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> spells will also remove the <i>sickness</i>, but a <a href=\"/spells/cure-disease-cleric-lvl-3/\"><i>cure disease</i></a> will not. Note: All non-human, non-demi-human, and non-humanoid creatures save at +4 versus this effect.\n\n"
            "<i>Sleep</i>: The magic-user can cause any individual to fall into a comatose slumber by means of a gaze and a single word, unless the subject makes its saving throw versus spell. Creatures normally subject to the 1st-level spell <a href=\"/spells/sleep-magic-user-lvl-1/\"><i>sleep</i></a> save at -2. Undead are not subject to this power. Affected creatures must be shaken or otherwise shocked to bring them back to conciousness."
        )
    ),
    Spell('Geas','M',6,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="A <i>geas</i> spell places a magical command upon the creature (usually human or humanoid) to carry out some service, or refrain from same action or course of activity, as desired by the spell caster. The creature must be intelligent, conscious, and under its own volition. While a <i>geas</i> cannot compel a creature to kill itself, or to perform acts which are likely to result in certain death, it can cause almost any other course of action. The spell causes the <i>geased</i> creature to follow the instructions until the <i>geas</i> is completed. Failure to do so will cause the creature to grow sick and die within 1 to 4 weeks. Deviation from or twisting of the instructions causes corresponding loss of strength points until the deviation ceases. A <i>geas</i> can be done away with by a <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> spell, but a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> or <a href=\"/spells/remove-curse-cleric-lvl-3/\"><i>remove curse</i></a> will not negate it. Your referee will instruct you as to any additional details of a <i>geas</i>, for its casting and fulfilment are tricky, and an improperly cast <i>geas</i> is null and void immediately (cf. <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a>)."
    ),
    Spell('Glassee','M',6,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell the magic-user is able to make a section of metal, stone or wood as transparent as glass to his gaze, or even make it into transparent material as explained hereafter. Normally, up to four inches of metal can be seen through, stone up to 6' thick can be made transparent, and 20' of wood can be affected by the <i>glassee</i> spell. The spell will not work on lead, gold or platinum. The magic-user can opt to make the <i>glassee</i> apply to himself or herself only, and apply it up to once per round while spell duration lasts; or the caster can actually make a transparent area, a one-way window, in the material affected. Either case gives a viewing area 3' wide by 2' high. The material component of the spell is a small piece of crystal or glass."
    ),
    Spell('Globe of Invulnerability','M',6,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is the same as the fourth level <a href=\"/spells/minor-globe-of-invulnerability-magic-user-lvl-4/\"><i>minor globe of invulnerability</i></a>, except as regards casting time and for the fact that it prevents the functioning of first through fourth level spells affecting the magic-user within the <i>globe</i>, while he or she can cast spells through it, of course."
    ),
    Spell('Guards and Wards','M',6,
        cast=tp(3,T),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc=("This special and powerful spell is primarily used to defend the magic-user's stronghold. The following take place in the area of effect upon casting of the spell:\n\n"
            "1. All corridors become misty, and visibility is reduced to 10'.\n"
            "2. All doors are <a href=\"/spells/wizard-lock-magic-user-lvl-2/\"><i>wizard locked</i></a>.\n"
            "3. One door per level of experience of the magic-user is covered by an illusion as if it were a plain wall.\n"
            "4. Stairs are filled with <a href=\"/spells/web-magic-user-lvl-2/\"><i>webs</i></a> from top to bottom."
            "5. Where there are choices in direction — such as a cross or side passage — a minor confusion-type spell functions so as to make it 50% probable that intruders will believe they are going in the exact opposite direction.\n"
            "6. The whole area radiates magic.\n"
            "7. The magic-user can place <i>one</i> of the following additional magics:\n"
            "   A. <a href=\"/spells/dancing-lights-magic-user-lvl-1/\"><i>Dancing lights</i></a> in four corridors, or\n"
            "   B. <a href=\"/spells/magic-mouth-magic-user-lvl-2/\"><i>Magic mouths</i></a> in two places, or\n"
            "   C. <a href=\"/spells/stinking-cloud-magic-user-lvl-2/\"><i>Stinking clouds</i></a> in two places, or\n"
            "   D. <a href=\"/spells/gust-of-wind-magic-user-lvl-3/\"><i>Gust of wind</i></a> in one corridor or room, or\n"
            "   E. <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>Suggestion</i></a> in one place.\n\n"
            "Note that items 3 and 7 function only when the magic-user is totally familiar with the area of the spell's effect. <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>Dispel magic</i></a> can remove one effect, at random, per casting of a dispel. A <a href=\"/spells/remove-curse-cleric-lvl-3/\"><i>remove curse</i></a> will not work. The material components of the spell are burning incense, a small measure of sulphur and oil, a knotted string, a small amount of umber hulk blood, and a small silver rod."
        )
    ),
    Spell('Invisible Stalker','M',6,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell summons an <a href=\"/creatures/invisible-stalker/\"><i>invisible stalker</i></a> from the Elemental Plane of Air. This 8 hit die monster will obey and serve the spell caster in performance of whatever tasks are set before it. However, the creature is <i>bound</i> to serve; it does not do so from loyalty or desire. Therefore, it will resent prolonged missions or complex tasks, and it will attempt to pervert instructions accordingly. The <i>invisible stalker</i> will follow instructions even at hundreds or thousands of miles distance. The material components of this spell are burning incense and a piece of horn carved into a crescent shape."
    ),
    Spell('Legend Lore','M',6,
        cast=tp(1,VA),
        duration=tp(0),
        sourcebook=V,
        desc="The <i>legend lore</i> spell is used to determine information available regarding a known person, place or thing. If the person or thing is at hand, or if the magic-user is in the place in question, the likelihood of the spell producing results is far greater and the casting time is only 1 to 4 turns. If detailed information on the person, place or thing is known, casting time is 1 to 10 days. If only rumours are known, casting time is 2 to 12 weeks. During the casting, the magic-user cannot engage in other activities other than routine: eating, sleeping, etc. When completed, the divination will reveal if legendary material is available. It will often reveal where this material is — by place name, rhyme, or riddle. It will sometimes give certain information regarding the person, place or thing (when the object of the <i>legend lore</i> is at hand), but this data will always be in some cryptic form (rhyme, riddle, anagram, cipher, sign, etc.). The spell is cast with incense and strips of ivory formed into a rectangle, but some item must be sacrificed in addition — a potion, magic scroll, magic item, creature, etc. Naturally, <i>legend lore</i> will reveal information only if the person, place or thing is noteworthy or legendary."
    ),
    Spell('Lower Water','M',6,
        cast=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="Except as noted above, and for the facts that the reverse spell raises water only ½'/level of experience of the spell caster, and the material components for the spell are a small vial of water and a small vial of dust, it is the same as the fourth level cleric spell, <a href=\"/spells/lower-water-cleric-lvl-4/\"><i>lower water</i></a>."
    ),
    Spell('Monster Summoning IV','M',6,
        cast=tp(6,S),
        duration=tp(5,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell summons 1 to 3 fourth level monsters, and they appear within 1 to 3 rounds. See <a href=\"/spells/monster-summoning-i-magic-user-lvl-3/\"><i>monster summoning I</i></a> for other details."
    ),
    Spell('Mordenkainen\'s Lucubration','M',6,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=U,
        desc="By use of this spell, the magic-user is able to instantly recall any spell he or she has used and otherwise forgotten during the past 24 hours. The spell must have been memorized and actually used during the stated time period, and it cannot be of greater power than fifth level. <i>Mordenkainen's Lubrication</i> enables the spell caster to recall any 1st- through 5th-level spell precisely as if it had never been cast. Only one such spell can be so recalled by use of the <i>lubrication</i> dweomer. The spell recalled can thereafter be cast normally on any succeeding round. Material spell components must be available if the spell recalled requires such, or else the remembered spell is not usable until the material components are available."
    ),
    Spell('Move Earth','M',6,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="When cast, the <i>move earth</i> spell moves dirt (clay, loam, sand) and its other components. Thus, embankments can be collapsed, hillocks moved, dunes shifted, etc. The area to be affected will dictate the casting time; for every 4\" square area, 1 turn of casting time is required. If terrain features are to be moved — as compared to simply caving in banks or walls of earth — it is necessary that an earth elemental be subsequently summoned to assist. All spell casting and/or summoning must be completed before any effects occur. In no event can rock prominences be collapsed or moved. The material components for this spell are a mixture of soils (clay, loam, sand) in a small bag, and an iron blade."
    ),
    Spell('Otiluke\'s Freezing Sphere','M',6,
        cast=tp(6,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="<i>Otiluke's Freezing Sphere</i> is a multi-purpose dweomer of considerable power. If the caster opts, he or she may create a globe of matter at <i>absolute zero</i> temperature which spreads upon contact with water or liquid which is principally composed of water, so as to freeze it to a depth of 6 inches over an area equal to 100 square feet per level of the magic-user casting the spell. The ice so formed lasts for 1 round per level of the caster. The spell can also be used as a thin ray of cold which springs from the caster's hand to a distance of 1\" per level of the magic-user; this ray will inflict 4 hit points of damage per level of the caster upon the creature struck, with a saving throw versus magic applicable, and all damage negated if it is successful (as the ray is so narrow a save indicates it missed), but the path of the ray being plotted to its full distance, as anything else in its path must save (if applicable) or take appropriate damage. Finally, <i>Otiluke's Freezing Sphere</i> can be cast so as to create a small globe about the size of a sling stone, cool to the touch, but not harmful. This globe can be cast, and it will shatter upon impact, inflicting 4-24 hit points of cold damage upon all creatures within a 10' radius (one-half damage if saving throw versus magic is made). Note that if the globe is not thrown or slung within a time period equal to 1 round times the level of the spell caster, it automatically shatters and causes cold damage as stated above. This timed effect can be employed against pursuers, although it can also prove hazardous to the spell caster and/or his or her associates as well. The material components of the spell depend upon in which form it is to be cast. A thin sheet of crystal about an inch square is needed for the first application of the spell, a white sapphire of not less than 1,000 g.p. value for the second application of the spell, and a 1,000 g.p. diamond is minimum for the third application of the spell. All components are lost when the spell is cast."
    ),
    Spell('Part Water','M',6,
        cast=tp(1,T),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="Except as shown above, and also that the material components for this spell are two small sheets of crystal or glass, this spell is the same as the sixth level cleric spell, <a href=\"/spells/part-water-cleric-lvl-6/\"><i>part water</i></a>."
    ),
    Spell('Project Image','M',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell, the magic-user creates a non-material duplicate of himself or herself, projecting it to any spot within spell range which is desired. This image performs actions identical to the magic-user — walking, speaking, spell-casting — as the magic-user determines. A special channel exists between the image of the magic-user and the actual magic-user, so spells cast actually originate from the image. The image can be dispelled only by means of a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell (or upon command from the spell caster), and attacks do not affect it. The image must be within view of the magic-user projecting it at all times, and if his or her sight is obstructed, the spell is broken. The material component of this spell is a small replica (doll) of the magic-user."
    ),
    Spell('Reincarnation','M',6,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc=("This spell is similar to the <a href=\"/spells/reincarnate-druid-lvl-7/\"><i>seventh level druid spell</i></a> of the same name. It does not require a saving throw for system shock or resurrection survival. The corpse is touched, and a new incarnation of the person will appear in the area in 1 to 6 turns, providing the person has not been dead for longer than 1 day per level of experience of the magic-user. The new incarnation will be:\n\n"
            "<table>"
            "<tr><th>Die Roll</th><th>Incarnation</th></tr>"
            "<tr><td>01-05</td><td>bugbear</td></tr>"
            "<tr><td>06-11</td><td>dwarf</td></tr>"
            "<tr><td>12-18</td><td>elf</td></tr>"
            "<tr><td>19-23</td><td>gnoll</td></tr>"
            "<tr><td>24-28</td><td>gnome</td></tr>"
            "<tr><td>29-33</td><td>goblin</td></tr>"
            "<tr><td>34-40</td><td>half-elf</td></tr>"
            "<tr><td>41-47</td><td>halfling</td></tr>"
            "<tr><td>48-54</td><td>half-orc</td></tr>"
            "<tr><td>55-59</td><td>hobgoblin</td></tr>"
            "<tr><td>60-73</td><td>human</td></tr>"
            "<tr><td>74-79</td><td>kobold</td></tr>"
            "<tr><td>80-85</td><td>orc</td></tr>"
            "<tr><td>86-90</td><td>ogre</td></tr>"
            "<tr><td>91-95</td><td>ogre mage</td></tr>"
            "<tr><td>96-00</td><td>troll</td></tr>"
            "</table>\n\n"
            "Note: Very good or very evil persons will not be <i>reincarnated</i> as creatures whose general alignment is the opposite. The material components of the spell are a small drum and a drop of blood."
        )
    ),
    Spell('Repulsion','M',6,
        cast=tp(6,S),
        duration_lvl=tp(5,S),
        sourcebook=V,
        desc="When this spell is cast, the magic-user is able to cause all creatures in the path of the area of effect to move away from his or her person. Repulsion is at 3\" per round, or at the motive speed of the creature attempting to move towards the spell caster. The repelled creature will continue to move away for the balance of a complete move even though this takes it beyond spell range. The material component of this spell is a pair of small magnetized iron bars attached to two small canine statuettes, one ivory and one ebony."
    ),
    Spell('Spiritwrack','M',6,
        cast=tp(3,R),
        duration_lvl=tp(1,Y),
        sourcebook=V,
        desc=("A <i>spiritwrack</i> spell is a very strong protection/punishment spell against the powerful creatures of the nether planes (Abyssal, Hades, Hell, etc.), but to employ the magic, the spell caster must know the name of the being at whom he or she will direct the energy. Prior to actual utterance of a <i>spiritwrack</i> spell the magic-user must prepare an illuminated sheet of vellum, carefully inscribed in special inks made from powdered rubies and the ichor of a slain demon of type I, II, or III and covered with gold leaf in a continuous border. The spell caster must personally prepare this document, including the being's name thereon. (This will require from 8-32 hours of time and cost 1,000 g.p. for vellum, special pens, gold leaf, and other miscellaneous materials alone; the cost of the powdered rubies is a minimum of 5,000 g.p. for each document.) If the demon, devil, or other powerful being from a nether outer plane is present in some form (and not possessing another creature's body instead), the magic-user can then begin actual spell incantation.\n\n"
            "Immediately upon beginning the reading of the document, the being named will be rooted to the spot unless it makes its <i>magic resistance</i> percentage (adjusted for the level of the magic-user) as a saving throw; and even if such a saving throw is made, the monster feels greatly uncomfortable, and if it has not been magically forced to the locale and so held there, it is 90% likely to retreat to its own (or another) plane, as the named being is powerless to attack the magic-user while he or she is reading the spell document. This first part of the document continues for 1 full round, with the discomfort to the named being becoming greater at the end. During the second minute of the incantation, the being named undergoes acute pain and loses 1 hit point per hit die it possesses. At the end of this round of reading, the being is in wracking pain. The third and final round of utterance of the condemnation will cause a loss to the being of 50% of its existing hit points, horrible pain, and at the end consign it to some confined space on its own plane — there to remain in torture for a number of years equal to the level of the magic-user who prepared the document.\n\n"
            "Obviously, the being so dealt with will be the sworn foe of the magic-user forever afterwards, so the magic-user will be loath to finish the spell but rather use it as a threat to force submission of the being. Each round of reading will cause the being forced to listen to be a cumulative 25% likely to concede even without any other offerings or payment."
        )
    ),
    Spell('Stone To Flesh','M',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>stone to flesh</i> spell turns any sort of stone into flesh — if the recipient stone object was formerly living, it will restore life (and goods), although the survival of the creature is subject to the usual system shock survival dice roll. Any formerly living creature, regardless of size, can be thus returned to flesh. Ordinary stone can be likewise turned to flesh at a volume of 9 cubic feet per level of experience of the spell caster. The reverse will turn flesh of any sort to stone, just as the <i>stone to flesh</i> spell functions. All possessions on the person of the creature likewise turn to stone. This reverse of the spell will require a saving throw be allowed the intended victim. The material components of the spell are a pinch of earth and a drop of blood; lime and water and earth are used for the reverse."
    ),
    Spell('Tenser\'s Transformation','M',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="<i>Tenser's Transformation</i> is a sight guaranteed to astound any creature not aware of its power, for when the magic-user casts the dweomer, he or she undergoes a startling transformation. The size and strength of the magic-user increase to heroic proportions, so he or she becomes a formidable fighting machine, for the spell causes the caster to become a berserk fighter! The magic-user's hit points double, and all damage he or she sustains comes first from the magical points gained; so if damage does not exceed original hit points, none is actually taken, but if damage beyond the additional amount is sustained, each point counts as 2 (double damage). The armor class of the magic-user is a full 4 factors better than that he or she possessed prior to casting the spell (AC 10 goes to 6, AC 9 to 5, AC 8 to 4, etc.), all attacks are at a level equal to those of a fighter of the same level as the magic-user (i.e., the spell caster uses the combat table normally restricted to fighters), and although he or she can employ a dagger only in attacking, damage inflicted by the weapon is at +2 <i>additional</i> hit points, and 2 such attacks per round are made by the magic-user. However, it is worth noting that this spell must run its full course, and the magic-user will continue attacking until all opponents are slain, he or she is killed, the magic is dispelled, or the <i>Transformation</i> duration expires. The material component for casting this dweomer is a potion of <i>heroism</i> (or <i>superheroism</i>) which the magic-user must consume during the course of uttering the spell."
    ),
    Spell('Transmute Water To Dust','M',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="This spell is identical to the <a href=\"/spells/transmute-water-to-dust-druid-lvl-6/\">6th-level druid spell</a> of the same name, except as noted above. The magic-user does not need mistletoe as a material component."
    ),
    Spell('Banishment','M',7,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=U,
        desc=("A <i>banishment</i> spell enables the caster to force some creature from another plane to return to its own abode. The effect is instantaneous, and the subject cannot come back without some special summoning or means of egress from its own plane to the one from which it was banished. More than one creature can be forced into magical <i>banishment</i>, providing the spell caster is of sufficient strength (levels of experience) to do so, and providing that the potential subjects are within range of the spell. The spell requires that the magic-user both name the type of creature(s) to be sent away, give its true and proper name as well, and call upon powers opposed to the creature(s). In any event, the target creature's magic resistance must be defeated for the spell to be effective.\n\n"
            "The material components of the spell are substances harmful, hateful, and/or opposed to the nature of the subject(s) of the dweomer. For every such substance included in the casting, a subject creature loses -2 from the dice rolled to determine its save versus spell. For example, if iron, holy water, sunstone, and a sprig of rosemary were used in casting a <i>banishment</i> upon a demon, its saving throw versus the spell would be made at -8 (four substances times the factor of 2). Special items, such as hair from the tail of a ki-rin, or couatl feathers, could also be added to bring the factor up to -3 or -4 per such item. In contrast, a devil's scale or titan's hair, or mistletoe blessed by a druid might lower the factor to -1 with respect to a demon. If the subject creature makes its saving throw versus the spell, the caster will be stung by a backlash of energy, take 2-12 points of damage, and be stunned for 2-12 segments.\n\n"
            "Note: If the powers called upon when casting the <i>banishment</i> spell are directly and actively opposed to the creature(s) to be banished, or if they are favorably and actively concerned with the interests of the spell caster, these powers can augment the efficacy of the spell components by from -1 (least concerned) to -6 (most concerned). Specifics of this effect are left up to the judgement of the referee."
        )
    ),
    Spell('Bigby\'s Grasping Hand','M',7,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="<i>Bigby's Grasping Hand</i> is a superior version of the sixth level <a href=\"/spells/bigbys-forceful-hand-magic-user-lvl-6/\"><i>Bigby's Forceful Hand</i></a> spell, being like it in many ways. The <i>Grasping Hand</i> can actually hold motionless a creature or object of up to 1,000 pounds weight, or move creatures as a double strength <a href=\"/spells/bigbys-forceful-hand-magic-user-lvl-6/\"><i>Forceful Hand</i></a>. The material component is a leather glove."
    ),
    Spell('Cacodemon','M',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("This perilous excercise in dweomercraeft summons up a powerful demon of type IV, V, or VI, depending upon the demon's name being known to the magic-user. Note that this spell is <i>not</i> of sufficient power to bring a demon of greater power, and lesser sorts are not called as they have no known names. In any event, the spell caster <i>must</i> know the name of the type IV, V, or VI demon he or she is summoning. As the spell name implies, the demon so summoned is most angry and evilly disposed. The spell caster must be within a circle of <i>protection</i> (or a thaumaturgic triangle with <a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a>) and the demon confined within a pentagram (circled pentacle) if he or she is to avoid being slain or carried off by the summoned cacodemon. The summoned demon can be treated with as follows:\n\n"
            "1) The magic-user can require the monster to perform a desired course of action by force of threat and pain of a <a href=\"/spells/spiritwrack-magic-user-lvl-6/\"><i>spiritwrack</i></a> spell, allowing freedom whenever the demon performs the full extent of the service, and forcing the demon to pledge word upon it. This is exceedingly dangerous, as a minor error in such a bargain will be seized upon by the monster to reverse the desired outcome or simply to kill and devour the summoner. Furthermore, the demon will bear great enmity for the magic-user forever after such forced obedience, so the spell caster had better be most powerful and capable.\n\n"
            "2) By tribute of fresh human blood and the promise of 1 or more human sacrifices, the summoner can bargain with the demon for willing service. Again, the spell caster is well advised to have ample protection and power to defend himself or herself, as the demon might decide the offer is insufficient — or it is easier to enjoy the summoner's slow death — and decide not to accept the bargain as offered. Although the demon will have to abide by a pledge, as his name is known, he will have to hold only to the exact word of the arrangement, not to the spirit of the agreement. On the other hand, only highly evil magic-users are likely to attempt to strike such a bargain, and the summoned <i>cacodemon</i> might be favorably disposed towards such a character, especially if he or she is also chaotic.\n\n"
            "3) The summoned demon can be the object of a <a href=\"/spells/trap-the-soul-magic-user-lvl-8/\"><i>trap the soul</i></a> spell. In this case, the magic-user will not speak with or bargain for the demon's services, although the <i>cacodemon</i> might be eager to reach an accord with the dweomercraefter before he is forced into imprisonment. The trapping of the demon is risky only if proper precautions have not been taken, for failure to confine the monster usually means only that it is able to escape to its own plane. Once trapped, the demon must remain imprisoned until the possessor of his object of confinement breaks it and frees him, and this requires one service from the now loosed monster. If the individual(s) freeing the demon fails to demand a service when the monster asks what is required of him, the demon is under no constraint not to slay the liberator(s) on the spot, but if a service is required, the creature must first do his best to perform it and then return to the Abyss.\n\n"
            "The duration of service of any demon must be limited unless the demon is willing to serve for an extended period. Any required course of action or service which effectively requires an inordinate period of time to perform, or is impossible to perform, is 50% likely to free the demon from his obligations and enable him to be unconstrained in his vengeance upon the spell caster if he or she is not thereafter continually protected, for a demon so freed can remain on the plane it was summoned to for as long as 666 days.\n\n"
            "The demon summoned will be exceptionally strong, i.e. 8 hit points per hit die.\n\n"
            "Casting time is 1 hour per type (numeric) of the demon to be summoned. If there is any interruption during this period, the spell fails. If there is an interruption while the <i>cacodemon</i> is summoned, it is 10% probable that it will be able to escape its boundaries and attack the magic-user, this percentage rising cumulatively each round of continued interruption.\n\n"
            "Each demon is entitled to a saving throw versus this summoning spell. If a score higher than the level of the magic-user summoning is rolled with 3d6 (2d10 with respect to type VI demons), that particular spell failed to bring the desired demon. When this occurs, it is certain that the named demon is imprisoned or destroyed or the name used was not perfectly correct, so the spell caster will have to call upon another name to bring forth a cacodemon.\n\n"
            "The components of this spell are 5 flaming black candles; a brazier of hot coals upon which must be burned sulphur, bat hairs, lard, soot, mercuric-nitric acid crystals, mandrake root, alcohol, and a piece of parchment with the demon's name inscribed in runes inside a pentacle; and a dish of blood from some mammal (preferably a human, of course) placed inside the area where the <i>cacodemon</i> is to be held."
        )
    ),
    Spell('Charm Plants','M',7,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>charm plants</i> spell allows the spell caster to bring under command vegetable life forms, communicate with them, and these plants will obey instructions to the best of their ability. The spell will <i>charm plants</i> in a 3\" x 1\" area. While the spell does not endow the vegetation with new abilities, it does allow the magic-user to command the plants to use whatever they have in order to fulfil his or her instructions, and if the plants in the area of effect do have special or unusual abilities, these will be used as commanded by the magic-user. The saving throw applies only to intelligent plants, and it is made at -4 on the die roll. The material components of the spell area pinch of humus, a drop of water and a twig or leaf."
    ),
    Spell('Delayed Blast Fireball','M',7,
        cast=tp(7,S),
        duration=tp(5,R),
        sourcebook=V,
        desc="This spell creates a <i>fire ball</i> with +1 on each of its dice of damage, and it will not release its blast for from 1 to 50 segments (1/10 to 5 rounds), according to the command upon casting by the magic-user. In other respects, the spell is the same as the third level <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a> spell."
    ),
    Spell('Drawmij\'s Instant Summons','M',7,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=V,
        desc="When this spell is cast, the magic-user teleports some desired item from virtually any location directly to his or her hand. The object must be singular, can be no larger than a sword is long, have no more mass and weight than a shield (about 75 g.p. weight), and it must be non-living. To prepare this spell, the magic-user must hold a gem of not less than 5,000 g.p. value in his or her hand and utter all but the final word of the conjuration. He or she then must have this same gem available to cast the spell. All that is then required is that the magic-user utter the final word while crushing the gem, and the desired item is transported instantly into the spell caster's right or left hand as he or she desires. The item must, of course, have been previously touched during the initial incantation and specifically named, and only that particular item will be summoned by the spell. If the item is in the possession of another creature, the spell will not work, but the caster will know who the possessor is and roughly where he, she, or it is located when the <i>summons</i> is cast. Items can be summoned from other planes of existence, but only if such items are not in the possession (not necessarily physical grasp) of another creature. For each level of experience above the 14th, the magic-user is able to summon a desired item from 1 plane further removed from the plane he or she is upon at the time the spell is cast, i.e. 1 plane at 14th level, but 2 at 15th, 3 at 16th. etc. Thus, a magic-user of 16th level could effect the spell even if the item desired was on the second layer of one of the outer planes, but at 14th level the magic-user would be able to summon the item only if it were on one of the Elemental Planes or the Astral or the Ethereal Plane."
    ),
    Spell('Duo-Dimension','M',7,
        cast=tp(7,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("A <i>duo-dimension</i> spell causes the caster to have only two dimensions, height and width but no depth. He or she is thus invisible when a sideways turn is made, and this invisibility can only be detected by means of a <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a> spell or similar means. In addition, the <i>duo-dimensional</i> magic-user can pass through the thinnest of spaces as long as they have the proper height according to his or her actual length — going through the space between a door and its frame is a simple matter. The magic-user can perform all actions on a normal basis. He or she can <i>turn</i> and become invisible, move in this state, and appear again next round and cast a spell, disappearing on the following round. Note that when <i>turned</i> the magic-user cannot be affected by any form of attack, but when visible he or she is subject to triple the amount of damage normal for an attack form, i.e. a dagger thrust would inflict 3-12 hit points of damage if it struck a <i>duo-dimensional</i> magic-user. Furthermore, the magic-user has a portion of his or her existence on the Astral Plane when the spell is in effect, and he or she is subject to possible notice from creatures thereupon. If noticed, it is 25% probable that the magic-user will be entirety brought to the Astral Plane by attack from the astral creature.\n\n"
            "The material components of this spell are a thin, flat ivory likeness of the spell caster (which must be of finest workmanship, gold filigreed, and enamelled and gem-studded at an average cost of 5,000 to 10,000 g.p.) and a strip of parchment. As the spell is uttered, the parchment is given a half twist and joined at the ends. The figurine is then passed through the parchment loop, and both disappear forever."
        )
    ),
    Spell('Forcecage','M',7,
        cast=tp(1,VA),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc=("This powerful spell enables the caster to bring into being a <i>cube of force</i>, but it is unlike the magic item of that name in one important respect: the <i>forcecage</i> does not have solid walls of force; it has alternating bands of force with ½' gaps between. Thus, it is truly a cage rather than an enclosed space with solid walls. Creatures within the area of effect of the dweomer are caught and contained unless they are able to pass through the opening — and of course all spells and breath weapons can pass through the gaps in the bars of force of the <i>forcecage</i>. Furthermore, creatures with a magic resistance can apply that resistance in a single attempt to pass through the walls of the cage. If resistance fails, then the creature in question is caged. Regardless of success, any and all other creatures also in the area of effect of the spell are trapped unless they also have magic resistance which allows them to escape. The <i>forcecage</i> is also unlike the solid-walled protective device, <i>cube of force</i>, in that it can be gotten rid of only by means of a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell or by expiration of the dweomer.\n\n"
            "By means of special preparation at the time of memorization, a <i>forcecage</i> spell can be altered to a <i>forcecube</i> spell. <i>Forcecube</i> has one-eighth the area of effect (a cube 1\" on a side), and the dweomer then resembles the magic of a <i>cube of force</i> in all respects except for the differences between a cast spell and the magic of a device, including the methods of defeating its power.\n\n"
            "Although the actual casting of either application of the spell requires no material component, the study of the spell required to commit it to memory does demand that the magic-user powder a diamond of at least 1,000 gp value, using the diamond dust to trace the outlines of the cage or cube he or she desirse to create via spell casting at some later time. Thus, in memorization, the diamond dust is employed and expended, for upon completion of study, the magic-user must then toss the dust into the air and it will disappear."
        )
    ),
    Spell('Limited Wish','M',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V,
        desc="A <i>limited wish</i> is a very potent but difficult spell. It will fulfil literally, but only partially or for a limited duration, the utterance of the spell caster. Thus, the actuality of the past, present or future might be altered (but possibly only for the magic-user unless the wording of the <i>limited wish</i> is most carefully stated) in some limited manner. The use of a <i>limited wish</i> will not substantially change major realities, nor will it bring wealth or experience merely by asking. The spell can, for example, restore some hit points (or all hit points for a limited duration) lost by the magic-user. It can reduce opponent hit probabilities or damage, it can increase duration of some magical effect, it can cause a creature to be favourably disposed to the spell caster, and so on (cf. <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a>). The <i>limited wish</i> can possibly give a minor clue to some treasure or magic item. Greedy desires will usually end in disaster for the wisher. Casting time is the actual number of seconds — at six per segment — to phrase the <i>limited wish</i>."
    ),
    Spell('Mass Invisibility','M',7,
        cast=tp(7,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This is the same as an <a href=\"/spells/invisibility-magic-user-lvl-2/\"><i>invisibility</i></a> spell except that it can hide creatures in a 3\" x 3\" area, up to 300 to 400 man-sized creatures, 30 to 40 giants, or 6 to 8 large dragons."
    ),
    Spell('Monster Summoning V','M',7,
        cast=tp(6,S),
        duration=tp(6,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell summons 1-2 fifth level monsters, and they will appear in 1-3 rounds. See <a href=\"/spells/monster-summoning-i-magic-user-lvl-3/\"><i>monster summoning I</i></a> for other details."
    ),
    Spell('Mordenkainen\'s Magnificent Mansion','M',7,
        cast=tp(7,R),
        duration_lvl=tp(1,H),
        sourcebook=U,
        desc=("By means of this spell, the magic-user conjures up an extra-dimensional dwelling, entrance to which can be gained only at a single point of space on the plane from which the spell was cast. From the entry point, those creatures observing the area will see only a faint shimmering in the air, an area of some 4' in width and 8' in height. The caster of the spell controls entry to the <i>mansion</i>, and the portal is shut and made invisible behind him when he enters. He may open it again from his own side at will. Once observers have passed beyond the entrance, they will behold a magnificent foyer and numerous chambers beyond. The place will be furnished and contain sufficient foodstuffs to serve a nine-course banquet to as many dozens of people as the spell caster has levels of experience. There will be a staff of near-transparent servants, liveried and obedient, there to wait upon all who enter. The atmosphere and temperature will be clean, fresh, and warm.\n\n"
            "Since the place can be entered only through its special portal, outside conditions do not affect the <i>mansion</i>, nor do conditions inside it pass to the plane beyond. Rest and relaxation within the place is normal, but the food is not. It will seem excellent and be quite filling as long as one is within the place. Once outside, however, its effects disappear immediately, and ravenous hunger will strike unless the individuals actually ate normal food. For each imaginary meal eaten inside the <i>mansion</i>, the individual must spend 1 hour sitting and eating normal fare. Failure to do so means that he or she has lost as many points of strength as he or she ate meals when in the mansion-like space. Such strength loss is restorable upon eating as noted, but this must be done within 6 hours or the loss of strength will be permanent. The components for this spell are a miniature portal carved from ivory, a small piece of polished marble, and a tiny silver spoon. These are utterly destroyed when the spell is cast.\n\n"
            "(It is worth mentioning that this spell has been used in conjunction with a normal portal, as well as with <i>illusion</i> magic. There is evidence that the design and interior of the space created can be altered to suit the caster's wishes.)"
        )
    ),
    Spell('Mordenkainen\'s Sword','M',7,
        cast=tp(7,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Upon casting this spell, the magic-user brings into being a shimmering sword-like plane of force. The spell caster is able to mentally wield this weapon (to the exclusion of activities other than movement), causing it to move and strike as if it were being used by a fighter. The basic chance for <i>Mordenkainen's Sword</i> to hit is the same as the chance for a sword wielded by a fighter of one-half the level of the spell caster, i.e. if cast by a 14th level magic-user, the weapon has the same hit probability as a sword wielded by a 7th level fighter. The sword has no magical \"to hit\" bonuses, but it can hit any sort of opponent even those normally struck only by +3 weapons or astral, ethereal or out of phase; and it will hit <i>any</i> armor class on a roll of 19 or 20. It inflicts 5-20 hit points on opponents of man-size or smaller, and 5-30 on opponents larger than man-sized. It can be used to subdue. It lasts until the spell duration expires, a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> is used successfully upon it, or its caster no longer desires it. The material component is a miniature platinum sword with a grip and pommel of copper and zinc which costs 500 g.p. to construct, and which disappears after the spell's completion."
    ),
    Spell('Phase Door','M',7,
        cast=tp(7,S),
        duration=tp(0),
        sourcebook=V,
        desc="When this spell is cast, the magic-user attunes his or her body, and a section of wall is affected as if by a <a href=\"/spells/passwall-magic-user-lvl-5/\"><i>passwall</i></a> spell. The <i>phase door</i> is invisible to all creatures save the spell caster, and only he or she can use the space or passage the spell creates, disappearing when the <i>phase door</i> is entered, and appearing when it is exited. The <i>phase door</i> lasts for 1 usage for every 2 levels of experience of the spell caster. It can be dispelled only by a casting of <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> from a higher level magic-user, or by several lower level magic-users, casting in concert, whose combined levels of experience are more than double that of the magic-user who cast the spell."
    ),
    Spell('Power Word, Stun','M',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When a <i>power word, stun</i> is uttered, any creature of the magic-user's choice will be stunned — reeling and unable to think coherently or act — for 2 to 8 (2d4) melee rounds. Of course, the magic-user must be facing the creature, and it must be within the spell caster's range of ½\" per level of experience. Creatures with 1 to 30 hit points will be stunned for 4-16 (4d4) rounds, those with 31 to 60 hit points will be stunned for 2 to 8 (2d4) rounds, those with 61 to 90 hit points will be stunned for 1 to 4 (d4) rounds, and creatures with over 90 hit points will not be affected. Note that if a creature is weakened due to any cause so that its hit points are below the usual maximum, the <i>current</i> number of hit points possessed will be used."
    ),
    Spell('Reverse Gravity','M',7,
        cast=tp(7,S),
        duration=tp(1,S),
        sourcebook=V,
        desc="This spell reverses gravity in the area of effect, causing all unfixed objects and creatures within it to \"fall\" upwards. The <i>reverse gravity</i> lasts for 1 second (1/6 segment) during which time the objects and creatures will \"fall\" 16' up. If some solid object is encountered in this \"fall\", the object strikes it in the some manner as a normal downward fall. At the end of the spell duration, the affected objects and creatures fall downwards. As the spell affects an area, objects tens, hundreds or even thousands of feet in the air can be affected. The material components of this spell are a lodestone and iron filings."
    ),
    Spell('Sequester','M',7,
        cast=tp(1,R),
        duration=tp(7,D),
        duration_lvl=tp(1,D),
        sourcebook=U,
        desc="When cast, this spell not only prevents detection and location spells from working to detect or locate the objects affected by the <i>sequester</i> spell, it also renders the affected object(s) invisiblle to any form of sight or seeing. Thus a <i>sequester</i> spell can mask a secret door, a treasure vault, or whatever. Of course, it does not render the subject proof from tactile discovery or from devices such as <i>robe of eyes</i> or a <i>gem of seeing</i>. If cast upon a creature not desiring to be affected and able to resist and avoid the spell, a normal saving throw versus spell is given. Living creatures (and even undead types) affected by a <i>sequester</i> spell become comatose and are kept effectively in a state of suspended animation until the spell wears off or is dispelled. The material components for the spell are basilisk eyelash, gum arabic, and a dram of whitewash."
    ),
    Spell('Simulacrum','M',7,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this spell the magic-user is able to create a duplicate of any creature. The duplicate appears exactly the same as the real. There are differences: the <i>simulacrum</i> will have only 51% to 60% (50% + 1% to 10%) of the hit points of the real creature, there will be personality differences, there will be areas of knowledge which the duplicate does not have, and a <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a> spell will instantly reveal it as a <i>simulacrum</i>, as will a <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a> spell. At all times the <i>simulacrum</i> remains under the absolute command of the magic-user who created it, although no special telepathic link exists, so command must be exercised in the normal manner. The spell creates the form of the creature, but it is only a zombie-like creature. A <a href=\"/spells/reincarnation-magic-user-lvl-6/\"><i>reincarnation</i></a> spell must be used to give the duplicate a vital force, and a <a href=\"/spells/limited-wish-magic-user-lvl-7/\"><i>limited wish</i></a> spell must be used to empower the duplicate with 40% to 65% (35% + 5% to 30%) of the knowledge and personality of the original. The level, if any, of the <i>simulacrum</i>, will be from 20% to 50% of the original creature. The duplicate creature is formed from ice or snow. The spell is cast over the rough form, and some piece of the creature to be duplicated must be placed inside the snow or ice. Additionally, the spell requires powdered ruby. The <i>simulacrum</i> has no ability to become more powerful, i.e. it cannot increase its levels or abilities."
    ),
    Spell('Statue','M',7,
        cast=tp(7,S),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="When a <i>statue</i> dweomer is cast, the magic-user or other creature is apparently turned to solid stone, along with any garments and equipment worn or carried. The initial transformation from flesh to stone requires 1 full round after the spell is cast. Thereafter the creature can withstand any inspection and appear to be a stone statue, although a faint magic will be detected from the stone if it is checked for. Despite being in this condition, the petrified individual can see, hear, and smell normally. Feeling is only as acute as that which will actually affect the granite-hard substance of the individual's body, i.e. chipping is equal to a slight wound, but breaking off one of the statue's arms is another matter. The individual under the magic of a <i>statue</i> spell can return to normal state in 1/6 of a segment, and then return to <i>statue</i> state in the same period if he or she so desires, as long as the spell duration is in effect. During the initial transformation from flesh to stone, the creature must make a saving throw of 82% or less, with -1 deducted from the dice roll score for each point of his or her constitution score, so an 18 constitution indicates certain success. Failure indicates system shock and resultant death. The material components of this spell are lime, sand, and a drop of water stirred by an iron bar such as a nail or spike."
    ),
    Spell('Teleport Without Error','M',7,
        cast=tp(1,S),
        duration=tp(0),
        sourcebook=U,
        desc="This spell is similar to a <a href=\"/spells/teleport-magic-user-lvl-5/\"><i>teleport</i></a> spell. The caster is able to transport himself or herself, along with the material weight noted for a <a href=\"/spells/teleport-magic-user-lvl-5/\"><i>teleport</i></a> spell, to any known location on his or her home plane — with no chance of error. The spell also enables the caster to travel to other planes of existence, but any such plane is, at best, \"Studied carefully.\" This assumes the caster has, in fact actually been to the plane and carefully perused an area so that it could later be used as a destination for <i>teleportation without error</i>. The table for <a href=\"/spells/teleport-magic-user-lvl-5/\"><i>teleport</i></a> is used for teleporting to other planes, with the appropriate knowledge of the plane to which transportation is desired used to determine the chance of error. (Exception: See 9th-level magic-user spell <a href=\"/spells/succor-magic-user-lvl-9/\"><i>succor</i></a>, described hereafter.) The caster can do nothing else in the round that he or she appears from a teleport."
    ),
    Spell('Torment','M',7,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("When this spell is cast, the magic-user seeks to force submission and obedience from a captive creature from another plane from whom a service is being demanded (also see <a href=\"/spells/dolor-magic-user-lvl-5/\"><i>dolor</i></a> and <a href=\"/spells/ensnarement-magic-user-lvl-6/\"><i>ensnarement</i></a> spells herein). The initial uttering of the spell causes a link from the caster to the captive creature bound in a magic circle, thaumaturgic triangle, or pentagram. (An intended victim of this spell must fail a magic resistance check, if applicable, for the <i>torment</i> to have any effect.) Thereafter, the magic-user continues to read the balance of the specially prepared writing, and each round this continues, the captive feels progressively worse — discomfort and then pain. The first two rounds bring <i>twinges</i>, the third and fourth rounds of reading brings <i>shooting pains</i>, and the fifth and sixth rounds of reading cause <i>aches</i> and then <i>cramps</i>.\n\n"
            "The creature refusing to submit to the performance of a service is given a straight saving throw versus spell, adjusted each round for the intensity of the dweomer to be affected by it. The save in the first round is made at -1 to the die roll, the second at -2, the third at -3, the fourth at -4, and the fifth and sixth at -6 and -8 respectively. Failing the saving throw indicates the creature has agreed to the mage's demands. There is no penalty following round 8 in any event.\n\n"
            "The effects of the <i>torment</i> will have an effect on the creature should it break loose. The creature is -1 on initiative for every 2 rounds the spell has been in effect, up to a maximum penalty of -4 on round 8. In addition, the creature is -1 to hit and -1 per die of damage after 3 rounds of the spell, this increasing by -1 per round to -4 in round 6, then decreasing again to -1 in round 9.\n\n"
            "It is likely that any intelligent creature with low moral standards will submit once it realizes the nature of the spell it is being subjected to. Naturally, this does not cause the creature to feel anything other than immense hatred for the magic-user. The forced service will be carried out to the letter, as is the case with all such agreements, but the creature will most certainly seek whatever revenge it can.\n\n"
            "Preparation for the casting of a <i>torment</i> spell requires either the secret name for the type of creature or its given name to be inscribed in the text of the incantation. The caster must also identify himself or herself. This establishes the link and allows the dweomer to be efficacious. However, for every 1 point of intelligence of the creature above that of the spell caster, there is a 1% chance that the captive creature will gain control, draw the caster into the confines of its prison, and carry him or her off to its own plane and whatever fate is thus decreed. If the magic-user is interrupted or distracted during the reading, there is a 5% chance per point of intelligence of the captive creature that it will gain control.\n\n"
            "The material component of the spell is the aforementioned \"specially prepared writing\" (in the form of a scroll). Its special inks will require an expenditure of not less than 1,000 gp per hit die of the creature to be affected by the dweomer of the spell."
        )
    ),
    Spell('Truename','M',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("This spell enables the magic-user to have great power over any living thing which has a name, generic or individual, known to the spell caster. Naturally, most <i>true</i> names are not known (even by the creaturs themselves), for the common names of most things are not their true and secret names. True names are discovered through hard work, spying, extensive use of <a href=\"/spells/legend-lore-magic-user-lvl-6/\"><i>legend lore</i></a> and sagecraft (at the most difficult levels). The casting of a <i>truename<i/> spell requires the magic-user to call out the true name of the subject and then begin a recitation of verse which encompasses the nature and/or history of the subject. This will require 3 segments. Thereafter, still in verse (and preferably rhyming or near-rhyming), the caster must desrive the desired result of the <i>truename</i> spell. Each possible result differs in the length of time necessary to effectuate it:\n\n"
            "<i>Multiple Suggestion</i>: The verse can contain from 1 to 4 <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> powers, just as if each were a spell. Each verse requires 1 segment to recite. (See <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> spell.) In a total of 7 segments (including the time for the initial reading), 4 suggestions can be made.\n\n"
            "<i>Weakness and Surrender</i>: The verses recited cause actual loss of 1 point of strength (-1 to hit and damage, -1 on movement rate) for each segment of recitation. With the loss of each point of strength, the subject must save versus paralyzation or meekly surrender. Each verse must continue for 1 segment. Strength loss is recovered in from 2-8 rounds after the recitation ceases, and with recovery of strength the subject regains its will to resist."
            "<i>Polymorph</i>: The verses can cause the subject to change into something else, just as if a <a href=\"/spells/polymorph-any-object-magic-user-lvl-8/\"><i>polymorph any object</i></a> spell had been cast. No system shock saving throw is needed. The length of time in verses (1 segment per verse) to cause the <i>polymorph</i> depends on how radical the change:\n"
            "   mineral to animal = 10 verses\n"
            "   mineral to vegetable = 9 verses\n"
            "   vegetable to animal = 8 verses\n"
            "   monster to normal = 7 verses\n"
            "   monster to monster = 6 verses\n"
            "   other to human = 5 verses\n"
            "   animal to animal = 4 verses\n"
            "   vegetable to vegetable = 3 verses\n"
            "   mineral to mineral = 2 verses\n\n"
            "The reverse of the preceding cases also holds. In cases not stated, the DM is to use the closest stated case as a guide. The subject returns to its natural form in time. Duration is 6 turns per level of the spell caster minus 1 turn for every verse required to effect the <i>polymorph</i>. The subject will think and behave exactky as a non-polymorphed thing of the same type, but have its original hit points.\n\n"
            "<i>Transport</i>: When the <i>transport</i> verses are recited, the subject will be <a href=\"/spells/teleport-without-error-magic-user-lvl-7/\"><i>teleported without error</i></a> or otherwise moved to some other place. The number of verses required depends on the location of the <i>transport</i>:\n"
            "   same plane/100 mile range = 4 verses\n"
            "   same plane/500 mile range = 5 verses\n"
            "   same plane/2,000 mile range = 6 verses\n"
            "   one plane/world removed = 7 verses\n"
            "   two planes/worlds removed = 8 verses\n\n"
            "The subject will automatically by altered so as to be able to physically survive the normal conditions of the place to which it is sent. There is no saving throw if the subjects are willing, even if they have a magic resistance.\n\n"
            "If at any time during the recitation of the spell the caster is interrupted, the magic fails and the spell is lost."
        )
    ),
    Spell('Vanish','M',7,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When the magic-user employs this spell, he or she causes an object to <i>vanish</i>. The magic-user can cause the object to be teleported (see <a href=\"/spells/teleport-magic-user-lvl-5/\"><i>teleport</i></a> spell) if it weighs up to a maximum of 500 g.p. per level of experience of the spell caster, i.e. 14th level magic-user can <i>vanish</i> and cause to reappear at his or her desired location 7000 g.p. weight. Greater objects can be made to <i>vanish</i>, but they are simply placed into the ethereal plane and replaced with stone. Thus, a door can be made to disappear, and it will be replaced by a stone wall of 1' thickness, or equal in thickness to the door, whichever is greater. The maximum volume of material which can be affected is 3 cubic feet per level of experience. Thus, both weight and volume limit the spell. A <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> which is successful will bring back vanished items from the ethereal plane."
    ),
    Spell('Volley','M',7,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="This highly dangerous dweomer enables the prospective recipient of a spell to turn the casting back upon its sender. Thus, the range, duration, area of effect, and saving throw of this spell depend upon circumstances and the spell being <i>volleyed</i>. Assume that a <a href=\"/spells/power-word-kill-magic-user-lvl-9/\"><i>power word kill</i></a> is cast at a magic-user prepared with a <i>volley</i> spell. The <i>volley</i> has been cast also, so that when the <a href=\"/spells/power-word-kill-magic-user-lvl-9/\"><i>power word kill</i></a> is aimed at the target, the <i>volley</i> causes the spell to bounce back upon its caster. Then, if the caster of the first spell fails to make a saving throw versus spell, the <a href=\"/spells/power-word-kill-magic-user-lvl-9/\"><i>power word kill</i></a> works upon its caster rather than its intended target. However, if the original caster does save versus spell, the spell once again flies toward the original target. The caster of the <i>volley</i> spell must then save versus spell, or be affected by the attack. Again, if the caster of the <i>volley</i> spell saves, then the spell is returned to its originator, who must again save or be affected. The spell will be sent back and forth until one or the other fails to save, or until the spell loses its power. The entire spell is <i>volleyed</i>, such that if a <a href=\"/spells/lightning-bolt-magic-user-lvl-3/\"><i>lightning bolt</i></a> were to start 10 feet before the volleying magic-user, the full spell would be returned, leaving others in the volleying party unscathed. Each exchange will take a single second. A spell will lose power if it passes through a number of exchanges equal to its level, counting each volley, but not the original casting, as half of a single exchange; i.e., a 1st-level spell will be cast, <i>volleyed</i> the first time, (perhaps) return <i>volleyed</i>, and then will dissipate; a 2nd-level spell would go through four <i>volley</i> portions (two complete exchanges) before being exhausted; and so on. The material component is a bit of bent willow or other flexible wood, crisscrossed with specially prepared strands of gut."
    ),
    Spell('Antipathy/Sympathy','M',8,
        cast=tp(6,T),
        duration_lvl=tp(12,T),
        sourcebook=V,
        desc=("This spell allows the magic-user to set up certain vibrations which will tend to either repel or attract a specific type of living, intelligent creature or characters of a particular alignment. The magic-user must decide which effect is desired with regard to what creature or alignment type before beginning the dweomercraefting, for the components of each application differ. The spell cannot be cast upon living creatures.\n\n"
            "<i>Antipathy</i>: This dweomer causes the affected creature or alignment type to feel an overpowering urge to leave the area or not touch the affected item. If a saving throw versus magic is successful, the creature may stay/touch the item, but the creature will feel very uncomfortable, and a persistent itching will cause it to suffer the loss of 1 point of dexterity per round the area or item is remained in or touched, subject to a maximum of 4 points. Failure to save versus magic forces the creature/alignment type to abandon the magicked area or item, shunning it permanently and never willingly enter/touch it until the spell is removed or expires. The material component for this application of the spell is a lump of alum soaked in vinegar.\n\n"
            "<i>Sympathy</i>: By casting the <i>sympathy</i> application of the spell, the magic-user can cause a particular type of creature or alignment of character to feel elated and pleased to be in an area or with the prospect of touching or possessing an object or item. The desire to stay in the area or touch/possess the magicked object/item will be overpowering, and unless a saving throw versus magic is made, the creature or character will stay or refuse to release the object. If the saving throw is successful, the creature or character is released from the enchantment, but a subsequent saving throw must be made from 1-6 turns later, and if this one fails, the affected creature will return to the area or object. The material components of this spell are 1,000 g.p. worth of crushed pearls and a drop of honey.\n\n"
            "Note that the particular kind of creature to be affected must be named specifically, i.e. red dragons, hill giants, wererats, lammasu, catoblepas, vampires, etc. Likewise, the specific alignment type for characters must be named, i.e. chaotic evil, chaotic good, lawful neutral, neutral, etc.\n\n"
            "If this spell is cast upon an area, a 10' per side cube can be magicked per level of experience of the magic-user. If an object or item is magicked, only that single thing can be enchanted, but affected creatures/characters save versus magic thereon at -2."
        )
    ),
    Spell('Bigby\'s Clenched Fist','M',8,
        cast=tp(8,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("<i>Bigby's Clenched Fist</i> spell brings forth a huge disembodied hand which is balled into a fist. This magical member is under the mental control of the spell caster, and he or she can cause it to strike an opponent each round. No other spell casting or magical activity may be undertaken for the duration of the spell. The <i>Clenched Fist</i> never misses, but the effectiveness of its blow varies from round to round.\n\n"
            "<table>"
            "<tr><th>Die Roll</th><th>Result</th></tr>"
            "<tr><td>1-12</td><td>glancing blow — 1 to 6 hit points</td></tr>"
            "<tr><td>13-16</td><td>solid punch — 2 to 12 hit points</td></tr>"
            "<tr><td>17-19</td><td>hard punch — 3 to 18 hit points and opponent is stunned next round</td></tr>"
            "<tr><td>20</td><td>crushing punch — 4 to 24 hit points and opponent is stunned for next 3 rounds</td></tr>"
            "</table>\n\n"
            "Note: Any <i>stunned</i> opponent allows the magic-user to add +4 to his or her die roll to determine how well the <i>fist</i> strikes, as the opponent is not capable of dodging or defending against the attack effectively. (This spell can be used with any of the other <i>Hand</i> spells of the Archmage Bigby.) The material component of this spell is a leather glove and a small device consisting of four rings joined so as to form a slightly curved line, with an \"I\" upon which the bottoms of the rings rest, the whole fashioned of an alloyed metal of copper and zinc. The <i>Fist</i> is destroyed by damage equal to the hit points of its caster being inflicted upon it."
        )
    ),
    Spell('Binding','M',8,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("A <i>binding</i> spell enables the caster to capture a creature from the lower planes. The subject must already be confined by some form of restraining diagram. The duration of the spell depends upon the form of the <i>binding</i> and the level of the caster(s), as well as the length of time the spell is actually uttered. The components vary according to the form of the dweomer, but include: a continuous chanting utterance read from the scroll or book page giving the spell; gestures appropriate to the form of <i>binding</i>; and materials such as miniature chains of special metal (iron for demonkind, silver for diabolical creatures, nickel for the minions of Hades, etc.), soporific herbs of the rarest sort, a diamond or corundum gem of great size (1,000 gp value per hit die of the subject creature), and a vellum depiction or carved statuette of the subject to be captured.\n\n"
            "A saving throw is not applicable as long as the experience level(s) of the caster(s) is (are) at least twice as great as the hit dice of the subject. In a case where the foregoing does not hold, then the subject gains a saving throw versus spell, modified by the form of <i>binding</i> being attempted and the relative ratio of level(s) of experience of the caster(s) to the subject creature's hit dice. For purposes of determining this number, the level of the principal caster is augmented by one-third of the level of experience of each assistant magic-user of 9th or higher level, and an additional level is gained for each assistant of 4th to 8th level. No more than six other magic-users can assist with a <i>binding</i> spell. The various forms of <i>binding</i> are these:\n\n"
            "<i>Chaining</i>: The subject is confined by restraints which generate an <a href=\"/spells/antipathysympathy-magic-user-lvl-8/\"><i>antipathy</i></a> affecting all creatures who approach the subject, except the caster. Duration is as long as one year per level of the caster(s). The subject of this form of <i>binding</i> (as well as of <i>slumber</i> and <i>bound slumber</i>; see below), remains within the restraining diagram.\n\n"
            "<i>Slumber</i>: Brings a comatose sleep upon the subject for a duration of up to one year per level of the caster(s).\n\n"
            "<i>Bound Slumber</i>: A combination of <i>chaining</i> and <i>slumber</i> which lasts for up to one month per level of the caster(s).\n\n"
            "<i>Hedged Prison</i>: The subject is transported to or otherwise brought within a confined area from which it may not wander by any means until freed. The dweomer remains until the magical hedge is somehow broken.\n\n"
            "<i>Metamorphosis</i>: Causes the subject to change to some noncorporeal form, save for its head or face. The <i>binding</i> is permanent until some prescribed act frees the subject.\n\n"
            "<i>Minimus Containment</i>: The subject is shrunk to a height of one inch or even less and held within the hedged prison of some gem or similar object. The subject of a <i>minimus containment</i>, <i>metamorphosis</i>, or <i>hedged prison</i> radiates a very faint aura of magic.\n\n"
            "The saving throw, if applicable, is made at the normal level for the <i>chaining</i> form of the spell. <i>Slumber</i> allows the subject a +1, <i>bound slumber</i> a +2, <i>hedged prison</i> a +3, <i>metamorphosis</i> a +4, and <i>minimus containment</i> a +5 on the save. However, if the subject is initially weakened by magical means such as <a href=\"/spells/dolor-magic-user-lvl-5/\"><i>dolor</i></a> or <a href=\"/spells/torment-magic-user-lvl-7/\"><i>torment</i></a> spells, the saving throw is subject to an adjustment or -1 for the former spell, -2 for the latter spell, and -4 for both in successive combination. A successful saving throw enables the subject to burst its bonds and do as it pleases.\n\n"
            "A <i>binding</i> spell can be renewed in the case of the first three forms of the dweomer, for the subject does not have the opportunity to break the bonds. After one year the subject gains a normal saving throw versus spell. Whenever it is successful, the <i>binding</i> spell is broken and the subject creature is free. (If anything has caused a weakening of the <i>chaining</i> or <i>slumber</i>, such as attempts to contact the subject or magically touch it, a normal saving throw applies to the renewal of the spell.)"
        )
    ),
    Spell('Clone','M',8,
        cast=tp(1,T),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell creates a duplicate of a person. This clone is in all respects the duplicate of the individual, complete to the level of experience, memories, etc. However, the duplicate <i>is</i> the person, so that if the original and a duplicate exist at the same time, each knows of the other's existence; and the original person and the <i>clone</i> will each desire to do away with the other, for such an alter-ego is unbearable to both. If one cannot destroy the other, one (95%) will go insane (75% likely to be the <i>clone</i>) and destroy itself, or possibly (5%) both will become mad and commit suicide. These probabilities will occur within 1 week of the dual existence. The material component of the spell is a small piece of the flesh of the person to be duplicated. Note that the <i>clone</i> will become the person as he or she existed at the time at which the flesh was taken, and all subsequent knowledge, experience, etc. will be totally unknown to the <i>clone</i>. Also, the <i>clone</i> will be a physical duplicate, and possessions of the original are another matter entirely. Note that a clone takes from 2-8 months to grow, and only after that time is dual existence established."
    ),
    Spell('Demand','M',8,
        cast=tp(1,T),
        duration=tp(1,VA),
        sourcebook=U,
        desc="This spell is essentially the same as a <a href=\"/spells/sending-magic-user-lvl-5/\"><i>sending</i></a> spell. <i>Demand</i> differs from <a href=\"/spells/sending-magic-user-lvl-5/\"><i>sending</i></a> in that the spell caster may phrase his or her message so as to contain a <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> spell and if the subject fails to make its saving throw versus spell, it will do its best to carry out the <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> contained in the message of the <i>demand</i>. Of course, if the message is relatively impossible or incongruous according to the circumstances which exist for the subject at the time the <i>demand</i> comes, the message is understood but no saving throw is necessary and the <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> is ineffective. The material components of the spell are a pair of cylinders, each open at one end, connected by a thin piece of copper wire and some small part of the subject creature — a hair, bit of nail, etc."
    ),
    Spell('Glassteel','M',8,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>glassteel</i> spell turns crystal or glass into a transparent substance which has the tensile strength and unbreakability of actual steel. Only a relatively small volume of material can be affected, a maximum weight of 10 pounds per level of experience of the spell caster, and it must form one whole object. The material components of this spell area small piece of glass and a small piece of steel."
    ),
    Spell('Incendiary Cloud','M',8,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="An <i>incendiary cloud</i> spell exactly resembles the smoke effects of a <a href=\"/spells/pyrotechnics-druid-lvl-3/\"><i>pyrotechnics</i></a> spell, except that its minimum dimensions are a cloud of 10' height by 20' length and breadth. This dense vapor cloud billows forth, and on the 3rd round of its existence it begins to flame, causing ½ hit point per level of the magic-user who cast it. On the 4th round it does 1 hit point of damage per level of the caster, and on the 5th round it again drops to ½ h.p. of damage per level of the magic-user as its flames burn out. Any successive rounds of existence are simply harmless smoke which obscures vision within its confines. Creatures within the cloud need make only 1 saving throw if it is successful, but if they fail the first, they roll again an the 4th and 5th rounds (if necessary) to attempt to reduce damage sustained by one-half. In order to cast this spell the magic-user must have an available fire source (just as with a <a href=\"/spells/pyrotechnics-druid-lvl-3/\"><i>pyrotechnics</i></a> spell), scrapings from beneath a dung pile, and a pinch of dust."
    ),
    Spell('Mass Charm','M',8,
        cast=tp(8,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="A <i>mass charm</i> spell affects either persons or monsters just as a <a href=\"/spells/charm-person-magic-user-lvl-1/\"><i>charm person</i></a> spell or a <a href=\"/spells/charm-monster-magic-user-lvl-4/\"><i>charm monster</i></a> spell does. The <i>mass charm</i>, however, will affect a number of creatures whose combined levels of experience and/or hit dice does not exceed twice the level of experience of the spell caster. All affected creatures must be within the spell range and within a maximum area of 3\" by 3\". Note that the creatures' saving throws are unaffected by the number of recipients (cf. <a href=\"/spells/charm-person-magic-user-lvl-1/\"><i>charm person</i></a> and <a href=\"/spells/charm-monster-magic-user-lvl-4/\"><i>charm monster</i></a>), but all target creatures are subject to a penalty of -2 on the saving throw because of the efficiency and power of a <i>mass charm</i> spell."
    ),
    Spell('Maze','M',8,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("An extra-dimensional space is brought into being upon utterance of a <i>maze</i> spell. The recipient will wander in the shifting labyrinth of force planes for a period of time which is totally dependent upon its intelligence. (Note: Minotaurs are not affected by this spell.)\n\n"
            "<table>"
            "<tr><th>Intelligence of Mazed Creature</th><th>Time Trapped in Maze</th></tr>"
            "<tr><td>under 3</td><td>2 to 8 turns</td></tr>"
            "<tr><td>3 to 5</td><td>1 to 4 turns</td></tr>"
            "<tr><td>6 to 8</td><td>5 to 20 rounds</td></tr>"
            "<tr><td>9 to 11</td><td>4 to 16 rounds</td></tr>"
            "<tr><td>12 to 14</td><td>3 to 12 rounds</td></tr>"
            "<tr><td>15 to 17</td><td>2 to 8 rounds</td></tr>"
            "<tr><td>18 and up</td><td>1 to 4 rounds</td></tr>"
            "</table>"
        )
    ),
    Spell('Mind Blank','M',8,
        cast=tp(1,S),
        duration=tp(1,D),
        sourcebook=V,
        desc="When the very powerful <i>mind blank</i> spell is cast, the recipient is totally protected from all devices and/or spells which detect, influence, or read emotions and/or thoughts. Protection includes <a href=\"/spells/augury-cleric-lvl-2/\"><i>augury</i></a>, <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charm</i></a>, <a href=\"/spells/command-cleric-lvl-1/\"><i>command</i></a>, <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a>, <a href=\"/spells/divination-cleric-lvl-4/\"><i>divination</i></a>, empathy (all forms), <a href=\"/spells/esp-magic-user-lvl-2/\"><i>ESP</i></a>, <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a>, <a href=\"/spells/feeblemind-druid-lvl-6/\"><i>feeblemind</i></a>, <a href=\"/spells/mass-suggestion-illusionist-lvl-6/\"><i>mass suggestion</i></a>, <a href=\"/spells/phantasmal-killer-illusionist-lvl-4/\"><i>phantasmal killer</i></a>, possession, rulership, <a href=\"/spells/trap-the-soul-magic-user-lvl-8/\"><i>soul trapping</i></a>, <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a>, and <i>telepathy</i>. Cloaking protection also extends to prevention of discovery or information gathering by <i>crystal balls</i> or other scrying devices, <a href=\"/spells/clairaudience-magic-user-lvl-3/\"><i>clairaudience</i></a>, <a href=\"/spells/clairvoyance-magic-user-lvl-3/\"><i>clairvoyance</i></a>, <a href=\"/spells/commune-cleric-lvl-5/\"><i>communing</i></a>, <a href=\"/spells/contact-other-plane-magic-user-lvl-5/\"><i>contacting other planes</i></a>, or wish-related methods (<a href=\"/spells/wish-magic-user-lvl-9/\"><i>wishing</i></a>, <a href=\"/spells/limited-wish-magic-user-lvl-7/\"><i>limited wish</i></a>, <a href=\"/spells/alter-reality-illusionist-lvl-7/\"><i>alter reality</i></a>). Of course, exceedingly powerful deities would be able to penetrate the spell's powers. Note that this spell also protects from psionic-related detection and/or influence such as <i>domination</i> (or <i>mass domination</i>), <i>hypnosis</i>, <i>invisibility</i> (the psionic sort is mind related), and <i>precognition</i>, plus those powers which are already covered as spells."
    ),
    Spell('Monster Summoning VI','M',8,
        cast=tp(8,S),
        duration=tp(7,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell summons 1 or 2 sixth level monsters, the creature(s) appearing in 1 to 3 rounds. See <a href=\"/spells/monster-summoning-i-magic-user-lvl-3/\"><i>monster summoning I</i></a> for other details."
    ),
    Spell('Otiluke\'s Telekinetic Sphere','M',8,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell is exactly the same as the 4th-level magic-user spell, <a href=\"/spells/otilukes-resilient-sphere-magic-user-lvl-4/\"><i>Otiluke's Resilient Sphere</i></a>, with the addition that the interior of the globe is virtually weightless; i.e., anything contained within it weighs only 1/16 of its normal weight. Any subject weighing up to 5,000 pounds can be telekinetically lifted in the sphere by the caster. Range of control extends to a maximum distance of 1\" per level of the caster after the sphere has actually succeeded in encapsulating a subject or subjects. Note that even if more than 5,000 pounds of weight is englobed, the essential weight is but 1/16 of actual, so the orb can be rolled without exceptional effort. Because of the reduced weight, rapid motion or falling within the field of the sphere is relatively harmless to the obect therein, althought it can be disastrous should the globe disappear when the subject inside is high above a hard surface. In addition to the material components for the <a href=\"/spells/otilukes-resilient-sphere-magic-user-lvl-4/\"><i>resilient sphere</i></a>, the caster must have a pair of small bar magnets to effectuate this spell."
    ),
    Spell('Otto\'s Irresistible Dance','M',8,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When <I>Otto's Irresistible Dance</i> is placed upon a creature, the spell causes the recipient to begin dancing, feet shuffling and tapping. This dance makes it impossible for the victim to do anything other than caper and prance, this cavorting lowering the armor class of the creature by -4, making saving throws impossible, and negating any consideration of a shield. Note that the creature must be touched — possibly as if melee combat were taking place and the spell caster were striking to do damage."
    ),
    Spell('Permanency','M',8,
        cast=tp(2,R),
        duration=tp(1,P),
        sourcebook=V,
        desc=("This spell affects the duration of certain other spells, making the duration <i>permanent</i>. The spells upon which a personal <i>permanency</i> will be effective are:\n\n"
            "<a href=\"/spells/comprehend-languages-magic-user-lvl-1/\"><i>comprehend languages</i></a>\n"
            "<a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect evil</i></a>\n"
            "<a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detect invisibility</i></a>\n"
            "<a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect magic</i></a>\n"
            "<a href=\"/spells/infravision-magic-user-lvl-3/\"><i>infravision</i></a>\n"
            "<a href=\"/spells/protection-from-evil-cleric-lvl-1/\"><i>protection from evil</i></a>\n"
            "<a href=\"/spells/protection-from-normal-missiles-magic-user-lvl-3/\"><i>protection from normal missiles</i></a>\n"
            "<a href=\"/spells/read-magic-magic-user-lvl-1/\"><i>read magic</i></a>\n"
            "<a href=\"/spells/tongues-magic-user-lvl-3/\"><i>tongues</i></a>\n"
            "<a href=\"/spells/unseen-servant-magic-user-lvl-1/\"><i>unseen servant</i></a>\n\n"
            "The magic-user casts the desired spell and then follows with the <i>permanency</i> spell. Each <i>permanency</i> spell lowers the magic-users constitution by 1 point. The magic-user cannot cast these spells upon other creatures. In addition to personal use, the <i>permanency</i> spell can be used to make the following object/creature or area effect spells lasting:\n\n"
            "<a href=\"/spells/enlarge-magic-user-lvl-1/\"><i>enlarge</i></a>\n"
            "<a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a>\n"
            "<a href=\"/spells/gust-of-wind-magic-user-lvl-3/\"><i>gust of wind</i></a>\n"
            "<a href=\"/spells/invisibility-magic-user-lvl-2/\"><i>invisibility</i></a>\n"
            "<a href=\"/spells/magic-mouth-magic-user-lvl-2/\"><i>magic mouth</i></a>\n"
            "<a href=\"/spells/prismatic-sphere-magic-user-lvl-9/\"><i>prismatic sphere</i></a>\n"
            "<a href=\"/spells/stinking-cloud-magic-user-lvl-2/\"><i>stinking cloud</i></a>\n"
            "<a href=\"/spells/wall-of-fire-magic-user-lvl-4/\"><i>wall of fire</i></a>\n"
            "<a href=\"/spells/wall-of-force-magic-user-lvl-5/\"><i>wall of force</i></a>\n"
            "<a href=\"/spells/web-magic-user-lvl-2/\"><i>web</i></a>\n\n"
            "The former application of <i>permanency</i> can be dispelled only by a magic-user of greater level than the spell caster was when he or she initially cast it. The <i>permanency</i> application to other spells allows it to be cast simultaneously with any of the latter when no living creature is the target, but the <i>permanency</i> can be dispelled normally, and thus the entire spell negated."
        )
    ),
    Spell('Polymorph Any Object','M',8,
        cast=tp(1,R),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("This spell changes one object (living or otherwise) into another. When used as a <a href=\"/spells/polymorph-other-magic-user-lvl-4/\"><i>polymorph other</i></a> or <a href=\"/spells/stone-to-flesh-magic-user-lvl-6/\"><i>stone to flesh</i></a>, simply treat the spell as a more powerful version, with saving throws made at -4 on the die. When it is cast in order to change other objects, the duration of the spell will depend on how radically removed the original was from its magicked state, as well as how different in size. This will be determined by your Dungeon Master by comparing:\n\n"
            "<i>kingdom</i> — animal, vegetable, mineral\n"
            "<i>class</i> — mammals, bipeds, fungi, metals, spheres, etc.\n"
            "<i>relationship</i> — twig is to tree, sand is to beach, etc.\n"
            "<i>size</i> — smaller, equal, larger\n"
            "shape — comparative resemblance of the original to the polymorphed state\n"
            "intelligence — particularly with regard to a change in which the end product is more intelligent\n\n"
            "Change in <i>kingdom</i> makes the spell work for hours or turns, i.e. hours if one removed, turns if two removed. Other changes likewise affect spell duration. Thus, changing a lion to an androsphinx would be permanent, but turning a turnip to a purple worm would be a change of only hours duration; turning a tusk into an elephant would be permanent, but turning a twig into a sword would be only a change of several turns duration. All <i>polymorphed</i> objects radiate a strong magic, and if a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> is used upon them, they will return to their natural form. Note that a <a href=\"/spells/stone-to-flesh-magic-user-lvl-6/\"><i>stone to flesh</i></a>, or its reverse, will affect objects under this spell. The material components of this spell are mercury, gum arabic, and smoke. N.B.: <i>System shock</i> applies to living creatures, as do the restrictions noted regarding <a href=\"/spells/polymorph-other-magic-user-lvl-4/\"><i>polymorph others</i></a> and <a href=\"/spells/stone-to-flesh-magic-user-lvl-6/\"><i>stone to flesh</i></a>."
        )
    ),
    Spell('Power Word, Blind','M',8,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When a <i>power word, blind</i> is cast, one or more creatures within spell range and area of effect will become temporarily sightless. The spell affects up to 100 hit points of creatures, but the duration is dependent upon how many hit points of creatures are affected. If 50 or less points are affected, blindness lasts for 2 to 5 (d4+1) turns, if 51 or more hit points of creatures are affected, the spell duration is but 2 to 5 rounds. Note that the spell caster must indicate which creatures he or she desires to affect with the spell, noting one as target center, prior to determining results. Creatures with over 100 hit points are not affected. Blindness can be removed by <a href=\"/spells/cure-blindness-cleric-lvl-3/\"><i>cure blindness</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>."
    ),
    Spell('Serten\'s Spell Immunity','M',8,
        cast=tp(1,VA),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc=("By use of this spell the magic-user is able to confer virtual immunity to certain spells and magical attack forms upon those he or she touches and magicks. For every 4 levels of experience of the magic-user, 1 creature can be protected by the <i>Serten's Spell Immunity</i> spell, but the duration of the protection is similarly disbursed upon these additional figures. (Example: A 16th level magic-user can cast the dweomer upon 1 creature and it will last 16 turns, or he or she can place it upon 2 creatures for an 8 turn duration, or upon 4 creatures for but 4 turns duration.) The protection gives a bonus to saving throws as follows:\n\n"
            "<i>Beguiling, Charm, Suggestion</i>   +9\n"
            "<i>Command, Domination, Fear, Hold, Scare</i> +7\n"
            "<i>Geas, Quest</i> +5\n\n"
            "The material component of this spell is a diamond which must be crushed and sprinkled over the spell recipients, and each such creature must also have in its possession a diamond of any size, intact and carried on its person."
        )
    ),
    Spell('Sink','M',8,
        cast=tp(8,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("When the magic-user casts a <i>sink</i> spell, he or she must chant the spell for 4 segments without interruption. At that juncture, the subject creature or object will become rooted to the spot unless a saving throw versus spell (with respect to a creature) or a saving throw versus <a href=\"/spells/disintegrate-magic-user-lvl-6/\"><i>disintegration</i></a> (for an object with magical properties) is successful. (Note: \"Magical properties\" include those of magic items as listed in the Dungeon Masters Guide, those of items enchanted or otherwise of magical origin, and those of items with protection-type spells or with permanent magical properties or similar spells upon them.) Items of a non-magical nature are not entitled to a saving throw. The subject will also become of the same density as the surface upon which it stands at this juncture if its saving throw was not successful.\n\n"
            "The spell caster now has the option of ceasing his or her spell and leaving the subject as it is, in which case the spell will lose its dweomer in 4 turns, and the subject will return to normal. If the magic-user proceeds with the spell, the subject will begin to slowly <i>sink</i> into the ground. On the 5th segment the subject will <i>sink</i> to one-quarter of its height, on the 6th another quarter, on the 7th another, and on the 8th segment it will be totally sunken into the ground.\n\n"
            "This virtual entombment will place a living subject into a state which duplicates <a href=\"/spells/temporal-stasis-magic-user-lvl-9/\"><i>stasis</i></a> but does not otherwise harm the subject. Non-living or living, the subject will exist in undamaged form in the surface into which it was sunk, its upper extremity as far beneath the surface as the subject has height; i.e., a 6' high subject will be 6' beneath the surface, while a 60' high subject will have its uppermost portion 60' below ground level. If the ground around the subject is somehow removed, the spell is broken and the subject will return to normal — although it will not then rise up. Such spells as <a href=\"/spells/dig-magic-user-lvl-4/\"><i>dig</i></a>, <a href=\"/spells/transmute-rock-to-mud-druid-lvl-5/\"><i>transmute rock to mud</i></a>, and <a href=\"/spells/imprisonment-magic-user-lvl-9/\"><i>freedom</i></a> (reverse of imprisonment) will not harm the subject of a <i>sink</i> spell and will be helpful in recovering it in many cases. If a <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a> spell is cast over an area upon which a <i>sink</i> spell was used, it will reveal a faint dweomer of undefinable nature, even if the subject is beyond detection range. If the subject is within range of the <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a>, the dweomer will be noted as magic of an enchantment-alteration nature."
        )
    ),
    Spell('Symbol','M',8,
        cast=tp(8,S),
        duration=tp(1,P),
        sourcebook=V,
        desc=("A <i>symbol</i> spell causes the creation of magical runes which affect creatures which pass over, touch, read, or pass through a portal upon which the <i>symbol</i> is inscribed. Upon casting the spell, the magic-user inscribes the <i>symbol</i> upon whatever surface he or she desires. Likewise, the spell caster is able to place the <i>symbol</i> of his or her choice, using any one of the following:\n\n"
            "<i>Death</i> — One or more creatures whose total hit points do not exceed 80 are slain.\n\n"
            "<i>Discord</i> — All creatures are affected and immediately fall to loudly bickering and arguing; furthermore, there is a 50% probability that creatures of different alignment will attack each other. The bickering lasts for 5-20 rounds; the fighting for 2-8 rounds.\n\n"
            "<i>Fear</i> — This <i>symbol</i> operates as an extra-strong <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a> spell, causing all creatures to save vs. the spell at -4 on the die or panic and flee as if affected by a <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a> spell."
            "<i>Hopelessness</i> — All creatures are affected and must turn back in dejection unless they save versus magic. Affected creatures will submit to the demands of any opponent, i.e. surrender, get out, etc.; the <i>hopelessness</i> lasts for 3 to 12 (3d4) turns, and during this period it is 25% probable that affected creatures will take no action during any round, and 25% likely that those taking action will turn back or retire from battle, as applicable.\n\n"
            "<i>Insanity</i> — One or more creatures whose total hit points do not exceed 120 will become insane and remain so, acting as if a <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> spell had been placed upon them until a <a href=\"/spells/heal-cleric-lvl-6/\"><i>heal</i></a>, <a href=\"/spells/restoration-cleric-lvl-7/\"><i>restoration</i></a>, or <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> spell is used to remove the madness.\n\n"
            "<i>Pain</i> — All creatures are affected, having wracking pains shooting through their bodies, which causes them to have -2 on dexterity and -4 on attack dice for from 2-20 turns.\n\n"
            "<i>Sleep</i> — All creatures under 8+1 hit dice will immediately fall into a catatonic slumber and cannot be awakened for 5 to 16 (d12 + 4) turns.\n\n"
            "<i>Stunning</i> — One or more creatures whose total hit points do not exceed 160 will be <i>stunned</i> and reeling for 3-12 (3d4) rounds, dropping anything it or they hold in manipulative members.\n\n"
            "The type of symbol cannot be recognized without it being read and thus activating its effects. The material components of this spell are powdered black opal and diamond dust worth not less than 5000 g.p. each."
        )
    ),
    Spell('Trap The Soul','M',8,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is similar to the <a href=\"/spells/magic-jar-magic-user-lvl-5/\"><i>magic jar</i></a>, except that the <i>trap the soul</i> spell forces the subject creature's life force (and its material body, if any) into a special prison magicked by the spell caster. The subject of the spell must be seen by the caster, and the magic-user must know the subject's true name as well when the final word is uttered. Preparatory to the actual casting of the <i>trap the soul</i>, the magic-user must prepare the soul prison, a gem of 1,000 g.p. value for every hit die or level of experience the creature whose soul is to be trapped possesses, i.e. it requires a gem of 10,000 g.p. value to trap a 10 hit dice (or 10th level) creature by placing an <a href=\"/spells/enchant-an-item-magic-user-lvl-6/\"><i>enchant an item</i></a> spell upon it and then placing a <a href=\"/spells/maze-magic-user-lvl-8/\"><i>maze</i></a> spell into the gem, thereby forming the prison for the soul to be trapped. There are 2 manners in which the soul of the victim can be imprisoned. The final word of the spell can be spoken when the creature is within spell range, but this entitles it to exercise its magic resistance (if any) and a saving throw versus magic as well, and if the latter is successful, the gem shatters. The second method of soul trapping is far more insidious, for it tricks the victim into accepting a trigger object inscribed with the final spell word which will automatically place the creature's soul into the trap. If this method is used, it will be necessary to name the triggering item when the prison gem is magicked. A <a href=\"/spells/antipathysympathy-magic-user-lvl-8/\"><i>sympathy</i></a> spell may be placed on the trigger item. As soon as the subject creature picks up or accepts the trigger item, its soul is automatically transferred to the gem. The gem prison will hold the soul trapped until time indefinite, or until it is broken and the soul is released, allowing the material body to reform. If the creature trapped is a powerful creature from another plane (and this could actually mean a character trapped by some inhabitant of another plane of existence when the character is not on the Prime Material Plane), it can be required to perform a service immediately upon being freed. Otherwise, the creature can go totally free once the gem imprisoning it is broken."
    ),
    Spell('Astral Spell','M',9,
        cast=tp(9,S),
        duration=tp(0),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the seventh level cleric spell, <a href=\"/spells/astral-spell-cleric-lvl-7/\"><i>astral spell</i></a>."
    ),
    Spell('Bigby\'s Crushing Hand','M',9,
        cast=tp(9,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("<i>Bigby's Crushing Hand</i> causes the appearance of a huge disembodied hand which is similar to <a href=\"/spells/bigbys-forceful-hand-magic-user-lvl-6/\"><i>Bigby's Forceful Hand</i></a> and <a href=\"/spells/bigbys-clenched-fist-magic-user-lvl-8/\"><i>Bigby's Clenched Fist</i></a>. The <i>Crushing Hand</i> is under the mental control of the caster, and he or she can cause it to grasp and squeeze an opponent. Damage from this constriction depends on the number of rounds it acts upon the victim:\n\n"
            "1st round: 1-10 hit points\n"
            "2nd & 3rd rounds: 2-20 hit points\n"
            "4th & beyond: 4-40 hit points\n\n"
            "The <i>hand</i> can sustain hit points equal to those of the magic-user who created it before being dispelled. The material components of the spell are a glove of snake skin and the shell of an egg."
        )
    ),
    Spell('Crystalbrittle','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=U,
        desc=("The dweomer of this spell causes metal, whether as soft as gold or as hard as adamantite, to turn to a crystalline substance as brittle and fragile as crystal. Thus a sword, metal shield, metal armor, or even iron golem can be changed to a delicate, glass-like material easily shattered by any forceful blow. Furthermore, this change is unalterable short of by means of a <a href=\"/spells/wish-magic-user-lvl-9/\"><i>wish</i></a> spell; i.e., <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> will not reverse the spell.\n\n"
            "The caster must physically touch the target item — equal to a hit in combat if the item is being worn or wielded, or is a monster. Any single metal item can be affected by the spell. Thus a suit of armor being worn by the subject can be changed to crystal, but the subject's shield would not be affected, or vice versa. All items gain a saving throw equal to their magical bonus value or protection. A +1/+3 sword would get a 10% (average of the two plusses) chance to save; +5 magic armor a 25% chance to be unaffected; an iron golem a 15% chance to save (for it is only hit by magic weapons of +3 or better quality). Artifacts and relics of metal have a 95% chance to be unaffected by the spell. Affected items not immediately protected will be shattered and permanently destroyed if struck by a normal blow from a metal tool or any weighty weapon, including a staff."
        )
    ),
    Spell('Energy Drain','M',9,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="By casting this spell, the magic-user opens a channel between the plane he or she is on and the Negative Material Plane, the caster becoming the conducter between the two planes. As soon as he or she touches (equal to a hit if melee is involved) any living creature, the victim loses two energy levels (as if struck by a spectre). A monster loses two hit dice permanently, both for hit points and attack ability. A character loses level, hit dice and hit points, and abilities permanently (until regained through adventuring, if applicable). The material component of this spell is essence of spectre or vampire dust. Preparation requires three segments, the material component is then cast forth, and upon touching the victim the magic-user speaks the triggering word, causing the dweomer to take effect instantly. There is always a 5% (1 in 20) chance that the caster will also be affected by the <i>energy drain</i> and lose one energy level at the same time the victim is drained of two. Humans or humanoids brought to zero energy level by this spell become <a href=\"/creatures/juju-zombie/\">juju zombies</a>."
    ),
    Spell('Gate','M',9,
        cast=tp(9,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the seventh level cleric spell, <a href=\"/spells/gate-cleric-lvl-7/\"><i>gate</i></a>."
    ),
    Spell('Imprisonment','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When an <i>imprisonment</i> spell is cast and the victim is touched, the recipient is entombed in a state of suspended animation (cf. <a href=\"/spells/temporal-stasis-magic-user-lvl-9/\"><i>temporal stasis</i></a>) in a small sphere far below the surface of the earth. The victim remains there unless a reverse of the spell, with the creature's name and background, is cast. Magical search by <i>crystal ball</i>, a <a href=\"/spells/locate-object-cleric-lvl-3/\"><i>locate objects</i></a> spell or similar means will not reveal the fact that a creature is <i>imprisoned</i>. The reverse (<i>freedom</i>) spell will cause the appearance of the victim at the spot he, she or it was entombed and sunk into the earth. There is a 10% chance that 1 to 100 other creatures will be freed from Imprisonment at the same time if the magic-user does not perfectly get the name and background of the creature to be freed. The spell only works if the name and background of the victim are known."
    ),
    Spell('Meteor Swarm','M',9,
        cast=tp(9,S),
        duration=tp(0),
        sourcebook=V,
        desc="A <i>meteor swarm</i> is a very powerful and spectacular spell which is similar to a <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a> in many aspects. When it is cast, either four spheres of 2' diameter or eight spheres of 1' diameter spring from the outstretched hand of the magic-user and streak in a straight line up to the distance demanded by the spell caster, up to the maximum range. Any creature in the straight line path of these missiles will receive the full effect of the missile, or missiles, without benefit of a saving throw. The \"meteor\" missiles leave a fiery trail of sparks, and each bursts as a <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>. The large spheres each do 10 to 40 hit points of damage, the four bursting in a diamond or box pattern. Each has a 3\" diameter area of effect, and each sphere will be 2\" apart, along the sides of the pattern, so that there are overlapping areas of effect, and the center will be exposed to all four blasts. The eight small spheres have one-half diameter (1½\") and one-half the damage potential (5-20). They burst in a pattern of a box within a diamond or vice versa, each of the outer sides 2\" long, and the inner sides being 1\" long. Note that the center will have 4 areas of overlapping effect, and there are numerous peripheral areas which have two overlapping areas of effect. A saving throw for each area of effect will indicate whether full hit points of damage, or half the indicated amount of damage, will be sustained by creatures within each area, except as already stated with regard to the missiles impacting."
    ),
    Spell('Monster Summoning VII','M',9,
        cast=tp(9,S),
        duration=tp(8,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell summons 1 or 2 seventh level monsters which appear 1 round after the spell is cast, or 1 8th level monster which will appear 2 rounds after the spell is cast. See <a href=\"/spells/monster-summoning-i-magic-user-lvl-3/\"><i>monster summoning I</i></a> for other details."
    ),
    Spell('Mordenkainen\'s Disjunction','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=U,
        desc=("When this spell is cast, all magic and/or magic items within the radius of the spell, except those on the person of or being touched by the spell caster, are <i>disjoined</i>. That is, spells being cast are separated into their individual components (usually spoiling the effect as does a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>), and <i>permanent</i> and magicked items must likewise save (versus spell if actually cast on a creature, or versus a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> otherwise) or be turned into normal items. Even artifacts and relics are subject to <i>Mordenkainen's Disjunction</i>, although there is only a 1% chance per level of the spell caster of actually affecting such powerful items. Thus, all potions, scrolls, rings, rods <i>et al</i>, miscellaneous magic items, artifacts and relics, arms and armor, swords and miscellaneous weapons within 3\" of the spell caster can possibly lose all their magical properties when <i>Mordenkainen's Disjunction</i> is cast.\n\n"
            "Note: Destroying artifacts is a dangerous business, and 95% likely to attract the attention of some powerful being who has an interest or connection with the device. Additionally, if an artifact is destroyed, the casting magic-user must save versus spell at -4 or permanently lose all spell casting abilities."
        )
    ),
    Spell('Power Word, Kill','M',9,
        cast=tp(1,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When a <i>power word, kill</i> is uttered, one or more creatures within the spell range and area of effect will be slain. The <i>power word</i> will destroy a creature with up to 60 hit points, or it will kill 2 or more creatures with 10 or fewer hit points, up to a maximum of 20 hit points. The option to attack a single creature, or multiple creatures, must be stated along with the spell range and area of effect center."
    ),
    Spell('Prismatic Sphere','M',9,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc=("This spell enables the magic-user to conjure up an opaque globe of shimmering, multi-colored spheres of light to surround him or her which give protection from all forms of attack. This scintillating sphere flashes all the seven colors of the visible spectrum, and each of these spheres of color has a different power and purpose. Any creature with fewer than eight hit dice will be blinded for from 2 to 8 turns by the colors of the sphere. This phenomenon is immobile and only the spell caster can pass in and out the <i>prismatic sphere</i> without harm. Note that typically the upper hemisphere of the globe will be visible, as the spell caster is at the center of the sphere, so the lower half is usually hidden by the floor surface he or she is standing upon. The colors and effects of the <i>prismatic sphere</i>, as well as what will negate each globe, are:\n\n"
            "<table>"
            "<tr><th>Color of Globe</th><th>Order of Globe</th><th>Effects of Globe</th><th>Spell Negated By</th></tr>"
            "<tr><td>red</td><td>1st</td><td>prevents all non-magical missiles — inflicts 10 hit points of damage</td><td><a href=\"/spells/cone-of-cold-magic-user-lvl-5/\"><i>cone of cold</i></a></td></tr>"
            "<tr><td>orange</td><td>2nd</td><td>prevents all magical missiles — inlficts 20 hit points of damage</td><td><a href=\"/spells/gust-of-wind-magic-user-lvl-3/\"><i>gust of wind</i></a></td></tr>"
            "<tr><td>yellow</td><td>3rd</td><td>prevents poisons, gasses, and petrification — inflicts 40 hit points of damage</td><td><a href=\"/spells/disintegrate-magic-user-lvl-6/\"><i>disintegrate</i></a></td></tr>"
            "<tr><td>green</td><td>4th</td><td>prevents all breath weapons — save vs. poison or dead</td><td><a href=\"/spells/passwall-magic-user-lvl-5/\"><i>passwall</i></a></td></tr>"
            "<tr><td>blue</td><td>5th</td><td>prevents location/detection and psionics — save vs. petrification or turned to stone</td><td><a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>magic missile</i></a></td></tr>"
            "<tr><td>indigo</td><td>6th</td><td>prevents all magical spells — save vs. wand or insane</td><td><a href=\"/spells/continual-light-cleric-lvl-3/\"><i>continual light</i></a></td></tr>"
            "<tr><td>violet</td><td>7th</td><td>force field protection — save vs. magic or sent to another plane</td><td><a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a></td></tr>"
            "</table>\n\n"
            "Note that a <i>rod of cancellation</i> will destroy a <i>prismatic sphere</i>. Otherwise, anything entering the sphere will be destroyed, any creature subject to the effects of each and every globe as indicated, i.e. 70 hit points of damage plus death, petrification, insanity, and/or instantaneous transportation to another plane, and only the four latter effects are subject to saving throws. The individual globes may be destroyed by appropriate magical attacks in consecutive order, the 1st globe destroyed before any others, then the 2nd, etc."
        )
    ),
    Spell('Shape Change','M',9,
        cast=tp(9,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="With this spell, the magic-user is able to assume the form of any creature short of a demi-god, greater devil, demon prince, singular dragon type, greater demon or the like. The spell caster becomes the creature he or she wishes, and has all of the abilities save those dependent upon intelligence, for the mind of the creature is that of the spell caster. Thus, he or she can change into a griffon, thence to an efreet, and then to a titan, etc. These creatures have whatever hit points the magic-user has at the time of the <i>shape change</i>. Each alteration in form requires 1 segment. No system shock is incurred. Example: A wizard is in combat and assumes the form of a will o' wisp, and when this form is no longer useful, the wizard changes into a stone golem and walks away. When pursued, the golem-shape is changed to that of a flea, which hides upon a horse until it can hop off and become a bush. If detected as the latter, the magic-user can become a dragon, pool of water, or just about anything else. The material component of the spell is a jade circlet worth no less than 5000 g.p. which will shatter at the expiration of the magic's duration. In the meantime it is left in the wake of the <i>shape change</i>, and premature shattering will cause the magic to be dispelled."
    ),
    Spell('Succor','M',9,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U,
        desc="This spell is essentially the same as the <a href=\"/spells/succor-cleric-lvl-7/\">7th-level cleric spell</a> of the same name. A <i>succor</i> spell cast by a magic-user will <a href=\"/spells/teleport-without-error-magic-user-lvl-7/\"><i>teleport without error</i></a> the individual breaking the object and speaking the command word. If the reverse is used, the archmage is likewise brought to the presence of the individual. Unlike the cleric spell of the same name (qv), the summoned archmage has no choice than to answer the summons, making this version of the spell rare indeed. Intervening planes have only a 1% chance each, cumulative, of causing irrevocable loss of the individual or spell caster involved in the <i>succor</i>. The material component used must be gem material of not less than 5,000 gp value; whether it is a faceted gem or not is immaterial. The components can only be enchanted once per month (usually on the night of a clear, full moon). At that time, the object is \"set\" for the type of <i>succor</i> and its final destination (either the location of the spell casting or an area well known to the mage)."
    ),
    Spell('Temporal Stasis','M',9,
        cast=tp(9,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Upon casting this spell, the magic-user places the recipient creature into a state of suspended animation. This cessation of time means that the creature does not grow older. Its body functions virtually cease. This state persists until the magic is removed by a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell or the reverse of the spell (<i>temporal reinstatement</i>) is uttered. Note that the reverse requires only a single word and no somatic or material components. The material component of a <i>temporal stasis</i> spell is a powder composed of diamond, emerald, ruby, and sapphire dust, one stone of each type being required."
    ),
    Spell('Time Stop','M',9,
        cast=tp(9,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Upon casting a <i>time stop</i> spell, the magic-user causes the flow of time to stop in the area of effect, and outside this area the sphere simply seems to shimmer for an instant. During the period of spell duration, the magic-user can move and act freely within the area where time is stopped, but all other creatures there are frozen in their actions, for they are literally between ticks of the time clock, and the spell duration is subjective to the caster. No creature can enter the area of effect without being stopped in time also, and if the magic-user leaves it, he or she immediately negates the spell. When spell duration ceases, the magic-user will again be operating in normal time."
    ),
    Spell('Wish','M',9,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The <i>wish</i> spell is a more potent version of a <a href=\"/spells/limited-wish-magic-user-lvl-7/\"><i>limited wish</i></a>. If it is used to alter reality with respect to hit points sustained by a party, to bring a dead character to life, or to escape from a difficult situation by lifting the spell caster (and his or her party) from one place to another, it will not cause the magic-user any disability. Other forms of wishes, however, will cause the spell caster to be weak (-3 on strength) and require 2 to 8 days of bed rest due to the stresses the <i>wish</i> places upon time, space, and his or her body. Regardless of what is wished for, the exact terminology of the <i>wish</i> spell is likely to be carried through. (This discretionary power of the referee is necessary in order to maintain game balance. As wishing another character dead would be grossly unfair, for example, your DM might well advance the spell caster to a future period where the object is no longer alive, i.e. putting the wishing character out of the campaign.)"
    )
]

illusionist_spells = [
    Spell('Audible Glamer','I',1,
        cast=tp(5,S),
        duration_lvl=tp(3,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the second level magic-user spell, <a href=\"/spells/audible-glamer-magic-user-lvl-2/\"><i>audible glamer</i></a>."
    ),
    Spell('Change Self','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell enables the illusionist to alter the appearance of his or her form — including clothing and equipment — to appear 1' shorter or taller; thin, fat, or in between; human, humanoid, or any other generally man-shaped bipedal creature. The duration of the spell is 2 to 12 (2d6) rounds base plus 2 additional rounds per level of experience of the spell caster."
    ),
    Spell('Chromatic Orb','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("The <i>chromatic orb</i> spell enables the illusionist to create a small globe of varying hue in his or her hand and hurl it at any opponent he or she desires, providing there are no barriers between the illusionist and the target creature, and that the target creature is within 3\" (the longest distance the chromatic orb can be hurled). It is magical, and even creatures normally struck only by +5, +4, etc. magic weapons will be affected by the <i>chromatic orb</i> if it strikes. Magic resistance withstands this spell, of course. At 1\" or closer, there is a +3 chance \"to hit\", at over 1\" to 2\" there is a +2 chance to strike the target, and from over 2\" to the maximum 3\" range the chance \"to hit\" is only +1. If a <i>chromatic orb</i> misses a target, it dissipates without further effect. The color of the globe determines its effect when a subject is struck. Low-level illusionists are restricted as to what color orb they can bring into existence by means of this spell, although the hues below their level are always available should the choice be made to select a color not commensurate with level of experience. Colors and effects are shown on the table below.\n\n"
            "<table>"
            "<tr><th>Minimum Level of Caster</th><th>Color of Orb Generated</th><th>Hit Points of Damage</th><th>Special Powers</th></tr>"
            "<tr><td>1st</td><td>Pearly</td><td>1-4</td><td>light<sup>1</sup></td></tr>"
            "<tr><td>2nd</td><td>Ruby</td><td>1-6</td><td>heat<sup>2</sup></td></tr>"
            "<tr><td>3rd</td><td>Flame</td><td>1-8</td><td>fire<sup>3</sup></td></tr>"
            "<tr><td>4th</td><td>Amber</td><td>1-10</td><td>blindness<sup>4</sup></td></tr>"
            "<tr><td>5th</td><td>Emerald</td><td>1-12</td><td>stinking cloud<sup>5</sup></td></tr>"
            "<tr><td>6th</td><td>Turquoise</td><td>2-16</td><td>magnetism<sup>6</sup></td></tr>"
            "<tr><td>7th</td><td>Sapphire</td><td>2-8</td><td>paralysis<sup>7</sup></td></tr>"
            "<tr><td>10th</td><td>Amethyst</td><td>(slow)</td><td>petrification<sup>8</sup></td></tr>"
            "<tr><td>12th</td><td>Ashen</td><td>(paralysis)</td><td>death<sup>9</sup></td></tr>"
            "</table>\n\n"
            "Notes on special powers:\n"
            "1: Light equal to a <a href=\"/spells/light-cleric-lvl-1/\"><i>light</i></a> spell will be generated and persist for 1 round/level of the caster, and any subject failing to save versus spell will be blinded for the duration.\n"
            "2: Heat from the ruby orb will melt up to 1 cubic yard of ice, and creatures not saving versus spell will suffer a loss of 1 point of strength and 1 point of dexterity (or -1 \"to hit\" and AC) for 1 round following being struck by the orb.\n"
            "3: Fire from the orb will set aflame all combustibles within a 1' radius of the target, and unless the target saves versus spell an additional 2 points of fire damage will be suffered (except when protected from fire by magical or natural means).\n"
            "4: The target subject will suffer blindness for 5-8 rounds unless a successful saving throw versus spell is made (<a href=\"/spells/cure-blindness-cleric-lvl-3/\"><i>cure blindness</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> negates this effect).\n"
            "5: A magical <a href=\"/spells/stinking-cloud-magic-user-lvl-2/\"><i>stinking cloud</i></a> of 5' radius (around the target) is created when a successful hit is made, and the subject must save versus poison or else be helpless, and in any event will be helpless until leaving the area of the vapors (cf. <a href=\"/spells/stinking-cloud-magic-user-lvl-2/\"><i>stinking cloud</i></a> spell).\n"
            "6: The turquoise orb inflicts electrical damage, and if the target is wearing ferrous metal it will be magnetized for 3-12 rounds unless a saving throw versus spell is successful. Magnetized metal will stick fast to other magnetized metal items, and non-magnetized ferrous metal items will cling until pulled free.\n"
            "7: Unless a saving throw versus paralyzation is made, the subject creature will be paralyzed for 5-20 rounds.\n"
            "8: The subject creature will be turned to stone unless a saving throw versus petrification is made, and even if the save is made, the subject will be slowed for 2-8 rounds (cf. <a href=\"/spells/slow-magic-user-lvl-3/\"><i>slow</i></a> spell).\n"
            "9: The subject creature will die unless a successful saving throw versus death magic is made, and even if a save is made, the subject will be paralyzed for 2-5 rounds.\n\n"
            "The material component of the spell is a gem of the appropriate hue, or else a clear crystal one (such as a diamond). The gem can be as small (in value) as 50 gold pieces as long as its color is appropriate."
        )
    ),
    Spell('Color Spray','I',1,
        cast=tp(1,S),
        duration=tp(1,S),
        sourcebook=V,
        desc="Upon casting this spell, the illusionist causes a vivid fan-shaped spray of clashing colors to spring forth from his or her hand. From 1 to 6 creatures within the area of effect can be affected. The spell caster is able to affect 1 level or hit die of creatures for each of his or her levels of experience. Affected creatures are struck unconscious for 2 to 8 rounds if their level is less than or equal to that of the spell caster; they are blinded for 1 to 4 rounds if their level or number of hit dice is 1 or 2 greater than the illusionist; and they are stunned (cf. <a href=\"/spells/power-word-stun-magic-user-lvl-7/\"><i>power word, stun</i></a>, seventh level magic-user spell) for 2 to 8 segments if their level or number of hit dice is 3 or more greater than the spell caster. All creatures above the level of the spell caster and all creatures of 6th level or 6 hit dice are entitled to a saving throw versus the <i>color spray</i> spell. The material components of this spell area pinch each of powder or sand colored red, yellow and blue."
    ),
    Spell('Dancing Lights','I',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="This spell is the same as the first level magic-user spell, <a href=\"/spells/dancing-lights-magic-user-lvl-1/\"><i>dancing lights</i></a>."
    ),
    Spell('Darkness','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the second level magic-user spell of <a href=\"/spells/darkness-15-radius-magic-user-lvl-2/\"><i>darkness</i></a>."
    ),
    Spell('Detect Illusion','I',1,
        cast=tp(1,S),
        duration=tp(3,R),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="By means of this spell the illusionist is able to see an illusion and know it for exactly that. Note that it can be used to enable others to see illusions as unreal if the spell caster touches the creature with both hands and the creature looks at the illusion while so touched. The material component is a piece of yellow tinted crystal, glass, or mica."
    ),
    Spell('Detect Invisibility','I',1,
        cast=tp(1,S),
        duration_lvl=tp(5,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the second level magic-user spell, <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detect invisibility</i></a>."
    ),
    Spell('Gaze Reflection','I',1,
        cast=tp(1,S),
        duration=tp(1,R),
        sourcebook=V,
        desc="The <i>gaze reflection</i> spell creates a mirror-like area of air before the illusionist. Any gaze attack, such as that of a basilisk or a medusa, will be reflected back upon the gazer if it looks upon the spell caster."
    ),
    Spell('Hypnotism','I',1,
        cast=tp(1,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="The gestures of the illusionist, along with his or her droning incantation, cause from 1 to 6 creatures to become susceptible to <i>suggestion</i> (see the third level magic-user <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a> spell). The <i>suggestion</i> must be given after the <i>hypnotism</i> spell is cast, and until that time the success of the spell is unknown. Note that the subsequent <i>suggestion</i> is not a spell, but simply a vocalized urging. Creatures which make their saving throw are not under hypnotic influence."
    ),
    Spell('Light','I',1,
        cast=tp(1,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="This spell is the same as the first level magic-user <a href=\"/spells/light-magic-user-lvl-1/\"><i>light</i></a> spell (cf. first level cleric <a href=\"/spells/light-cleric-lvl-1/\"><i>light</i></a> spell.)"
    ),
    Spell('Phantasmal Force','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level magic-user spell, <a href=\"/spells/phantasmal-force-magic-user-lvl-3/\"><i>phantasmal force</i></a>."
    ),
    Spell('Phantom Armor','I',1,
        cast=tp(1,R),
        duration=tp(1,P),
        sourcebook=U,
        desc="When this spell is cast, the illusionist creates a quasi-real suit of plate mail. This semi-illusory material covers the subject and actually gives some real protection unless the opponent actively disbelieves in the armor (saves versus spell), or else a <a href=\"/spells/dispel-illusion-illusionist-lvl-3/\"><i>dispel illusion</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell is cast upon it, or a <i>wand of negation</i> affects it. Until gone, or disbelieved, the armor protects the wearer as if he or she were in plate mail (AC 3, and armor type 3 as well). For each level of the spell caster, the <i>phantom armor</i> will absorb 1 point of damage delivered by a blow which would otherwise hit armor class 3. When the <i>phantom armor</i> has absorbed as many points of damage as the spell caster has levels of experience, it is dispelled and vanishes. Any remaining and all additional damage accrues to the person. Additionally, <i>phantom armor</i> allows a bonus of +1 on saving throws versus all attack forms which would be similarly modified by magic armor. The dweomer in no way affects the movement or spell-casting abilities of the wearer. It is not subject to rust monster attack (and such may enhace disbelief). The spell will not function with any other form of magical protection. The material component is a small plate of mithral (10 gp value) which disappears when the spell is cast."
    ),
    Spell('Read Illusionist Magic','I',1,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=U,
        desc="This spell is the same as the 1st level magic-user spell <a href=\"/spells/read-magic-magic-user-lvl-1/\"><i>read magic</i></a>, except that it applies only to spells usable by and used by illusionists, as well as to various other inscriptions written in illusionist-type magic script by illusionists."
    ),
    Spell('Spook','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="A <i>spook</i> spell enables the illusionist to play upon natural fears to cause the subject creature to perceive the spell caster as someone or something inimical. Without actually knowing what this is, the illusionist merely advances threateningly upon the subject, and if a successful saving throw versus spell is not made, the creature will react by rapidly turning and fleeing in as opposite a direction from the illusionist as possible (effects as a <i>wand of fear</i>, though items carried are not dropped). Although the spell caster does not actually pursue the fleeing creature, a phantasm from its own mind will do so. However, each round after the initial casting of the <i>spook</i> spell the creature is entitled to another saving throw, and each such saving throw is at a cumulative +1 per round, until the subject sucessfully saves versus spell and the spell is broken. In any event, the spell will function only against creatures with intelligence of not less than 1."
    ),
    Spell('Wall of Fog','I',1,
        cast=tp(1,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="By casting this spell. the illusionist creates a wall of misty vapors in whatever area within the spell range he or she desires. The <i>wall of fog</i> obscures all sight normal and/or infravisual, beyond 2'. The area of effect is a cube of 2\" per side per level of experience of the spell caster. The misty vapors persist for 3 or more rounds unless blown away by a strong breeze (cf. <a href=\"/spells/gust-of-wind-magic-user-lvl-3/\"><i>gust of wind</i></a>). The material component is a pinch of split dried peas."
    ),
    Spell('Alter Self','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        duration_lvl=tp(2,R),
        sourcebook=U,
        desc="When this spell is cast the illusionist is able to alter himself or herself in a manner similar to a <a href=\"/spells/change-self-illusionist-lvl-1/\"><i>change self</i></a> spell. However, <i>alter self</i> enables the caster to effect a quasi-real change, so that size can be altered by 50% of actual. If the form selected has wings, the illusionist can actually fly, but only at one-quarter the rate of speed of a true creature of that type, and with a loss of two Maneuverability Classes (to a minimum of \"E\"). If the form has gills, he can breathe underwater as long as the spell lasts. Using <i>alter self</i> to change into a larger creature does not permit additional attacks or damage unless the illusionist is accustomed to this form."
    ),
    Spell('Blindness','I',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>blindness</i> spell causes the recipient creature to become blind and able to see only a greyness before its eyes. Various <i>cure</i> spells will not remove this effect, and only a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> or the spell caster can do away with the blindness if the creature fails its initial saving throw versus the spell."
    ),
    Spell('Blur','I',2,
        cast=tp(2,S),
        duration=tp(3,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When a <i>blur</i> spell is cast, the illusionist causes the outline of his or her form to become blurred, shifting and wavery. This distortion causes all missile and melee combat attacks to be made at -4 on the first attempt and -2 on all successive attacks. It alto allows a +1 on the saving throw die roll for any direct magical attack."
    ),
    Spell('Deafness','I',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>deafness</i> spell causes the recipient creature to become totally deaf and unable to hear any sounds (cf. <a href=\"/spells/blindness-illusionist-lvl-2/\"><i>blindness</i></a>). This <i>deafness</i> can be done away with only by means of a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> or by the spell caster. The victim is allowed a saving throw. The material component of the spell is beeswax."
    ),
    Spell('Detect Magic','I',2,
        cast=tp(2,S),
        duration_lvl=tp(2,R),
        sourcebook=V,
        desc="This spell is similar to the first level cleric and the first level magic-user spell, <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a>."
    ),
    Spell('Fascinate','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="By means of this spell the illusionist attempts to captivate the subject creature's attention and gain its love, friendship and/or obedience. The spell creates an illusion around the spell caster so that he or she becomes, in the eyes of the subject, a trusted and/or desired companion. Unless a saving throw versus spell is successful, the subject will follow the illusionist wherever he or she goes, if possible without undue risk to life and safety. If the illusionist is able to converse with the <i>fascinated</i> creature, the subject will obey requests from the spell caster as long as a roll of 3d6 per request does not exceed the comeliness of the illusionist. (Requests which are obviously against the better interests of the creature add +1 to the dice roll, and the more hazardous and unreasonable of these requestse will add from +2 to +6 to the dice roll.) The spell is shattered whenever comeliness is exceeded, and the subject will certainly be filled with rage and hate. Creatures of normal sort with animal intelligence will remain <i>fascinated</i> for only a short period of time (1-4 days), but if the illusionist has been careful to treat the subject well, attend to its needs, and feed it, there is a 2% chance per point of comeliness of the illusionist that the subject will willingly choose to befriend and follow him or her. Otherwise, the creature will attack (if it was not cared for) or leave (if it was cared for) when the spell wears off. Non-intelligent creatures are not subject to a <i>fascinate</i> spell (cf. <a href=\"/spells/charm-person-or-mammal-druid-lvl-2/\"><i>charm person</i></a>)."
    ),
    Spell('Fog Cloud','I',2,
        cast=tp(2,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="The <i>fog cloud</i> is a billowing mass of misty vapors which is of similar appearance to a <a href=\"/spells/cloudkill-magic-user-lvl-5/\"><i>cloudkill</i></a>, the fog being greenish. The spell caster creates the <i>fog cloud</i> and it moves away from him or her at a 1\" per round rate. Although it behaves in most respects just as if it were a <a href=\"/spells/cloudkill-magic-user-lvl-5/\"><i>cloudkill</i></a>, the only effect of the fog is to obscure vision, just as a <a href=\"/spells/wall-of-fog-illusionist-lvl-1/\"><i>wall of fog</i></a> does."
    ),
    Spell('Hypnotic Pattern','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="When this spell is cast the illusionist creates a weaving, turning pattern of subtle colors in the air. This <i>hypnotic pattern</i> will cause any creature looking at it to become fascinated and stand gazing at it as long as the spell caster continues to maintain the shifting interplay of glowing lines. Note that the spell can captivate a maximum of 24 levels, or hit dice, of creatures, i.e. 24 creatures with 1 hit die each, 12 with 2 hit dice, etc. All creatures affected must be within the area of effect, and each is entitled to a saving throw. The illusionist need not utter a sound. but he or she must gesture appropriately while holding a glowing stick of incense or a crystal rod filled with phosphorescent material."
    ),
    Spell('Improved Phantasmal Force','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, and as detailed hereafter, this spell is the same as the third level magic-user <a href=\"/spells/phantasmal-force-magic-user-lvl-3/\"><i>phantasmal force</i></a> spell. The spell caster can maintain the illusion with minimal concentration. i.e. he or she can move at half normal speed (but not cast other spells). Some minor sounds are included in the effects of the spell, but not understandable speech. Also, by concentration on the form of the phantasm, the <i>improved phantasmal force</i> will continue for 2 rounds after the illusionist ceases to concentrate upon the spell."
    ),
    Spell('Invisibility','I',2,
        cast=tp(2,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the second level magic-user spell, <a href=\"/spells/invisibility-magic-user-lvl-2/\"><i>invisibility</i></a>."
    ),
    Spell('Magic Mouth','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell is the same as the second level magic-user <a href=\"/spells/magic-mouth-magic-user-lvl-2/\"><i>magic mouth</i></a> spell."
    ),
    Spell('Mirror Image','I',2,
        cast=tp(2,S),
        duration_lvl=tp(3,R),
        sourcebook=V,
        desc="Except as noted above, and except for the fact that there are 2-5 (d4 + 1) <i>mirror images</i> created, this spell is the same as the second level magic-user spell, <a href=\"/spells/mirror-image-magic-user-lvl-2/\"><i>mirror image</i></a>."
    ),
    Spell('Misdirection','I',2,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell the illusionist misdirects the information from a detection-type spell, i.e. <a href=\"/spells/detect-charm-cleric-lvl-2/\"><i>detect charm</i></a>, <a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect evil</i></a>, <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detect invisibility</i></a>, <a href=\"/spells/detect-lie-cleric-lvl-4/\"><i>detect lie</i></a>, <a href=\"/spells/detect-magic-cleric-lvl-1/\"><i>detect magic</i></a> and <a href=\"/spells/detect-snares-pits-druid-lvl-1/\"><i>detect snares & pits</i></a>. While the detection spell functions, the information it reveals will indicate the wrong area, creature. or the opposite of the truth with respect to <a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect evil</i></a> or <a href=\"/spells/detect-lie-cleric-lvl-4/\"><i>detect lie</i></a>. The illusionist directs the spell effect upon the creature or item which is the object of the detection spell. If the caster of the detection-type spell fails his or her saving throw, the <i>misdirection</i> takes place."
    ),
    Spell('Ultravision','I',2,
        cast=tp(2,S),
        duration=tp(6,T),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="Except as noted above, this spell is essentially the same as the <a href=\"/spells/ultravision-magic-user-lvl-4/\">4th-level magic-user spell</a> of the same name. Note additionally that creatures with high intelligence might be able to <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detect invisible</i></a> creatures by the use of ultravision, either natural or magically bestowed. The required material component for the illusionist version of this spell is a powdered essence of carrots."
    ),
    Spell('Ventriloquism','I',2,
        cast=tp(2,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the first level magic-user spell, <a href=\"/spells/ventriloquism-magic-user-lvl-1/\"><i>ventriloquism</i></a>."
    ),
    Spell('Whispering Wind','I',2,
        cast=tp(2,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="By means of this spell the illusionist is able to either send a message or cause some desired sound effect. The <i>whispering wind</i> can be prepared to travel as many tens of feet underground or miles above ground as the spell caster has levels of experience. Thus, a 3rd-level illusionist could send the spell wafting 30' in a dungeon or as far as three miles outdoors. The <i>whispering wind</i> will be as gentle and unnoticed as a zephyr until it reaches the desired objective of the spell caster. It then delivers its whisper-quiet message or other sound for a duration of up to two segments. The dweomer then fades and vanishes — as it will do if the subject is beyond range, or more than two hours of time have elapsed, or it is magically dispelled. The illusionist can prepare the spell to bear a message of up to 12 words, cause the spell to deliver other sounds for 12 seconds, or merely have the <i>whispering wind</i> seem to be a faint stirring of the air which has a susurrant sound. He or she can likewise cause the <i>whispering wind</i> to move as slowly as 1\" per round or as quickly as 20\" (or any rate in between). When the spell reaches its objective, it swirls and remains for the full two segments, regardless of its speed otherwise. As with the <a href=\"/spells/magic-mouth-magic-user-lvl-2/\"><i>magic mouth</i></a> spell, no spells may be cast through the <i>whispering wind</i>."
    ),
    Spell('Continual Darkness','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="When this spell is cast, a globe of impenetrable darkness is created. The effects of this darkness, as well as the material component of the spell, are the same as the second level magic-user spell, <a href=\"/spells/darkness-15-radius-magic-user-lvl-2/\"><i>darkness, 15' radius</i></a> (cf. <a href=\"/spells/continual-light-cleric-lvl-3/\"><i>continual light</i></a>)."
    ),
    Spell('Continual Light','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell is the same as the second level cleric <a href=\"/spells/continual-light-cleric-lvl-3/\"><i>continual light</i></a> spell, except as noted above."
    ),
    Spell('Delude','I',3,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="By means of a <i>delude</i> spell, the illusionist is able to replace the aura of his or her own alignment with that of any other creature within a 3\" radius, although the creature must be of higher than animal intelligence for the aura exchange to work. The target creature retains his or her original alignment. Any attempt to <a href=\"/spells/know-alignment-cleric-lvl-2/\"><i>know alignment</i></a> will discover only the aura (alignment) which the illusionist has opted to assume. A <a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect good</i></a> or <a href=\"/spells/detect-evil-cleric-lvl-1/\"><i>detect evil</i></a> will detect this only of the subsituted creature's aura. The creature whose aura has been copied will radiate magic, but the illusionist will radiate magic only to the creature whose aura has been exchanged. If <i>delude</i> is used in conjunction with a <a href=\"/spells/change-self-illusionist-lvl-1/\"><i>change self</i></a> or <a href=\"/spells/alter-self-illusionist-lvl-2/\"><i>alter self</i></a> spell, the actual class of the illusionist will be totally hidden, and he or she will absolutely appear to be whatever class he or she has chosen to appear as, for a saving throw (versus spell) applies only to the aura transfer."
    ),
    Spell('Dispel Illusion','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="By means of this spell, the spell caster can dispel any <a href=\"/spells/phantasmal-force-magic-user-lvl-3/\"><i>phantasmal force</i></a> — with or without <a href=\"/spells/audible-glamer-magic-user-lvl-2/\"><i>audible glamer</i></a> — cast by a non-illusionist; and the spell has the same chance of dispelling any illusion/phantasm spells at another illusionist as a <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell does, i.e. 50% base chance adjusted by 2% downward, or 5% upward for each level of experience lesser/greater of the illusionist casting the <i>dispel illusion</i> compared to the illusionist casting the spell to be dispelled."
    ),
    Spell('Fear','I',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the fourth level magic-user spell, <a href=\"/spells/fear-magic-user-lvl-4/\"><i>fear</i></a>."
    ),
    Spell('Hallucinatory Terrain','I',3,
        cast=tp(5,R),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the fourth level magic-user <a href=\"/spells/hallucinatory-terrain-magic-user-lvl-4/\"><i>hallucinatory terrain</i></a> spell."
    ),
    Spell('Illusionary Script','I',3,
        cast=tp(1,VA),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell enables the illusionist to write instructions or other information on parchment, paper, skin, etc. The <i>illusionary script</i> appears to be some form of foreign or magical writing. Only the person (or class of persons or whatever} whom the illusionist desires to read the writing will be able to do so, although another illusionist will recognize it for <i>illusionary script</i>. Others attempting to read it will become confused as from a <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> spell for 5 to 20 turns, minus 1 turn for each level of experience he or she has attained. The material component of the spell is a lead-based ink which requires special manufacture by an alchemist."
    ),
    Spell('Invisibility 10\' Radius','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level magic-user spell, <a href=\"/spells/invisibility-10-radius-magic-user-lvl-3/\">invisibility, 10' radius</i></a>. See also the second level magic-user spell, <a href=\"/spells/invisibility-magic-user-lvl-2/\"><i>invisibility</i></a>."
    ),
    Spell('Non-detection','I',3,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="By casting this spell, the illusionist makes himself or herself invisible to divination spells such as <a href=\"/spells/clairaudience-magic-user-lvl-3/\"><i>clairaudience</i></a>, <a href=\"/spells/clairvoyance-magic-user-lvl-3/\"><i>clairvoyance</i></a>, <i>\"detects\"</i>, and <a href=\"/spells/esp-magic-user-lvl-2/\"><i>ESP</i></a>. It also prevents location by such magic items as <i>crystal balls</i> and <i>ESP medallions</i>. The material component of the spell is a pinch of diamond dust."
    ),
    Spell('Paralyzation','I',3,
        cast=tp(3,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="The <i>paralyzation</i> spell enables the spell caster to create illusionary muscle slowdown in creatures whose combined hit dice do not exceed twice the total level of experience of the illusionist. If the recipient creatures fail their saving throws, they become paralyzed, and a <a href=\"/spells/dispel-illusion-illusionist-lvl-3/\"><i>dispel illusion</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell must be used to remove the effect, or the illusionist may dispel it at anytime he or she desires."
    ),
    Spell('Phantom Steed','I',3,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc=("When this spell is cast the illusionist creates a quasi-real, horse-like creature. This creature can be ridden only by the illusionist who created it, or by any person for whom the illusionist creates such a mount specifically. All <i>phantom steeds</i> have black heads and bodies with gray manes and tails, and smoke-colored, insubstantial hooves which make no sound. Their eyes are milky-colored. They do not fight, but all normal animals shun them, so only monstrous ones will attack. If more than 12 points of damage accrue to such a mount, the dweomer is dispelled and the <i>phantom steed</i> disappears. A <i>phantom steed</i> moves at a maximum rate of 4\" per level of the spell caster. It has what seems to be a saddle and a bit and bridle, but it can not carry saddlebags and the like — only its rider and what he or she carries. These mounts gain certain powers according to the level of the illusionist who created them:\n\n"
            "8th level: Ability to pass over sandy, muddy, or even swampy ground without difficulty.\n\n"
            "10th level: Ability to pass over water as if it were firm, dry ground.\n\n"
            "12th level: Ability to travel in the air as if it were firm land instead, so chasms and the like can be crossed without benefit of a bridge. Note, however, that the mount can not casually take off and fly.\n\n"
            "14th level: Ability to perform as if it were a pegasus."
        )
    ),
    Spell('Phantom Wind','I',3,
        cast=tp(3,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When this spell is employed, the illusionist creates a wind which cannot be seen or felt. This movement of air does, however, serve to blow light objects before it, flutter curtains or drapes, flap loose clothing (such as capes, cloaks, and mantles), fan fires, and move clouds of gaseous materials (such as a <a href=\"/spells/wall-of-fog-illusionist-lvl-1/\"><i>wall of fog</i></a>, a <a href=\"/spells/fog-cloud-illusionist-lvl-2/\"><i>fog cloud</i></a>, a <a href=\"/spells/cloudkill-magic-user-lvl-5/\"><i>cloudkill</i></a> cloud, etc.). The wind created moves in the direction in which the illusionist points, its effects being felt in a progressively longer path as the spell continues, at a movement rate of 1\" per round, with the effects lasting the entire course of the path. Thus, the spell could, for example, be employed to move several sailed vessels, but the first affected by the wind would also be the one to move the farthest."
    ),
    Spell('Rope Trick','I',3,
        cast=tp(3,S),
        duration_lvl=tp(2,T),
        sourcebook=V,
        desc="This spell is the same as the second level magic-user spell, <a href=\"/spells/rope-trick-magic-user-lvl-2/\"><i>rope trick</i></a>."
    ),
    Spell('Spectral Force','I',3,
        cast=tp(3,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The <i>spectral force</i> spell creates an illusion in which sound, smell and thermal illusions are included. It is otherwise similar to the second level <a href=\"/spells/improved-phantasmal-force-illusionist-lvl-2/\"><i>improved phantasmal force</i></a> spell. The spell will last for 3 rounds after concentration."
    ),
    Spell('Suggestion','I',3,
        cast=tp(3,S),
        duration=tp(0),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the third level magic-user spell, <a href=\"/spells/suggestion-magic-user-lvl-3/\"><i>suggestion</i></a>."
    ),
    Spell('Wraithform','I',3,
        cast=tp(1,S),
        duration_lvl=tp(2,R),
        sourcebook=U,
        desc="When this spell is cast, the illusionist and all of his or her gear become insubstantial. The caster can be hit only by magic weapons of +1 or better, or by creatures otherwise able to affect those struck only by magic weapons. Undead of most sorts will ignore an individual in <i>wraithform</i>, believing him or her to be a wraith or spectre, though a lich or \"special\" undead may save versus spell at -4 to recognize the dweomer. The illusionist will be able to pass through small holes or narrow openings, even mere cracks, with all he or she wears or holds in his or her hands, as long as the spell persists. No form of attack is possible when in <i>wraithform</i>, except against creatures which exist on the Ethereal Plane, where all attacks (both ways) are normal. <a href=\"/spells/dispel-illusion-illusionist-lvl-3/\"><i>Dispel illusion</i></a> and <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> are the only ways to force an illusionist in <i>wraithform</i> back to normal form. The spell caster can return to normal form at will, but this ends the spell effect. The material components for this spell are a bit of gauze and a wisp of smoke."
    ),
    Spell('Confusion','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the fourth level magic-user <a href=\"/spells/confusion-magic-user-lvl-4/\"><i>confusion</i></a> spell. See also the seventh level druid <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> spell."
    ),
    Spell('Dispel Exhaustion','I',4,
        cast=tp(4,S),
        duration_lvl=tp(3,T),
        sourcebook=V,
        desc="By means of this spell, the illusionist is able to restore 50% of lost hit points to all persons (humans, demi-humans and humanoids) he or she touches during the round it is cast, subject to a maximum of four persons. The spell gives the illusion to the person touched that he or she is fresh and well. Stamina is renewed, but when the spell duration expires, the recipient drops back to their actual hit point strength. The spell will allow recipients to move at double speed for 1 round every turn (cf. <a href=\"/spells/haste-magic-user-lvl-3/\"><i>haste</i></a> spell)."
    ),
    Spell('Dispel Magic','I',4,
        cast=tp(4,S),
        duration=tp(1,P),
        sourcebook=U,
        desc="This spell is essentially identical to the <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>3rd-level clerical spell</i></a> of the same name. An illusionist casts this spell as if he or she were two levels below actual, i.e. a 9th-level illusionist casts a <i>dispel magic</i> as if he or she were of 7th level."

    ),
    Spell('Emotion','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("When this spell is cast, the illusionist can project his or her choice of 1 of the following 4 emotions:\n\n"
            "1. <i>Fear</i>: This is the same as the <a href=\"/spells/fear-magic-user-lvl-4/\">spell of the same name</a>, but as it is not illusionary, the saving throw is made at -2. It counters/is countered by <i>rage</i>.\n\n"
            "2. <i>Hate</i>: The effect of <i>hate</i> is to raise morale, saving throw dice, \"to hit\" dice, and damage done by +2. It counters/is countered by <i>hopelessness</i>.\n\n"
            "3. <i>Hopelessness</i>: This has the same effect as the <a href=\"/spells/symbol-cleric-lvl-7/\"><i>hopelessness</i> symbol</a>. It counters/is countered by <i>hate</i>.\n\n"
            "4. <i>Rage</i>: The <i>rage</i> emotion causes the recipient to become berserk, attack at a +1 on the \"to hit\" dice, do +3 hit points of damage, and gives a temporary +5 hit points to the enraged creature. The recipient will fight without shield, and regardless of life as well. It counters/is countered by <i>fear</i>.\n\n"
            "The spell lasts as long as the illusionist continues to concentrate on projecting the chosen <i>emotion</i>"
        )
    ),
    Spell('Improved Invisibility','I',4,
        cast=tp(4,S),
        duration=tp(4,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is similar to <a href=\"/spells/invisibility-magic-user-lvl-2/\"><i>invisibility</i></a>, but the recipient is able to attack, either by missile discharge, melee combat, or spell casting and remain unseen. Note, however, that there are sometimes telltale traces, a shimmering, so that an observant opponent can attack the invisible spell recipient. Such attacks are at -4 on the \"to hit\" dice, and all saving throws are made at +4."
    ),
    Spell('Massmorph','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as noted above, this spell is the same as the fourth level magic-user spell, <a href=\"/spells/massmorph-magic-user-lvl-4/\"><i>massmorph</i></a>."
    ),
    Spell('Minor Creation','I',4,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="This spell enables the illusionist to create an item of non-living, vegetable nature, i.e. soft goods, rope, wood, etc. The item created cannot exceed 1 cubic foot per level of the spell caster in volume., (Cf. <a href=\"/creatures/djinni/\"><i>Djinni</i></a>.) Note the limits of the spell's duration, The spell caster must have at least a tiny piece of matter of the same type of item he or she plans to create by means of the minor creation spell, i.e. a bit of twisted hemp to create rope, a splinter of wood to create a door, and so forth."
    ),
    Spell('Phantasmal Killer','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("When this spell is cast, the illusionist creates the illusion of the most fearsome thing imagined, simply by forming the fears of the subject creature's subconcious mind into something which its concious mind can visualize — <i>the</i> most horrible beast. Only the spell caster and the spell recipient can see the <i>phantasmal killer</i>, but if it succeeds in scoring a hit, the victim dies (from fright). The beast attacks as a 4 hit dice monster with respect to its victim. It is invulnerable to all attacks, and it can pass through any barriers, for it exists only in the beholder's mind. The only defense against a <i>phantasmal killer</i> is an attempt to disbelieve, which can be tried but once, or slaying or rendering unconscious the illusionist who cast the spell. Note that the saving throw against this spell is not standard. The subject must roll three six-sided dice (3d6) and score a sum equal to or less than its intelligence ability score in order to disbelieve the apparition. The dice score is modified as follows:\n\n"
            "<table>"
            "<tr><th>Condition</th><th>Modifier*</th></tr>"
            "<tr><td>Complete surprise</td><td>+2</td></tr>"
            "<tr><td>Surprise</td><td>+1</td></tr>"
            "<tr><td>Subject previously attacked by this spell</td><td>-1 per previous attack</td></tr>"
            "<tr><td>Subject is an illusionist</td><td>-2</td></tr>"
            "<tr><td>Subject is wearing a <i>helm of telepathy</i></td><td>-3 plus the ability to turn the <i>phantasmal killer</i> upon its creator if disbelieved</td></tr>"
            "*Note that magic resistance and wisdom factors also apply, magic resistance being checked first to determine spell operation (or -1 to -5 on dice if spell resistance is at that of a dwarf, gnome, etc.), and then wisdom bonus applies as a minus to the dice roll to match or score less than intelligence.\n\n"
            "If the subject of the attack by a <i>phantasmal killer</i> succeeds in disbelieving and is wearing a <i>helm of telepathy</i>, the beast can be turned upon the illusionist, and then he or she must disbelieve it or be subject to its attack and possible effects."
        )
    ),
    Spell('Rainbow Pattern','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="By means of this spell the illusionist creates a pastel, glowing, rainbow-hued band of interplaying patterns. The effect is the same as a <a href=\"/spells/hypnotic-pattern-illusionist-lvl-2/\"><i>hypnotic pattern</i></a> spell. However, once the <i>rainbow pattern</i> is cast, the illusionist need only gesture in the direction he or she desires, and the pattern of colors will move slowly off in that direction, at the rate of 3\" per round. It will persist without further attention from the spell caster for 1-3 rounds, and all creatures (up to 24 levels or hit dice) subject to the dweomer will follow the moving rainbow of light. If the pattern leads its targets into a dangerous area (through flame, off a cliff), allow a second saving throw. If the view of the lights is completely blocked (by an <a href=\"/spells/obscurement-druid-lvl-2/\"><i>obscurement</i></a> spell, for instance), the spell is negated. The material components for the spell are a crystal prism and a piece of phosphor."
    ),
    Spell('Shadow Monsters','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="The <i>shadow monsters</i> spell enables the illusionist to create semi-real phantasms of one or more monsters. The total hit dice of the shadow monster or monsters thus created cannot exceed the level of experience of the illusionist; thus a 10th level illusionist can create one creature which has 10 hit dice (in normal circumstances), two which have 5 hit dice (normally), etc. All <i>shadow monsters</i> created by one spell must be of the same sort, i.e. hobgoblins, orcs, spectres, etc. They have 20% of the hit points they would normally have. To determine this, roll the appropriate hit dice and multiply by .20, any score less than .4 is dropped — in the case of monsters with one (or fewer) hit dice, this indicates the monster was not successfully created — and scores of .4 or greater are rounded up to one hit point. If the creature or creatures viewing the <i>shadow monsters</i> fail their saving throw and believe the illusion, the <i>shadow monsters</i> perform as normal with respect to armor class and attack forms. If the viewer or viewers make their saving throws, the <i>shadow monsters</i> are armor class 10 and do only 20% of normal melee damage (biting, clawing, weapon, etc.), dropping fractional damage less than .4 as done with hit points. Example: A <i>shadow monster</i> <a href=\"/creatures/dragonne/\">dragonne</a> attacks a person knowing it is only quasi-real. The monster strikes with 2 claw attacks and 1 bite, hitting as a 9 die monster. All 3 attacks hit, and the normal damage dice are rolled: d8 scored 5, d8 scores 8, 3d6 scores 11 and each total is multiplied by .2 (.2 x 5 = 1, .2 x 8 = 1.6 = 2, 2 x 11 = 2.2 = 2) and 5 hit points of real damage are scored upon the victim."
    ),
    Spell('Solid Fog','I',4,
        cast=tp(4,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When this spell is cast, the illusionist creates an area of fog similar to the effect of a <a href=\"/spells/wall-of-fog-illusionist-lvl-1/\"><i>wall of fog</i></a> spell. However, while these rolling, billowing vapors conform to a <a href=\"/spells/wall-of-fog-illusionist-lvl-1/\"><i>wall of fog</i></a> in most respects, only a very strong wind can move them, and any creature attempting to move through the <i>solid fog</i> will progress at a rate of but 1' per 1\" of normal movement rate per round. A <a href=\"/spells/gust-of-wind-magic-user-lvl-3/\"><i>gust of wind</i></a> spell cannot affect it. A <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, <a href=\"/spells/flame-strike-cleric-lvl-5/\"><i>flame strike</i></a>, or a <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a> will burn it away in a single round. The material components for the spell are a pinch of dried, powdered peas combined with powdered animal hoof."
    ),
    Spell('Vacancy','I',4,
        cast=tp(4,S),
        duration_lvl=tp(1,T),
        sourcebook=U,
        desc="When a <i>vacancy</i> spell is cast, the illusionist causes an area to appear to be vacant, neglected, and unused. Those who behold the area will see dust on the floor, cobwebs, dirt, or any other condition which would be typical of a long-abandoned place. If they pass through the area of spell effect, they will seemingly leave tracks, tear away cobwebs, and so on. Unless they actually contact some object cloaked by the spell, the place will seem empty of what is actually contains. Merely brushing some invisible object will not cause the <i>vacancy</i> spell to be disturbed, and only forceful contact will allow any chance to note that all is not as it seems. The spell is a very powerful combination of advanced invisibility/illusion, but it can cloak only non-living things. Living things will not be invisible, but their presence does not otherwise disturb the spell. If forceful contact with a cloaked object occurs, those creatures subject to the dweomer will be able to penetrate the spell only if they discover several items which they cannot \"see\"; each is then entitled a saving throw versus spell. Failure indicates a belief that the objects only are invisible. A <a href=\"/spells/dispel-illusion-illusionist-lvl-3/\"><i>dispel illusion</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a> spell will remove the dweomer, so that the actual area can be viewed as it is in reality. <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>True seeing</i></a>, a <i>gem of seeing</i>, and similar effects can penetrate the deception, but <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detect invisibility</i></a> cannot. The illusionist must have a square of finest black silk to effect the spell. This material component must be of not less than 100 gp value."
    ),
    Spell('Advanced Illusion','I',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell is essentially a <a href=\"/spells/spectral-force-illusionist-lvl-3/\"><i>spectral forces</i></a> spell which operates through a program (similar to a <a href=\"/spells/programmed-illusion-illusionist-lvl-6/\"><i>programmed illusion</i></a> spell) determined by the caster. It is thus unnecessary for the illusionist to concentrate on the spell for longer than 5 segments after casting it, as the program has then been started and will continue. The illusion has visual, full audial, olfactory, and thermal components. If any viewer actively attempts to disbelieve the dweomer, then he or she gains a saving throw versus spell. If any viewer successfully disbelieves and communicates this fact to other viewers able to comprehend the communication, each such viewer gains a saving throw versus spell with a +4 bonus. The material components are a bit of fleece and several grains of sand."
    ),
    Spell('Chaos','I',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc=("This spell is similar to the seventh level druid <a href=\"/spells/confusion-druid-lvl-7/\"><i>confusion</i></a> spell, but all creatures in the area of effect are confused for the duration of the spell. Only fighters other than paladins or rangers and illusionists are able to combat the spell effects and are thus allowed a saving throw. Similarly, monsters which do not employ magic and have intelligences of 4 (semi-intelligent) or less are entitled to saving throws.\n\n"
            "The material component for this spell is a small disc of bronze and a small rod of iron."
        )
    ),
    Spell('Demi-Shadow Monsters','I',5,
        cast=tp(5,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is similar to the fourth level spell, <a href=\"/spells/shadow-monsters-illusionist-lvl-4/\"><i>shadow monsters</i></a>, except that the monsters created are of 40% hit points. Damage potential is 40% of normal, and they are armor class 8."
    ),
    Spell('Dream','I',5,
        cast=tp(1,D),
        duration=tp(1,VA),
        sourcebook=U,
        desc=("A <i>dream</i> spell is a form of <a href=\"/spells/limited-wish-magic-user-lvl-7/\"><i>limited wish</i></a>, but it has far more limited scope. The illusionist must actually find a comfortable place to rest, lie prone, compose his or her thoughts so as to concentrate upon the desired result, and then go to sleep. If he or she has an undisturbed sleep of not less than 8 hours duration, the <i>dream</i> magic will be effectuated 1 to 12 hours thereafter. Typical things which can be brought about by a <i>dream</i> are:\n\n"
            "   Recovery of an individual's lost hit points\n"
            "   Restoration of a body member such as a hand or foot\n"
            "   Success in locating some object not heavily guarded by magic wards and protections\n"
            "   Discovery of a means of ingress or egress\n"
            "   Location of a safe path through a wilderness\n"
            "   Improvement of chances for gaining a rich treasure\n"
            "   Approximate strength of enemy/opponent forces. Note: If a creature scried by this effect has 7+ or more hit dice, it may make a saving throw versus spell. If successful, it will be undetected by the <i>dream</i>, and might furthermore sense the illusionist as if <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detecting invisible</i></a>.\n\n"
            "It must be noted that a <i>dream</i> is not an ultra-powerful spell, and the results of its casting must be strictly limited. The guide given above denotes the maximum capability of the casting of a <i>dream</i> spell. Results will never exceed these parameters on a permanent basis. If, for example, a dead companion, slain in a recent battle, were dreamed alive, he or she would remain living for but 1 turn per level of experience of the illusionist casting the spell. Thereafter, the dweomer would disappear, the companion would return to his or her previous state, and a more permanent form of magic would be needed to allow the lost individual to actually live fully again.\n\n"
            "A <i>dream</i> cannot by affected by an <a href=\"/spells/extension-i-magic-user-lvl-4/\"><i>extension</i></a> or <a href=\"/spells/permanency-magic-user-lvl-8/\"><i>permanency</i></a> spell. The illusionist can use this spell but once per week. If it is cast twice within the same week, the spell will absolutely fail the second time and the illusionist will age from 1-10 years."
        )
    ),
    Spell('Magic Mirror','I',5,
        cast=tp(1,H),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="This spell is virtually the same as the <a href=\"/spells/magic-mirror-magic-user-lvl-4/\">4th-level magic-user spell</a> of the same name. It uses the same material components, except that if the illusionist casts a <a href=\"/spells/vision-illusionist-lvl-7/\"><i>vision</i></a> spell in place of the normal material components, the mirror will scry properly, although the <a href=\"/spells/vision-illusionist-lvl-7/\"><i>vision</i></a> spell will not function normally."
    ),
    Spell('Major Creation','I',5,
        cast=tp(1,T),
        duration_lvl=tp(6,T),
        sourcebook=V,
        desc="This spell is comparable to a <a href=\"/spells/minor-creation-illusionist-lvl-4/\"><i>minor creation</i></a> spell except that it allows the illusionist to create mineral objects. If vegetable objects are created, they have a duration of 12 turns per level of experience of the spell caster."
    ),
    Spell('Maze','I',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell, except as noted above, is the same as the eighth level magic-user <a href=\"/spells/maze-magic-user-lvl-8/\"><i>maze</i></a> spell."
    ),
    Spell('Projected Image','I',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="Except as shown above, this spell is the same as the sixth level magic-user spell <a href=\"/spells/project-image-magic-user-lvl-6/\"><i>project image</i></a>."
    ),
    Spell('Shadow Door','I',5,
        cast=tp(2,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell, the illusionist creates the illusion of a door. The illusion also permits the illusionist to appear to step through this \"door\" and disappear, when in reality he or she has darted aside, and can then flee totally invisible for the spell duration. Creatures viewing this are deluded into seeing/entering an empty 10' x 10' room if they open the \"door\". Only a <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a> spell, a <i>gem of seeing</i>, or similar magical means will discover the illusionist."
    ),
    Spell('Shadow Magic','I',5,
        cast=tp(5,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The <i>shadow magic</i> spell allows the illusionist to cast a quasi-real magic-user spell. This spell can be <a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>magic missile</i></a>, <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, <a href=\"/spells/lightning-bolt-magic-user-lvl-3/\"><i>lightning bolt</i></a>, or <a href=\"/spells/cone-of-cold-magic-user-lvl-5/\"><i>cone of cold</i></a> and will have normal effects upon creatures in the area of effect if they fail to make their saving throws. If saving throws are made, the <i>shadow magic</i> spell will inflict but 1 hit point of damage per level of experience of the illusionist casting it, regardless of which quasi-real spell was cast."
    ),
    Spell('Summon Shadow','I',5,
        cast=tp(5,S),
        duration=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="When this spell is cast, the illusionist conjures up 1 <a href=\"/creatures/shadow/\">shadow</a> for every three levels of experience he or she has attained. These monsters are under the control of the spell caster and will attack his or her enemies on command. The <i>shadows</i> will remain until slain or turned or the spell duration expires. The material component for this spell is a bit of smoky quartz."
    ),
    Spell('Tempus Fugit','I',5,
        cast=tp(5,S),
        duration_lvl=tp(5,T),
        sourcebook=U,
        desc=("This powerful illusion affects the minds and bodies of all those within the area of effect. The spell causes those affected to perceive the passage of time in a much faster manner. Those entering this area after the casting is completed are similarly affected. Every turn (10 minutes) spent under the <i>tempus fugit</i> spell seems like a full hour to those within its dweomer. Because of this, all functions of affected individuals are speeded up accordingly. They must eat, sleep, and so forth according to an accelerated rate. The duration of other spells cast within the <i>tempus fugit</i> area is also sped up accordingly. One hour is as six to them, four hours a full day. This acceleration of time allows rest, renewal of spells, and recovery of hit points lost.\n"
            "If desired, the spell caster can reverse the spell so that time is slowed for the individuals: An hour will seem only a turn, a day merely four hours. Reversal requires no special preparation. In either case, the illusionist is also affected by the spell. Under the reverse, the effects will always last at least one turn after the caster desires its dispelling, because his or her reactions are so greatly slowed."
        )
    ),
    Spell('Conjure Animals','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="Except as shown above, this spell is the same as the sixth level cleric spell, <a href=\"/spells/conjure-animals-cleric-lvl-6/\"><i>conjure animals</i></a>."
    ),
    Spell('Death Fog','I',6,
        cast=tp(6,S),
        duration=tp(1,VA),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc=("The casting of a <i>death fog</i> spell creates an area of <a href=\"/spells/solid-fog-illusionist-lvl-4/solid\"><i>solid fog</i></a> which has the additional property of being highly acidic. The vapors are deadly to living things, so that vegetation exposed to them will die — grass and similar small plants in 2 rounds, bushes and shrubs in 4, small trees in 8, and large trees in 16 rounds. Animal life not immune to acid will suffer damage according to the length of time it is exposed to the vapors of a <i>death fog</i>:\n\n"
            "1st round: 1 point\n"
            "2nd round: 2 points\n"
            "3rd round: 4 points\n"
            "4th & each succeeding round: 8 points\n\n"
            "The characteristics of a <i>death fog</i> are otherwise the same as a <a href=\"/spells/solid-fog-illusionist-lvl-4/solid\"><i>solid fog</i></a>. The material components are a pinch of dried and powdered peas, powdered animal hoof, and strong acid of any sort (including highly distilled vinegar or acid crystals)."
        )
    ),
    Spell('Demi-Shadow Magic','I',6,
        cast=tp(6,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell is similar to the fifth level <a href=\"/spells/shadow-magic-illusionist-lvl-5/\"><i>shadow magic</i></a> spell, but in addition to the quasi-real spells listed thereunder it enables the illusionist to cast a quasi-real <a href=\"/spells/wall-of-fire-druid-lvl-5/\"><i>wall of fire</i></a>, <a href=\"/spells/ice-storm-magic-user-lvl-4/\"><i>wall of ice</i></a>, or <a href=\"/spells/cloudkill-magic-user-lvl-5/\"><i>cloudkill</i></a>. If recognized as <i>demi-shadow magic</i> (the victim makes its saving throw), the <a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>magic missile</i></a>, <a href=\"/spells/fireball-magic-user-lvl-3/\"><i>fireball</i></a>, et al. do 2 hit points of damage per level of experience of the spell caster, the <i>wall</i> spells cause 1-4 hit points of damage per level, and the <a href=\"/spells/cloudkill-magic-user-lvl-5/\"><i>cloudkill</i></a> will slay only creatures with fewer than 2 hit dice."
    ),
    Spell('Mass Suggestion','I',6,
        cast=tp(6,S),
        duration=tp(4,T),
        duration_lvl=tp(4,T),
        sourcebook=V,
        desc="This spell is the same as the third level <a href=\"/spells/suggestion-illusionist-lvl-3/\"><i>suggestion</i></a> spell, except that the illusionist is able to cast the spell upon more than one subject, provided the prospective recipients of the suggestion are within the 3\" range. One creature per level of experience the spell caster has attained can be affected. If only one creature is the subject, its saving throw is at -2. The suggestion must be the same for all hearing it."
    ),
    Spell('Mirage Arcane','I',6,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=U,
        desc="The dweomer of this spell is similar to that of the <a href=\"/spells/vacancy-illusionist-lvl-4/\"><i>vacancy</i></a> spell, only it is more powerful and elaborate. <i>Mirage arcane</i> is also similar to the <i>mirage</i> cantrip. The spell enables the caster to make an area appear to be something other than it is. The illusionist is able to make it appear as whatever he or she envisions. The spell will remain as long as the caster maintains a faint concentration upon it, and even after this is no longer held the spell will persist for a total of 6 turns plus 1 additional turn for each experience level of the caster. (Note: Faint concentration can be maintained during normal conversation but not while spell casting, in melee, or if harmed by an attack.) In all cases the <i>mirage arcane</i> must be of some place the illusionist has actually seen personally. If he or she actually has a small bit of anything connected with the place envisioned to create this spell, then it takes on a form of reality. In its basic form, where casting time is but 3 segments, forceful contact and tactile discovery are necessary to have any hope of discovering the magic, short of a detection device or spell. In its more complex from, where a material component is used, and 6 segments of casting time are expended, detection is possible only by some magical means, whether device, item, or spell. Either form of <i>mirage arcane</i> is subject to <a href=\"/spells/dispel-illusion-illusionist-lvl-3/\"><i>dispel illusion</i></a> or <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>. As with all powerful illusions, the mind of the beholder will cause appropriate effects upon the viewer's body. Conversely, belief cannot usually affect the laws of nature and magic. However, under the influence of this spell, the viewer could possibly walk across a bed of hot coals thinking it was a shallow stream of water which was cooling his feet (and taking no damage), dine upon imaginary food and actually be nutritionally satisfied, or rest comfortably upon a bed of sharp stones, thinking it to be a featherbed. Gravity, for instance, is not affected by the dweomer, so that an envisioned bridge spanning a deep chasm will not support the believer. Those who may be there to witness the event will see it as a sudden disappearance of the individual. They will in no way connect it with an illusion unless they are otherwise aware of some magic at work."
    ),
    Spell('Mislead','I',6,
        cast=tp(1,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="When a <i>mislead</i> spell is cast by the illusionist, he or she actually creates a phantasmal double at the same time that he or she is cloaked by <a href=\"/spells/improved-invisibility-illusionist-lvl-4/\"><i>improved invisibility</i></a> magic. The illusionist is then free to go elsewhere while his or her phantasm seemingly moves away. The spell allows the phantasm of the illusionist to speak and gesture as if it were real, and there are full olfactory and touch components as well. A <a href=\"/spells/detect-illusion-illusionist-lvl-1/\"><i>detect illusion</i></a>, <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a> or <a href=\"/spells/true-sight-illusionist-lvl-6/\"><i>true sight</i></a> spell, or a <i>gem of seeing</i>, will reveal the illusion for what it is, and a <a href=\"/spells/detect-invisibility-magic-user-lvl-2/\"><i>detect invisibility</i></a>, <a href=\"/spells/true-sight-illusionist-lvl-6/\"><i>true sight</i></a>, or <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a> spell, or a <i>gem of seeing</i> or <i>robe of eyes</i>, can detect the invisible illusionist (cf. <a href=\"/spells/shadow-door-illusionist-lvl-5/\"><i>shadow door</i></a>)."
    ),
    Spell('Permanent Illusion','I',6,
        cast=tp(6,S),
        duration=tp(1,P),
        sourcebook=V,
        desc="This spell creates a lasting <a href=\"/spells/spectral-force-illusionist-lvl-3/\"><i>spectral force</i></a> which requires no concentration. It is subject to <a href=\"/spells/dispel-magic-cleric-lvl-3/\"><i>dispel magic</i></a>, of course."
    ),
    Spell('Phantasmagoria','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=U,
        desc="By means of this spell, the illusionist prepares a special form of <a href=\"/spells/spectral-force-illusionist-lvl-3/\"><i>spectral forces</i></a> spell which is triggered by some special action. The <i>phantasmagoria</i> typically includes a full visual, audial, olfactory, and touch illusion which involves falling, sliding, or moving rapidly. The effect can be aimed at making the subjects believe that they are so doing or that something else is doing so. For example, the <i>phantasmagoria</i> may be triggered when falling into a pit, reaching the center of an area, opening a door, or performing some like action. The subject(s) will then believe that the fall continues for scores of feet; that the pit has opened and that they are hopelessly sliding down into an unknown area; that a wall of water is rushing down from the area beyond the just-opened door, or whatever. Note that unlike the <a href=\"/spells/programmed-illusion-illusionist-lvl-6/\"><i>programmed illusion</i></a> spell, the <i>phantasmagoria</i> spell must always involve the illusion of something falling or rushing, or a dwindling perspective."
    ),
    Spell('Programmed Illusion','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="By means of this spell, the illusionist sets up a <a href=\"/spells/spectral-force-illusionist-lvl-3/\"><i>spectral forces</i></a> spell which will activate upon command or when a specified condition occurs (cf. <a href=\"/spells/magic-mouth-magic-user-lvl-2/\"><i>magic mouth</i></a>). The illusion will last for a maximum of 1 round per level of the spell caster."
    ),
    Spell('Shades','I',6,
        cast=tp(6,S),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is related to <a href=\"/spells/shadow-monsters-illusionist-lvl-4/\"><i>shadow monsters</i></a> and <a href=\"/spells/demi-shadow-monsters-illusionist-lvl-5/\"><i>demi-shadow monsters</i></a>, but the monsters created are of 60% hit points and damage potential and are of armor class 6."
    ),
    Spell('True Sight','I',6,
        cast=tp(1,R),
        duration_lvl=tp(1,R),
        sourcebook=V,
        desc="This spell is very like the fifth level cleric spell, <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a>. However, while the <i>true sight</i> spell allows the illusionist to see its actual or former form, it does not allow determination of alignment."
    ),
    Spell('Veil','I',6,
        cast=tp(3,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>veil</i> spell enables the illusionist to instantly change the appearance of his or her surroundings and/or party or create <a href=\"/spells/hallucinatory-terrain-magic-user-lvl-4/\"><i>hallucinatory terrain</i></a> so as to fool even the most clever creatures unless they have <a href=\"/spells/true-seeing-cleric-lvl-5/\"><i>true seeing</i></a>/<a href=\"/spells/true-sight-illusionist-lvl-6/\"><i>sight</i></a>, a <i>gem of seeing</i>, or similar magical aid. The <i>veil</i> can make a sumptuous room seem a filthy den and even touch will conform to the visual illusion. If <a href=\"/spells/hallucinatory-terrain-magic-user-lvl-4/\"><i>hallucinatory terrain</i></a> is created, touch will not cause it to vanish."
    ),
    Spell('Alter Reality','I',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V,
        desc="The <i>alter reality</i> spell is similar to the seventh level magic-user <a href=\"/spells/limited-wish-magic-user-lvl-7/\"><i>limited wish</i></a> spell. In order to effect the magic fully, the illusionist must depict the enactment of the alteration of reality through the casting of a <a href=\"/spells/phantasmal-force-magic-user-lvl-3/\"><i>phantasmal force</i></a>, as well as verbalization in a limited form, before the spell goes into action."
    ),
    Spell('Astral Spell','I',7,
        cast=tp(3,T),
        duration=tp(1,VA),
        sourcebook=V,
        desc="This spell is the same as the seventh level cleric spell, <a href=\"/spells/astral-spell-cleric-lvl-7/\"><i>astral spell</i></a>."
    ),
    Spell('Prismatic Spray','I',7,
        cast=tp(7,S),
        duration=tp(0),
        sourcebook=V,
        desc=("When this spell is cast, the illusionist causes 7 rays of the <a href=\"/spells/prismatic-sphere-magic-user-lvl-9/\"><i>prismatic sphere</i></a> spell to spring from his or her hand. Any creature in the area of effect will be touched by 1 or more of the rays. To determine which ray strikes the concerned creature, roll an eight-sided die:\n\n"
            "1 = red\n"
            "2 = orange\n"
            "3 = yellow\n"
            "4 = green\n"
            "5 = blue\n"
            "6 = indigo\n"
            "7 = violet\n"
            "8 = struck by 2 rays, roll again twice ignoring any 8's.\n\n"
            "Saving throws apply only with respect to those prismatic color rays which call for such."
        )
    ),
    Spell('Prismatic Wall','I',7,
        cast=tp(7,S),
        duration_lvl=tp(1,T),
        sourcebook=V,
        desc="The <i>prismatic wall</i> spell is similar to the <a href=\"/spells/prismatic-sphere-magic-user-lvl-9/\"><i>prismatic sphere</i></a> spell. It differs only in that the spell creates a wall, or curtain, of scintillating colors. The wall is of maximum proportions of 4' wide per level of experience of the spell caster and 2' high per level of experience."
    ),
    Spell('Shadow Walk','I',7,
        cast=tp(1,S),
        duration_lvl=tp(6,T),
        sourcebook=U,
        desc="In order to effectuate a <i>shadow walk</i> spell, the illusionist must be in an area of heavy shadows. The caster and any creatures he or she touches will then be transported to the edge of the Prime Material Plane where it borders the Plane of Shadow. In this region the illusionist can move at a relative rate of up to 7 leagues per turn, moving normally on the borders of the Plane of Shadow but aware of his or her position relative to the Prime Material Plane. Thus, rapid travel can be accomplished by stepping from the Plane of Shadow to the Prime Material Plane, with the destination controlled by the illusionist. The <i>shadow walk</i> spell can also be used to travel to other planes which border on the Plane of Shadow, but this requires a rather perilous transit of the Plane of Shadow to arrive at a border with another plane of reality. Any creatures touched by the illusionist when <i>shadow walk</i> is cast will also make the transition to the borders of the Plane of Shadow. They may opt to follow the illusionist, wander off into Shadowland, or stumble back onto the Prime Material Plane (50% chance for either result if they are lost or abandoned by the illusionist). Creatures unwilling to accompany the illusionist into the Plane of Shadow get a saving throw, negating the effect if made."
    ),
    Spell('Vision','I',7,
        cast=tp(7,S),
        duration=tp(1,VA),
        sourcebook=V,
        desc="At such time as the illusionist wishes to gain supernatural guidance, he or she casts a <i>vision</i> spell, calling upon whatever power he or she desires aid from, and asking the question for which a vision is to be given to answer. Two six-sided dice are rolled. If they total 2 to 6, the power is annoyed and will cause the illusionist, by ultra-powerful <a href=\"/spells/geas-magic-user-lvl-6/\"><i>geas</i></a> or <a href=\"/spells/quest-cleric-lvl-5/\"><i>quest</i></a> to do some service, and no question will be answered. If the dice total 7 to 9, the power is indifferent, and some minor <i>vision</i>, possibly unrelated to the question, will be given. A score of 10 or better indicates the <i>vision</i> is granted. Note that the material component of the spell is the sacrifice of something valued by the spell caster and/or by the power supplicated. The more precious the sacrifice, the better he chance of spell success, for a very precious item will give a bonus of +1 on the dice, one that is extremely precious will add +2, and a priceless/nonesuch will add +3."
    ),
    Spell('Weird','I',7,
        cast=tp(7,S),
        duration=tp(1,VA),
        sourcebook=U,
        desc="When this spell is cast the illusionist must be able to converse with the subject or subjects to bring the dweomer into being. During the casting, the illusionist must call out to the subject or subjects, informing one or all that their final fate, indeed their doom is now upon them. The force of the magic is such that even if the subject or subjects make their saving throw, fear will paralyze them for a full 7 segments, and they will lose from 1-4 strength points from this fear, although the lost strength will return in 7 rounds. Failure to save versus spell will cause the subject or subjects to face their nemesis, the opponent(s) most feared and inimical to them. Actual combat must then take place, for no magical means of escape will be possible. The foe fought is real for all intents and purposes. If the subject or subjects lose, then death occurs. If the <i>weird</i> caused by the dweomer is slain, then the subject or subjects emerge with no damage, no loss of items seemingly used in the combat, and no loss of spells likewise seemingly expended. The characters gain experience for defeating the <i>weird</i> if applicable. Although each round of combat seems normal, it takes but 1 segment of real time. During the course of the spell, the illusionist must concentrate fully upon maintaining it."
    ),
    Spell('First Level Magic-User Spells','I',7,
        cast=tp(1,VA),
        duration=tp(1,VA),
        sourcebook=V,
        desc=("The illusionist gains four of the following first level magic-user spells at the 14th level of experience and an additional one as each additional level of experience is gained. The spells are:\n\n"
            "<a href=\"/spells/affect-normal-fires-magic-user-lvl-1/\"><i>Affect Normal Fires</i></a>\n"
            "<a href=\"/spells/burning-hands-magic-user-lvl-1/\"><i>Burning Hands</i></a>\n"
            "<a href=\"/spells/charm-person-magic-user-lvl-1/\"><i>Charm Person</i></a>\n"
            "<a href=\"/spells/comprehend-languages-magic-user-lvl-1/\"><i>Comprehend Languages</i></a>\n"
            "<a href=\"/spells/enlarge-magic-user-lvl-1/\"><i>Enlarge</i></a>\n"
            "<a href=\"/spells/erase-magic-user-lvl-1/\"><i>Erase</i></a>\n"
            "<a href=\"/spells/feather-fall-magic-user-lvl-1/\"><i>Feather Fall</i></a>\n"
            "<a href=\"/spells/friends-magic-user-lvl-1/\"><i>Friends</i></a>\n"
            "<a href=\"/spells/hold-portal-magic-user-lvl-1/\"><i>Hold Portal</i></a>\n"
            "<a href=\"/spells/magic-missile-magic-user-lvl-1/\"><i>Magic Missile</i></a>\n"
            "<a href=\"/spells/mending-magic-user-lvl-1/\"><i>Mending</i></a>\n"
            "<a href=\"/spells/message-magic-user-lvl-1/\"><i>Message</i></a>\n"
            "<a href=\"/spells/nystuls-magic-aura-magic-user-lvl-1/\"><i>Nystul's Magic Aura</i></a>\n"
            "<a href=\"/spells/protection-from-evil-magic-user-lvl-1/\"><i>Protection from Evil</i></a>\n"
            "<a href=\"/spells/read-magic-magic-user-lvl-1/\"><i>Read Magic</i></a>\n"
            "<a href=\"/spells/shield-magic-user-lvl-1/\"><i>Shield</i></a>\n"
            "<a href=\"/spells/shocking-grasp-magic-user-lvl-1/\"><i>Shocking Grasp</i></a>\n"
            "<a href=\"/spells/sleep-magic-user-lvl-1/\"><i>Sleep</i></a>\n"
            "<a href=\"/spells/tensers-floating-disc-magic-user-lvl-1/\"><i>Tenser's Floating Disc</i></a>\n"
            "<a href=\"/spells/unseen-servant-magic-user-lvl-1/\"><i>Unseen Servant</i></a>\n\n"
            "The illusionist may learn any spell or spells from the preceding list. He or she must seek the spells in the same manner as a magic-user. If the illusionist chooses to take this \"spell\", he or she actually takes four or more first level magic-user spells as a seventh level spell."
        )
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
