from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:   #["lc","cl","gg"]
        count = Counter(words)  #creating a dict upon words  {"lc":1,"cl":1,"gg":1}
        length = 0   #initialize lenght as 0
        for word in list(count):   #cnverting into list which will be ["lc":1,"cl":1,"gg":1]
            rev = word[::-1]     #reverse the current word
            if word != rev:      # if there are not equal ==> word = lc and rev = word[::-1] = cl
                pair_count = min(count[word], count[rev])    #to get a min_pair_count lets say lc and cl makes a single pair_count == 1
                length += pair_count * 4    #now we are having a palindromice double letter of length 4 beacuse lc and cl both having 4 letters thats why length will be 4
                count[word] -= pair_count   #we reduce its pair_count to reduce retundancy
                count[rev] -= pair_count   #as well as the reverse
            else:  #this is for gg which are symmetric palindromes
                pair_count = count[word] // 2    #here because if there are multiple symmetric palindromes within a dict, to get a pair_count we get by divides the count by 2
                length += pair_count * 4   #also we get 4 of length, it also involves  4 letters
                count[word] -= pair_count * 2  #we reduce both word and rev which are the same so we reduce it by 2 (count)
        for word in count:  #if there is a single symmetric palindrome
            if word[0] == word[1] and count[word] > 0:  # if first index element == 2nd element index and also count > 0
                length += 2 #we update length as 2
                break  #to get the first better length we break the loop
        return length  #simply return length
        
