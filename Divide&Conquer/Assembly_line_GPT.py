def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

def merge_sort_and_count(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += merge_sort_and_count(arr, temp, left, mid)
        count += merge_sort_and_count(arr, temp, mid + 1, right)
        count += merge(arr, temp, left, mid, right)
    return count

def count_students_not_in_order_n_log_n(heights):
    n = len(heights)
    temp = [0] * n
    return merge_sort_and_count(heights, temp, 0, n - 1)

if __name__ == '__main__':
    heights = [3, 2, 1]
    print(count_students_not_in_order_n_log_n(heights))