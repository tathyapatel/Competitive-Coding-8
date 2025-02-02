#76. Minimum Window Substring
"""
Time Complexity : O(m + n)
Space Complexity : O(n)
"""

class Solution:
    def minWindow(self, s, t):

        d1 = Counter(t)

        criteria = len(d1)

        start = 0
        end = 0

        final_start = 0
        final_end = 0
        
        curr = 0

        d2 = dict()

        ans = ""
        go = True

        while end < len(s):

            ch = s[end]
            d2[ch] = d2.get(ch, 0) + 1

            if ch in d1 and d2[ch] == d1[ch]:
                curr += 1

            while start <= end and curr == criteria:
                ch2 = s[start]

                #if r - l + 1 < len(ans):
                temp = s[start:end+1]
                
                if go == True: #First time assignment to ans
                    ans = temp
                    go = False
                
                #print(temp, ans)
                if len(temp) < len(ans):
                    ans = temp

                d2[ch2] -= 1
                
                if ch2 in d1 and d2[ch2] < d1[ch2]:
                    curr -= 1

                start += 1    

            end += 1    
        
        return ans
