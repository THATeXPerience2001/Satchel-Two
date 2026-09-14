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
    
    def getHomework(self, homeworkId, myprinthwurl, saveLocation, isquiz):
        
        homeworkId = str(homeworkId)
        printurl = str(myprinthwurl)
        auth = str((printurl.split("smhw_token=", 1)[1]))

        # Whole bunch of URL stuff to send for specific headers using the token and response

        #If it's a quiz, use a fallback as this isn't implemented yet.
        if isquiz == True:
            url = ("https://api.satchelone.com/api/quizzes/" + homeworkId)
        else:
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
        homeworkinfo = ""

        # Getting that info from the response JSON
        if "'classwork':" in strdata:
            homeworkinfo = data.get("classwork", [{}])
        elif "'homework':" in strdata:
            homeworkinfo = data.get("homework", [{}])
        elif "'flexible_task':" in strdata:
            homeworkinfo = data.get("flexible_task", [{}])
        elif "'quiz':" in strdata:
            homeworkinfo = data.get("quiz", [{}])
        else:
            raise Exception("ERROR WITH RESPONSE DATA!")


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

        if isquiz == True: #If it's a quiz, add a special text to say that this isn't implemented yet.
            description = ("<!DOCTYPE html><body><h1>" + title + "</h1><br><h3>Homework set by " + teachername + ", due on " + duedate + "</h3><br><h5>Last Updated: " + advanced_updated + "</h5>" + rawdescription + "<br><h5>This assignment is a Quiz, and has not yet been implemented.</h5><h5>Please use the Satchel:One button and do the Quiz online.</h5><h5>Sorry for any inconveniences!</h5>" + "</body>")
        else:
            description = ("<!DOCTYPE html><body><h1>" + title + "</h1><br><h3>Homework set by " + teachername + ", due on " + duedate + "</h3><br><h5>Last Updated: " + advanced_updated + "</h5>" + rawdescription + "</body>")

        def removeStyle(html): #Remove that HTML style!
            style = re.compile(r' style\=.*?\".*?\"')    
            html = re.sub(style, '', html)

            return(html)
        
        description = removeStyle(description)
        
        hwinfodat = [title, subject, teachername, classgroup, duedate, advanced_hwid, advanced_created, advanced_issued, advanced_published, advanced_updated]

        # Write the homework to a HTML and save it
        try:
            with open((saveLocation + str(advanced_hwid) + ".html"), "w+", encoding="utf-8") as file:
                file.write(description)
                file.close()
        except FileExistsError:
            with open((saveLocation + str(advanced_hwid) + ".html"), "w", encoding="utf-8") as file:
                file.write(description)
                file.close()
        return hwinfodat

    def getTodos(self, myprinthwurl, taskid):

        #homeworkId = str(homeworkId)
        printurl = str(myprinthwurl)
        auth = str((printurl.split("smhw_token=", 1)[1]))
    
        # Same bunch of stuff but the todo version this time
        
        url = ("https://api.satchelone.com/api/todos")
        
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
        jsontodo = response.json()
        todoraw = jsontodo.get("todos", [{}])

        for x in todoraw:
            if str(x.get("class_task_id")) == str(taskid):
                idoftask = x.get("id")
                statusoftask = x.get("completed")
                status = [idoftask, statusoftask]
                return status
        return None

    def handin(self, classtaskid, myprinthwurl, status):
        # This is how we hand in assignments
        printurl = str(myprinthwurl)
        auth = str((printurl.split("smhw_token=", 1)[1]))
        
        # If the assignment IS NOT handed in, hand it in.
        if status == False:
            response = requests.put(
            ("https://api.satchelone.com/api/todos/" + str(classtaskid)),
            headers={
                "Accept": "application/smhw.v2021.5+json",
                "Authorization": ("Bearer" + auth),
                "Prefer": "safe",
                "x-platform": "web",
            },
            json={"todo": {"completed": True}},
            )

            response.raise_for_status()
            return True
        else: #If the assignmnet IS handed in, withdraw it.
            response = requests.put(
            ("https://api.satchelone.com/api/todos/" + str(classtaskid)),
            headers={
                "Accept": "application/smhw.v2021.5+json",
                "Authorization": ("Bearer" + auth),
                "Prefer": "safe",
                "x-platform": "web",
            },
            json={"todo": {"completed": False}},
            )

            response.raise_for_status()
            return False

        

if __name__ == '__main__':
    print("HOMEWORKLIB TEST MODE")
    phwurl = str(input("Enter Print Homework URL for auth: "))
    ano = str(input("Enter Assignment ID: "))
    save = str(input("Enter save location: "))
    hw = homework()
    assignment = (hw.getHomework(ano, phwurl, save))
    #hw = homework()
    #todos = homework.getTodos(None, myprinthwurl=phwurl, taskid=None)
    #print(todos)
    