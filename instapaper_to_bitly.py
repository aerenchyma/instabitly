# script to save links from Instapaper in bitly, thoroughly commented

# assumes you have an Instapaper account (http://www.instapaper.com)
# AND a bitly account (http://bitly.com)

# TODO: neater and more comprehensive error checking!
# TODO: offer options to not run through all 2000> of your latest Instapaper links
# TODO: more options via command-line args in general

##########

import secure_info_instabitly as sib
import getpass
import mechanize
# some code adapted from http://stockrt.github.com/p/emulating-a-browser-in-python-with-mechanize/
import urllib, requests

# instantiate browser object
br = mechanize.Browser()

# browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


# open a site
try:
    r = br.open('http://www.instapaper.com/')
    html = r.read()
except:
    print "Error -- do you have an internet problem? \n Can't access Instapaper."
  
    
try:
    login_link = [l for l in br.links(url_regex='login')][0]
except:
    print "Error: no login link. Try again? \n You are going for instapaper.com, right?"
else:
    req = br.click_link(login_link)
    br.open(req)
    br.select_form(nr=0)
    username = raw_input("Input the email address for your Instapaper account.\n")
    password = getpass.getpass("Input your Instapaper password.\n")
    br.form['username'] = username
    br.form['password'] = password 
    br.submit()
    
    br.select_form(nr=8) # 10 forms, appropriate one is second to last, programmatical numbering
    br.submit()
    links = br.response().read() # 
    links_list = links.split("\n")


# interact with bitly!

# (assumes another file: secure_info_instabitly.py with oauth token -- 
#    could store Instapaper login info there as well. 
#    otherwise, can fill in your personal bitly oauth token here. 
#  GET A TOKEN @ https://bitly.com/a/oauth_apps )

oauth_token = sib.oauth_token
baseurl = "https://api-ssl.bitly.com/v3/user/link_save?"

# bitly returns a 'link already saved' response and doesn't save same link twice
try:
    for l in links_list[1:]: # don't include CSV header
        link = l.split(",")[0]
        params = {'access_token': oauth_token, 'longUrl': link}
        req = baseurl+urllib.urlencode(params)
        res = requests.get(req)
        #print "Just saved: ", link ## if you want to see it working
except:
    print "...Did you ignore an error somewhere or something?"
