# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import  lxml.etree as et

tree = ET.parse("Config.xml")
root = tree.getroot()
#print(root)

data = open("Config.xml").read()
root = ET.fromstring(data)
#print(root)
'''
for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag,":", child.attrib) 
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        print(children.tag, ":", children.attrib)
       ''' 
#Q1 locate attribute value in line 44
for setting in root.iter('Settings'):
    print(setting.attrib) #
print("In line 44, Source is:",root.find("CleanupData/Settings[@Source]").get('Source')) #find "Source"
print("In line 44, Target is:",root.find("CleanupData/Settings[@Target]").get('Target')) #find "Source"
#Q2 locate value between two tags in line 21

for node in root.iter('TrainingPaths'):
    print('\n')
    for elem in node.iter():
        if not elem.tag==node.tag:
            print(elem.text)
#Q3
''''we use parser=et.XMLParser(remove_comments=True) to ignore comments '''
tree = ET.parse("Config.xml",parser=et.XMLParser(remove_comments=True))
root = tree.getroot()

#Q4
'''create a new xml file'''
def create_XML(fileName) :
      
    root = ET.Element("sample")
    food = ET.SubElement(root, "food")
    ET.SubElement(food, "east", name = "Chinese").text = "mapodoufu"
    ET.SubElement(food, "east", name="Japanese").text = "ramen"
    city = ET.SubElement(root, "city")
    ET.SubElement(city, "east", name = "Chinese").text = "Xian"
    ET.SubElement(city, "west", name="United States").text = "Boston"
    tree = ET.ElementTree(root)
    with open (fileName, "wb") as files :
        tree.write(files)
if __name__ == "__main__": 
    create_XML("sample.xml")
