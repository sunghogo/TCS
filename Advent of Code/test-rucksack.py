import unittest
from rucksack import solve_rucksack

class TestRucksack(unittest.TestCase):

    def test_add(self):
        input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
        rucksacks = input.split('\n')
        self.assertEqual(solve_rucksack(rucksacks), 157)

if __name__ == "__main__":
    unittest.main()