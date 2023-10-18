def schedule(workers, b):
    workers.sort(reverse=True, key=lambda x: x[1])
    print(workers)
    k = 0
    select =[]
    select.append(workers[k])

    for j in range(len(workers)):
        for i in range(len(workers)-1, k-1, -1):  # traversing from reverse
            if (workers[i][1] - workers[k][0]) >= 0:
                select.append(workers[i])
                k = i
                break
        if workers[k][0] == b:
            break
    print("Selected persons are: ", select)


if __name__ == '__main__':
    b = 9
    persons = [[9, 13],
               [10, 14],
               [11, 15],
               [12, 16],
               [13, 17]]
    persons = [[9, 12],
               [9, 14],
               [10, 11],
               [10, 12],
               [13, 15],
               [15, 17]]
    schedule(persons, b)
