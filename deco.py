
def dec(func):
    def in_dec(x,y):
        print('in_deco')
        func(x,y)
    print('call deco')
    return in_dec

@dec
def bar(x,y):
    print('in_bar',x+y)

# 装饰器的本质是对闭包的使用
bar(1,2)

# dec(bar) -> in_dec
# bar = in_dec
# bar() in_dec() bar()