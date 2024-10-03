def find_minimum_time(jobs, k):
    total = 0
    for job in jobs :
        total += job
    if total % k == 0:
        return total // k
    else:
        return total // k + 1
        


job,k = input('Enter jobs and number of workers : ').split('/')
time = find_minimum_time(map(int,job.split()), int(k))
print(f'Minimum time to complete jobs with {k} workers is {time}')
