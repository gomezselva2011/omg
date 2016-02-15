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
    try:
        page = 'http://www.laprensa.com.ni/feed'
        page1 = 'http://www.elnuevodiario.com.ni/rss/'
        sourceCode = opener.open(page).read()
        sourceCode1 = opener.open(page1).read()
        #print sourceCode
        try:
            print ('----------------------------------------')
            titles= re.findall(r'<title>(.*?)</title>', sourceCode)
            for title in titles:
                print title
            print ('----------------------------------------')
            titles1= re.findall(r'<title>(.*?)</title>', sourceCode1)
            for title1 in titles1:
                print title1
                
        except Exception, e:
            print str(e)
        
    except Exception, e:
        print str(e)

if __name__ == "__main__":
    main()
