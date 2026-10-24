# Link: https://leetcode.com/problems/valid-parentheses/description/
# Date solved: 2026-10-24
"""
Valid Parentheses

Problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.

* Given: s = "()[]{}"
* Return: true

Approach
* Use a stack to keep track of open brackets, last in first out LIFO. 
When close bracket found, check if it matches most recently added open bracket at the top of stack by popping it out.
If it matches then continue, otherwise return false.  

Complexity Analysis
* Time Complexity: O(n), n is length of string
* Space Complexity: O(n), all chars end up stored in stack
"""

def validParenthesis(s: str) -> bool:
    """Determine if string of brackets is valid & properly nested."""
    stack = []

    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in mapping: # char is closing bracket
            # pop top element from stack if not empty, else assign *
            top_element = stack.pop() if stack else "*"

            # if mapped open bracket doesnt match stacks top, return false
            if mapping[char] != top_element:
                return False
        else: # char is open bracket
            stack.append(char)

    return not stack




if __name__ == "__main__":
    # Test with LeetCode Sample Dataset
    print(validParenthesis("()[]{}"))
    print(validParenthesis("(]"))