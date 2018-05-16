# def dec1(fuc):
#     def dec(*args):
#         print("哈哈哈")
#         fuc(*args)
#         print("呵呵")
#         return None
#     return dec
#
# @dec1
# def test_1(info):
#     print(info)
#     return None
#
# test_1("我爱你，中国")

# def dec2(fuc):
#     print("呵呵呵")
#     fuc()
#     print("哈哈哈")
#
# def test():
#     print("小时")
#
# test1 = dec2(test)
#
# test1()
# test1()

def login():
    print('in login')


def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')

    return __decorator  # function as return value


debug_login = printdebug(login)  # function assign to variable

debug_login()  # execute the returned function