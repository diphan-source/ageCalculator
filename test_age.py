"""my unit test for age cal"""
import unittest
from age_cal import age_calculator

class TestAgeCal(unittest.TestCase):
    
    def test_age_calculator(self):
        year_of_birth = 1994
        assert age_calculator(year_of_birth) == 28

        
    def test_year_of_birth_is_less_than_1900(self):
        year_of_birth = 1899
        self.assertEqual (age_calculator(year_of_birth),"Enter valid year")
        
if __name__ == '__main__':
    unittest.main()
    