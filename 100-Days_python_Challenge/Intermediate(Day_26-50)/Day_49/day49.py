"""
Day 49: Profiling and Optimizing Python Code

Objective: Use 'cProfile' to find bottlenecks and 'timeit' to compare performance, 
demonstrating an optimization using a Set for faster lookups.
"""

import timeit
import cProfile
import random
import io
import pstats

# --- 1. Setup: Create Large Data Structures for Testing ---
# We will simulate a large dataset (e.g., 100,000 unique IDs)
DATA_SIZE = 100000
search_count = 1000

# Create the original list and the optimized set
large_data_list = [f"ID_{i:06}" for i in range(DATA_SIZE)]
large_data_set = set(large_data_list) # Optimization: Sets offer O(1) average lookup time

# Create a list of IDs to search for (some present, some not)
search_targets = [f"ID_{random.randint(0, DATA_SIZE * 2)}" for _ in range(search_count)]


# ==============================================================================
# 2. Inefficient Implementation: List Lookup (O(n) average)
# ==============================================================================
def find_ids_in_list(data_list, targets):
    """Checks if each target ID is present in the large list."""
    found_count = 0
    for target in targets:
        # Inefficient: 'in' operator on a list requires checking every element 
        # in the worst case (O(n) complexity).
        if target in data_list:
            found_count += 1
    return found_count

# ==============================================================================
# 3. Optimized Implementation: Set Lookup (O(1) average)
# ==============================================================================
def find_ids_in_set(data_set, targets):
    """Checks if each target ID is present in the large set."""
    found_count = 0
    for target in targets:
        # Efficient: 'in' operator on a set uses hashing, providing 
        # near-constant time lookups (O(1) complexity).
        if target in data_set:
            found_count += 1
    return found_count


# ==============================================================================
# A. Profiling with cProfile: Analyze the Inefficient Code
# ==============================================================================
print("=" * 60)
print("A. PROFILING WITH cProfile (Analyzing the Inefficient List function)")
print("=" * 60)

# Prepare the data and function call for cProfile
profile_command = (
    f"find_ids_in_list(large_data_list, search_targets)"
)

# Run the profiler and capture the output
# Using io.StringIO and pstats for cleaner, formatted output
s = io.StringIO()
ps = pstats.Stats(cProfile.Profile().run(profile_command), stream=s).sort_stats('tottime')
ps.print_stats(10) # Print the top 10 lines that took the most time

print(s.getvalue())
print("Interpretation: The majority of the time will be spent inside list's '__contains__' method (the 'in' operator).")
print("-" * 60)

# ==============================================================================
# B. Micro-benchmarking with timeit: Compare Performance
# ==============================================================================
print("\n" * 2)
print("=" * 60)
print("B. MICRO-BENCHMARKING WITH timeit (Comparing List vs. Set)")
print("=" * 60)

# The setup code provides the necessary variables to the timer function scope
setup_code = """
from __main__ import large_data_list, large_data_set, search_targets, find_ids_in_list, find_ids_in_set
"""

number_of_runs = 10 # How many times to execute the entire code block

# --- Measure List Performance ---
list_time = timeit.timeit(
    stmt="find_ids_in_list(large_data_list, search_targets)", 
    setup=setup_code, 
    number=number_of_runs
)

# --- Measure Set Performance ---
set_time = timeit.timeit(
    stmt="find_ids_in_set(large_data_set, search_targets)", 
    setup=setup_code, 
    number=number_of_runs
)


print(f"Total time for List Lookup ({search_count * number_of_runs} lookups):")
print(f"  -> {list_time:.4f} seconds")

print(f"\nTotal time for Set Lookup ({search_count * number_of_runs} lookups):")
print(f"  -> {set_time:.4f} seconds")

if list_time > 0:
    speedup = list_time / set_time
    print(f"\nOptimization Result: Set lookup was approximately {speedup:.2f} times faster!")

print("-" * 60)
print("Conclusion: By profiling (cProfile), we identify the lookup ('in' operator) as the bottleneck. \nWe then micro-benchmark (timeit) the optimized solution (Set) and confirm a significant speedup.")