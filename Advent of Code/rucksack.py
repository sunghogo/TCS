"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

To begin, get your puzzle input.
"""

# O(m * n log n) where m = # of rucksacks, n = # of items
def solve_rucksacks_first_half(rucksacks):
    """Finds duplicate items in both compartments of each rucksack, and returns the sum of the corresponding duplicate priorities.

    Args:
        rucksacks (List[str]): Array of strings representing each rucksack
        
    Returns:
        (int): Sum of priorities corresponding to duplicate item in each rucksasck.
    """
    priorities_sum = 0
    
    # Iterate through each rucksack
    # O(m)
    for rucksack in rucksacks:
        # Slice each compartment
        # Odd number of items will result in 1 more item being in the second compartment
        # O(n)
        first_compartment = rucksack[:int(len(rucksack) / 2)]
        second_compartment = rucksack[int(len(rucksack) / 2):]
        
        # Sort each compartment
        # O(n log n)
        sorted_first_compartment = sorted(first_compartment)
        sorted_second_compartment = sorted(second_compartment)
        
        # Find duplicate item
        # Working under assumption that there is exactly 1 duplicate item in both compartments
        # O(n)
        duplicate = ''
        first_index = 0
        second_index = 0
        while (not duplicate):
            first_item = sorted_first_compartment[first_index]
            second_item = sorted_second_compartment[second_index]
            if first_item == second_item:
                duplicate = first_item
                break
            elif first_item < second_item:
                first_index += 1
            else:
                second_index += 1
        
        # Calculate priority
        # O(1)
        priority = 0
        # If duplicate is lower case alphabet
        if 97 <= ord(duplicate) and ord(duplicate) <= 122:
            priority = ord(duplicate) - 96
        # If duplicate is upper case alphabet
        if 65 <= ord(duplicate) and ord(duplicate) <= 90:
            priority = ord(duplicate) - 38
            
        # Add priority to running sum
        priorities_sum += priority
    
    # return priorities running sum
    return priorities_sum

def solve_rucksacks_second_half(rucksacks):
    """Finds duplicate items in both compartments of each rucksack, and returns the sum of the corresponding duplicate priorities.

    Args:
        rucksacks (List[str]): Array of strings representing each rucksack
        
    Returns:
        (int): Sum of priorities corresponding to the duplicate item for each group.
    """
    return 1
    