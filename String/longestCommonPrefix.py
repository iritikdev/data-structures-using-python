# Given a array of N strings, find the longest common prefix among all strings present in the array.


# Example 1:

# Input:
# N = 4
# arr[] = {geeksforgeeks, geeks, geek, geezer}
# Output: gee
# Explanation: "gee" is the longest common
# prefix in all the given strings.

def longestCommonPrefix(words):
    result = ""
    for i in range(len(words[0])):
        for word in words:
            if word[i] != words[0][i]:
                if result == "": return "-1"
                return result
        result+=words[0][i]
    
    return result

print(longestCommonPrefix(['hello', 'world']))
print(max([4,8,96]))