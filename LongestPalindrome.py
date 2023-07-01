"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:

        
       letters = {} #hashmap to hold our frequencies for each letter. Ex 1: {a:1, b:1, c:4, d:2}

       #Here we are doing a for loop to add these frequencies to the hashmap
       for char in s:
           if char not in letters:
                letters[char] = 1 #We are making the frequency 1 if the letter is not in the hashmap.
           else:
               letters[char] += 1 #IF the letter exists in the map, we are adding 1 to the frequency.
        
        #Variables for our result and odd number values.
       result, oddValues = 0, 0 

        #Now we will do a for loop through the letters hashmap.
       for i in letters.values():
            if i > 1: #IF the frequency is greater than one
                if i % 2 == 0: #Also if the remainder of I mod 2 is 0, we will add this to our result.
                    result += i
                else: #IF not, we are subtracting 1 from our results because it is an odd value.
                    result += i - 1
                    oddValues += 1 #Here we are adding to our oddValues variable because it is in an odd number.
            else:
                oddValues += 1 #If the frequency is not greater than one, we know it's an odd number.
        
       #If the odd values are greater than 0, we will add 1 to our result.
       if oddValues > 0:
            result += 1
        
       return result