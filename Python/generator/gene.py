# 데이터를 읽어오는 delegate
# read, delegate, make_sum

def read_data(filename):
    print("read_data start")
    r = delegate()
    f = open(filename, 'rt')
    while True: 
        line = f.readline()
        yield from delegate(line)  
    return "end" 

def delegate(data):
    print("delegate start")
    sum_data = make_sum(data)
    ret = yield from sum_data # list
     
    return ret
    

def make_sum(data):
    sum = 0
    print("sum data")
    for i in data:
        sum += i 
    
if __name__ == "__main__":
    g = delegate("data1.txt")
    next(g)
    next(g)
    next(g)
    next(g)
    next(g)
    next(g)   
    next(g) 
    next(g) 