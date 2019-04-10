def find_ins_idx(r, v):
    for i in range(len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print(a, " ", result)
    return result

d = [2, 4, 6, 1, 3,10, 53, 5, 8, 6]
print(ins_sort(d))
    