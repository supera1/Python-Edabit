def sort_ascending(arr):
    """
    Sorts an array of numbers in ascending order based on the reversed string representation of the number.

    Args:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.
    """
    # Sort the list with a custom key: reversed string representation of the number
    sorted_arr = sorted(arr, key=lambda x: str(x)[::-1])
    return sorted_arr

# Read input
n = int(input())
arr = [int(x) for x in input().split()]

# Sort the array
sorted_arr = sort_ascending(arr)

# Print the sorted array
for num in sorted_arr:
    print(num)
