from queue import PriorityQueue

def sort_ascending(arr):
  """
  Sorts an array of numbers in ascending order using a custom priority queue.

  Args:
      arr (list): The list of numbers to be sorted.

  Returns:
      list: The sorted list of numbers.
  """

  # Create a priority queue that sorts based on the reversed string representation of the number
  pq = PriorityQueue()
  for num in arr:
    reversed_str = str(num)[::-1]  # Reverse the string representation of the number
    pq.put((reversed_str, num))  # Add (reversed_str, original_num) to the queue

  # Extract elements from the queue and print them in original order
  sorted_arr = []
  while not pq.empty():
    _, original_num = pq.get()  # Extract the original number
    sorted_arr.append(original_num)

  return sorted_arr

# Read input
n = int(input())
arr = [int(x) for x in input().split()]

# Sort the array
sorted_arr = sort_ascending(arr)

# Print the sorted array
for num in sorted_arr:
  print(num)