def no_unordered(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count



def d_c_unordered(arr, count, sub_count):
    sub_count += 1
    if len(arr) > 1:

        mid = (len(arr)) // 2
        l = arr[:mid]
        r = arr[mid:]
        count, sub_count = d_c_unordered(l, count, sub_count)
        count, sub_count = d_c_unordered(r, count, sub_count)

        i = 0
        j = 0
        temp = []

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                temp.append(l[i])
                i += 1
            else:
                temp.append(r[j])
                count += len(l) - i
                j += 1

        while i < len(l):
            temp.append(l[i])
            i += 1

        while j < len(r):
            temp.append(r[j])
            j += 1
        arr = temp
    return count, sub_count


if __name__ == '__main__':
    n = int(input())
    height = []
    for _ in range(n):
        height.append(int(input()))
    # print(no_unordered(height))
    count, sub_count = d_c_unordered(height, 0, 0)
    print(count)
    print(sub_count)
