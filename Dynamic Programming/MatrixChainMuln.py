# Given the dimension of a sequence of matrices in an array arr[], where the dimension of the ith matrix is (arr[i-1]
# * arr[i]), the task is to find the most efficient way to multiply these matrices together such that the total
# number of element multiplications is minimum.


def mat_chain(dimensions):
    n = len(dimensions) - 1

    min_arr = [[0 for columns in range(n)] for rows in range(n)]
    for i in range(n):
        min_arr[i][i] = 0

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            min_arr[i][j] = float('inf')
    for k in range(i, j):
        cost = min_arr[i][k] + min_arr[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
        if cost < min_arr[i][j]:
            min_arr[i][j] = cost

if __name__ == '__main__':
    arr = [2, 3, 6, 4, 5]
    print("The minimum no. of multiplications required is ", mat_chain(arr))