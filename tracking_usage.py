# WHEN YOU IMPORT THIS FILE AND YOU CALL A FUNCTION USE IT LIKE THIS: (tu.track_time(lambda: hard_chaine.find(motif)) with the lambda inside


import time
import tracemalloc

def track_time(func, *args, **kwargs):
    total_time = 0
    n = 100 # FOR THE AVERAGE (TO SAY REPEAT THIS 10 TIME AND GIVE THE AVERAGE)
    for _ in range(n):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        total_time += (end_time - start_time)
    average_time = total_time / n
    return average_time


def track_memory(func, *args, **kwargs):
    tracemalloc.start()
    func(*args, **kwargs)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_memory_kb = peak / 1024
    return peak_memory_kb

