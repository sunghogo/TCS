import unittest
from rucksack_data import example_rucksacks, actual_rucksacks
from rucksack import solve_rucksacks_first_half, solve_rucksacks_second_half

class TestRucksack(unittest.TestCase):
    def test_first_half_example(self):
        self.assertEqual(solve_rucksacks_first_half(example_rucksacks), 157)
        
    def test_first_half_actual(self):
        self.assertEqual(solve_rucksacks_first_half(actual_rucksacks), 8039)

    def test_second_half_example(self):
        self.assertEqual(solve_rucksacks_second_half(example_rucksacks), 70)
        
    def test_second_half_actual(self):
        self.assertEqual(solve_rucksacks_second_half(actual_rucksacks), 2510)
   
        
if __name__ == "__main__":
    unittest.main()