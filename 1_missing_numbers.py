# Alfredo Flores Garcia

# The method "find_missing_numbers" accepts a list nums as input and
# fills a set num_set with all the numbers from 1 to the length of the list n.
# It then iterates through the provided nums list, removing each entry from the set num_set.
# After eliminating all items from the set, the remaining elements in num_set will be the missing numbers.

# At the end, he method transforms the set back to a list and returns the missing numbers.

# Time & space complexity: The complexity of this solution is O(n), where n is the length of the input nums list.

def find_missing_numbers(nums):
    n = len(nums)
    # Create a set to store the numbers from 1 to n
    num_set = set(range(1, n + 1))

    # Iterate through the given nums list and remove the elements from the set
    for num in nums:
        num_set.discard(num)

    # Convert the set back to a list and return the missing numbers
    return list(num_set)


# Unit testing
def test_find_missing_numbers():
    assert find_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_missing_numbers([1, 1]) == [2]
    assert find_missing_numbers([3, 2, 1]) == []
    assert find_missing_numbers([5, 4, 3, 2, 1]) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_missing_numbers()
