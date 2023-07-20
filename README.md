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