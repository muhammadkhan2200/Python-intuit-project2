def two_sum(nums: [int], target: int) -> [int]:
  """
  Finds the indices of two numbers in a list that add up to a target.

  Args:
      nums: A list of integers.
      target: The target sum.

  Returns:
      A list of two indices representing the positions of the numbers that add up to the target.
      Returns an empty list if no such pair exists.
  """
  seen = {}  # Create a hash table to store seen numbers and their indices
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement], i]  # Found a pair that adds up to the target
    seen[num] = i  # Add current number and its index to the hash table
  return []  # No such pair exists

# Example usage
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of two numbers that add up to {target}: {indices}")