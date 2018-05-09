# -*- coding: utf-8 -*-

import get_json 
import json_parse 
import download 
import download_process

if __name__ == '__main__':
	get_json.main()
	json_parse.main()
	# download.main()		# 单进程
	download_process.main() # 多进程