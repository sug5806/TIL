import random as rd

def re(li, leng):
    if leng == 1:
        return li[leng-1]

    max_val = re(li, leng-1)

    if max_val >= li[leng-1]:
        return max_val
    else:
        return li[leng]

li = []
for _ in range(10):
    li.append(rd.randint(0,100))

print(li)
print(re(li, len(li)))
