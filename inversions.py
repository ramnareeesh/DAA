def inversion(A):
    inversion_count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                inversion_count += 1
    return inversion_count

def main():
    n = int(input())  # size
    A = input().split(",")# array elements
    for i in range(len(A)):
        A[i] = int(A[i].strip())
        
    print(inversion(A))

main()
    