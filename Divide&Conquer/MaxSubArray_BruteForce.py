def brute(arr):
    max_ = float("-inf")

    for i in range(0, len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ = sum_ + arr[j]
            if sum_ > max_:
                max_ = sum_
    return max_

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(brute(arr))