'''
Проанализируйте базу данных старых компьютерных игр.
(https://github.com/Newbilius/Old-Games_DOS_Game_Gauntlet/blob/master/GAMES.csv)

С помощью графиков ответьте на следующие вопросы:

Какие годы были самыми популярными с точки зрения выхода игр?
Какие жанры были популярны в различные периоды времени?
'''
import re

with open("database.txt", "r", encoding="utf-8") as f:
    count = 0
    year = ""
    dict = {}
    for line in f.readlines():
        match = re.search(";\"\d\d\d\d", line)
        if match is not None:
            if year == match[0][2:]:
                count += 1
            else:
                dict[year] = count
                count = 1
                year = match[0][2:]

print(dict)
