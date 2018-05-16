import re

def requireInt(value,message):
    if isinstance(value,int) != True:
        raise ValueError(value,message)
    return value
class Member(object):
    def __init__(self,id,name,email):
        self.__id = id
        self.__name = name
        self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = requireInt(value,"ID值必须为整数")


