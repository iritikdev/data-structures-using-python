def romanToDecimal(input):
    symbol = {'I' : 1, 'V' : 5, "X" : 10, "L" : 10, "C" : 100,"D" : 500, "M" : 1000 }
    value = 0
    for i in range(len(input)-1, -1, -1):
        if i != len(input) -1 and symbol[input[i]] < symbol[input[i+1]]:
            value -= symbol[input[i]]
        else:value += symbol[input[i]]
    return value

res = romanToDecimal("MCCCLXXXVII")
print(res)