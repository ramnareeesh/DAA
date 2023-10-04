# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the
# deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job
# is 1. Maximize the total profit if only one job can be scheduled at a time.

def job_sequence(jobs):
    # let's start by sorting the tasks by deadline (desc)
    jobs.sort(reverse=True, key=lambda x: x[2])
    # print(jobs)
    max_slots = max(task[1] for task in jobs)
    busy = [False] * max_slots
    total_profit = 0

    for job in jobs:
        deadline, profit = job[1], job[2]
        for i in range(deadline - 1, -1, -1):
            if not busy[i]:
                busy[i] = job[0]
                total_profit += profit
                break

    return total_profit, busy


if __name__ == '__main__':
    # tasks are stored in the format:
    # [0] -> task_no
    # [1] -> deadline
    # [2] -> profit

    tasks = [[1, 7, 15],
             [2, 2, 20],
             [3, 5, 30],
             [4, 3, 18],
             [5, 4, 18],
             [6, 5, 10],
             [7, 2, 23],
             [8, 7, 16],
             [9, 3, 25]]
    print("Profit: ", job_sequence(tasks)[0])
    print("Schedule: ", job_sequence(tasks)[1])
