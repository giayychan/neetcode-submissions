class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        targetCounts, windowCounts = [0] * 26, [0] * 26

        for i in range(len(s1)):
            tIndex = ord(s1[i]) - ord('a')
            wIndex = ord(s2[i]) - ord('a')
            targetCounts[tIndex] += 1
            windowCounts[wIndex] += 1
        
        matches = 0
        for i in range(26):
            if targetCounts[i] == windowCounts[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            windowCounts[index] += 1
            if targetCounts[index] == windowCounts[index]:
                matches += 1
            elif windowCounts[index] == targetCounts[index] + 1:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            windowCounts[index] -= 1
            if targetCounts[index] == windowCounts[index]:
                matches += 1
            elif windowCounts[index] == targetCounts[index] - 1:
                matches -= 1
            l += 1

        return matches == 26