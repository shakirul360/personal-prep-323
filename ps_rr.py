
dict1 = {}

def PS_init(n, dict1):
    
    tq = int(input("Enter the Time Quantum Value: "))
    print("Enter the priorities and their burst time separated by a space: ")
    for i in range(0, n):
        print(f"Process no: {i}")

        pri, bt = map(int, input().split())

        if pri not in dict1:
            dict1[pri] = {}

        dict2 = dict1[pri]
        dict2[i] = bt



    dict1 = dict(sorted(dict1.items(), key=lambda x: x))
    print_processes(dict1)
    PS_RR(n, dict1, tq)
    #PS(dict1, tq)

def print_processes(dict1):
    print("Priority --- Pi --- BT")
    
    for i in dict1:
        print(i, dict1[i]);


def print_waits(waits, n):

        # Printing waiting times and average waiting time
    print("Waiting times:")
    for i in waits:
        print(f"Process {i}: {waits[i]}")



def PS_RR(n, dict1, tq):
    waits = {key: 0 for key in range(n)} #total waiting time
    prev_end = {key: 0 for key in range(n)} #previous waiting time

    print("Time quantum = ", tq)


    cur_t = 0
    
    print(dict1)
    for i in dict1:
        cur_prio = dict1[i]

        while any(value > 0 for value in cur_prio.values()): # checking if priority has completed RR

            for j in cur_prio:     #j = process, curprio[j] = bt
                if (cur_prio[j] > 0):
                    st = cur_t
                    waits[j] += cur_t - prev_end[j]

                    if (cur_prio[j] >= tq):    #comparing bt with tq
                        cur_prio[j] -= tq
                        cur_t += tq
                    else:
                        cur_t += cur_prio[j]
                        cur_prio[j] = 0

                    prev_end[j] = cur_t

                print(f"Process {j}  runs from {st} to {cur_t}")


    print_waits(waits, n)

    # Calculating average waiting time
    avg_wt = sum(waits.values()) / n

    print(f"Average waiting time: {avg_wt}")


n = int(input("Please enter the number of processes: "))

if (n > 0):
    PS_init(n, dict1)
else:
    print("Enter a value greater than 0")
