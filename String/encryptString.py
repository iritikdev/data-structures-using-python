# Encrypt the string - 2    
# https://practice.geeksforgeeks.org/problems/encrypt-the-string-21117/1

def decryptString(inputText):
    frequency = dict()
    hexa = [0,1,2,3,4,5,6,7,8,9,'A','B', 'C', 'D', 'E', 'F']
    for char in inputText:
        frequency[char] = frequency.get(char,0) + 1
    text = ''
    for k,v in frequency.items():
        text = text + str(k) + str(hexa[v]).lower()
    return text[::-1]
result = decryptString("abbc")
print(result)


map1 = {"A" : 2, "C" : 5}
print(map1.values())
x = len(map1)
print(x)

