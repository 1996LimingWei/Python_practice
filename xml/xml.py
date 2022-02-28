# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
tree = ET.parse("Config.xml")
root = tree.getroot()
#print(root)

data = open("Config.xml").read()
root = ET.fromstring(data)
#print(root)

for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag,":", child.attrib) 
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        print(children.tag, ":", children.attrib)
        
#Q1
for setting in root.iter('Settings'):
    print(setting.attrib)
#Q2
for node in root.iter('TrainingPaths'):
    print('\n')
    for elem in node.iter():
        if not elem.tag==node.tag:
            print(elem.text)
#Q3
'''comments are automatically skipped in in xml parse, i will research on how to retain it'''