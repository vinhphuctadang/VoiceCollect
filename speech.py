
from recorder import play 
from wordSet import nextWord


def main ():
	txt = 'Làm ngay thưa xếp'
	print (txt)
	for word in nextWord (txt):
		play ('data/%s.mp3'%word)
if __name__=='__main__':
	main ()