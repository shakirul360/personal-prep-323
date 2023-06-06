import time

# First Come First Serve Algorithm
def fcfs(process_queue, count_process):
    # Making a copy of our ready queue
    process_queue_fcfs = process_queue.copy()

    # To keep track of run time and wait time
    run_time = 0
    wait_time = 0

    for i in range(5):
        time.sleep(1)
        print(".")

    # Applying FCFS logic
    print("Using FCFS: ")
    for item in process_queue:
        run_time+=process_queue[item] 
        del process_queue_fcfs[item]
        if process_queue_fcfs:
            wait_time +=  run_time  
        time.sleep(2)
        print("Process: ",item," ",end="")
        for i in range(10):
            print('[]', end="", flush=True)
            time.sleep(0.5)
        print()
        print(item, ": completed. Time: ", run_time)

    # Calculate and print Average Wait Time
    avg_wait = wait_time/count_process
    time.sleep(2)
    print("Average waiting time: ", avg_wait)
    
# Main function
if __name__ == '__main__':

    # Declaring our dictionary to store processes and their burst times as key-value pairs in a ready queue
    process_queue = {}

    # Keeping track of the number of processes
    count_process = 0

    # Taking input
    quantum = int(input("Please enter quantum time: "))
    print("Please enter processes with burst time: ")
    print("Press q to quit.")
    while True:
        process = input("Enter process: ")
        if process == 'q':
            print("CPU scheduling will begin now...")
            time.sleep(2)
            break
        count_process += 1
        burst_time = int(input("Enter burst time: "))
        process_queue[process] = burst_time

    # Calling our FCFS algorithm on given processes
    fcfs(process_queue, count_process)