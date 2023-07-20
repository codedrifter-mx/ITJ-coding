# Alfredo Flores Garcia

# The function "two_sum" takes a list of integers nums and an integer target as input.
# It initializes an empty dictionary num_dict to store the complement of each number encountered in the nums list and its corresponding index.
# Then iterates through the nums list, calculates the complement of the current number with respect to the target, and checks if the complement exists in the num_dict.
# If the complement is found in the dictionary, it means we have found two numbers that add up to the target, and the function returns their indices.
# If the complement is not found, the current number and its index are added to the dictionary for future reference.

# Time & space complexity: The time complexity of this solution is O(n),
# where n is the length of the input nums list. The function iterates through the list once,
# and each dictionary operation (lookup, insertion) takes constant time on average.
# In the worst case, the function may need to store all n elements of the nums list in the dictionary.

def two_sum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            # If the complement is already in the dictionary, return its index and the current index
            return [num_dict[complement], i]
        else:
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

# Unit tests
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()
