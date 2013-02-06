# Main Script for Eval

import evalParser as EP
import evalModel as EM
import urllib, urllib2, cookielib, re, string
from bs4 import BeautifulSoup
from getpass import getpass

#baseurl = "https://evaluations-uchicago-edu.proxy.uchicago.edu/evaluation.cfm?fk_olcourseid={0}"
baseurl = "https://evaluations.uchicago.edu/list.cfm"

deptCode = raw_input("Which department? (4-letter code) ")

opener, listOfClassesFile = EP.connect(deptCode)
listOfClassURLs = EP.parseCourseListPage(listOfClassesFile)

dept = EM.Dept(deptCode)



print "Which metric do you want to use? (1-6)"
print "1) Most Organized"
print "2) Most Understandable"
print "3) Most Interesting"
print "4) Best Attitude Towards Students"
print "5) Most Accessible"
print "6) Best Overall"

metricNum = int(raw_input())
while metricNum not in range(1,7):
    print "Invalid input. Please enter a number 1-6"
    metricNum = raw_input()

keyword = EM.numToKeyword(metricNum)



for index, urlAdd in enumerate(listOfClassURLs):
    fullUrl = "https://evaluations-uchicago-edu.proxy.uchicago.edu/" + urlAdd
    teacher, statDict = EP.parsePage(fullUrl, opener)

    dept.addTeacher(teacher, statDict)
    
    teacher = dept.getTeacher(teacher.name)
    
    print "Progress: (%d / %d)" % (index+1, len(listOfClassURLs))
    
dept.rankTeachers(keyword)

for i, t in enumerate(dept.teachers):
    queryScore = "t.%sScore" % (keyword)
    print "%d. %s - %f" % (i+1, t.name, t.scoreDict[keyword])
    print t.rawDict[keyword]
    







