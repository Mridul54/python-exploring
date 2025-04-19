# Write a function that sorts a list of strings alphabetically. 
#["apple", "banana", "cherry", "kiwi", "grape"]
def sort_strings(string_list):
    return sorted(string_list)

fruits = ["apple", "banana", "cherry", "kiwi", "grape"]

sorted_fruits = sort_strings(fruits)
print("Sorted list:", sorted_fruits)
