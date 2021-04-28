"""
Usage::

    >>> from checker import WebserverChecker
    >>> ws1 = WebserverChecker("https://www.example.org/")
    >>> good, color, text = ws1.check()
    >>> good
    True
    >>> color
    'green'
    >>> text
    '✓ 200'
"""

import requests

class WebserverChecker:

    def __init__(self, url):
        self.url = url
    
    def _status_is_okay(self, http_status):

        if not (100 <= http_status < 599):
            return False, "darkRed", f"Protocol violation ({http_status!r})"
        
        if http_status == 200:
            return True, "green", "✓ 200"

        hundreds = http_status // 100
        if hundreds == 2:
            return False, "yellow", f"? {http_status}"

        return false, "red", f"? {http_status}"


    def check(self):
        response = requests.head(self.url)
        return self._status_is_okay(response.status_code)


        