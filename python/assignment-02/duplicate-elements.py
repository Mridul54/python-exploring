#Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].
nums = [1, 5, 6, 5, 1, 2, 3]
duplicate = []

for n in nums:
    if nums.count(n) > 1 and n not in duplicate:
        duplicate.append(n)

print("Duplicates:", duplicate)
