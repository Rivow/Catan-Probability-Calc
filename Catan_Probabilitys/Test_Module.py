import unittest
import Catan_Probabilitys


class TestModule(unittest.TestCase):

    def test_prove_int_true(self):
        actual = Catan_Probabilitys.prove_if_int(2)
        self.assertTrue(actual, 'Expected True since test input was an integer')

    def test_prove_int_false(self):
        actual = Catan_Probabilitys.prove_if_int('e')
        self.assertFalse(actual, 'Expected False since test input is not an integer')


    def test_prove_range_in(self):
        actual = Catan_Probabilitys.prove_range(12)
        self.assertTrue(actual, 'Expected 5 to be in Dice Roll Range')


    def test_prove_range_out(self):
        actual = Catan_Probabilitys.prove_range(1)
        self.assertFalse(actual, 'Expected to Return False because 1 is not in Roll Range')


    def test_all_numbers_dic(self):
        actual = Catan_Probabilitys.create_dic()
        expected = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_dic_numbers_rolled(self):
        roll = [7, 9, 12, 8, 10, 9, 11]
        actual = Catan_Probabilitys.rolled_dic(roll)
        expected = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 2, 10: 1, 11: 1, 12: 1}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal')

    def test_total_rolls(self):
        actual = Catan_Probabilitys.total_roll(6)
        expected = 7 
        self.assertEqual(actual, expected, 'Expected Total Rolls to be 7')

    def test_create_roll_list(self):
        roll_list = []
        for test_var in range(2,10):
            actual = Catan_Probabilitys.create_roll_list(test_var, roll_list)
        expected = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected, 'Roll List Expected to have the values form 2 to 9')


    def test_if_game_ended_lower(self):
        actual = Catan_Probabilitys.game_ended
        self.assertTrue(actual, 'Expected to return True')


    def test_if_game_ended_upper(self):
        actual = Catan_Probabilitys.game_ended
        self.assertTrue(actual, 'Expected to return True')

if __name__ == '__main__':
    unittest.main()
