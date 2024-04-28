import math
from bitarray import bitarray
from succinct.compressed_runs_bit_array import CompressedRunsBitArray


class SuffixArray:
    #sets self.T to the input string and self.ranks to the lexographical ordering
    def __init__(self, T):
        self.T = T + '$'
        self.n = len(self.T)
        self.ranks = [0]*self.n
        k = math.ceil(math.log2(len(self.T)))

        # constructing a_0 array out of inital rankings
        initialVals = []
        for c in self.T:
            if(c == '$'):
                initialVals.append(0)
            else:
                initialVals.append(ord(c) - ord('a') + 1)
        a = self.flattenRanks(initialVals)
        
        #compute A arrays from previous A arrays until reach final ranks
        for i in range(1, k+1):
            b = self.combineRanks(a, i)
            a = self.flattenRanks(b)

        #set ranks to inverse of a
        for i in range(0, self.n):
            self.ranks[a[i]] = i

    #combines the ranks of two cells according to the SA construction algorithm
    def combineRanks(self, prevA, i):
        b = []
        for j in range(0, len(prevA)):
            #check if range out of bounds
            if(j + 2**(i-1) < len(prevA)):
                b.append(prevA[j] * len(self.T) + prevA[j + 2**(i-1)])
            else:
                b.append(prevA[j] * len(self.T) + 1)
        return b
    
    #takes array of numbers and sets each index to the rank of its contents
    def flattenRanks(self, B):
        #the range of values in B is [0, n^2+n]. Create one hot encoding of values in B
        oneHotVal = [0] * (self.n**2 + self.n)
        for val in B:
            oneHotVal[val] = 1

        #create mapping of what value corresponds to what rank
        valToRank = {}
        currentRank = 0
        for i in range(0, len(oneHotVal)):
            if oneHotVal[i] == 1:
                valToRank[i] = currentRank
                currentRank += 1

        #compute ranks from B array and mappings
        ranks = []
        for val in B:
            ranks.append(valToRank[val])
        return ranks
    

    def getEncodedPLCP(self):
        phi = [0] * self.n
        for i in range(self.n):
            if self.ranks[i] == 0:
                phi[self.ranks[i]] = self.ranks[-1]
            else:
                phi[self.ranks[i]] = self.ranks[i - 1]

        l = 0
        # Calculate maximum index for bitarray
        max_index = 2 * self.n
        bit_arr = bitarray(max_index)
        bit_arr.setall(False)

        for i in range(self.n):
            p = phi[i]
            while i + l < self.n and p + l < self.n and self.T[i + l] == self.T[p + l]:
                l += 1
            bit_position = 2 * i + l  # Calculate the bit position
            bit_arr[bit_position] = True  # Set the bit at the calculated position
            l = max(l - 1, 0)

        compressed_bit_array = CompressedRunsBitArray(bit_array=bit_arr)
        return compressed_bit_array
    
    def getPLCP(self):
        #compute phi array of lexographically previous elements
        phi = [0] * self.n
        for i in range (0, self.n):
            if self.ranks[i] == 0:
                phi[self.ranks[i]] = self.ranks[-1]
            phi[self.ranks[i]] = self.ranks[i-1]

        #compute plcp
        l = 0
        pclp = []
        for i in range(0, self.n):
            p = phi[i]
            while self.T[i + l] == self.T[p + l]:
                l += 1
            pclp.append(l)
            l = max(l - 1, 0)
        
        return pclp
        
    def construct_lcp_normal(self):
        plcp = self.getPLCP()
        
        lcp = [0] * self.n
        
        for i in range(1, self.n):  
            lcp[i] = plcp[self.ranks[i]]  
        
        lcp[0] = 0
        
        return lcp

    def construct_lcp_from_encoded_plcp(self):

        encoded_plcp = self.getEncodedPLCP()
        lcp = [0] * self.n
        
        for i in range(1, self.n):  
            # use select to find the position of the i-th 1 which represents the encoded PLCP value

            encoded_index = encoded_plcp.select(self.ranks[i])  # select is 0-based
            plcp_value = encoded_index - 2 * (self.ranks[i])  # Decode PLCP[i] using the formula PLCP[i] = j - 2i
            lcp[i] = plcp_value
        
        # The LCP value corresponding to the first index is always 0
        lcp[0] = 0
        
        return lcp
    

if __name__ == '__main__':
    sa = SuffixArray('gatagaca')
    print('SA = ', sa.ranks)
    print('PLCP = ', sa.getPLCP())
    print('PLCP = ', sa.getEncodedPLCP())
    print("LCP = ", sa.construct_lcp_normal())
    print("LCP = ", sa.construct_lcp_from_encoded_plcp())

