
def func_150(val):
    passline = 90
    if val > passline :
        print('%d pass' %val)
    else:
        print('fail')

def func_100(val):
    passline = 60
    if val > passline :
        print('%d pass' %val)
    else:
        print('fail')

func_150(89)
func_100(89)

def set_passline(passline):
    def cmp(val):
        if val > passline:
            print('%d pass' % val)
        else:
            print('fail')
    return cmp

my_150 = set_passline(90)
my_100 = set_passline(60)
my_150(89)
my_100(89)