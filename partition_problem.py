# Given on 03.08.23

def partition(A):
    subsets = [[]]
    for element in A:
        new_subsets = [subset + [element] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets


def sum_calc(powerset):
    for i in powerset:
        for j in powerset:
            if i != j:
                sum_i = sum(tuple(i))
                sum_j = sum(tuple(j))
                if sum_i == sum_j:
                    print(i, end=" ")
                    print(j)


A = [2, 5, 8, 11, 12]
powerset_A = partition(A)
sum_calc(powerset_A)
