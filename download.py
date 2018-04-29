# -*- coding: utf-8 -*-

import os
import urllib
import requests

url_filename = 'url_list.txt'

# PROXIES = { "http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080" } 
PROXIES = {}

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
			print('download err ->', name)
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

if __name__ == "__main__":

	url_list = get_url()
	chdir()
	for i in range(0,len(url_list)):
		download(url_list[i])
