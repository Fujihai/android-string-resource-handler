#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author : liufushihai
# Descriptor : 读取各类文件编码格式
# Language : Python
# Latest Edited Time : 2018-04-12

import chardet

with open("../xls/Android_Multi_Language_Proofread.xls",'rb') as fp:
    result = chardet.detect(fp.read())
    print('生成xls文件信息：')
    print(result)

with open("../multi-strings-values/values-ko/strings.xml",'rb') as fp:
    result = chardet.detect(fp.read())
    print('源xml文件信息：')
    print(result)

with open("../xml/value-ko.xml",'rb') as fp:
    result = chardet.detect(fp.read())
    print('生成目标xml文件信息：')
    print(result)

