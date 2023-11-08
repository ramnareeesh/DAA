def find_max_in_array(arr, low, high):
    # Base case: If there's only one element, return it as the maximum
    if low == high:
        return arr[low]

    # Divide: Find the middle index
    mid = (low + high) // 2

    # Conquer: Recursively find the maximum in the left and right subarrays
    left_max = find_max_in_array(arr, low, mid)
    right_max = find_max_in_array(arr, mid + 1, high)

    # Combine: Compare and return the maximum of the two subarray maxima
    return max(left_max, right_max)

# Example usage:
arr = [4, 7, 1, 9, 3, 6]
max_element = find_max_in_array(arr, 0, len(arr) - 1)
print("Maximum element:", max_element)