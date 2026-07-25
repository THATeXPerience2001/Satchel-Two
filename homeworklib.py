# Satchel:Two Homework Library
# "You know what this needs? Even more subscripts." - Aaron McCormick, 2026

# This script is not implemented yet, but is here for experimental testing for future releases.

# Library setup 

"""Satchel:Two Homework Library

This module can take an input of a specific homework id from 
Satchel:One and the user's authentication token (Via the Print Homework URL) 
and return key information about the specified assignment in a list and generate
a HTML with the description from the info.
"""

import sys
import os
import ssl
from pathlib import Path
import requests
import base64
import warnings
import re

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

class homework:
    
    def getHomework(self, homeworkId, myprinthwurl, saveLocation):
        
        homeworkId = str(homeworkId)
        printurl = str(myprinthwurl)
        if "homeworks" in printurl:
            auth = printurl[65:289]
        elif "flexible_tasks" in printurl:
            auth = printurl[70:294]
        elif "classworks" in printurl:
            auth = printurl[66:290]

        # Whole bunch of URL stuff to send for specific headers using the token and response

        url = ("https://api.satchelone.com/api/homeworks/" + homeworkId)

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

        response = requests.get(url, headers=headers, verify=False)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response from the Satchel:One API
        data = response.json()

        strdata = str(data)

        global homeworkinfo
        homeworkinfo = None

        # Getting that info from the response JSON
        if "{'classwork':" in strdata:
            homeworkinfo = data.get("classwork", [{}])
        elif "{'homework':" in strdata:
            homeworkinfo = data.get("homework", [{}])
        elif "{'flexible_task':" in strdata:
            homeworkinfo = data.get("flexible_task", [{}])


        advanced_hwid = homeworkinfo.get("id")
        title = homeworkinfo.get("title")
        subject = homeworkinfo.get("subject")
        duedate = homeworkinfo.get("due_on")
        advanced_issued = homeworkinfo.get("issued_at")
        advanced_published = homeworkinfo.get("published_at")
        advanced_created = homeworkinfo.get("created_at")
        advanced_updated = homeworkinfo.get("updated_at")
        classgroup = homeworkinfo.get("class_group_name")
        teachername = homeworkinfo.get("teacher_name")
        rawdescription = homeworkinfo.get("description")

        description = ("<!DOCTYPE html><body><h1>" + title + "</h1><br><h3>Homework set by " + teachername + ", due on " + duedate + "</h3><br><h5>Last Updated: " + advanced_updated + "</h5>" + rawdescription + "</body>")

        def removeStyle(html):
            style = re.compile(r' style\=.*?\".*?\"')    
            html = re.sub(style, '', html)

            return(html)
        
        description = removeStyle(description)
        
        hwinfodat = [title, subject, teachername, classgroup, duedate, advanced_hwid, advanced_created, advanced_issued, advanced_published, advanced_updated]

        try:
            with open((saveLocation + str(advanced_hwid) + ".html"), "w+", encoding="utf-8") as file:
                file.write(description)
                file.close()
        except FileExistsError:
            with open((saveLocation + str(advanced_hwid) + ".html"), "w", encoding="utf-8") as file:
                file.write(description)
                file.close()
        return hwinfodat

if __name__ == '__main__':
    print("HOMEWORKLIB TEST MODE")
    phwurl = str(input("Enter Print Homework URL for auth: "))
    ano = str(input("Enter Assignment ID: "))
    save = str(input("Enter save location: "))
    hw = homework()
    assignment = (hw.getHomework(ano, phwurl, save))

    