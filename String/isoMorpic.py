def areIsomorphic(str1,str2):
    m1, m2 = {}, {}
    for i in range(len(str1)):
        if(str1[i] not in m1 and str2[i] not in m2 or m1[str1[i]] != m2[str2[i]]): return False
        else:
            m1[str1[i]] = i
            m2[str2[i]] = i
    return True
        
res = areIsomorphic("aab", "xxy")
print(res)