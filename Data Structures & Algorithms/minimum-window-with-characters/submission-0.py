class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freq={}
        for ch in t:
            freq[ch]=freq.get(ch,0)+1
        window={}
        left=0
        have=0
        req=len(freq)
        mini=float('inf')
        start=0
        for right in range(len(s)):
            ch=s[right]
            window[ch]=window.get(ch,0)+1
            if ch in freq and window[ch] == freq[ch]:
                have += 1
            while have==req:
                if right-left+1<mini:
                    mini=right - left + 1
                    start = left
                window[s[left]] -= 1

                if s[left] in freq and window[s[left]] < freq[s[left]]:
                    have -= 1
                left += 1

        if mini == float('inf'):
            return ""

        return s[start:start + mini]



        