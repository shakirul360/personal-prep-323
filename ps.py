
dict1 = {}

def PS_init(n, dict1):
    print("Enter the priorities and their burst time separated by a space: ")
    for i in range(0, n):
        print(f"Process no: {i + 1}")
        pri, bt = map(int, input().split())
        dict1[i] = (pri, bt)

    dict1 = dict(sorted(dict1.items(), key=lambda x: x[1][0]))
    print_processes(dict1)
    PS(dict1)

def print_processes(dict1):
    for i in dict1:
        print(i + 1, dict1[i]);

def PS(dict1):
    wt = {}
    total_wt = 0
    prev_end_time = 0
    for i in dict1:
        wt[i] = prev_end_time
        total_wt += wt[i]
        prev_end_time += dict1[i][1]
        
        print(f"Process {i + 1}  runs from {wt[i]} to {prev_end_time}")

    # Calculating average waiting time
    avg_wt = total_wt / n

    # Printing waiting times and average waiting time
    print("Waiting times:")
    for i in wt:
        print(f"Process {i + 1}: {wt[i]}")


    print(total_wt)
    print(f"Average waiting time: {avg_wt}")


n = int(input("Please enter the number of processes: "))

if (n > 0):
    PS_init(n, dict1)
else:
    print("Enter a value greater than 0")



