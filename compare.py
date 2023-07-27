# Sample lists of tuples
list1 = [(1, 2), (3, 4), (5, 6)]
list2 = [(1, 2), (3, 4), (7, 8)]

# Create a new list to store the changed tuples
changed_tuples = []

# Compare the tuples and add the changed ones to the new list
for tuple1, tuple2 in zip(list1, list2):
    if tuple1 != tuple2:
        changed_tuples.append((tuple1, tuple2))

# Output the changed tuples
print(changed_tuples)

