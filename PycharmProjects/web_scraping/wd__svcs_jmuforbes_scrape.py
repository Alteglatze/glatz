# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:32:09 2019

@author: glatze
"""

from bs4 import BeautifulSoup
import requests
import re

class SoupScrapes(object):
    def __init__(self, web_addr):
        self.web_addr = web_addr
        
    def scrape_wisdom_ganga(self):
        r = requests.get(self.web_addr, headers={"User-Agent": "XY"})
        soup = BeautifulSoup(r.text, 'lxml')
        te = soup.findAll('figure', {'class':'wp-block-table'})
        with open(filename_wisdom_ganga, 'w') as file_object:
            file_object.write("Wisdom Ganga's Phishing and Scam Sites List")
            for tbl in te:
                sites = tbl.findAll('td')
                for site in sites:
                   file_object.write(site.text)
                   file_object.write('\n') 
                 
                   
    def scrape_shen_valley_choral(self):
        page = requests.get(web_addr)
        soup = BeautifulSoup(page.content, 'html.parser')
        body = soup.find(class_="entry-content")
        with open(filename_svcs, 'w', encoding='utf-8')as file_object:
            file_object.write("Concert Schedule")
            for paragraph in body.find_all('p'):
                file_object.write(str(paragraph.text))
                file_object.write('\n' '\n')
              
    def scrape_jmu_forbes(self):
        page = requests.get(web_addr)
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
        
web_addr = "https://wisdomganga.com/list-of-scam-sites-update-regularly/"        
filename_wisdom_ganga = "C:/users/glatz/working_projects/wisdom_ganga_sites.txt"

phishing_sites = SoupScrapes(web_addr)
phishing_sites.scrape_wisdom_ganga()

web_addr = 'https://www.singshenandoah.org/concert-schedule/'
filename_svcs = 'C:/users/glatz/working_projects/svcs_schedule.txt'

shen_valley_choral = SoupScrapes(web_addr)
shen_valley_choral.scrape_shen_valley_choral()

web_addr = 'https://jmuforbescenter.com/index.shtml'
filename_jmu_forbes_center = 'C:/users/glatz/working_projects/jmu_forbes_center.txt'

jmu_forbes_center = SoupScrapes(web_addr)
jmu_forbes_center.scrape_jmu_forbes()
