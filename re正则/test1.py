#命令行输入端口名称，得出IP地址

import re
import sys



def get_address(port):
    f = open('1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        if not data:
            return 'Not found teh port'
        #匹配出首个单词
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        if port == PORT:
            #pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'
            address = re.search(pattern,data).group(1)
            return address


if __name__ == '__main__':
    port = sys.argv[1]
    print(get_address(port))