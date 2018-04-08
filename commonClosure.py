
def my_sum(*arg):
    # 在后面的闭包函数里调用
    # if len(arg) == 0:
    #     return 0
    # for item in arg:
    #     if not isinstance(item, int):
    #         return 0
    return sum(arg)

def my_average(*arg):
    return sum(arg)/len(arg)

def dec(func):
    def dec_in(*arg):
        # 公共方法写在这里面
        if len(arg) == 0:
            return 0
        for item in arg:
            if not isinstance(item, int):
                return 0
        # 这里直接进行函数调用
        return func(*arg)
    return dec_in

my_sum = dec(my_sum)
my_average = dec(my_average)
print(my_sum(1,2,3))
print(my_sum(1,2,3,'4'))
print(my_average(1,2,3))
print(my_average())