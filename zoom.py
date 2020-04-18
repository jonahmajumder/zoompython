import subprocess
from urllib import parse

class Meeting():
    '''
    Represents a zoom meeting.

    kwargs are:

    location: domain, defaults to 'zoom.us'
    confno: conference ID number
    withav: boolean, whether to join with audio/video or not
    browser: 'chrome', 'firefox', 'msie', 'safari'
    username
    accounttype: 'work', 'facebook', 'google', 'sso', 'api'
    hostid: host user ID number
    password

    '''

    SCHEME = 'zoommtg'
    PARAMS = ['confno', 'zc', 'browser', 'uname', 'stype', 'sid', 'pwd']

    def __init__(self, *args, **kwargs):
        self._parse_kwargs(kwargs)
        pass

    def _parse_kwargs(self, kwargs):
        self.location = kwargs.get('location', 'zoom.us')

        self.confno = kwargs.get('confno')
        self.zc = 0 if kwargs.get('withav', True) else 1
        self.browser = kwargs.get('browser')
        self.uname = kwargs.get('username')

        stypedict = {'work': 100, 'facebook': 0,
            'google': 1, 'sso': 101, 'api': 99}

        self.stype = stypedict.get(kwargs.get('accounttype'))
        self.sid = kwargs.get('hostid')
        self.pwd = kwargs.get('password')

    def _make_url(self, action):
        querydict = {k:getattr(self, k) for k in self.PARAMS if getattr(self, k) is not None}

        query = parse.urlencode(querydict)

        urltuple = (self.SCHEME, self.location, action, '', query, '')
        url = parse.urlunparse(urltuple)

        return url

    def _follow_url(self, url):
        pobj = subprocess.Popen(['open', url])

    def start(self):
        u = self._make_url('start')
        self._follow_url(u)

    def join(self):
        u = self._make_url('join')
        self._follow_url(u)




