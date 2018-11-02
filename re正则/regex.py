import re

pattern = r'\d+'
s = '2008年事情多，08奥运，512地震'

#返回可迭代对象
it = re.finditer(pattern,s)

for i in it:
    #match对象group函数获取匹配内容
    print(i.group())

try:
    obj = re.fullmatch(r'\w+','hello 1973')
    print(obj.group())
except AttributeError as e:
    print(e)

obj = re.match(r'[A-Z]\w+','Hello world')
print(obj.group())

obj = re.search(r'\d+',s)
print(obj.group())

