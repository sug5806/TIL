def read_data(filename):
    f = open(filename,'rt')
    line = f.readline()
    while line != '':
        print(f'read_data : {line}')
        yield int(line)        
        line = f.readline()
        
def delegate(*filelist):
    for i in filelist:
        g = read_data(i)
        print(f'delegate : {i}')
        ret = yield from g   
        print("sending...")
    
def make_sum(gen):
    result = 0 
    try :
        while True:
            result += next(gen)
        print(result)    
    except StopIteration as e:
        print(result)
        
if __name__=="__main__":
    make_sum(delegate('data1.txt','data2.txt','data3.txt'))
