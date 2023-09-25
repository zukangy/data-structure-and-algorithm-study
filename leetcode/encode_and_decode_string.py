# 271. Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# You are not allowed to solve the problem using any serialize methods (such as eval).

# As my solution failed some edge cases, I adopted a solution shared on Leetcode that is very
# simple to understand and implement: https://leetcode.com/problems/encode-and-decode-strings/solutions/4053335/python3-simple-and-most-efficient-solution/


# This solution concatenate the length of each string with the string itself; and then in the decoder, 
# the target substrings in the encoded string are extracted based on the length of the substring that
# was encoded into it. 

# However, this solution is not 100% scalable as it was hardcoded to consider only strings no more than 3 digits (which is given by the question). 
def encode(strs):
        encoded_str = [f'{len(s):3}{s}' for s in strs]
        return ''.join(encoded_str)

def decode(s: str):
    decoded_strs = []
    i = 0

    while i < len(s):
        char_len = int(s[i : i  + 3])
        decoded_strs.append(s[i + 3 : i + char_len + 3])
        i += char_len + 3

    return decoded_strs


inputs = ["Hello", "World"]
print(encode(inputs))
print(decode(encode(inputs)))

inputs = ["#"]
print(encode(inputs))
print(decode(encode(inputs)))

inputs = ["",""]
print(encode(inputs))
print(decode(encode(inputs)))