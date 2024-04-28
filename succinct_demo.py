from bitarray import bitarray
from succinct.compressed_runs_bit_array import CompressedRunsBitArray

def encode_plcp_and_initialize_bitarray(plcp):
    n = len(plcp)
    max_index = 2 * n 

    
    bit_arr = bitarray(max_index) #max index is length
    bit_arr.setall(False)

    for i, value in enumerate(plcp):
        bit_position = 2 * i + value
        bit_arr[bit_position] = True  

    compressed_bit_array = CompressedRunsBitArray(bit_array=bit_arr)
    return compressed_bit_array

def main():
    plcp = [0, 3, 2, 1, 0, 0 ,0]

    compressed_bit_array = encode_plcp_and_initialize_bitarray(plcp)
    print(compressed_bit_array)
    print("Length of the compressed bit array:", len(compressed_bit_array))

    print("Rank of ones up to index 5:", compressed_bit_array.rank(5))
    print("Select the position of the 3rd '1':", compressed_bit_array.select(6))

if __name__ == "__main__":
    main()
