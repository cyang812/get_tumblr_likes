# -*- coding: utf-8 -*-

import json
# from json import loads
# import json as JSON

JSON_FIlE = 'likes.json'

url_list = open("url_list.txt",'w',encoding='utf-8')

def open_json_file():
	with open(JSON_FIlE,'r',encoding="utf-8") as load_f:
		# load_dict = json.load(load_f)
		# print(load_dict)		
		raw_jsons = load_f.read()
		# raw_jsons = raw_jsons.replace("============================\n", ",") 
		raw_jsons = raw_jsons.split("\n")

		# print(raw_jsons)

		json_lists = list()
		for raw_json in raw_jsons:
		    json_list = raw_json.lstrip().rstrip()
		    if json_list:
		        json_lists.append(json_list)

		print('list_len = ',len(json_lists))	        
		# for i in range(0,len(jsons)):
		# print(jsons[0])
		return json_lists


def get_pic(json_data,item_len):

	for x in range(0,item_len):
		try:
			pic_len = len(json_data['response']['liked_posts'][x]['photos'])
			# print('len = ',pic_len)
			for y in range(0,pic_len):
				url_item = json_data['response']['liked_posts'][x]['photos'][y]['original_size']['url']
				# print(url_item)
				url_list.write(url_item+'\n')
		except Exception as e:
			# print("video")
			pass

    # print("pic_cnt = ",pic_cnt)	
	# return pic_len


def get_video(json_data,item_len):

	for x in range(0,item_len):
		try:
			url_item = json_data['response']['liked_posts'][x]['video_url'] 
			# print(url_item)
			url_list.write(url_item+'\n')
		except Exception as e:
			# print("pic")
			pass

    # print('video_cnt = ',video_cnt)
	# return video_cnt

def get_content(json_data):

	item_len = len(json_data['response']['liked_posts'])
	print("item_len = ",item_len)

	try:
	    # print( len(load_dict['response']['liked_posts'][i]['photos']) ) #[0]['original_size']['url'] ) #pic
	    # print( load_dict['response']['liked_posts'][i]['video_url'] ) #video
	   	get_pic(json_data,item_len)
	   	get_video(json_data,item_len)

	except Exception as e:
		print("error")

if __name__ == "__main__":

	json_lists = open_json_file()
	for i in range(0,len(json_lists)):
		json_data = json.loads(json_lists[i])
		get_content(json_data)
