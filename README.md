# Movie trailer site
Use Python create a movie trailer site.

[media.py](https://github.com/WoHotan/movie-trailer-site/blob/master/media.py),class，open the tailer url.

[entertainment_center.py](https://github.com/WoHotan/movie-trailer-site/blob/master/entertainment_center.py),movie list and image.

[fresh_tomatoes.py](https://github.com/WoHotan/movie-trailer-site/blob/master/fresh_tomatoes.py),create a HTML file.

## 项目概述
  用python编写代码，存储喜爱的电影信息，包括剧照和电影预告片网址。然后编写一个静态网页，允许网页访客浏览电影和观看预告片。
  
## 项目细节

  
  - 安装 Python 2.7
  
  - 创建一个数据结构（即 Python 类）来存储喜爱的电影，包括电影片名、剧照网址（或海报网址）以及电影预告片的 YouTube 链接。
  - 创建该 Python 类的多个实例来代表喜爱的电影；将所有实例放在一个列表中。
  - 使用fresh_tomatoes.py 的 Python 模块 - 此模块有一个名为 open_movies_page的函数，它将一个参数作为输入，即电影列表，然后创建一个 HTML 文件来可视化喜爱的所有电影。 （这个fresh_tomatoes.py同时兼容 YouTube 和 Youku 的链接，需要 Movie 类中 trailer_youtube_url 属性改成 trailer_url）
  
