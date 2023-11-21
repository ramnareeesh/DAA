def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    s, start, end = 0, 0, 0

    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    return max_so_far, arr[start:end+1]


if __name__ == '__main__':
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_subarray_sum(a))