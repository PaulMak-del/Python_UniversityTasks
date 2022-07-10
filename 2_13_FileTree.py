'''
Реализуйте утилиту командной строки, формирующую дерево каталогов и файлов с учетом вложенности и начиная с заданного пути. 
Результат должен быть выдан в виде текста в формате graphviz.
'''

import os
import graphviz

directory_name = '.'
tree = os.walk(directory_name)
dot = graphviz.Digraph(directory_name)

letter = 'B'
for el in tree:
    direct = (el[0].split("\\"))[-1]
    for el_2 in el[1]:
        dot.edge(direct, el_2)
    for el_2 in el[2]:
        dot.edge(direct, el_2)


print(dot)
