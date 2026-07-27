# 1.Write a program to find the second largest element in a list of integers.


nums = [5, 88, 66, 69, 32]

nums.sort(reverse=True)  # Sort the list in descending order
print(nums[1])