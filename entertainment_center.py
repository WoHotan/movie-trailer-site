# -*- coding: utf-8 -*-
import fresh_tomatoes
'''import html module,input movie list and output a html file that display movie
   trailer,poster and title'''
import media
'''import media module that contain class Movie to create instance'''
trailer_list=[["War Wolf 2","chinese hero",
"http://p0.meituan.net/movie/02ac72c0e8ee2987f7662ad921a2acc7999433.jpg@464w_644h_1e_1c",
"https://www.youtube.com/watch?v=SeubYXtDGlE"],
['Gintama','fuck avatar,stupid boy',
'http://p0.meituan.net/movie/f6915bebf74da3613e21772218191c30440943.png@464w_644h_1e_1c',
'https://www.youtube.com/watch?v=nQBUQmfuMlU'],
['avatar2','Avatar saves the planet，save your life ',
'https://images-na.ssl-images-amazon.com/images/M/MV5BNmM1NmY4N2QtNmVkOS00MjMyLWI5ZGUtYWYxMDRjY2MzNDdiXkEyXkFqcGdeQXVyMTAwMDAwMA@@._V1_.jpg',
'https://www.youtube.com/watch?v=vGNGGBzaNQ0'],
["Dunkirk",'Dunkirk war',
"http://p0.meituan.net/movie/782099c2b840b890150913d01ddfd7db5144766.jpg@464w_644h_1e_1c",
"https://www.youtube.com/watch?v=VQ01tJ4EWeg"],
['Colossal','official trailer for Colossal',
'https://resizing.flixster.com/-hMATuiQcLu9MjWZyU1f-MvmdzM=/206x305/v1.bTsxMjMyMzE1ODtqOzE3NDY3OzEyMDA7MjAzMjsyOTU2',
'https://www.youtube.com/watch?v=APQtxnfCxXU'],
['VROSKIII - "III" ft. YoungQueenz',
'Official video of  " III " by Vroskiii ft. YoungQueenz',
'https://i.ytimg.com/vi/glNwm13eC2g/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLApgVcY2IQRmIaWQ0g9kgbwV4NGtw',
'https://www.youtube.com/watch?v=beb8o5iPVXY'],
['GAME OF THRONES: SEASON 7','Winter is coming....',
'https://resizing.flixster.com/_MYOux4r7_b43uxRrkENZmFV-LI=/206x305/v1.dDsyNTk3Mjc7ajsxNzQ2MzsxMjAwOzIwMDA7MzAwMA',
'https://www.youtube.com/watch?v=1Mlhnt0jMlg']]
YoungQueenz=media.Movie(*trailer_list[5])
Dunkirk=media.Movie(*trailer_list[3])
game_of_thrones=media.Movie(*trailer_list[6])
Colossal=media.Movie(*trailer_list[4])
avatar=media.Movie(*trailer_list[2])
Gintama=media.Movie(*trailer_list[1])
War_Wolf_2=media.Movie(*trailer_list[0])
movie=[YoungQueenz,Dunkirk,game_of_thrones,Colossal,War_Wolf_2,avatar,Gintama]
fresh_tomatoes.open_movies_page(movie)
