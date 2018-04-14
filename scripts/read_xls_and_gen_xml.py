#!/usr/bin/python
# -*- coding: UTF-8 -*-

#   __author__ = 'liufushihai'
#   __date__ = '2018-04-12'
#   __desc__ = '从xls文件中读取数据并生成xml文件'

##-----------------代码流程-----------------------
## 1.读取xls文件
## 2.将读取的单元格数据拼接成一行字串
## 3.将拼接字串写入到相应xml文件中
##------------------------------------------------

#导入相应处理库
import xml.etree.ElementTree as ET
import xlwt
import xlrd     
import xml.dom.minidom
import sys
import io
import locale
import codecs
from ruamel import yaml 

list_language = ['en','cn','ja','fr','ko']

#printCodeType()
with open('../config.yml') as f:
    content = yaml.load(f, Loader=yaml.RoundTripLoader)
    print('*** Read config.yml successfully !')
    target_xls_path = 'target_xls_path'
    target_xml_path = 'target_xml_path'

#读取xls文件
readWorkbook = xlrd.open_workbook(content[target_xls_path])
#查看xls文件中的sheet表名
#print(readWorkbook.sheet_names())
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
    fp.write('\r\n</resources>\r\n')
    fp.close()

i = 2
for tmp_str in list_language:
    tmp_str1 = content[target_xml_path][tmp_str]
    generateXml(tmp_str1,'w','UTF-8-SIG',i)
    print('*** Generated xml file successfully: '+ \
           str(content[target_xml_path][tmp_str]))
    i += 1
    




