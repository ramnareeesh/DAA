def sort_key(a):
    return a[1]  # sorting by finish time


def activity_selector(activities):
    select = []
    activities.sort(key=sort_key)
    print(activities)

    k = 0
    select.append(activities[k])
    for i in range(1, len(activities)):
        if activities[i][0] >= activities[k][1]:  # if start_time[i] >= finish_time[k]
            select.append(activities[i])
            k = i

    return select


if __name__ == '__main__':
    list_acts = [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
    print("The selected activities are: ", activity_selector(list_acts))
