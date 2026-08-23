class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq={}
        for ch in s1:
            freq[ch]=freq.get(ch,0)+1

        k=len(s1)
        window={}
        for i in range(k):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == freq:
            return True
        left = 0
        for right in range(k, len(s2)):

            # Add new character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Remove old character
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            # Check current window
            if window == freq:
                return True

        return False

        

        
        