# Project 2: Valid Parentheses
# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


s = "()[]{}"
print(is_valid(s))  # Output: True

s = "(]"
print(is_valid(s))  # Output: False


# Project 2: Single Number
# Problem Statement: Given a non-empty array of integers, every element appears twice except for one. Find that single one.


def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res