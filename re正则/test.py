#命令行输入端口名称，得出IP地址

import re
import sys

f = open('1.txt')
if len(sys.argv) < 2:
    sys.exit('输入错误')
port = sys.argv[1]
#print(port)
while True:
    data = ''

    if sys.argv[1] in data:

        pattern = r'\d+\.?\d+\.\d+\.+\d+/?\d+'
        l = re.findall(pattern,data)
        print(l)
    if data == '\n':
        break

def get_address(port):
    f = open('1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        try:
            port = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue

    return address


if __name__ == '__main__':
    port = sys.argv[1]
    print(get_address(port))
