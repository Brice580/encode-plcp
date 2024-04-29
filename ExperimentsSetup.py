import random
import string
import time
import csv
from SA import SuffixArray
from TestingUtils import generate_test_cases
import sys
import matplotlib.pyplot as plt
def generate_random_string(length, alphabet_size):
    alphabet = string.ascii_lowercase[:alphabet_size]  # Limit alphabet size
    return ''.join(random.choice(alphabet) for _ in range(length))
 
def run_tests():
    size = 10
    encoded_size = []
    regular_size = []
    encoded_runtime = []
    regular_runtime = []
    encoded_lcp_runtime = []
    regular_lcp_runtime = []
    while size <= 100000:
        average_encoded_size = 0
        average_regular_size = 0
        average_encoded_runtime = 0
        average_regular_runtime = 0
        average_encoded_lcp_runtime = 0
        average_regular_lcp_runtime = 0
        for i in range(5):
            case = generate_test_cases(1,4,size)[0]
            test_string = case['text']
            sa = SuffixArray(test_string)

            start_time = time.time()
            plcp_encoded = sa.getEncodedPLCP()
            time_encoded = time.time() - start_time
            size_encoded = sys.getsizeof(plcp_encoded)

            start_time = time.time()
            sa.construct_lcp_from_encoded_plcp(plcp_encoded)
            time_lcp_encoded = time.time() - start_time
            plcp_encoded = None

            start_time = time.time()
            plcp_regular = sa.getPLCP()
            time_regular = time.time() - start_time
            size_regular = sys.getsizeof(plcp_regular)     

            start_time = time.time()
            sa.construct_lcp_normal(plcp_regular)
            time_lcp_regular = time.time() - start_time
            plcp_encoded = None

            average_encoded_size += size_encoded
            average_regular_size += size_regular

            average_encoded_runtime += time_encoded
            average_regular_runtime += time_regular

            average_encoded_lcp_runtime += time_lcp_encoded
            average_regular_lcp_runtime += time_lcp_regular

        
        average_encoded_size /= 5
        average_regular_size /= 5

        average_encoded_runtime /= 5
        average_regular_runtime /= 5

        average_encoded_lcp_runtime /= 5
        average_regular_lcp_runtime /= 5

        encoded_size.append((size, average_encoded_size))
        regular_size.append((size, average_regular_size))

        encoded_runtime.append((size, average_encoded_runtime))
        regular_runtime.append((size, average_regular_runtime))

        encoded_lcp_runtime.append((size, average_encoded_lcp_runtime))
        regular_lcp_runtime.append((size, average_regular_lcp_runtime))

        size *= 10

    # Separating x and y coordinates
    print(regular_runtime)
    print(regular_lcp_runtime)

    regular_x, regular_y = zip(*regular_size)
    encoded_x, encoded_y = zip(*encoded_size)

    # Plotting
    plt.figure(figsize=(8, 4))
    plt.xscale('log')
    plt.plot(regular_x, regular_y, label='Regular Size', marker='o')
    plt.plot(encoded_x, encoded_y, label='Encoded Size', marker='o')

    # Adding labels and title
    plt.xlabel('Input String Length')
    plt.ylabel('Average Size (Bytes)')
    plt.title('Regular and Succint PLCP Sizes by String Length')
    plt.legend()

    # Show the plot
    plt.savefig('sizes')

    # Separating x and y coordinates
    regular_x, regular_y = zip(*regular_runtime)
    encoded_x, encoded_y = zip(*encoded_runtime)

    # Plotting
    plt.figure(figsize=(8, 4))
    plt.xscale('log')
    plt.plot(regular_x, regular_y, label='Regular Runtime', marker='o')
    plt.plot(encoded_x, encoded_y, label='Encoded Runtime', marker='o')

    # Adding labels and title
    plt.xlabel('Input String Length')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Regular and Succint PLCP Construction Runtimes by String Length')
    plt.legend()

    # Show the plot
    plt.savefig('pclp_construction_runtime')

    # Separating x and y coordinates
    regular_x, regular_y = zip(*regular_lcp_runtime)
    encoded_x, encoded_y = zip(*encoded_lcp_runtime)

    # Plotting
    plt.figure(figsize=(8, 4))
    plt.xscale('log')
    plt.plot(regular_x, regular_y, label='Regular Runtime', marker='o')
    plt.plot(encoded_x, encoded_y, label='Encoded Runtime', marker='o')

    # Adding labels and title
    plt.xlabel('Input String Length')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Regular and Succint LCP from PLCP Runtimes by String Length')
    plt.legend()

    # Show the plot
    plt.savefig('lcp_runtime')

if __name__ == '__main__':
    run_tests()
