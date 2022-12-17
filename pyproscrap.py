import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title= []
companyname=[]
job_salary=[]
skill=[]

results=requests.get("https://arc.dev/remote-jobs")
sorc=results.content
soup=BeautifulSoup(sorc,"lxml")

infos=soup.find_all("div", {"class":"categories"})
jobtitles=soup.find_all("a", {"class":"job-title"})
companynames=soup.find_all("div",{"class":"company-name"})
job_salaries=soup.find_all("div", {"class":"sc-e7eddc9f-0 gjCxiD sc-51fada06-4 iKHQgE"})
print(jobtitles)
print(companynames)
print(job_salaries)

u=0
j=0
for i in range(len(companynames)):
    job_title.append(jobtitles[i].text)
    companyname.append(companynames[i].text)
    r = (infos[i].find_all("a"))
    sk = []
    for u in range(len(r)):
       sk.append(r[u].text)
    skill.append(sk)
    s = infos[i].find_all("div")
    if s!=[]:
       job_salary.append(s[0].text)
    else:
         job_salary.append("Not found")
print(skill)

file_list=[job_title,companyname,job_salary,skill]
xx =zip_longest(*file_list)
with open("E:/uuu.csv", "w") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["JOB_TITLE","COMPANY_NAME","JOB_SALARY","SKILLS"])
    wr.writerows(xx)