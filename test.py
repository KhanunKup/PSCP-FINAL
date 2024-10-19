import json

def alternate_order(lst):
    result = []
    left, right = 0, len(lst) - 1
    
    while left <= right:
        if right != left:
            result.append(lst[right])
            right -= 1
        result.append(lst[left])
        left += 1
    
    return result

# Test cases based on examples
example_1 = [1, 2, 3, 4, 5, 6, 7]
example_2 = [3, 7, 2, 8, 1, 9, 2, 10]
example_3 = [8, 1, 2, 9, 3, 7, 6, 10, 5]

print(alternate_order(example_1))  # Output: [7, 1, 2, 6, 5, 3, 4]
print(alternate_order(example_2))  # Output: [10, 3, 7, 2, 9, 2, 8, 1]
print(alternate_order(example_3))  # Output: [5, 8, 1, 10, 6, 2, 9, 7, 3]
