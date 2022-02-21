'''CTRL+K then CTRL+C adds the # in VS for selected lines. CTRL+K then CTRL+U removes the # in VS for selected lines.'''
import os
from os import walk
import glob
import re

## Q.a.1 计算某个特定文本包含了多少行数据。
count = len(open('C:/Users/v-limingwei/source/repos/SentenceCount/test/Test.txt').readlines())
print(count)

## Q.a.2 计算某个特定文本包含了多少行数据，方法2：for不需要全部读取文档，比较省空间
filename = "C:/Users/v-limingwei/source/repos/SentenceCount/test/Test.txt"
count = 0
with open(filename, 'r') as f:
    for line in f:
        count += 1
print("Total number of lines is:", count)

## Q.b 计算某个文件夹总共包含了多少行数据。
folder_path = "C:/Users/v-limingwei/source/repos/SentenceCount/test/"
def count_rows(filename):
	f = open(filename,'r')
	res = len(f.readlines())
	f.close()
	return res
counts = 0
for filename in os.listdir(folder_path):
	filename = folder_path + filename
	count = count_rows(filename)
	counts += count
print(counts)

## Q.c 计算某个文件夹当中包含的某种类型的文件，总共包含了多少行数据
'''glob can specify a type of file to list'''
filepaths = glob.glob("C:/Users/v-limingwei/source/repos/SentenceCount/test/*.txt")
def count_rows(filepath):
	res = 0
	f = open(filepath,'r')
	res = len(f.readlines())
	f.close()
	return res
counts = [count_rows(filepath) for filepath in filepaths]
print("number of lines in the directory is:", sum(counts))

## Q.d 计算WORD COUNT count of words应该是在去除了特殊符号后，计算由空格分隔的字符个数
filename = "C:/Users/v-limingwei/source/repos/SentenceCount/test/Test.txt"
punct = re.compile("[^\w\s]")
text = (open(filename)).read()
punct_text= re.sub(punct, "", text)
res = len(punct_text.split())
print(res)

## Q.e 计算CHAR COUNT count of words应该是不去除特殊符号后，计算由空格分隔的字符个数（包括特殊字符）
filename = "C:/Users/v-limingwei/source/repos/SentenceCount/test/Test.txt"
text = (open(filename)).read()
res = len(text.split())
print(res)