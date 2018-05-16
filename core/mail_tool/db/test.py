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
#=====================================================================
# def login():
#     print('in login')
#
#
# def printdebug(func):
#     def __decorator():
#         print('enter the login')
#         func()
#         print('exit the login')
#
#     return __decorator  # function as return value
#
#
# debug_login = printdebug(login)  # function assign to variable
#
# debug_login()  # execute the returned function


# def dec1(func):
#     def wrapper(name):
#         print("包装开始")
#         func(name)
#         print("包装结束")
#     return wrapper
#
# @dec1
# def printName(name):
#     print("我爱你%s"%name)
#
# if __name__ == '__main__':
#     printName("中国")

#==========================================================================
# def dec2(msg):
#     def _dec2(fuc):
#         def wrapper(name):
#             print("包装开始")
#             print("包装器信息:%s"%msg)
#             fuc(name)
#             print("包装结束")
#         return wrapper;
#     return _dec2
#
# @dec2("我是一个小小的包装器")
# def printName(name):
#     print("我爱你%s"%name)
#
# if __name__ == '__main__':
#     printName("中国")

#==============================================================
# class Member(object):
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self,value):
#         self._name = value
#
# member = Member("张三",15)
# member.name = "哈哈哈"
# print(member._name)

#===============================================================
class Animal(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value


ani = Animal("长颈鹿")
ani.name = "兔子"
print(ani.name)