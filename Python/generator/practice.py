import random as rd

def add(li):
    sum = 0
    print("add start")
    for i in li:
        sum += i
    print("sum = {}".format(sum))
    yield sum
    return 'done'

def delegate(li):
    ad = add(li)
    print("delegate start")
    ret = yield from ad
    
    return ret


if __name__ == "__main__":
    li = [rd.randint(1,20) for _ in range(5)]
    print(li)
    del_func = delegate(li)
    print(del_func.send(None))
    #print(del_func.send(li))
