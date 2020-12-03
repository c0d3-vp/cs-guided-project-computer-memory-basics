"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    ascii_values = [ord(l) for l in string] # O(n) time, O(n) space 
​
    for i, v in enumerate(ascii_values): # O(n) time 
​
    # for i in range(len(ascii_values)):
    #     v = ascii_values[i]
​
        if 65 >= v and v <= 90: # O(1)
            # lowercasing the letter 
            ascii_values[i] += 32 # O(1)
    
    # turn the ascii values back into a string 
    # letters = [chr(v) for v in ascii_values]
​
    return ''.join(chr(v) for v in ascii_values) # O(n) time
​
​
print(to_lower_case("LambdaSchool"))

