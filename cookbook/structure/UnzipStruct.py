# 1解压序列赋值给多个对象
p = (4,5)
x,y = p
print(x)
print(y)

data = ["Alice",50,91.1,(2012,12,21)]
name,shares,price,date = data
print(name)

name,shares,price,(year,month,day) = data
print(month)

str = "hello"
a,b,c,d,e = str
print(e)

data = ["Alice",50,91.1,(2012,12,21)]
name,_,price,(year,_,day) = data
print(day)