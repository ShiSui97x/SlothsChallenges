"""
                                                    CHALLENGE
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored 
into sub lists. Items of the same value should be in the same sub list.

Examples:
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

Notes:
The sub lists should be returned in the order of each element's first appearance in the given list.
"""

# Solution


def advanced_sort(lst):
    return [[i for i in lst if i == j] for j in list(dict.fromkeys(lst))]


# Examples
lst1 = [2, 1, 2, 1]
lst2 = [5, 4, 5, 5, 4, 3]
lst3 = ["b", "a", "b", "a", "c"]

# Results
print(advanced_sort(lst1))  # ➞ [[2, 2], [1, 1]]
print(advanced_sort(lst2))  # ➞ [[5, 5, 5], [4, 4], [3]]
print(advanced_sort(lst3))  # ➞ [["b", "b"], ["a", "a"], ["c"]]
