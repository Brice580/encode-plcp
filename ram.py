import random
import string
import time
import os
import psutil
import csv
from SuffixArray import SuffixArray

def generate_random_string(length, alphabet_size):
    alphabet = string.ascii_lowercase[:alphabet_size]  # Limit alphabet size
    return ''.join(random.choice(alphabet) for _ in range(length))

def measure_memory_process():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)  # memory in MB

def run_test_cases(num_cases, min_len, max_len, alphabet_size, output_file):
    results = []
    for _ in range(num_cases):
        length = random.randint(min_len, max_len)
        test_string = generate_random_string(length, alphabet_size)
        sa = SuffixArray(test_string)
        
        start_time = time.time()
        plcp_regular = sa.getPLCP()
        time_regular = time.time() - start_time
        mem_usage_regular = measure_memory_process()

        start_time = time.time()
        plcp_encoded = sa.getEncodedPLCP()  # Assuming you have a method similar to getPLCP
        time_encoded = time.time() - start_time
        mem_usage_encoded = measure_memory_process()

        results.append([length, mem_usage_regular, time_regular, mem_usage_encoded, time_encoded])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['String Length', 'Memory Usage Regular (MB)', 'Time Regular (s)',
                         'Memory Usage Encoded (MB)', 'Time Encoded (s)'])
        writer.writerows(results)

run_test_cases(100, 10, 30, 10, 'small_plcp_comparison_results.csv')
run_test_cases(100, 1000, 5000, 20, 'large_plcp_comparison_results.csv')

