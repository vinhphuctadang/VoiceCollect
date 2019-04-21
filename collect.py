import recorder as rd
#import re

def readInput (name='input.txt'):
	f=open (name,'r',encoding='utf-8')
	data = str(f.read ())
	f.close ()
	return data.split ()

def exists (name):# check wav file's existential
	import os
	result = os.path.isfile( '%s.wav' % name)
	return result

def recordWord (word):#record a word
	if (exists (word)):
		return
	data = rd.record ('Đọc: "%s" ...' % word,time=2)
	rd.save (data, '%s.wav'%word)
	print ('--------------------------------------')
	
def main ():
	
	# rd.plot ('chị.wav')
	print ('Bắt đầu thu thập dữ liệu ...')
	words = readInput ()
	for word in words:
		recordWord (word)
	print ('Xong, cảm ơn')

if __name__=='__main__':
	main ()