import time
import threading
import queue

# Function responsible for simulating Pipelined execution
def simulate_time():

    # Read all instructions from the input file
    data = open("mips_instructions.asm").readlines()

    # Count the number of instructions
    count = len(data)

    # Create 5 queues representing the pipeline stages
    stages = [queue.Queue() for _ in range(5)]

    # Display simulation title
    print("====================================")
    print("        Pipelined Simulation")
    print("====================================\n")

    # Function executed by each pipeline stage
    def worker(i):

        # Keep the stage running
        while True:

            # Get instruction from current stage
            item = stages[i].get()

            # Stop thread when None is received
            if item is None:
                break

            # Simulate stage execution time
            time.sleep(0.0002)

            # Pass instruction to the next stage
            if i < 4:
                stages[i + 1].put(item)

            # Mark current task as completed
            stages[i].task_done()

    # Store all pipeline threads
    threads = []

    # Create and start the 5 pipeline stages
    for i in range(5):

        t = threading.Thread(target=worker, args=(i,))

        t.start()

        threads.append(t)

    # Feed instructions into the first stage
    for instruction in data:

        stages[0].put(instruction)

        # Delay between stage starts
        time.sleep(0.0002)

    # Wait until all stages finish processing
    for stage in stages:
        stage.join()

    # Send termination signal to all stages
    for stage in stages:
        stage.put(None)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Display the total number of processed instructions
    print(f"Instructions Processed : {count}")


# Program execution starts here
if __name__ == "__main__":

    # Record start time
    start_time = time.time()

    # Run the simulation
    simulate_time()

    # Record end time
    end_time = time.time()

    # Display total execution time
    print(f"\nTime taken by Pipelined Execution = {(end_time - start_time)} seconds\n")