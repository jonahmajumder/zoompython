import subprocess
from urllib import parse

'''
URL Scheme Explanation
https://medium.com/zoom-developer-blog/zoom-url-schemes-748b95fd9205

Sample URL
zoommtg://zoom.us/join?confno=123456789&pwd=xxxx&zc=0&browser=chrome&uname=Betty

Params are:
    
confno: Meeting ID
zc: Zoom meeting control options
    0: with video and audio
    1: screen share only without video and audio
browser: browser type (optional)
    “chrome”
    “firefox”
    “msie”
    “safari”
uname: User name
stype: User’s login type
    100: Work Email user
    0: Facebook user
    1: Google user
    101: SSO user
    99: Cust API user
sid: Host user ID
token: Host user token
pwd: Meeting Password

'''

PMI = '5424941851'

d = {
    # 'confno': PMI,
    # 'pwd': 'xxxx',
    'zc': 1,
    # 'browser': 'chrome',
    # 'stype': 1,
    # 'uname': 'Jonah Majumder',
}


s = 'zoommtg'

loc = 'zoom.us'

path = '/start'

q = parse.urlencode(d)

u = parse.urlunparse((s, loc, path, '', q, ''))

print(u)

pobj = subprocess.Popen(['open', u])

# pobj.wait()