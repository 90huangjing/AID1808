import re

pattern = r'(ab)cd(?P<dog>ef)'
regex = re.compile(pattern)

#获取match对象
obj = regex.search('abcdefghi',pos=0,endpos=6)

#obj属性变量
print(obj.pos) #目标字串的开始位置
print(obj.endpos) #目标字串的结束位置
print(obj.re)#正则表达式
print(obj.string) #目标字符串
print(obj.lastgroup) #最后一组组名
print(obj.lastindex) #最后一组的序号
print('============================')

#属性方法
print(obj.start())#匹配内容的开始位置
print(obj.span()) #起止位置
print(obj.end()) #结束位置

print(obj.group())#获取正则匹配到的内容
print(obj.group(2))#获取某一子组对应的内容
print(obj.group('dog'))#获取dog组的内容

print(obj.groupdict())#获取捕获组字典,组名作为键，内容作为值,没有捕获组就不显示
print(obj.groups())#获取每个子组匹配到的内容