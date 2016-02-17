from urllib.request import urlopen
import re
import time
#https://www.youtube.com/watch?v=CMyoQbBq5IE
#http://www.elnuevodiario.com.ni/rss/
#http://www.tn8.tv/comments/feed/


def main():
    
    page = 'http://www.elnuevodiario.com.ni/rss/sucesos'
    crawl(page)
    
    
def crawl(page):
    
    sourceCode = urlopen(page).read()
    
    print ('----------------------------------------')
    titles= re.findall(b'<title>(.*?)</title>', sourceCode)	
	#asi es?te dormiste?
    for title in titles:
        print (title)    

if __name__ == "__main__":
    main()
