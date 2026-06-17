# Satchel:Two GUI Info Fetcher
# "So what's your name?" "I dunnno."

"""Satchel:Two Info Library

This module can take an input of a Print Homework URL from Satchel:One 
and return the Forename, Surname and Avatar URL of the Student encoded in 
the authentication token of the Print Homework URL.
"""

# Library setup 

import sys
import os
import ssl
from pathlib import Path
import requests
import base64
import warnings

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()


# Setting up an ssl context because it gets mad if you don't

class getinfo():

    def fetchinfo(self, myprinthwurl=""):

        printurl = myprinthwurl
        if "homeworks" in printurl:
            auth = printurl[65:289]
        elif "flexible_tasks" in printurl:
            auth = printurl[70:294]
        elif "classworks" in printurl:
            auth = printurl[66:290]
        decoded = str(base64.b64decode(auth))
        studenttoken = decoded[10:18]

        # Whole bunch of URL stuff to send for specific headers using the token and response

        url = ("https://api.satchelone.com/api/students/" + studenttoken)
        params = {
            "include": "package"
        }

        headers = {
            "Accept": "application/smhw.v2021.5+json",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://www.satchelone.com/todos/upcoming",
            "X-Platform": "web",
            "Authorization": ("Bearer" + auth ),
            "Origin": "https://www.satchelone.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "If-None-Match": 'W/"72d6b5ac5b8eec8c5f5ce2e0d1f5979a"',
            "User-Agent": (
                "python-requests/2.32.5"
            ),
        }

        response = requests.get(url, headers=headers, params=params, verify=False)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response from the Satchel:One API
        data = response.json()

        # Getting that info from the response JSON
        studentinfo = data.get("student", [{}])

        forename = studentinfo.get("forename")
        surname = studentinfo.get("surname")
        avatarurl = str(studentinfo.get("avatar"))

        details = [forename, surname, avatarurl]
        
        return details

if __name__ == '__main__':
    print("I'm a module, not a script silly!")