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


# O(m * n log n) where m = # of rucksacks, n = # of items
def solve_rucksacks_second_half(rucksacks):
    """Finds duplicate item that is representative for each group of 3. and returns the sum of the corresponding duplicate priorities representing each group.

    Args:
        rucksacks (List[str]): Array of strings representing each rucksack
        
    Returns:
        (int): Sum of priorities corresponding to the duplicate item representing each group.
    """
    priorities_sum = 0
    
    # Form groups of 3 from rucksacks data
    # Working under assumption that all rucksacks form perfect group of 3's
    # O(m)
    groups = []
    for i, rucksack in enumerate(rucksacks):
        if i % 3 == 0:
            groups.append([rucksack])
        else:
            groups[len(groups) - 1].append(rucksack)
        
    # Iterate through each group, and each rucksack in group
    # O(m)
    for group in groups:
        # Access rucksack for each group member
        # O(1)
        first_rucksack = group[0]
        second_rucksack = group[1]
        third_rucksack = group[2]
   
        # Sort each rucksack
        # O(n log n)
        sorted_first_rucksack = sorted(first_rucksack)
        sorted_second_rucksack = sorted(second_rucksack)
        sorted_third_rucksack = sorted(third_rucksack)
    
        # Find duplicate item
        # Working under assumption that there is exactly 1 duplicate item in all 3 rucksacks
        # O(n)
        duplicate = ''
        first_index = 0
        second_index = 0
        third_index = 0
        pair_found = False
        false_pairs = []
        while (not duplicate):
            first_item = sorted_first_rucksack[first_index]
            second_item = sorted_second_rucksack[second_index]
            third_item = sorted_third_rucksack[third_index]
            # Iterate first two rucksacks to find a matching pair
            if not pair_found:
                if first_item == second_item and first_item not in false_pairs:
                    pair_found = True
                elif first_item < second_item:
                    first_index += 1
                else:
                    second_index += 1
            # Iterate through third rucksack to find a matching pair
            else:
                if first_item == third_item:
                    duplicate = first_item
                    break
                elif first_item > third_item:
                    third_index += 1
                else:
                    # Reset if no matching pair found
                    false_pairs.append(first_item)
                    pair_found = False
        
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