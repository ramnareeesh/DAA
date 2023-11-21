def lcs(A, B, i, j):
    # base condition
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + lcs(A, B, i+1, j+1)
    else:
        return max(
            lcs(A, B, i+1, j),
            lcs(A, B, i, j+1)
        )


if __name__ == '__main__':
    A = "bd"
    B = "abcd"
    print(lcs(A, B, 0, 0))
