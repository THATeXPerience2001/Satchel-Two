# Satchel:Two Fetcher Lib
# A library based on the legacy Satchel:Two CLI fetch script
# ProjectSCR 2026

"""Satchel:Two FetchLib

THIS MODULE IS DEPRECATED AND IS NO LONGER SUPPORTED 
PLEASE USE THE UPDATED FETCHLIB V2. 
"""

#Lots of library setup

from icalendar import Calendar
import csv
import urllib.request
import sys
import os
import ssl
from datetime import datetime, date
import pandas as pd
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')  # Suppress all warnings

#Setting up an SSL HTTPS context so it doesn't throw security errors

ssl._create_default_https_context = ssl._create_unverified_context

# Specific variable for passing a url from mainscript into the library

apiurl = None

#Variables for configuring directories

downloadlocation = 0
calendarlocation = 0
downloadfolder = 0
configlocation = 0

#Checks for a config file to avoid the user always inputting a calendar api url
#Since win32 can't create a text file pathlib steps in again to save the day!

def checkConfig():
    if os.path.exists(configlocation) == False:
        if sys.platform == "win32":
            home = Path.home()
            target_dir = home / "Documents" / "SatchelTwo"
            target_dir.mkdir(parents=True, exist_ok=True)
            file_path = target_dir / "config.txt"
            file_path.write_text("")    
        config = open(configlocation, "w")
        config.write(apiurl)
        config.close()
        config = open(configlocation, "r")
        satchellink = config.read()
        config.close()
        return satchellink
    else:
        config = open(configlocation, "r")
        satchellink = config.read()
        config.close()
        return satchellink

#Setting directories for specific platforms (Linux and MacOS share the same file structure so they're grouped together)
#Win32 needs to use pathlib because of course it does

if sys.platform == "win32":
    home = Path.home()
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo\Download"')
    downloadlocation = home / "Documents" / "SatchelTwo" / "Download" / "icalendars.ics"
    calendarlocation = home / "Documents" / "SatchelTwo" / "Download" / "icalendars.csv"
    cleanedlocation = home / "Documents" / "SatchelTwo" / "Download" / "cleaned.csv"
    downloadfolder = home / "Documents" / "SatchelTwo" / "Download"
    configlocation = home / "Documents" / "SatchelTwo" / "config.txt"
elif sys.platform == "darwin" or sys.platform ==  "linux":
    os.system("mkdir ~/SatchelTwo/")
    os.system("mkdir ~/SatchelTwo/Download/")
    downloadlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.ics")
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.csv")
    cleanedlocation = os.path.expanduser("~/SatchelTwo/Download/cleaned.csv")
    downloadfolder = os.path.expanduser("~/SatchelTwo/Download/")
    configlocation = os.path.expanduser("~/SatchelTwo/config.txt")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!") #Throwing an error for those who try running SatchelTwo on their... idk... Wii U?


satchellink = checkConfig()
destination = downloadlocation
print("Downloading ICAL")
urllib.request.urlretrieve(satchellink, destination)

#Preparing the ics to csv conversion

filename = downloadlocation
file_extension = str("ics")
headers = ('Summary', 'UID', 'Description', 'Location', 'Start Time', 'End Time', 'URL')

#Object oriented to make things cleaner down the line

class CalendarEvent:
    """Calendar event class"""
    summary = ''
    uid = ''
    description = ''
    location = ''
    start = ''
    end = ''
    url = ''

    def __init__(self, name):
        self.name = name

events = []

# The big chunk of the script that reads the ical

def open_cal():
    if os.path.isfile(filename):
        if file_extension == 'ics':
            f = open(downloadlocation, 'rb')
            gcal = Calendar.from_ical(f.read())

            for component in gcal.walk():
                event = CalendarEvent("event")
                if component.get('TRANSP') == 'TRANSPARENT': continue #skip event that have not been accepted
                if component.get('SUMMARY') == None: continue #skip blank items
                event.summary = component.get('SUMMARY')
                event.uid = component.get('UID')
                if component.get('DESCRIPTION') == None: continue #skip blank items
                event.description = component.get('DESCRIPTION')
                event.location = component.get('LOCATION')
                if hasattr(component.get('dtstart'), 'dt'):
                    event.start = component.get('dtstart').dt
                    if isinstance(event.start, date):
                        event.start = datetime.combine(event.start, datetime.min.time())
                if hasattr(component.get('dtend'), 'dt'):
                    event.end = component.get('dtend').dt
                    if isinstance(event.end, date):
                        event.end = datetime.combine(event.end, datetime.min.time())


                event.url = component.get('URL')
                events.append(event)
            f.close()
        else:
            print("You entered ", filename, ". ")
            print(file_extension.upper(), " is not a valid file format. Looking for an ICS file.")
            exit(0)
    else:
        print("I can't find the file ", filename, ".")
        print("Please enter an ics file located in the same folder as this script.")
        exit(0)

# Writing the ical data to the CSV

def csv_write(icsfile):
    if sys.platform == "win32":
        csvfile = calendarlocation
    else:
        csvfile = icsfile[:-3] + "csv"
    try:
        with open(csvfile, 'w') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(headers)
            for event in sortedevents:
                values = (event.summary.encode('utf8').decode(), event.uid, event.description.encode('utf8').decode(), event.location, event.start, event.end, event.url)
                wr.writerow(values)
    except IOError:
        print("Could not open file! Please close Excel!")
        exit(0)

open_cal() #Deprecated but runs anyways -\('_')/-
sortedevents=sorted(events, key=lambda obj: obj.start)
print("Writing CSV...")
csv_write(filename)

#Preparing to clean the CSV
#More annoyingness with windows using cp1252 over utf-8 grrrr

calendarlocation_str = str(calendarlocation)
input_csv = calendarlocation_str
output_csv = cleanedlocation

if sys.platform == "win32":
    df = pd.read_csv(input_csv, encoding="cp1252")
else:
    df = pd.read_csv(input_csv)

# Prepare new columns
new_columns = [
    "Name",
    "Class Name",
    "Homework Title",
    "Set By",
    "Set On",
    "Due On"
]

for col in new_columns:
    df[col] = None

# Parsing the whole thing to remove the leftover newlines from ical format

def parse_description(desc):
    if pd.isna(desc):
        return [None] * 6

    # Normalize newlines and split
    parts = (
        desc.replace("\\n", "\n")
            .replace("\r\n", "\n")
            .split("\n")
    )

    # Pad or trim to exactly 6 elements
    parts = (parts + [None] * 6)[:6]

    cleaned = []
    for i, part in enumerate(parts):
        if part is None:
            cleaned.append(None)
        elif ":" in part and i != 0:
            cleaned.append(part.split(":", 1)[1].strip())
        else:
            cleaned.append(part.strip())

    return cleaned

# Apply parsing so it looks nice and tidy
df[new_columns] = df["Description"].apply(
    lambda x: pd.Series(parse_description(x))
)

# Dropping the original Description column
df = df.drop(columns=["Description"])

df.to_csv(output_csv, index=False)

print("Cleaning up CSV...")

print("Calendar has been setup!")
