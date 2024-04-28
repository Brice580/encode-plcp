import math

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

    def getEncodedPLCP(self):
        phi = [0] * self.n
        for i in range(self.n):
            if self.ranks[i] == 0:
                phi[self.ranks[i]] = self.ranks[-1]
            else:
                phi[self.ranks[i]] = self.ranks[i - 1]

        l = 0
        encoded_plcp = [0] * self.n
        for i in range(self.n):
            p = phi[i]
            while i + l < self.n and p + l < self.n and self.T[i + l] == self.T[p + l]:
                l += 1
            encoded_plcp[i] = 2 * i + l  # Encoding the PLCP value
            l = max(l - 1, 0)
        return encoded_plcp




if __name__ == '__main__':
    sa = SuffixArray('banana$')
    x = sa.getPLCP()