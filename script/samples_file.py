# -*- coding: UTF-8 -*-

import os
import sys

def samples_file(start_path):

    # 输入格式化
    if start_path[-1] == "/":
        start_path = start_path[:-1]

    for root, dirs, files in os.walk(start_path): 

        os.chdir(root + "/")
        file_names = os.listdir("./")

        for name in file_names:
            # 判断是不是文件
            if os.path.isfile(name):
                name = os.path.abspath(name)

                if os.path.splitext(name)[-1] == '.fq':
                    if name[-4] == '1':
                        
                        f_name = name.split("/")[-2][:-2]
                        f_name_rep = f_name + "_rep" + name.split("/")[-2][-1]
                        fq1 = name    
                        fq2 = name[:-4] + '2' + name[-3:]
                        cmd = '{0}\t{1}\t{2}\t{3}'.format(f_name, f_name_rep, fq1, fq2)
                        print(cmd)
                    

if __name__ == "__main__":    

    # 绝对路径
    # start_path = ''

    samples_file(*sys.argv[1])
