import urllib2, urllib, cookielib
from getpass import getpass

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

top_level_url = "https://evaluations.uchicago.edu"
url = "https://evaluations.uchicago.edu/list.cfm"

username = raw_input("CNET ID: ")
password = getpass()

password_mgr.add_password(None, top_level_url, username, password)

authHandler = urllib2.HTTPBasicAuthHandler(password_mgr)

cj = cookielib.CookieJar()
cookHandler = urllib2.HTTPCookieProcessor(cj)

opener = urllib2.build_opener(authHandler, cookHandler)
opener.open("https://evaluations.uchicago.edu/list.cfm")
urllib2.install_opener(opener)

dept = urllib.urlencode({'Department': "CMSC"})

f = urllib2.urlopen(url, dept)

print f.read()



