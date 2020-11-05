"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""

from typing import List
#Plan #1-- O(n) and doesnt take advantage that this data is sorted
    # iterate list of names
    # check the names two at a time
    # if we see the second name doesn't come after first in alphabetical order,
    # that is our rotation point, return the index of that second name

def find_rotation_point(surnames: List[str]) -> int:
#Plan #2 BINARY SEARCH
    #if you are ever tasked with searching through sorted data, consider Binary search
    #two variable, left and right boundaries
    left = 0
    right = len(surnames) - 1
    #loop so long as left < right
    while left < right:
    #get midpoint of current search space
        mid = ((right - left) // 2) + left
    #check midpoint element against first element in search space
        #if the midpoint element > the first element
        if surnames[mid] > surnames[left]:
        #go right
            left = mid
        #otherwise we go left
        else:
            right = mid
        # check if left and right are next to each other
        if left + 1 == right:
            # if they are, return the right index
            return right




surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
print(find_rotation_point(surnames))




