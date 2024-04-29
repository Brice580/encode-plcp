import random
import string

def compute_plcp_naive(input_string, suffix_array):

    input_string += '$'

    n = len(input_string)
    lcp = [0] * n

    for i in range(1, n):
        
        lcp_length = 0
        x = suffix_array[i]
        y = suffix_array[i - 1]

        while x < n and y < n and input_string[x] == input_string[y]:
            lcp_length += 1
            x += 1
            y += 1
            
        
        lcp[i] = lcp_length

    plcp = [0] * n
    for i in range(1, n):
        plcp[suffix_array[i]] = lcp[i]

    return plcp


def construct_suffix_array_naive(string):

    string += "$"
    suffixes = []
    for i in range(len(string)):
        suffixes.append((string[i:], i))        
    suffix_array = []
    
    for suffix in sorted(suffixes):
        suffix_array.append(suffix[1])
    return suffix_array


def generate_test_cases(instances, alphabet_size, length):
    tests = []
    for i in range(instances):
        
        text = ''.join(random.choice(string.ascii_lowercase[:alphabet_size]) for _ in
        range(length))

        
        sa_naive = construct_suffix_array_naive(text)
        plcp_naive = compute_plcp_naive(text, sa_naive)
        
      
        tests.append({
            'text': text, 
            'expectedSA':sa_naive, 
            'expectedPCLP':plcp_naive
        })
        
    return tests
    
generate_test_cases(10, 26, 10)
