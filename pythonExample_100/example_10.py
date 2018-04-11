#题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def three_numbers(index=5):
    range_a = range(1, index)
    for i in range_a:
        for j in range_a:
            if j == i:
                continue
            for k in range_a:
                if k == j or k == i:
                    continue
                print (i, j, k)
three_numbers(5);


