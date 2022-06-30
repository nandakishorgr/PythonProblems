# Program to find duplicate characters in String.
# input : programming
# output : r g m
def print_duplicate_characters(word):
    duplicates = {}
    for i in word:
        if i in duplicates:
            print(duplicates)
            duplicates[i] += 1
        else:
            duplicates[i] = 1
            print(duplicates)
    for key, value in duplicates.items():
        if value > 1:
            print(key, end=" ")


print_duplicate_characters("programming")
#print_duplicate_characters("24tutorials")

print_duplicate_characters([2, 10,10, 100, 2, 10, 11,2,11,2])

#Time Complexity: O(N)
#Auxiliary Space: O(N)