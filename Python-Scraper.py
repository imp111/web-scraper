from types import CodeType
from bs4 import BeautifulSoup
import requests
from datetime import date

html_text = requests.get('https://dev.bg/company/jobs/back-end-development/').text 
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'box job-details-holder job-list-item')
day_today = date.today().day

for job in jobs:
    job_postTime = job.find('div', class_ = "job-info-holder").text.replace('\n', '')

    more_info = job.a['href']
    buff = job_postTime.split(" ")
    postTime = int(buff[0])

    if (postTime != day_today):
        break

    job_title = job.find('h3', class_ = 'h3-style3 no-margin').text.replace('\n', '')
    job_company = job.find('div', class_ = 'small-txt txt-grey').text.replace('\n', '')

    moreInfo = requests.get(more_info).text 
    soupTwo = BeautifulSoup(moreInfo, 'lxml')
    skills = soupTwo.find('div', class_ = 'tag-holder')

    skill = skills.find_all('div', class_ = "tag-name")
    listOfSkills = " "

    for x in skill:
        a = x.text
        listOfSkills += a
        listOfSkills += ' | '

    
    print(f'''
    Job Name: {job_title}
    Company name and location: {job_company}
    Post date: {job_postTime}
    Link to job: {more_info}
    Skills: {listOfSkills}
    ''')

    print('')
            