import time

# Function responsible for simulating Non-Pipelined execution
def simulate_time():

    # Read all instructions from the input file
    data = open("mips_instructions.asm").readlines()

    # Count the number of instructions
    count = len(data)

    # Display simulation title
    print("====================================")
    print("      Non-Pipelined Simulation")
    print("====================================\n")

    # Process instructions one by one
    for _ in data:

        # Simulate 800 microseconds execution time per instruction
        time.sleep(0.0008)

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
    print(f"\nTime taken by Nonpipelined Execution = {(end_time - start_time)} seconds\n")