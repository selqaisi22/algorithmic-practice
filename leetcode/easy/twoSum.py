# Link: https://leetcode.com/problems/two-sum/description/
# Date solved: 2026-10-24
"""
Two Sum

Problem
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

* Given: nums = [2,7,11,15], target = 9
* Return: [0,1]

Approach
* Use hash map / dictionary to store numbers & their index value while iterating through list.
Check to see if target - curr number already exists in dictionary.


Complexity Analysis
* Time Complexity: O(n), n is # elements in array
* Space Complexity: O(n), storing up to n elements in "seen" dictionary
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """Finds indices of two numbers in nums that add up to target."""
    seen = {} # stores value, index

    for i, num in enumerate(nums):
        temp = target - num
        if temp in seen:
            return [seen[temp], i]

        seen[num] = i

    return []




if __name__ == "__main__":
    # Test with LeetCode Sample Dataset
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target)) # Expected Output: [0, 1]