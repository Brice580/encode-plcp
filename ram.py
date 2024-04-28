import random
import string
import time
import csv
from memory_profiler import memory_usage
from SuffixArray import SuffixArray  # Ensure this import works based on your project structure

def generate_random_string(length, alphabet_size):
    alphabet = string.ascii_lowercase[:alphabet_size]  # Limit alphabet size
    return ''.join(random.choice(alphabet) for _ in range(length))

def measure_function_memory_usage(func, *args, **kwargs):
    mem_usage_before = memory_usage(-1, interval=0.01, timeout=1)
    result = func(*args, **kwargs)
    mem_usage_after = memory_usage(-1, interval=0.01, timeout=1)
    return result, max(mem_usage_after) - min(mem_usage_before)

def run_test_cases(num_cases, min_len, max_len, alphabet_size, output_file):
    results = []
    for _ in range(num_cases):
        length = random.randint(min_len, max_len)
        test_string = generate_random_string(length, alphabet_size)
        sa = SuffixArray(test_string)
        
        # Measure memory and time for regular PLCP
        start_time = time.time()
        plcp_regular, mem_usage_regular = measure_function_memory_usage(sa.getPLCP)
        time_regular = time.time() - start_time

        # Measure memory and time for encoded PLCP
        start_time = time.time()
        plcp_encoded, mem_usage_encoded = measure_function_memory_usage(sa.getEncodedPLCP)
        time_encoded = time.time() - start_time

        results.append([length, mem_usage_regular, time_regular, mem_usage_encoded, time_encoded])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['String Length', 'Memory Usage Regular (MB)', 'Time Regular (s)',
                         'Memory Usage Encoded (MB)', 'Time Encoded (s)'])
        writer.writerows(results)

# Example usage
run_test_cases(10, 5, 10, 10, 'small_plcp_comparison_results.csv')
run_test_cases(10, 10000, 11000, 10, 'large_plcp_comparison_results.csv')
