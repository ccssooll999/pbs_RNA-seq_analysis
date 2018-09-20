# -*- coding: UTF-8 -*-

import os
import sys

def unzip_linux(start_path):

    # 输入格式化
    if start_path[-1] == "/":
        start_path = start_path[:-1]

    root_name = start_path.split('/')[-1]

    for root, dirs, files in os.walk(start_path): 

        os.chdir(root + "/")
        file_names = os.listdir("./")

        for name in file_names:
            file_name = name
            # 判断是不是文件
            if os.path.isfile(name):
                name = os.path.abspath(name)

                if os.path.splitext(name)[-1] == '.gz':
                        
                    cmd4 = 'gunzip {0}'.format(name)
                    print(cmd4)
                    # os.system(cmd4)
                    




if __name__ == "__main__":    

    # 绝对路径    
    # start_path = ''

    unzip_linux(sys.argv[1])
