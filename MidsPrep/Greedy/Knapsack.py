def sort_keys(x):
    return x[1] / x[0]


def knapsack(bag_cap, valuables):
    valuables.sort(reverse=True, key=sort_keys)
    print(valuables)
    selected = []
    profit = 0
    current_cap = 0
    for i in valuables:
        if current_cap+i[0] <= bag_cap:
            current_cap += i[0]
            selected.append(str(i[0]))
            profit += i[1]
        else:
            remaining = bag_cap - current_cap
            current_cap += remaining
            selected.append(str(remaining) + "/" + str(i[0]))
            profit += (remaining / i[0]) * i[1]

    print("Profit: ", profit)

    return selected


if __name__ == '__main__':
    items = [(2, 20), (3, 25), (4, 40), (5, 50)]
    W = 10
    print(knapsack(W, items))