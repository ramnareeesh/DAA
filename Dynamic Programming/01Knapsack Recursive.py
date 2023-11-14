import time
def Knapsack(weight, value, bag_size, item_number):
    if item_number == 0 or bag_size == 0:  # base condition
        return 0
    if weight[item_number-1] <= bag_size:  # recursive condition 1
        return max(value[item_number-1] + Knapsack(weight, value, bag_size-weight[item_number-1], item_number-1),
                   Knapsack(weight, value, bag_size, item_number-1))
    elif weight[item_number-1] > bag_size:  # recursive condition 2
        return Knapsack(weight, value, bag_size, item_number-1)

def Knapsack_Mem(weight, value, size, items, t):
    if items == 0 or size == 0:  # base condition
        return 0
    if t[items][size] != -1:
        return t[items][size]
    if weight[items-1] <= size:
        t[items][size] = max(value[items-1] + Knapsack_Mem(weight, value, size-weight[items-1], items-1, t),
                             Knapsack_Mem(weight, value, size, items-1, t))
        return t[items][size]
    elif weight[items-1] > size:
        t[items][size] = Knapsack_Mem(weight, value, size, items-1, t)
        return t[items][size]


if __name__ == '__main__':
    w = [1, 3, 4, 5]
    v = [1, 4, 5, 7]
    W = 7
    start = time.time()
    print(Knapsack(w, v, W, len(w)))
    end = time.time()
    print(end-start)
    t = [[-1 for i in range(0, W+1)] for j in range(0, len(w)+1)]
    start = time.time()
    print(Knapsack_Mem(w, v, W, len(w), t))
    end = time.time()
    print(end-start)
