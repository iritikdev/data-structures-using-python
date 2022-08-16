def removeDuplicates(input):
    ans = ""
    for char in input:
        if char not in ans:
            ans += char
    print(ans)


removeDuplicates("geeksforgeeks")