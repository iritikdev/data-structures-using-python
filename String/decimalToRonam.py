def String_compression01(st):
	result = st[0]
	for i in range(1, len(st)):
		if(st[i] != st[i-1]):
			result += st[i]
	print(result)
    
def String_compression02(st):
	c = 1
	result = st[0]
	for i in range(1, len(st)):
		if(st[i] == st[i-1]):
			c+=1
		else:
			if c > 1:
				result += str(c)
				c = 1
			result += st[i]
	if c > 1 : c = 1
	print(result)

String_compression01("aaaaaaabbbbbbccccccddddwwqqrec")
String_compression02("aaaaaaabbbbbbccccccddddwwqqrec")

# abcdwqrec
# a7b6c6d4w2q2rec

# abcdwqre
# a7b6c7d4w2q2re