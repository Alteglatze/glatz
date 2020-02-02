# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:34:13 2020

@author: glatze
"""

import requests
from bs4 import BeautifulSoup
import re


web_addr = 'https://jmuforbescenter.com/index.shtml'
filename_jmu_forbes_center = 'C:/users/glatz/working_projects/jmu_forbes_center.txt'

page = requests.get('https://jmuforbescenter.com/index.shtml')
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.find_all(class_="mobiletitle")
event = []
days_of_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for x in range(len(body)):
    event.append(re.sub(r'\n\s*\n', ' ', body[x].get_text().strip()))

with open(filename_jmu_forbes_center, 'w', encoding='utf-8')as file_object:
   file_object.write("Forbes Center Coming Events")
   file_object.write("\n")
   file_object.write('\n')
   for y in range(len(event)):
       if event[y][0:3] in days_of_week:
           if y == 1:
                file_object.write(event[y])
                file_object.write('\n')
                file_object.write(event[y-1])
                file_object.write('\n')
                file_object.write('\n')
           elif event[y][0:3] and event[y-3][0:3] in days_of_week:
                file_object.write(event[y])
                file_object.write('\n')
                file_object.write(event[y-2])
                file_object.write('\n')
                file_object.write(event[y-1])
                file_object.write('\n')
                file_object.write('\n')
           elif event[y][0:3] and event[y-4][0:3] in days_of_week and event[y-2][0:3] not in days_of_week:
                file_object.write(event[y])
                file_object.write('\n')
                file_object.write(event[y-3])
                file_object.write('\n')
                file_object.write(event[y-2])
                file_object.write('\n')
                file_object.write(event[y-1])
                file_object.write('\n')
                file_object.write('\n')
           else:
                file_object.write(event[y])
                file_object.write('\n')
                file_object.write(event[y-1])
                file_object.write('\n')
                file_object.write('\n')
                
"""                
for y in range(len(event)):
    if event[y][0:3] in days_of_week:
        if y == 1:
            print(event[y])
            print(event[y-1])
            print('\n')
        elif event[y][0:3] and event[y-3][0:3] in days_of_week:
            print(event[y])
            print(event[y-2])
            print(event[y-1])
            print('\n')
        elif event[y][0:3] and event[y-4][0:3] in days_of_week and event[y-2][0:3] not in days_of_week:
            print(event[y])
            print(event[y-3])
            print(event[y-2])
            print(event[y-1])
            print('\n')
        else:
            print(y, event[y])
            print(y, event[y-1])
            print('\n')
"""            
            
           
            

