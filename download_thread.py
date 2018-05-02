# -*- coding: utf-8 -*-

import os
import urllib
import requests
import threading
import queue
import time

url_filename = 'url_list.txt'

PROXIES = { "http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080" } 
# PROXIES = {}

def get_url():
	with open(url_filename, "r") as f:
	    raw_sites = f.read()

	raw_sites = raw_sites.replace("\n", ",") 
	raw_sites = raw_sites.split(",")

	sites = list()
	for raw_site in raw_sites:
	    site = raw_site.lstrip().rstrip()
	    if site:
	        sites.append(site)

	print('list_len = ',len(sites))	        
	return sites

def get_filename(url):
	name = url.split("/")[-1].split("?")[0]
	return name    

def download(url):

	name = get_filename(url)

	file_path = os.path.join(name)
	if not os.path.isfile(file_path):
		try:
			r = requests.get(url,proxies=PROXIES) # use proxy
			print('downloading ->',name)

			with open(name, "wb") as code:
		   		code.write(r.content)
		except Exception as e:
			print('downloading err ->', name)
			pass
	else:
		print("file exist")		   

def chdir():

	current_folder = os.getcwd()
	print(current_folder)
	target_folder = os.path.join(current_folder, 'download')
	if not os.path.isdir(target_folder):
		os.mkdir(target_folder)
	os.chdir(target_folder)

def fetch_img_func(q):
    while True:
        try:
            # 不阻塞的读取队列数据
            url = q.get_nowait()
            i = q.qsize()
        except Exception as e:
            print(e)
            break;
        print('Current Thread Name Runing %s ...' % threading.currentThread().name)
        print('handle %s item... item url %s ' % (i, url))
        download(url)


if __name__ == "__main__":
	start = time.time()
	q = queue.Queue()
	url_lists = get_url()
	for url_list in url_lists:
	    q.put(url_list)

	chdir()

	t1 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_1")
	t2 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_2")
	t3 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_3")
	t4 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_4")
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()

	end = time.time()
	print('Done %s ' % (end-start))