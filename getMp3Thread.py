#!/usr/bin python
#!encoding=utf-8

import threading
import urllib2
import re
import time
import Queue
#urlmutex = threading.Lock() 
#mp3mutex = threading.Lock()

qmp3 = Queue.Queue()

class Mp3Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        
        global qmp3
        while True:
        	#print qmp3.qsize()
    		#if qmp3.empty():
    		#	time.sleep(10)
	    	#	continue
		    			
			#get a resource
			mp3name = qmp3.get()
			print mp3name
			
			#release the resource
			#mp2mutex.release()
			
			index = mp3name.rfind('/')
			
			#filename
			filename = mp3name[index+1:] + ".mp3"
			
			#read the mp3
			content = urllib2.urlopen(mp3name + ".mp3").read()
			
			with open(filename,'w') as fp:
				fp.write(content)
				fp.flush()
		
		
class UrlThread(threading.Thread):
    def __init__(self,qurl,baseurl,regx):
        self.qurl = qurl
        self.regx = regx
        self.baseurl = baseurl
        
        threading.Thread.__init__(self)
        
    def run(self):
    	global qmp3
        while True:
        	#if urlmutex.acquire():
	    	if self.qurl.empty():
	    		time.sleep(10)
	    		continue		    				    		
		        
	        u = self.qurl.get()
	        content = urllib2.urlopen(self.baseurl+u).read()
    		#urlmutex.release()
    		info = self.regx.findall(content)
    		for url in info:
    		    #if mp3mutex.acquire():
				qmp3.put(url)
    				#mp3mutex.release()
	    	time.sleep(10)
			#else:continue        			
