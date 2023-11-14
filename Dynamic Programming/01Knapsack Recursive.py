def Knapsack(weight, value, bag_size, item_number):
    if item_number == 0 or bag_size == 0:  # base condition
        return 0
    if weight[item_number-1] <= bag_size:  # recursive condition 1
        return max(value[item_number-1] + Knapsack(weight, value, bag_size-weight[item_number-1], item_number-1),
                   Knapsack(weight, value, bag_size, item_number-1))
    elif weight[item_number-1] > bag_size:  # recursive condition 2
        return Knapsack(weight, value, bag_size, item_number-1)


if __name__ == '__main__':
    w = [1, 3, 4, 5]
    v = [1, 4, 5, 7]
    W = 7
    print(Knapsack(w, v, W, len(w)))