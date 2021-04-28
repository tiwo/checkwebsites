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

    >>> WebserverChecker("http://example.invalid/").check()
    (False, 'darkRed', '🛑 Connection Error')

"""

import requests

class WebserverChecker:

    def __init__(self, url):
        self.url = url


    def check(self):
        """Run the test and return a tuple of good, color, text

        where
        - `good` is True or false depending on wether the test succeeded
        - `color` is a proposed color name depending on the result
        - `text` is a short description of the result, as a string.

        """
        try:
            response = requests.head(self.url)
        except requests.exceptions.RequestException:
            return False, "darkRed", "🛑 Connection Error"
        return self._status_is_okay(response.status_code)


    def _status_is_okay(self, http_status):


        if not (100 <= http_status < 599):
            return False, "darkRed", f"Protocol violation ({http_status!r})"
        
        if http_status == 200:
            return True, "green", "✓ 200"

        hundreds = http_status // 100
        if hundreds == 2:
            return False, "yellow", f"⚠️ {http_status}"

        return false, "red", f"🛑 {http_status}"


