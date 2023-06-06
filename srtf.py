# priority, arrival time, burst time
processes = {"P1": [2, 0, 8], "P2": [1, 1, 4],
             "P3": [3, 2, 9], "P4": [2, 3, 5]}

waiting_queue = {}
current_time = 0
# CPU_schedule = {}
temporary_dic = {}
process_with_CPU = {}
num_items = len(processes)

# sort process according to arrival time
processes = dict(sorted(processes.items(), key=lambda x: x[1][1]))


while True:
    if (all(process[2] == 0 for process in processes.values())):
        break

    for process, value in processes.items():
        # if burst time is 0, process not given to cpu
        if (processes[process][2] == 0):
            continue

        # processes added to waiting queue, if it is equal to current time
        if (current_time == value[1]):

            waiting_queue[process] = value

    # waiting sorted according to burst time
    waiting_queue = dict(sorted(waiting_queue.items(), key=lambda x: x[1][2]))
    copied_waiting_queue = waiting_queue.copy()

    for waiting_process, value in copied_waiting_queue.items():

        if bool(process_with_CPU) == False:
            # burst time decreaments by 1
            waiting_queue[waiting_process][2] = waiting_queue[waiting_process][2] - 1

            # process scheduled to cpu
            # CPU_schedule[waiting_process] = value

            # a reference created for the precess who got the cpu and process removed from waiting_queue
            process_with_CPU[waiting_process] = waiting_queue.pop(
                waiting_process)

            # printing proocess
            keys_of_item_with_CPU = process_with_CPU.keys()
            keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
            key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

            print(key_of_item_with_CPU + " [][][][][][][][] ")
            print("Process runs for 1s \n")

            # current time increamented
            current_time += 1
            break

        # If cpu not empty
        elif bool(process_with_CPU) == True:

            # First check if burst time of process with cpu is 0 or not

            key = process_with_CPU.keys()
            key_list = list(key)

            key2 = key_list[0]
            if (process_with_CPU[key2][2] != 0):

                # then check if burst time of process with current cpu is greater than the process in waiting queue
                if (waiting_queue[waiting_process][2] < process_with_CPU[key2][2]):

                    waiting_queue.update(process_with_CPU)
                    process_with_CPU.clear()

                    # burst time of new process getting the cpu decreamented
                    waiting_queue[waiting_process][2] = waiting_queue[waiting_process][2] - 1

                    # process scheduled to cpu
                    # CPU_schedule[waiting_process] = value

                    # a reference created for the precess who got the cpu and process removed from waiting_queue
                    process_with_CPU[waiting_process] = waiting_queue.pop(
                        waiting_process)

                    # printing proocess
                    keys_of_item_with_CPU = process_with_CPU.keys()
                    keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                    key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                    print(key_of_item_with_CPU + " [][][][][][][][] ")
                    print("Process runs for 1s \n")

                    # current time increamented
                    current_time += 1
                    break

                # if burst time of process with current cpu is less than the process in waiting queue
                elif (waiting_queue[waiting_process][2] > process_with_CPU[key2][2] and process_with_CPU[key2][2] != 0):

                    # burst time of process with cpu decrements
                    process_with_CPU[key2][2] = process_with_CPU[key2][2] - 1

                    # printing proocess
                    keys_of_item_with_CPU = process_with_CPU.keys()
                    keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                    key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                    print(key_of_item_with_CPU + " [][][][][][][][] ")
                    print("Process runs for 1s \n")

                    # current time increamented
                    current_time += 1
                    break

                else:
                    process_with_CPU[key2][2] = process_with_CPU[key2][2] - 1

                    # printing proocess
                    keys_of_item_with_CPU = process_with_CPU.keys()
                    keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                    key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                    print(key_of_item_with_CPU + " [][][][][][][][] ")
                    print("Process runs for 1s \n")

                    # current time increamented
                    current_time += 1

            # check if burst time of process with cpu is equal to 0
            elif (process_with_CPU[key2][2] == 0):

                process_with_CPU.clear()

                # burst time of new process getting the cpu decreamented
                waiting_queue[waiting_process][2] = waiting_queue[waiting_process][2] - 1

                # process scheduled to cpu
                # CPU_schedule[waiting_process] = value

                # a reference created for the precess who got the cpu and process removed from waiting_queue
                process_with_CPU[waiting_process] = waiting_queue.pop(
                    waiting_process)

                if (bool(waiting_queue) == False):
                    waiting_queue.update(process_with_CPU)

                # printing proocess
                keys_of_item_with_CPU = process_with_CPU.keys()
                keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                print(key_of_item_with_CPU + " [][][][][][][][] ")
                print("Process runs for 1s \n")

                # current time increamented
                current_time += 1
                break

    if (all(process[2] == 0 for process in processes.values())):
        break


# print(CPU_schedule)
print("Total Time : " + str(current_time))
print("Average Waiting TIme :" + str(current_time/num_items))