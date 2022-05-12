# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Dictionary has numbers as key and their index as value
        seenNums = {}

        for i, n in enumerate(nums):
            diff = target - n   # We get the difference between each number n and the target
            # If the difference matches a number in our dictionary of already seen numbers,
            # we return the index values of that number and the index value i of n
            if diff in seenNums:
                return [seenNums[diff], i]
            # If we don't see the difference, we add the number n to our dictionary with the value i
            seenNums[n] = i
