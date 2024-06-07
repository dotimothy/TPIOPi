import machine
import time
import gc

# Run garbage collection before starting the benchmark
gc.collect()

# Set the clock frequency before starting the benchmark
machine.freq(270000000) # You can change this number to over- or under-clock

# Calculate the value of pi using the Bailey–Borwein–Plouffe formula
# n: Threshold 
def calculate_pi(n):
    pi = 0
    k = 0
    while k < n:
        pi += (1 / (16 ** k)) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
        k += 1
    return pi

# Time how long it takes to estimate pi
start_time = time.time_ns()
pi = calculate_pi(1500)
end_time = time.time_ns()
execution_time = round((end_time - start_time) / 1e9, 4)

# Results
print("Pi estimate:", pi)

print("Execution time:", execution_time, "seconds")