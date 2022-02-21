'''CTRL+K then CTRL+C adds the # in VS for selected lines. CTRL+K then CTRL+U removes the # in VS for selected lines.'''
import os
import glob
import re

def Count(path):
	count = 0
	count = len(open(path).readlines())
	return count

def Count_for(path):
	count = 0
	with open(path, 'r') as f:
		for line in f:
			count += 1
	return count
def count_rows(filename):
	f = open(filename,'r')
	return len(f.readlines())

def Count_rows_f(folder):
	counts = 0
	for filename in os.listdir(folder):
		filename = folder + filename
		count = count_rows(filename)
		counts += count
	return counts


def counts_rows_type(typepaths):
	type_path = glob.glob(typepaths)
	counts = [count_rows(file) for file in type_path]
	return sum(counts)

def Count_words(file_path):
	text = (open(file_path)).read()
	return len(text.split())

def Count_char(file_path):
	text = (open(file_path)).read()
	return len(text)


file_path = 'C:/Users/v-limingwei/source/repos/SentenceCount/test/Test.txt'
folder_path = "C:/Users/v-limingwei/source/repos/SentenceCount/test/"
## Q.a.1 计算某个特定文本包含了多少行数据。
print(Count(file_path))

## Q.a.2 计算某个特定文本包含了多少行数据，方法2：for不需要全部读取文档，比较省空间
print(Count_for(file_path))

## Q.b 计算某个文件夹总共包含了多少行数据。
print(Count_rows_f(folder_path))

## Q.c 计算某个文件夹当中包含的某种类型的文件，总共包含了多少行数据
type = "*.txt"
typepaths = folder_path + type
print(counts_rows_type(typepaths))

## Q.d 计算WORD COUNT count of words应该是在去除了特殊符号后，计算由空格分隔的字符个数
print(Count_words(file_path))

## Q.e 计算CHAR COUNT count of char应该是不去除特殊符号后，计算由空格分隔的字符个数（包括特殊字符）
print(Count_char(file_path))

## 用户A希望计算某个文件的sentence count
'''Q.a.1或 Q.a.2，客户直接修改file_path文件地址即可'''

## 用户B希望计算某个文件夹内所有TXT文件的sentence count
'''Q.c即可，客户直接修改folder_path文件夹地址即可'''

## 用户C希望计算某个文件夹内所有文件的sentence count+word count
'''Q.a.1或 Q.a.2再加上Q.d，我们添加一个def function用来直接调用count_words函数给该文件夹, 
随后客户直接修改folder_path文件夹地址，再将wordcount和sentencecount加一起即可'''
def Count_words_f(folder):
	counts = 0
	for filename in os.listdir(folder):
		filename = folder + filename
		count = Count_words(filename)
		counts += count
	return counts
'''客户只需在括号内输入文件夹地址即可：'''
print(Count_rows_f(folder_path)+ Count_words_f(folder_path))
