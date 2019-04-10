def linear_search(num):
    stu_num = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    leng = len(stu_name)
    for i in range(leng):
        if num == stu_num[i]:
            return stu_name[i]            

print(linear_search(14))