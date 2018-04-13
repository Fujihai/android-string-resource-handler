#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author : liufushihai
# Descriptor : 读取多语言Strings文件并生成xls文件
# Language : Python
# Latest Edited Time : 2018-04-11

##------------- 代码流程 -----------------
##1.先读取yaml配置文件信息并测试打印
##2.将读取的对应项作为参数生成xml树结点
##3.得到xml树的根结点后，以英文'name'作为匹配标准
##4.依次匹配'中文'、'日文'、'法文'、'韩文'，并写入相关变量
##5.最后保存为xls文件
##----------------------------------------

#import xml、xls处理库
import xml.etree.ElementTree as ET
from ruamel import yaml 
import xlwt
import xlrd

#获取xml树根结点
def getTreeRoot(ElementTree):
    #print(type(ElementTree.getroot()))
    return ElementTree.getroot();

#进行匹配写入,以英文的'name'为匹配标准
def matchAndWriteXls(e1,e2,index1,index2):
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

##生成列表项名
def initXls():
    i = 1
    for tmp_str in list:
         bs_language_proofread.write(0,i,list[i-1])
         i += 1

with open('../config.yml') as f:
    content = yaml.load(f, Loader=yaml.RoundTripLoader)
    source_xml_path = 'source_xml_path'
    target_xls_path = 'target_xls_path'

    initXls()

    list_language = ['en','cn','ja','fr','ko']  #语言类型
    list = [None] * 5

    i = 0
    for tmp_name in list_language:
        list[i] = ET.parse(str(content[source_xml_path][tmp_name]))
        i += 1

    #匹配并写入相应列
    i = 3
    j = 1
    while i <= 6:
        matchAndWriteXls(getTreeRoot(list[0]),getTreeRoot(list[j]),2,i)
        i += 1
        j += 1

    #保存xls文件
    workbook.save(content[target_xls_path])
    f.close()
        

#读取yaml配置文件信息
##with open('../example.yml') as f:
##    content = yaml.load(f, Loader=yaml.RoundTripLoader)
##    source_xml_path = 'source_xml_path'
##    target_xls_path = 'target_xls_path'
##    target_xml_path = 'target_xml_path'
##
##    #配置文件信息中的子项
##    list_language = ['en','cn','ja','fr','ko']  #语言类型
##    #list = [None] * len(list_language)
##
##    print(content)
##
##    i = 0
##    for tmp_name in list_language:
##        #list[i] = str(content[source_xml_path][tmp_name])
##        print(str(content[source_xml_path][tmp_name]))
##        i += 1
##
###生成列表项名
##def initXls():
##    i = 0
##    for tmp_str in list:
##         bs_language_proofread.write(0,i,list[i])
##         i += 1
##
##
###获取xml树根结点
##def getTreeRoot(ElementTree):
##    #print(type(ElementTree.getroot()))
##    return ElementTree.getroot();
##

##    
###根据getTreeRoot返回的根结点查找并打印string项的值
##def printStringValue(Element):
##    for tmp_str in Element.findall('string'):
##        print(str('\t') + str(tmp_str.text))
##
##
###xls表第一行显示标题
##list =  ['字段名','英文','中文','日文','法文','韩文']
##
##def run(content,src_xml_path,list_language):
##    #初始化xls文件
##    initXls()
##    
##    #根据传入参数读取源xml文件
##    list = [None] * len(list_language)
##
##    #根据参数初始化xml树根节点
##    i = 0
##    for tmp_name in list_language:
##        list[i] = ET.parse(content[src_xml_path][tmp_name])
##        print(type(list[i]))
##        i += 1
##
##    #匹配并写入相应列
##    i = 3
##    j = 1
##    while i <= 6:
##        matchAndWriteXls(getTreeRoot(list[0]),getTreeRoot(list[j]),2,i)
##        i += 1
##        j += 1
##
##    #保存xls文件
##    workbook.save('../xls/Android_Multi_Language_Proofread.xls')
