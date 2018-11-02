import re

# s = 'Hello world'
# pattern = r'hello'

# regex = re.compile(pattern,flags=re.I)#匹配时忽略大小写


# s = '''Hello world
# hello kitty
# 你好，北京'''
# pattern = r'.+'

# regex = re.compile(pattern,flags=re.S)#可以匹配换行，打印出三行,不写flags时，只打印出第一行

# s = '''Hello world
# nihao beijing'''
# pattern = r'beijing$'

# regex = re.compile(pattern,flags=re.M) #匹配每一行的开始和结束位置

s = 'Hello world'
pattern = r'''Hello#匹配Hello
\s+#匹配空格
world#匹配world
'''

regex = re.compile(pattern,flags=re.X)


try:
    s = regex.search(s).group()
except Exception:
    print('没有匹配到内容')
else:
    print(s)

