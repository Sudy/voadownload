#!/usr/bin python
#!encoding=utf-8
import re
import sys
import urllib2
import getMp3Thread
import Queue


if __name__ == "__main__":
    
    #base url
	baseurl = "http://www.51voa.com"
	starturl = "http://www.51voa.com/VOA_Standard_1.html"

	#start url
	#starturl = baseurl + sys.argv[1] + ".html"

	html = urllib2.urlopen(starturl).read()

	newsrule = "<li> <a href=\"(.*?)\" target=_blank>.*?</a> .*?</li>"
	regx = re.compile(newsrule)
	urllist = regx.findall(html)
	
	
	#build two queues 
	#mp3 queue and url queue
	uque =  Queue.Queue()
    
    #get the mainpage url
	for url in urllist:
		uque.put(url)
	
    
	mp3rule = "<a href=\"(.*?).mp3\">"
	regmp3 = re.compile(mp3rule)
    
	for i in range(1,10):
		uthread = getMp3Thread.UrlThread(uque,baseurl,regmp3)
		uthread.start()
	for j in range(1,20)
		mthread = getMp3Thread.Mp3Thread()
		mthread.start()	
    	
   

