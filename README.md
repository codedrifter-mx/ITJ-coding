# ITJ-coding

This is a repository with the answers for the 2 Mid Level coding problems for iTjuana, this is made on Python 3, please make sure you have the latest version (https://www.python.org/downloads/)

# Problem 1 solution 

_Please review 1_missing_numbers.py_

1. The method "find_missing_numbers" accepts a list nums as input and fills a set num_set with all the numbers from 1 to the length of the list n.
2. It then iterates through the provided nums list, removing each entry from the set num_set.
3. After eliminating all items from the set, the remaining elements in num_set will be the missing numbers.
4. At the end, he method transforms the set back to a list and returns the missing numbers.

Time & space complexity: The complexity of this solution is O(n), where n is the length of the input nums list.

``` bash
python 1_missing_numbers.py
```

# Problem 2 solution

_Please review 2_two_sum.py_


1. The function "two_sum" takes a list of integers nums and an integer target as input.
2. It initializes an empty dictionary num_dict to store the complement of each number encountered in the nums list and its corresponding index.
3. Then iterates through the nums list, calculates the complement of the current number with respect to the target, and checks if the complement exists in the num_dict.
4. If the complement is found in the dictionary, it means we have found two numbers that add up to the target, and the function returns their indices.
5. If the complement is not found, the current number and its index are added to the dictionary for future reference.

Time & space complexity: The time complexity of this solution is O(n), where n is the length of the input nums list. The function iterates through the list once, and each dictionary operation (lookup, insertion) takes constant time on average. In the worst case, the function may need to store all n elements of the nums list in the dictionary.

``` bash
python 2_two_sum.py
```