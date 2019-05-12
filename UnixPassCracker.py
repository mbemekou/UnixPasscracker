#!/usr/bin/python
from termcolor import colored
from threading import Thread
import sys
import crypt
import getopt
import os
import time
global wordlist
global threads
global shadow_file
global words
global lines
class UnixCrack(Thread):
	def __init__(self,word,salted_digest):
		Thread.__init__(self)
		try:
			self.word=word.strip('\n')
			self.salted_digest=salted_digest
			self.found=""
		except Exception, e:
			print e

	def run(self):
		global i
		try:
			salt="$6$"+self.salted_digest.split("$")[2]
			salted_digest_word=crypt.crypt(self.word,salt)
			
			if salted_digest_word == self.salted_digest:
				sys.stdout.write('\r'+'                                                  ')
				sys.stdout.flush()
				print (colored("\n[+] password found :"+self.word+"\n","green"))
				sys.stdout.flush()
				self.found="trouver"
				return 
			else:
				i=i-1
				sys.stdout.write('\r'+self.word+'                ')
				sys.stdout.flush()
				return

		except KeyboardInterrupt:
			print "Ctrl+C has been pressed"
			sys.exit()
	


def banner():

	os.system("clear")
	
	print '''
				 _   _       _      ____                ____                _             
				| | | |_ __ (_)_  _|  _ \ __ _ ___ ___ / ___|_ __ __ _  ___| | _____ _ __ 
				| | | | '_ \| \ \/ / |_) / _` / __/ __| |   | '__/ _` |/ __| |/ / _ \ '__|
				| |_| | | | | |>  <|  __/ (_| \__ \__ \ |___| | | (_| | (__|   <  __/ |   
				 \___/|_| |_|_/_/\_\_|   \__,_|___/___/\____|_|  \__,_|\___|_|\_\___|_|   
    '''
	l="\t\t\t\t\tBy Mbemekou Fred\n"
	u=""
	for b in l:
		u=u+b
		sys.stdout.write('\t\t\t\r'+u)
		sys.stdout.flush()
		time.sleep(0.05)

	print "\n\n"	
	time.sleep(0.3)
def usage():
        print (colored('''USAGE:
./UnixPassCracker.py -w <wordlist_file> -f <shadow_file> -t <number of threads>

example: ./UnixPassCracker.py -w /usr/share/wordlist/rockyou.txt -f /etc/shadow -t 10
        ''','green'))
def launcher_thread(words,lines,threads):
	global i
	for line in lines:
		if (":" in line) & ( "$6$" in line):
			user=line.split(":")[0]
			salted_digest=line.split(":")[1].strip(" ")
			print "\n\ncracking password for user: "+user
			
			i=0

			j=0
			for word in words:
				try:
					if(i<threads):
						i=i+1
						thread=UnixCrack(word,salted_digest)
						thread.start()
						if(thread.found =="trouver"):
							j=1
							break

				except KeyboardInterrupt:
					print "Ctrl+C has been pressed"
					sys.exit()
				thread.join()
			if(j!=1):
				sys.stdout.write('\r'+'                                ')
				sys.stdout.flush()
				print (colored("\n[-]password not found\n", "red"))
				sys.stdout.flush()
	return

def start(argv):
	banner()
	if len(sys.argv)<5:
		usage()
		sys.exit()
	try:
		
		opts,args=getopt.getopt(sys.argv[1:],"w:f:t:")
		
		

	except getopt.GetoptError:
		print "error getting  argument"
		sys.exit()
	for o,a in opts:
		if o =='-w':
			wordlist=a
		elif o =='-f':
			shadow_file=a
		elif o =='-t':
			try:
			 threads=int(a)
			except:
				print (colored("the number of thread should be an integer !","red"))
				usage()
				sys.exit()
		else:
			usage()
	try:
		
		f1=open(wordlist)
		words=f1.readlines()
	except:
		print (colored("[-] Error while opening dictionnary ' "+wordlist+ " '. File not found or you don't have permission on it","red"))
		usage()
		sys.exit()
	try:
		f2=open(shadow_file)
		lines=f2.readlines()
	except:
		print (colored("[-] Error while opening shadow file' "+shadow_file+ " ' File not found or you don't have permission on it","red"))
		usage()
		sys.exit()
	launcher_thread(words,lines,threads)

start(sys.argv)
