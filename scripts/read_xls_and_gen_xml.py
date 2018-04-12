#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author : liufushihai
# Descriptor : 从xls文件中读取数据并生成xml文件
# Language : Python
# Latest Edited Time : 2018-04-12

#导入相应处理库
import xml.etree.ElementTree as ET
import xlwt
import xlrd     #xls文件读取
import xml.dom.minidom
import sys
import io
import locale
import codecs

#打印系统编码格式
def printCodeType():
    print(sys.getdefaultencoding())        #系统默认编码
    print(sys.getfilesystemencoding())     #文件系统编码
    print(locale.getdefaultlocale())       #系统当前编码
    print(sys.stdout.encoding)             #终端输出编码
    print(sys.stdin.encoding)              #终端输入编码

#printCodeType()

#读取xls文件
readWorkbook = xlrd.open_workbook("../xls/Android_Multi_Language_Proofread.xls")
#查看xls文件中的sheet表名
print(readWorkbook.sheet_names())
#使用索引读取第一个sheet
translate_sheet = readWorkbook.sheet_by_index(0)

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
#创建一个根节点对象
root = doc.createElement('resource')
#将根节点添加到文档对象中
doc.appendChild(root)


def generateXml(target_path,open_mode,encoding_type,index):
    count = 0
    fp = codecs.open(target_path,open_mode,encoding_type)
    rows = translate_sheet.get_rows()
    fp.write('<resources>\r\n')
    for row in rows:
        if(row[index].ctype != xlrd.book.XL_CELL_EMPTY):
            if(str(row[index]).strip() != ''):
                if(count != 0):
                    tmp_str = str('\r\t<string ')\
                        + str('name="')\
                        + str(row[1].value)\
                        + str('">')\
                        + str(row[index].value)\
                        + str('</string>')
                    fp.write(tmp_str)
                count += 1
    fp.write('</resources>\r\n')
    fp.close()

generateXml('../xml/values-en.xml','w','UTF-8-SIG',2)
generateXml('../xml/values-cn.xml','w','UTF-8-SIG',3)
generateXml('../xml/values-jp.xml','w','UTF-8-SIG',4)
generateXml('../xml/values-ko.xml','w','UTF-8-SIG',5)
generateXml('../xml/values-fr.xml','w','UTF-8-SIG',6)


