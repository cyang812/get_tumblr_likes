# -*- coding: utf-8 -*-

import requests
import os
import json
import urllib.parse

PROXIES = { "http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080" } 
# PROXIES = {}

consumer_key = 'mqyfWchrSDffLHqst0k9xLCvsI5JaCyTPJG3ZdCLyQJVm0FX2V'  # you can replace it by your api_key

def main():
	print('#1 get_json main()')
	like_json = open("likes.json",'w',encoding='utf-8')

	blog_identifier = input('Please input blog_id:' )

	# -1 get user info
	info_url = 'https://api.tumblr.com/v2/blog/{0}.tumblr.com/info?api_key={1}'
	info_url = info_url.format(blog_identifier, consumer_key)
	# print(info_url)

	resp = requests.get(info_url, proxies=PROXIES)
	print(resp)
	
	try:
		data = resp.json()
	except ValueError:
		data = {'meta': { 'status': 500, 'msg': 'Server Error'}, 'response': {"error": "Malformed JSON or HTML was returned."}}

	if 200 <= data['meta']['status'] <= 399:
		# print(data)
		if data['response']['blog']['share_likes']:
			like_item = data['response']['blog']['likes']
			print('like_item = ',like_item)
		else:
			print('[error]: blog likes is not share')	
			return
	else:
		print('error',data)
		print('[error]: blog is not exist')
		return

	# -2 get first user likes
	likes_url = 'https://api.tumblr.com/v2/blog/{0}.tumblr.com/likes?limit=2&api_key={1}'
	likes_url = likes_url.format(blog_identifier, consumer_key)
	# print(likes_url)
	liked_timestamp = 0

	resp = requests.get(likes_url, proxies=PROXIES)
	print(resp)

	try:
		data = resp.json()
	except ValueError:
		data = {'meta': { 'status': 500, 'msg': 'Server Error'}, 'response': {"error": "Malformed JSON or HTML was returned."}}

	if 200 <= data['meta']['status'] <= 399:
		res_item_len = len(data['response']['liked_posts'])
		print("res_item_len = ",res_item_len)
		liked_timestamp = data['response']['liked_posts'][res_item_len-1]['liked_timestamp']
		print("liked_timestamp =",liked_timestamp)
		json.dump(data, like_json)
		like_json.write(u'\n'); # json 文件分割符
	else:
		print('error',data)

	# get all user likes	
	raw_url = 'https://api.tumblr.com/v2/blog/{0}.tumblr.com/likes?limit=10&before={1}&api_key={2}'

	offset = res_item_len
	while offset<like_item:
		likes_url = raw_url.format(blog_identifier, liked_timestamp, consumer_key)

		resp = requests.get(likes_url, proxies=PROXIES)
		print(resp)

		try:
			data = resp.json()
		except ValueError:
			data = {'meta': { 'status': 500, 'msg': 'Server Error'}, 'response': {"error": "Malformed JSON or HTML was returned."}}

		if 200 <= data['meta']['status'] <= 399:
			# print(data['response'])
			# print(data['response']['user']['likes'])
			res_item_len = len(data['response']['liked_posts'])
			print("res_item_len = ",res_item_len)
			if res_item_len:
				liked_timestamp = data['response']['liked_posts'][res_item_len-1]['liked_timestamp']
				print("liked_timestamp =",liked_timestamp)
				json.dump(data, like_json)
			else:
				break	
		else:
			print('error',data)

		offset += res_item_len
		like_json.write(u'\n'); # json 文件分割符

	like_json.close()	

if __name__ == '__main__':
	main()