import re

def requireInt(value,message):
    if not isinstance(value,int):
        raise ValueError(value,message)
    return value

def required(value,message):
    if not value:
        raise ValueError(value,message)
    return value

class Member(object):
    def __init__(self,id,name,email):
        self._id = id
        self._name = name
        self._email = email

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id = requireInt(value,"ID值必须为整数")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = required(value,"名称为必输项")

    @property
    def email(self):
        return self._name
    @name.setter
    def email(self,value):
        self._email = value