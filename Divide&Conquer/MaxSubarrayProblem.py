def maxCrossingSum(arr, low, mid, high):
    sum = 0
    left_sum = float("-inf")
    for i in range(mid, low-1, -1):
        sum += arr[i]

        if sum > left_sum:
            left_sum = sum

    sum = 0
    right_sum = float("-inf")
    for i in range(mid, high+1, 1):
        sum += arr[i]

        if sum > right_sum:
            right_sum = sum

    return max(
        left_sum,
        right_sum,
        left_sum + right_sum - arr[mid]
    )

def maxSubarraySum(arr, low, high):
    max_val = float("-inf")
    if low > high:
        return max_val
    if low == high:
        return arr[low]
    mid = (low + high) // 2

    return max(
        maxSubarraySum(arr, low, mid-1),
        maxSubarraySum(arr, mid+1, high),
        maxCrossingSum(arr, low, mid, high)
    )


if __name__ == '__main__':
    in_arr = [-2, -3, -4, -5, -1]
    print("Maximum Subarray Sum: ", maxSubarraySum(in_arr, low=0, high=len(in_arr) - 1))
