time_quantum = 5
processes = {"P1": [2, 0, 24], "P2": [1, 1, 3],
             "P3": [3, 2, 3], "P4": [2, 3, 0]}


copied_processes = processes.copy()


CPU_schedule = {}
temporary_dic = {}
total_time = 0
avg_waiting_time = 0
num_items = len(processes)


while True:
    for process, value in processes.items():
        if process not in copied_processes:
            continue

        if ((processes[process][2]) <= time_quantum):
            print(process+" [][][][][][][][] ")
            print("Process Runs For : " + str(processes[process][2]) + "\n")
            total_time += processes[process][2]
            copied_processes.pop(process)

        else:
            # processes[process] = value
            # copied_processes[process] = value
            print(process+" [][][][][][][][] ")
            print("Process Runs For : " + "5" + "\n")
            processes[process][2] = processes[process][2] - time_quantum
            total_time += 5
            temporary_dic[process] = value
            copied_processes.pop(process)
            copied_processes.update(temporary_dic)
            temporary_dic.clear()

    if bool(copied_processes) == False:
        break

print("Total Time : " + str(total_time))
print("Average Waiting Time :" + str(total_time/num_items))