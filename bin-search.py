# def main():
#     given_array = [1, 2, 3, 5, 8, 9, 11]
#     find = 20  # Number to search.
#     number_found = False  # Determines if the number is found or not.
#     start_index = 0
#     end_index = len(given_array) - 1
#     while end_index > start_index:
#         mid_index = (end_index + start_index - 1) // 2
#         if given_array[mid_index] == find:
#             number_found = True
#             break
#         elif given_array[mid_index] > find:
#             end_index = mid_index - 1

#         else:
#             start_index = mid_index + 1

#     if number_found:
#         print("The Desired Element Is Present!")
#     else:
#         print("The Desired Element Is Not Present")
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(primes, num):
    number_found = False  # Determines if the number is found or not.
    start_index = 0
    end_index = len(primes) - 1
    while end_index > start_index:
        mid_index = (end_index + start_index - 1) // 2
        if primes[mid_index] == num:
            number_found = True
            break
        elif primes[mid_index] > num:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    if number_found:
        return "yes"
    else:
        return "no"

print(is_prime(primes, 4))

