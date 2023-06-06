import time

# Shortest Job First Algorithm
def sjf(process_queue, count_process):
    # Making a copy of our ready queue
    process_queue_sjf = process_queue.copy()

    for i in range(5):
        time.sleep(2)
        print(".")

    print("Using SJF: ")

    # Sort queue with respect to burst time
    process_queue_sjf = dict(sorted(process_queue_sjf.items(), key=lambda x:x[1]))
    process_queue_sjf2 = process_queue_sjf.copy()

    # To keep track of run time and wait time
    run_time = 0
    wait_time = 0

    # Applying SJF logic
    for item in process_queue_sjf:
        run_time+=process_queue_sjf[item] 
        del process_queue_sjf2[item]
        if process_queue_sjf2:
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

    # Calling our SJF algorithm on given processes
    sjf(process_queue, count_process)