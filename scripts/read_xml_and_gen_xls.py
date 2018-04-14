#!/usr/bin/python
# -*- coding: UTF-8 -*-

#   __author__ = 'liufushihai'
#   __date__ = '2018-04-11'
#   __desc__ = '读取多语言xml文件并生成xls文件'

## ------------- 代码流程 ------------------------------
## 1.读取yml配置文件相应信息
## 2.将读到的信息，作为参数传入ET句法解析器中，获取Element实例
## 3.根据Element实例得到xml根标签
## 4.以英文为标准，依次匹配'中-日-法-韩'文，并写入xls文件变量中对应的单元格
## 5.保存为xls文件
##-----------------------------------------------------

#import xml、xls处理库
import xml.etree.ElementTree as ET
from ruamel import yaml 
import xlwt
import xlrd

def getTreeRoot(elementTree):
    """[返回xml树根结点]
    
    Arguments:
        ElementTree {[type]} -- [ET句法解析器返回的实例]
    
    Returns:
        [type] -- [description]
    """
    return elementTree.getroot();

def matchAndWriteXls(e1, e2, index1, index2):
    """[进行匹配写入,以英文的'name'为匹配标准]
    
    Arguments:
        e1 {[type]} -- [匹配标准xml根结点]
        e2 {[type]} -- [被匹配标准xml跟结点]
        index1 {[type]} -- [写在sheet表中的列索引]
        index2 {[type]} -- [写在sheet表中的列索引]
    """

    i = 0
    for tmp_str1 in e1:
        i += 1
        for tmp_str2 in e2:
            if(tmp_str1.get('name') == tmp_str2.get('name')):
                if(str(tmp_str1.text).strip() != ''\
                       and str(tmp_str2.text).strip() != ''):
                    if(index2 == 3):
                        bs_language_proofread.write(i,1,tmp_str1.get('name'))
                    bs_language_proofread.write(i,index1,tmp_str1.text)
                    bs_language_proofread.write(i,index2,tmp_str2.text)

#全局xls相关变量
workbook = xlwt.Workbook(encoding='utf-8')
bs_language_proofread = workbook.add_sheet\
                ('Android多语言校对表',cell_overwrite_ok=True)

#xls表第一行显示标题
list =  ['字段名','英文','中文','日文','法文','韩文']

def initXls():
    """[生成列表项名]"""
    i = 1
    for tmp_str in list:
         bs_language_proofread.write(0,i,list[i-1])
         i += 1

with open('../config.yml') as f:
    content = yaml.load(f, Loader=yaml.RoundTripLoader)
    print('*** Read config.yml successfully !')
    source_xml_path = 'source_xml_path'
    target_xls_path = 'target_xls_path'

    initXls()

    list_language = ['en','cn','ja','fr','ko']  #语言类型
    list = [None] * 5

    i = 0
    for tmp_name in list_language:
        list[i] = ET.parse(str(content[source_xml_path][tmp_name]))
        i += 1
        print('*** Read xml file successfully: '\
              + str(content[source_xml_path][tmp_name]))

    #匹配并写入相应列
    i = 3
    j = 1
    while i <= 6:
        matchAndWriteXls(getTreeRoot(list[0]), getTreeRoot(list[j]), 2, i)
        i += 1
        j += 1

    #保存xls文件
    workbook.save(content[target_xls_path])
    f.close()
    print('*** Generated xls file successfully: '\
          + str(content[target_xls_path]))
        
