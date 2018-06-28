#creature_info_definitions_test.py
import unittest
import operator

from .creature_info_definitions import creature_list
from .creature_info import Intelligence

class ValidateCreatures(unittest.TestCase):
    """
    Takes a boolean function and field name and
    tests it for all creatures
    """
    def truth(self, func, field, note=None):
        message = '{m_name} INVALID FIELD {m_field}'
        
        if note:
            message = '{}; {}'.format(message, note)

        for c in creature_list:
            self.assertTrue( func( getattr(c,field)),
                msg = message.format(m_name=c.name, m_field=field))
    
    def test_iq_type(self):
        for c in creature_list:
            self.assertIsInstance(c.iq, Intelligence)
    
    def test_ac(self):
        self.truth(lambda x: -20 <= x <= 10, 'ac',
            note = 'expects range of [-20,10]')
    
    def test_magic_resist(self):
        self.truth(lambda x: 0.0 <= x <= 1.0, 'magic_resist')
    
    def test_attacks(self):
        self.truth(
            lambda x: not [attack for attack in x if len(attack) != 3],
            'attacks',
            note =
                ('expects a list of attacks represented '
                'by 3-tuples (die_type,num_die,added_dmg)'))

    def test_alignment(self):
        self.truth( lambda x: len(x) == 2 
            and x in ('LG','NG','CG','LN','NN','CN','LE','NE','CE'),
            'alignment')
    
    def test_size_class(self):
        self.truth(lambda x: x in ('S','M','L'), 'size_class',
            note = 'Expects one of: S M L')
        
    def test_hp_hd(self):
        for c in creature_list:
            self.assertTrue(c.hit_dice[0] <= c.hit_dice[1]
                and c.hit_point_mod[0] <= c.hit_point_mod[1],
                msg="{} has a min hp or hd greater than its max".format(c.name))
                
    def test_num_appearing(self):
        self.truth(lambda x: x[0] <= x[1], 'num_appearing')
        
    def test_parent_creature(self):
        names = [x.name for x in creature_list]
        for c in creature_list:
            if c.parent_creature:
                self.assertTrue(c.parent_creature in names,
                    msg='{} parent {} not found in list'.format(
                        c.name, c.parent_creature))
                        
    def test_child_creatures(self):
        names = [x.name for x in creature_list]
        parents = [x for x in creature_list if x.sub_creatures]
        for p in parents:
            for child in p.sub_creatures:
                self.assertTrue(child in names,
                msg='{} has non-existent child, {}'.format(
                    p.name, child))
                    

if __name__ == '__main__':
    unittest.main()
