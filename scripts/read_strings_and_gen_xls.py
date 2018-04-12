#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author : liufushihai
# Descriptor : 读取多语言Strings文件并生成xls文件
# Language : Python
# Latest Edited Time : 2018-04-11

#import xml、xls处理库
import xml.etree.ElementTree as ET
import xlwt
import xlrd

#依次读取string文件
tree_cn = ET.parse('../multi-strings-values/values-zh-rCN/strings.xml')
tree_en = ET.parse('../multi-strings-values/values/strings.xml')
tree_ja = ET.parse('../multi-strings-values/values-ja/strings.xml')
tree_ko = ET.parse('../multi-strings-values/values-ko/strings.xml')
tree_fr = ET.parse('../multi-strings-values/values-fr/strings.xml')

#print(type(tree_cn))

#获取xml树根结点
def getTreeRoot(ElementTree):
    #print(type(ElementTree.getroot()))
    return ElementTree.getroot();

#根据getTreeRoot返回的根结点查找并打印string项的值
def printStringValue(Element):
    for tmp_str in Element.findall('string'):
        print(str('\t') + str(tmp_str.text));

#打印各个语言的string项的值
#printStringValue(getTreeRoot(tree_cn))
#printStringValue(getTreeRoot(tree_en))
#printStringValue(getTreeRoot(tree_ja))
#printStringValue(getTreeRoot(tree_ko))
#printStringValue(getTreeRoot(tree_fr))

#xls文件相关变量
workbook = xlwt.Workbook(encoding='utf-8')
bs_language_proofread = workbook.add_sheet('Android多语言校对表',cell_overwrite_ok=True)

#生成列表项名
def initXls():
    bs_language_proofread.write(0,1,'字段名')
    bs_language_proofread.write(0,2,'英文')
    bs_language_proofread.write(0,3,'中文')
    bs_language_proofread.write(0,4,'日文')
    bs_language_proofread.write(0,5,'韩文')
    bs_language_proofread.write(0,6,'法文')


initXls()

#进行匹配写入,以英文的'name'为匹配标准
def matchAndWriteXls(e1,e2,index1,index2):
    i = 0
    for tmp_str1 in e1:
        i += 1
        for tmp_str2 in e2:
            if(tmp_str1.get('name') == tmp_str2.get('name')):
                if(str(tmp_str1.text).strip() != '' and str(tmp_str2.text).strip() != ''):
                    if(index2 == 3):
                        bs_language_proofread.write(i,1,tmp_str1.get('name'))
                    bs_language_proofread.write(i,index1,tmp_str1.text)
                    bs_language_proofread.write(i,index2,tmp_str2.text)
                   


#英文与各语言匹配
matchAndWriteXls(getTreeRoot(tree_en),getTreeRoot(tree_cn),2,3)
matchAndWriteXls(getTreeRoot(tree_en),getTreeRoot(tree_ja),2,4)
matchAndWriteXls(getTreeRoot(tree_en),getTreeRoot(tree_ko),2,5)
matchAndWriteXls(getTreeRoot(tree_en),getTreeRoot(tree_fr),2,6)

#生成最终xls文件
workbook.save("../xls/Android_Multi_Language_Proofread.xls")

    
