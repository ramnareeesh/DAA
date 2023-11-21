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


def lcs_dp(A, B):
    m = len(A)
    n = len(B)

    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],
                               dp[i-1][j])
    return dp, dp[m][n]


if __name__ == '__main__':
    A = "bd"
    B = "abcd"
    print(lcs(A, B, 0, 0))
    print(lcs_dp(A, B))
