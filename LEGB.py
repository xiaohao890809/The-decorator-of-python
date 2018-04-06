passline = 80

def func(val):
    passline = 95
    if val > passline :
        print('pass')
    else:
        print('fail')

    def fun_in():
        print(val)
    fun_in()

def Max(val1, val2):
    return max(val1, val2)

func(89)
print(Max(20,34))

# fail
# 89
# 34