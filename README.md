# 一、介绍

本项目使用 python 编写，分析 tumblr 账户中喜欢的内容，给出资源链接，并下载。
![](https://github.com/cyang812/get_tumblr_likes/raw/master/download_file.png)

# 二、使用方法

- 1. 首先，你需要通过 tumblr API 来获取账户喜欢内容。这个过程是需要通过 OAuth 认证
具体可参看[这个网页](https://www.tumblr.com/docs/en/api/v2#auth)


- 2. 得到认证后可以通过脚本来获取资源内容，也可以通过[这个网页](https://api.tumblr.com/console/calls/user/likes#)来查询。结果通过 json 的形式返回


- 3. 保存你得到的 json 数据，命名为`test.json`，执行命令 `python json_parse.py`
    ![](https://github.com/cyang812/get_tumblr_likes/raw/master/json_parse.png)

- 4.上一步执行完，可以从 json 文件中提取出资源的真正链接，并存为 `url_list.txt` 文件
    ![](https://github.com/cyang812/get_tumblr_likes/raw/master/downloading.png)

- 5.执行 `python download.py`，之后资源文件就会挨个下载到 download 文件夹下
    ![](https://github.com/cyang812/get_tumblr_likes/raw/master/downloading.png)
