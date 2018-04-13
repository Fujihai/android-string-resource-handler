#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author : liufushihai
# Descriptor : 主脚本文件
# Language : Python
# Latest Edited Time : 2018-04-13

import os
import ruamel

##os.system("python ./scripts/read_strings_and_gen_xls.py")
##os.system("python ./scripts/read_xls_and_gen_xml.py")

if __name__=="__main__":
    print(os.path.dirname(os.path.realpath(__file__)))
    os.system('python ' + str(os.path.dirname(os.path.realpath(__file__)))
          + str('\\read_strings_and_gen_xls.py'))

input()
