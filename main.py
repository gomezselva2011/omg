import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time
#https://www.youtube.com/watch?v=CMyoQbBq5IE
#http://www.elnuevodiario.com.ni/rss/
#http://www.tn8.tv/comments/feed/
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    
    page = 'http://www.laprensa.com.ni/feed'
    page1 = 'http://www.elnuevodiario.com.ni/rss/'
    crawl(page)
    crawl(page1)
    
    
def crawl(page):
    
    try:
        sourceCode = opener.open(page).read()
        print ('----------------------------------------')
        titles= re.findall(r'<title>(.*?)</title>', sourceCode)
        for title in titles:
            print title
            
        
                
    except Exception, e:
        print str(e)
    
    
    
    
    
    

if __name__ == "__main__":
    main()
