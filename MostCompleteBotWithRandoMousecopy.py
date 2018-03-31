#! /usr/bin/env python3
import random
import requests
from selenium import webdriver
import sys
import time
import random
import re
import os
from fake_useragent import UserAgent
import pyautogui
import webbrowser
import itertools

proxylisttext = 'proxylistlist.txt'
useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy_type", 1)
moves = random.randint(1,4)

def RandoMouser(i):
	global moves
	destx = random.randint(700,821);
	desty = random.randint(657,875);
	x, y = pyautogui.position() # Current Position
	pixelsx = destx-x
	pixelsy = desty-y
	avgpixelsx = pixelsx/moves
	avgpixelsy = pixelsy/moves
	while moves > 0 and moves < random.randint(8,11):
		offsetx = (avgpixelsx+random.randint(100, random.randint(151,300)));
		offsety = (avgpixelsy+random.randint(-200, random.randint(-175,-100)));
		print (x + offsetx, y + offsety, moves)
		pyautogui.moveTo(x + offsetx, y + offsety, duration=random.uniform(0.2,0.4))
		moves = moves+1
		avgpixelsx = pixelsx / moves
		avgpixelsy = pixelsy / moves

def Visiter(proxy1):
	try:
		proxy = proxy1.split(":")
		print ('Visit using proxy :',proxy1)
		profile.set_preference("network.proxy.http", proxy[0])
		profile.set_preference("network.proxy.http_port", int(proxy[1]))
		profile.set_preference("network.proxy.ssl", proxy[0])
		profile.set_preference("network.proxy.ssl_port", int(proxy[1]))
		driver = webdriver.Firefox(firefox_profile=profile)
		profile.set_preference("general.useragent.override", useragent.random)
		#driver.set_window_size(800, 600)
		#driver.get('https://www.iplocation.net/find-ip-address')
		driver.get('http://discoparty.000webhostapp.com')
		time.sleep(random.randint(2, 4))
		pyautogui.click(random.randint(400,500), random.randint(500,600)) #focus firef0x
		time.sleep(random.uniform(0.60,0.90))
		pyautogui.moveRel(random.randint(200,227), random.randint(-150,-119), duration=random.uniform(0.2,0.4))
		pyautogui.moveRel(random.randint(200,227), random.randint(-150,-119), duration=random.uniform(0.2,0.4))
		RandoMouser(moves)
		pyautogui.scroll(random.randint(-25, -7))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(-25, -5))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(-25, -9))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(-25, -6))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(-25, -8))
		time.sleep(random.uniform(0.10,0.30))
		pyautogui.scroll(random.randint(10,25))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(10,25))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(10,25))
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.scroll(random.randint(200,400))
		time.sleep(random.uniform(1, 2.4))
		pyautogui.moveTo(random.randint(400,465), random.randint(213,257), duration=.20)
		time.sleep(random.uniform(0.05,0.1))
		pyautogui.keyDown('command')
		pyautogui.click(random.randint(322,579), random.randint(208,271)) #ad click
		pyautogui.keyUp('command)')
		time.sleep(random.uniform(0.05,0.25))
		pyautogui.moveRel(random.randint(25,50), random.randint(-64,-37), duration=.20)
		pyautogui.moveRel(random.randint(25,50), random.randint(-64,-37), duration=.20)
		pyautogui.moveRel(random.randint(25,50), random.randint(-64,-37), duration=.20)
		pyautogui.moveTo(random.randint(515,530), random.randint(29,37), duration=.20)
		time.sleep(random.uniform(1.2,2))
		pyautogui.click(538, 39) #close tab
		time.sleep(random.uniform(1,3))
		driver.close()
	except:
		print('Proxy failed')
		driver.close()
		pass

def loadproxy():
	try:
		get_file = open(proxylisttext, "r")
		proxylist = get_file.readlines()
		count = 0
		for proxy in itertools.islice(proxylist, len(proxylist)):
			Visiter(proxy.strip())
		#proxy = []
		#while count < 13:
		#	proxy.append(proxylist[count].strip())
		#	count += 1
		#for i in proxy:
		#	Visiter(i)
	except IOError:
		print ("\n[-] Error: Check your proxylist path\n")
		sys.exit(1)

def main():
	loadproxy()
if __name__ == '__main__':
	main()


#proxy_set = urllib.request.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
		#opener = urllib.request.build_opener(proxy_set, urllib.request.HTTPHandler)
		#opener.addheaders = [('User-agent', random.choice(useragent))]
