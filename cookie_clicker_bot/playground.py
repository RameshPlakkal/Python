import time
import timeit


start_time = time.time_ns()
timeout = start_time + 5*60

while start_time < timeout:
    print("Hello")
