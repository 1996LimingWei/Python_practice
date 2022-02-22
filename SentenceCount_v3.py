'''CTRL+K then CTRL+C adds the # in VS for selected lines. CTRL+K then CTRL+U removes the # in VS for selected lines.'''
import os
import glob
import re
import sys 
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
def counts_words_type(typepaths):
	type_path = glob.glob(typepaths)
	counts = [Count_words(file) for file in type_path]
	return sum(counts)
def counts_char_type(typepaths):
	type_path = glob.glob(typepaths)
	counts = [Count_char(file) for file in type_path]
	return sum(counts)

def Count_words(file_path):
	text = (open(file_path)).read()
	return len(text.split())

def Count_char(file_path):
	text = (open(file_path)).read()
	return len(text)

def Count_words_f(folder):
	counts = 0
	for filename in os.listdir(folder):
		filename = folder + filename
		count = Count_words(filename)
		counts += count
	return counts
def Count_char_f(folder):
	counts = 0
	for filename in os.listdir(folder):
		filename = folder + filename
		count = Count_char(filename)
		counts += count
	return counts

if __name__ == "__main__":
	while True:
		value = sys.argv[1] #input("Would you like to work with a file or directory, choose A or B: \n A. File \n B. Directory")
		if value not in ("A","B",'a',"b"):
			print("Invalid input, try again")
			continue
		else:
			if value in ("A",'a') :
				file_dir = sys.argv[2] #input("Type your full file path, start with disk name:")
				break
			elif value in ("B","b"):
				file_dir = sys.argv[2] #input("Type your full directory path, start with disk name, end with '/' :")
				type_name = sys.argv[3] #input("Would you like to specify a file type(e.g. txt, csv), type 'no' to skip:")
				if type_name not in ("no","No","NO"):
				   file_dir = file_dir+"*."+type_name	
				break
	try:
		count = Count(file_dir)
		words = Count_words(file_dir)
		char = Count_char(file_dir)
		print("number of lines contained in the file you choose is: %s, \n number of words is %s, \n number of characters is: %s" % (count,words,char))
	except:
		try:
			count = Count_rows_f(file_dir)
			words = Count_words_f(file_dir)
			char = Count_char_f(file_dir)
			print("number of lines contained in the directory you choose is: %s, \n number of words is %s, \n number of characters is: %s" % (count,words,char))
		except:
			try:
				count = counts_rows_type(file_dir)
				words = counts_words_type(file_dir)
				char = counts_char_type(file_dir)
				print("number of lines contained in the directory you choose is: %s, \n number of words is %s, \n number of characters is: %s" % (count,words,char))

			except:
				print("invalid file or directory path input. Program will exit...")

##用户运行程序后，可根据提示选择想查找行数的文件、文件夹

	#file_path = 'C:/Users/v-limingwei/source/repos/SentenceCount/test/Test.txt'
	#folder_path = "C:/Users/v-limingwei/source/repos/SentenceCount/test/"
	#path = "C:\Users\v-limingwei\source\repos\SentenceCount\SentenceCount\SentenceCount_v3.py"
