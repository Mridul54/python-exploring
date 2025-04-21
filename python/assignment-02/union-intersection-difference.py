A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union = A.union(B)
print("Union of A and B:", union)

intersection = A.intersection(B)
print("Intersection of A and B:", intersection)

difference_AB = A.difference(B)
print("Difference of A - B:", difference_AB)

difference_BA = B.difference(A)
print("Difference of B - A:", difference_BA)
