# Satchel:Two
# Finally a client that actually looks nice!

print(r"  _________       __         .__           .__       ___________               ")
print(r" /   _____/____ _/  |_  ____ |  |__   ____ |  |   /\ \__    ___/_  _  ______   ")
print(r" \_____  \\__  \\   __\/ ___\|  |  \_/ __ \|  |   \/   |    |  \ \/ \/ /  _ \  ")
print(r" /        \/ __ \|  | \  \___|   Y  \  ___/|  |__ /\   |    |   \     (  <_> ) ")
print(r"/_______  (____  /__|  \___  >___|  /\___  >____/ \/   |____|    \/\_/ \____/  ")

print("Satchel:Two CONSOLE")
print("Version: 1.1a - Backpack")

# Library Setup

try:
    from tkinter import *
    import customtkinter as ctk
    import icalendar
    from PIL import Image, ImageFile
    import urllib.request
    import sys
    import os
    import ssl
    import re
    import pandas as pd
    from pathlib import Path
    import tkinterweb
    from tkinterweb import HtmlFrame
    import infolib
    import fetchlib2 as fetchlib
    import homeworklib
    import base64
    import requests
    import webbrowser
    from datetime import datetime
    import time
    import yaml
    print("Libraries loaded OK!")

except Exception as e:
    print(f"Satchel:Two encountered an error while importing necessary modules or libraries: {e}")

# All the config lines ect...

projfile = os.path.realpath(__file__)
dir = os.path.dirname(projfile)
requests.packages.urllib3.disable_warnings()
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
deftheme = str(dir + "/breaktime.json")
ctk.set_default_color_theme(deftheme)
hw = homeworklib.homework()
tkinterweb.utilities.DARK_STYLE = """
/* Additional stylesheet to be loaded whenever dark mode is enabled. */
/* Display properties document body. */
HTML, BODY {
  background-color: #232323;
  color: #ffffff;
}

/* Display properties for mark elements. */
MARK {
    background: #8c7c00;
}

/* Display properties for hyperlinks */
:link    { color: #7768d9; }
:visited { color: #5245a8; }

/* Display properties for form items. */
INPUT, TEXTAREA, SELECT, BUTTON { 
  background-color: #171524;
  color: #ffffff;
}
INPUT[type="submit"],INPUT[type="button"], INPUT[type="reset"], BUTTON {
  background-color: #171524;
  color: #ffffff;
  color: tcl(::tkhtml::if_disabled #666666 #ffffff);
}
"""

# Setting directories and DPI Scaling

if sys.platform == "win32":
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo\Download"')
    ctk.deactivate_automatic_dpi_awareness()
else:
    os.system("mkdir ~/SatchelTwo/")
    os.system("mkdir ~/SatchelTwo/Download/")

# Windows uses a different file structure

if sys.platform == "win32":
    home = Path.home()
    dldir = home / "Documents" / "SatchelTwo" / "Download"
    dldir = str(dldir) + "\\"
else:
    dldir = os.path.expanduser("~/SatchelTwo/Download/")

calendarlocation = 0

# Checking for platform configuration to get an actual path setup

if sys.platform == "win32":
    calendarlocation = home / "Documents" / "SatchelTwo" / "Download" / "cleaned.csv"
elif sys.platform == "darwin" or sys.platform == "linux":
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/cleaned.csv")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!")
    # I've run Satchel:Two on some REALLY obscure stuff, and that's only when this error shows up.

if os.path.isfile("config.yaml") == False:
    with open("config.yaml", "w") as conf:
        yaml.safe_dump({'currentTheme': 'Light', 'key': None, 'photoEnabled': True, 'nameEnabled': True, 'htmlScale': 1, 'dpiScalingEnabled': False}, conf)
        conf.close()

with open("config.yaml", "r") as conf:
    s2config = yaml.safe_load(conf)
    conf.close()

# Settings window

def openSettings():

    with open("config.yaml", "r") as conf:
        s2config = yaml.safe_load(conf)

    # Toggling the profile photo
    
    def togglePhoto():
        with open("config.yaml", "r") as conf:
            s2config = yaml.safe_load(conf)
            if s2config["photoEnabled"] == False:
                with open("config.yaml", "w") as conf:
                    s2config["photoEnabled"] = True
                    yaml.safe_dump(s2config, conf)
            else:
                with open("config.yaml", "w") as conf:
                    s2config["photoEnabled"] = False
                    yaml.safe_dump(s2config, conf)
        conf.close()

    def toggleName():
        with open("config.yaml", "r") as conf:
            s2config = yaml.safe_load(conf)
            if s2config["nameEnabled"] == False:
                with open("config.yaml", "w") as conf:
                    s2config["nameEnabled"] = True
                    yaml.safe_dump(s2config, conf)
            else:
                with open("config.yaml", "w") as conf:
                    s2config["nameEnabled"] = False
                    yaml.safe_dump(s2config, conf)
        conf.close()

    # Fix for inconsistent decimal values with CTkSlider

    def adjustScale(value):
        if value == (1.2999999999999998):
            scl = 1.3
        else:
            scl = value

        with open("config.yaml", "r") as conf:
            s2config = yaml.safe_load(conf)
            with open("config.yaml", "w") as conf:
                s2config["htmlScale"] = float(scl)
                yaml.safe_dump(s2config, conf)
        conf.close()
        

    # Config for Settings/About window

    about = ctk.CTkToplevel(root)
    about.configure(fg_color=("#ffffff", "#232323"))
    about.title("Satchel:Two Settings")
    about.geometry("640x340")  
    about.resizable(False, False)
    appearance = ctk.get_appearance_mode()
    if appearance == "Dark":
        aLg = ctk.CTkImage(dark_image = Image.open(str(dir + "/Assets/newlogotransparent.png")), size = (128,80))
        aBox = ctk.CTkImage(dark_image = Image.open(str(dir + "/Assets/aboutboxdark.png")), size = (300,320))
        icon = PhotoImage(file = dir + "/Assets/Dark.png")
        root.iconphoto(True, icon)
    else:
        aLg = ctk.CTkImage(light_image = Image.open(str(dir + "/Assets/newlogotransparent.png")), size = (128,80))
        aBox = ctk.CTkImage(light_image = Image.open(str(dir + "/Assets/aboutboxlight.png")), size = (300,320))
        icon = PhotoImage(file = dir + "/Assets/Light.png")
        root.iconphoto(True, icon)
    if s2config["photoEnabled"] == False:
        photoOn = ctk.StringVar(value="false")
    else:
        photoOn = ctk.StringVar(value="true")
    if s2config["nameEnabled"] == False:
        nameOn = ctk.StringVar(value="false")
    else:
        nameOn = ctk.StringVar(value="true")
    photoOn = ctk.CTkSwitch(about, text="Show Profile Photo", command=togglePhoto, variable=photoOn, onvalue="true", offvalue="false", button_color=("#eeeeee", "#323232"), button_hover_color=("#dddddd", "#434343"), progress_color=("#6472CD"))
    nameOn = ctk.CTkSwitch(about, text="Show Name", command=toggleName, variable=nameOn, onvalue="true", offvalue="false", button_color=("#eeeeee", "#323232"), button_hover_color=("#dddddd", "#434343"), progress_color=("#6472CD"))
    htmlscaletext = ctk.CTkLabel(about, text="Assignment Viewer Text Scale", fg_color="transparent")
    htmlScaleslider = ctk.CTkSlider(about, from_=1, to=2, number_of_steps=10, command=adjustScale, button_color=("#eeeeee", "#323232"), button_hover_color=("#dddddd", "#434343"), progress_color=("#6472CD"),)
    with open("config.yaml", "r") as conf:
        s2config = yaml.safe_load(conf)
        htmlScaleslider.set(s2config["htmlScale"])
    conf.close()
    aboutLogo = ctk.CTkLabel(about, image = aLg, text="", fg_color=("transparent"))    
    aboutBox = ctk.CTkLabel(about, image = aBox, text="", fg_color=("transparent"))
    aboutText = ctk.CTkLabel(about, text="Satchel:Two", fg_color=("transparent"))
    aboutVersion = ctk.CTkLabel(about, text = "Version 1.1a - Backpack", fg_color=("transparent"))
    aboutUs = ctk.CTkLabel(about, text = "Made in the UK by ProjectSCR", fg_color=("transparent"))
    if sys.platform == "win32" or sys.platform == "linux":
        aboutSettingsTitle = ctk.CTkLabel(about, text = "Settings", fg_color=("transparent"), font=robototitle)
    else:
        aboutSettingsTitle = ctk.CTkLabel(about, text = "Settings", fg_color=("transparent"), font=sfprotitle)
    aboutSettingsText = ctk.CTkLabel(about, text = "These options require a restart of Satchel:Two", fg_color=("transparent"))
    aboutLogo.place(x = 480, y = 120, anchor = CENTER)
    aboutLogo.lift()
    aboutUs.place(x = 480, y = 180, anchor = CENTER)
    aboutText.place(x = 480, y = 200, anchor = CENTER)
    aboutVersion.place(x = 480, y = 220, anchor = CENTER)
    aboutBox.place(x = 480, y = 170, anchor = CENTER)
    photoOn.place(x = 100, y = 80, anchor = CENTER)
    nameOn.place(x = 81, y = 105, anchor = CENTER)
    htmlScaleslider.place(x = 121, y = 170, anchor = CENTER)
    htmlscaletext.place(x = 110, y = 140, anchor = CENTER)
    aboutSettingsText.place(x = 150, y = 300, anchor = CENTER)
    aboutSettingsTitle.place(x = 75, y = 20, anchor = CENTER)
    aboutBox.lower()
    aboutText.lift()
    aboutUs.lift()

    about.mainloop()

# Dedicated function for handling errors, troubleshooting can be found in the Wiki.

def throwError(code):
    errorwin = ctk.CTkToplevel(root)
    errorwin.configure(fg_color=("#ffffff", "#232323"))
    errorwin.title("Satchel:Two")
    errorwin.geometry("360x180")
    errorwin.resizable(False, False)
    close = ctk.CTkButton(errorwin, text = "Close", command = errorwin.destroy, fg_color = "#6472CD", bg_color=("#ffffff", "#232323"), hover_color = "#4D589C", text_color = "#FFFFFF")
    tryagain = ctk.CTkButton(errorwin, text = "Try Again?", command = errorwin.destroy, fg_color = "#6472CD", bg_color=("#ffffff", "#232323"), hover_color = "#4D589C", text_color = "#FFFFFF")
    relog = ctk.CTkButton(errorwin, text = "Press 'Log Out' to try again", command = errorwin.destroy, fg_color = "#6472CD", bg_color=("#ffffff", "#232323"), hover_color = "#4D589C", text_color = "#FFFFFF")
    endmain = ctk.CTkButton(errorwin, text = "Exit", command = root.destroy, fg_color = "#6472CD", bg_color=("#ffffff", "#232323"), hover_color = "#4D589C", text_color = "#FFFFFF")
    ebadGateway = ctk.CTkLabel(errorwin, text="We failed to fetch your assignments! CODE = YIPEE", bg_color=("#ffffff", "#232323"))
    eNetwork = ctk.CTkLabel(errorwin, text = "We encountered a network error! CODE = WIFFY", bg_color=("#ffffff", "#232323"))
    eCritical = ctk.CTkLabel(errorwin, text = "Satchel:Two has encountered a critical error! CODE = REQUIES", bg_color=("#ffffff", "#232323"))
    eBadApi = ctk.CTkLabel(errorwin, text = "Your API key is invalid! CODE = FOOLISHNESS", bg_color=("#ffffff", "#232323"))
    eExpired = ctk.CTkLabel(errorwin, text = "Your token has expired! CODE = SOURMILK", bg_color=("#ffffff", "#232323"))
    eBadApin = ctk.CTkLabel(errorwin, text = "You didn't put in anything! CODE = SILLY", bg_color=("#ffffff", "#232323"))
    pHwFetched = ctk.CTkLabel(errorwin, text = "Homework has been fetched!",bg_color=("#ffffff", "#232323")) 
    if code == "badGateway":
        ebadGateway.place(x = 180, y = 40, anchor = CENTER)
        tryagain.place(x = 180, y = 80, anchor = CENTER)
        print("ERROR: HTTP 502 - Bad Gateway") 
    if code == "network":
        eNetwork.place(x = 180, y = 40, anchor = CENTER)
        tryagain.place(x = 180, y = 80, anchor = CENTER) 
        print("ERROR: Network issue detected!")
    if code == "critical":
        eCritical.place(x = 180, y = 40, anchor = CENTER)
        endmain.place(x = 180, y = 80, anchor = CENTER)
        root.destroy()
        print("CRITICAL FAILURE DETECTED! Terminating...")
        raise Exception("Satchel:Two has encountered an unrecoverable error and has been closed.")
    if code == "badApi":
        eBadApi.place(x = 180, y = 40, anchor = CENTER)
        relog.place(x = 180, y = 80, anchor = CENTER)
        print("ERROR: Bad API token!")
    if code == "expired":
            eExpired.place(x = 180, y = 40, anchor = CENTER)
            relog.place(x = 180, y = 80, anchor = CENTER)
            print("ERROR: Expired token!")
    if code == "badApin":
        eBadApin.place(x = 180, y = 40, anchor = CENTER)
        relog.place(x = 180, y = 80, anchor = CENTER)
        print("ERROR: No API token recieved!")
    if code == "hwFetched":
        pHwFetched.place(x = 180, y = 40, anchor = CENTER)
        close.place(x = 180, y = 80, anchor = CENTER)

# Basic login function that also validates the Print Homework URL before extracting the API Token.

def login(startup):
    ok = False
    buttonsatchelone.configure(state = "disabled")
    imagetoolbar.lift()
    buttonsatchelone.lift()
    buttonhandin.lift()
    buttonassignments.configure(state = "disabled")
    global summarypos
    summarypos = 0
    root.update()
    global apitoken    
    # Checking for a stored api url in the YAML config
    # It isn't encrypted because it doesn't store any credentials plus it's not shared online
    # which may seem controversial but it expires after a month and requires this program to really
    # do anything with it. ¯\_(ツ)_/¯
    with open("config.yaml", "r") as conf:
            s2config = yaml.safe_load(conf)
            
    if startup == True and s2config["key"] != None:
        apitoken = s2config["key"]
    elif startup != True:
        loginprompt = ctk.CTkInputDialog(title = "Satchel:Two Login", text = "Welcome back! Please enter your Print Homework URL to log in.", fg_color=("#ffffff", "#232323"), button_fg_color = "#6D78CF", button_hover_color = "#4D589C")
        apitoken = loginprompt.get_input()
    else:
        loginprompt = ctk.CTkInputDialog(title = "Satchel:Two Login", text = "Welcome back! Please enter your Print Homework URL to log in.", fg_color=("#ffffff", "#232323"), button_fg_color = "#6D78CF", button_hover_color = "#4D589C")
        apitoken = loginprompt.get_input()
    
    global printhwurl
    global studenttoken
    conf.close()
    
    #  Checking if the apitoken is nothing because the user does not understand the concept of "pasting".

    if apitoken == None or apitoken == "":
        loginprompt.destroy()
        apitoken = ""
        buttonassignments.configure(state = "disabled")
        throwError("badApin")
    else:
        # Decoding the 3 variants of the url to obtain the api token.
        # Issue #10 patched by changing method.
        printhwurl = apitoken
        auth = str((apitoken.split("smhw_token=", 1)[1]))
        dec = str(base64.b64decode(auth))
        #Handling expired tokens
        expdate = re.search(r'(?<=expiry_date=)(.*?)(?=T)', dec)
        if expdate:
            expiry_date = expdate.group(1)
        expiry = expiry_date.replace("-", " ")
        date = str(datetime.today()).split()[0]
        date = date.replace("-", " ")
        expcomp = datetime.strptime(expiry, "%Y %m %d")
        datecomp = datetime.strptime(date, "%Y %m %d")
        if expcomp <= datecomp: #Comparing the dates to see if the token is past expiry
            expiredtoken = True
        else:
            expiredtoken = False
        sdttkn = re.search(r'(?<=user_id=)(.*?)(?=&)', dec)
        if sdttkn:
            studenttoken = sdttkn.group(1)
        apitoken = auth


    # Checks if the input is nothing to avoid a type error.
    if len(apitoken) < 1:
        apitoken = ""
        buttonassignments.configure(state = "disabled")
        throwError("badApin")

    else:   # If it passes, check if it's divisible by 4 so it can be base64 decoded.
        if len(apitoken) % 4 != 0:
            apitoken = ""
            buttonassignments.configure(state = "disabled")
            throwError("badApi")
        else:
            decoded = dec

            # Checks if the decoded token begins with user_id to verify it's valid.

            if "user_id" in dec == False:
                apitoken = ""
                throwError("badApi")
                buttonassignments.configure(state = "disabled")
                print("Invalid login detected!")
            elif expiredtoken == True:
                apitoken = ""
                throwError("expired")
                buttonassignments.configure(state = "disabled")
            else:
                print("Logged in OK!")
                buttonassignments.configure(state = "enabled")
                uinf = infolib.getinfo()
                userinfo = uinf.fetchinfo(myprinthwurl = printhwurl)

                # Interfacing with the API to fetch the student name and avatar    

                global forename
                global surname
                global fullname

                forename = userinfo[0]
                surname = userinfo[1]
                avatar = userinfo[2]
                fullname = (forename + " " + surname)

                with open("config.yaml", "r") as conf:
                    s2config = yaml.safe_load(conf)
                with open("config.yaml", "w") as conf:
                    s2config["key"] = str(printhwurl)
                    yaml.safe_dump(s2config, conf)
                

                # Reporting back to the debug log and updating UI for user

                print("Welcome back,", forename, surname, "!")
                urllib.request.urlretrieve(avatar, dldir + "avatar.jpeg")
                avtr = ctk.CTkImage(Image.open(str(dldir + "avatar.jpeg")), size=(96,136))
                name = ctk.CTkLabel(root, text = fullname, text_color=("#232323", "#ffffff"), corner_radius=6, width = 140, height = 45, wraplength = 120, bg_color = ("#6472CD", "#384079"), fg_color=("#ffffff", "#232323"))
                avatarframe = ctk.CTkFrame(root, border_color = "#ffffff", border_width = 2, corner_radius=6, width = 100, height = 140, bg_color="#5D67B4")
                avatarpic = ctk.CTkLabel(avatarframe, image = avtr, text="")
                if s2config["photoEnabled"] == True:
                    avatarframe.place(x = 80, y = 360, anchor=CENTER)
                    avatarpic.place(x = 50, y = 70, anchor=CENTER)
                if s2config["nameEnabled"] == True:
                    name.place(x = 80, y = 460, anchor=CENTER)
                name.lift()
                conf.close()
                root.update()
    
    
# The incredibly long system to fetch all of the assignments

def assignments():
    # Getting the UI ready
    root.update()
    buttonassignments.configure(state = "disabled")
    buttonabout.configure(state = "disabled")
    greeting.destroy()
    htmlviewer.load_url("about:blank")
    pleasewait = ctk.CTkLabel(root, text = "Please wait... Downloading assignments...", text_color = ("#232323", "#ffffff"), bg_color=("#ffffff", "#232323"))
    pleasewait.place(x = 480, y = 300, anchor = CENTER)
    pleasewait.place(aboveThis = None)
    root.update()

    # Setting up proper authentication for Requests

    auth = apitoken

    url = "https://api.satchelone.com/api/students/" + studenttoken
    params = {
        "include": "user_private_info"
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

    response = requests.get(url, headers=headers, params=params, verify = False)
    # Getting the response headers to extract the calendar token


    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Parse the JSON response from the SatchelOne API
    data = response.json()

    # Getting that info from the response JSON
    upi = data.get("user_private_infos", [{}])[0]

    # Passing the calendar url into the fetchlib library to setup the calendar, similar to fetch.py from the CLI

    calendartoken = upi.get("calendar_token")
    calendarurl = ("https://api.satchelone.com/icalendars.ics?token=" + str(calendartoken))
    
    hwt = fetchlib.fetchhw()
    homeworktemp = hwt.apifetch(apiurl=calendarurl)

    # Setting encoding because Windows hates me still

    if sys.platform == "win32":
        df = pd.read_csv(calendarlocation, encoding="utf-8", usecols=["UID", "Homework Title", "URL"])
    else:
        df = pd.read_csv(calendarlocation, usecols=["UID", "Homework Title", "URL"])
    uid_list = df["UID"].tolist()
    global summarylist
    summarylist = df["Homework Title"].tolist()
    urllist = df["URL"].tolist()
    for x in urllist:
        if "quizzes" in x:
            quizno = urllist.index(x)
            uid_list[quizno] = str("Q" + str(uid_list[quizno]))

    # Cleaning up the downloads DIR to prevent an infinite ammount of HTML's

    todelete = os.listdir(dldir)

    for item in todelete:
        if item.endswith(".html"):
            if item.startswith("S") == False: # Specifically here for future plans for self created assignments
                os.remove(os.path.join(dldir, item))

    count = 0

    # Initialising the downloads

    global downloads
    downloads = []

    # attempt to download all the homework files as HTML's

    try:
        while count < (len(uid_list)):
            print("Downloading assignment:", count)
            uid_current = str(uid_list[count])
            if "Q" in uid_current:
                uid_current = uid_current.replace("Q", "")
                assignment = hw.getHomework(uid_current, printhwurl, dldir, True)
            else:
                assignment = hw.getHomework(uid_current, printhwurl, dldir, False)
            downloads.append(uid_current + ".html")
            count = count + 1
        print("Todos fetched successfully!")
        global ok
        ok = True
    # Throw an error for BadGateways (Low chance now due to change in methods)
    except urllib.error.HTTPError as e:
        if e.code == 502:
            throwError("badGateway")
            summarylist = []
            ok = False
            pleasewait.destroy()
        if e.code == 404:
            pass
        else:   # Throw an error for internet connection
            throwError("network")
            summarylist = []
            ok = False
            pleasewait.destroy()
    except ("ConnectionAbortedError", "ConnectionError", "ConnectionRefusedError", "ConnectionResetError", "BadGateway"):
        throwError("network") # Treat any other errors as network errors which are most likely.
        summarylist = []
        ok = False
        pleasewait.destroy()

    # Create a list of all of the HTML's in the downloads directory
    htmllist = []
    global htmls
    htmls = os.listdir(dldir)
    for item in htmls:
        if item.endswith(".html"):
            htmllist.append(item)

    # Stop the UI after updating
    pleasewait.destroy()
    root.update()
    assignmentslist = ctk.CTkOptionMenu(root, values = summarylist, command=assignments_callback, width = 140, height = 20, fg_color = ("#FFFFFF", "#232323"), button_color = "#6472CD", button_hover_color = "#4D589C", bg_color = ("#6472CD", "#444D8B"), dropdown_fg_color = ("#FFFFFF", "#232323"), dropdown_hover_color = "#ADADAD", text_color = ("#000000", "#FFFFFF" ), dynamic_resizing=False, hover = False)
    assignmentslist.place(x = 80, y = 500, anchor = CENTER) 
    if ok == True:
        throwError("hwFetched") # Uses the throwError as a leftover function but less complicated
        htmlviewer.load_file(dldir + (downloads[0]))
        buttonsatchelone.configure(state = "disabled")
        buttonhandin.configure(state = "disabled")
        imagetoolbar.lift()
        buttonsatchelone.lift()
        buttonhandin.lift()
        buttoncreatehw.lift()
        global summarypos
        summarypos = 0
        htmlviewer.load_url("about:blank")
        root.update()
    buttonassignments.configure(state = "enabled")
    buttonabout.configure(state = "enabled")
    root.update()
   
# Creating a callback for the assignments list

def assignments_callback(choice):
    global summarypos
    global currentstatus
    global currentid
    summarypos = summarylist.index(choice)
    selection = downloads[summarypos]
    currentid = selection[:-5]
    currentstatus = hw.getTodos(myprinthwurl=printhwurl, taskid=currentid)
    if currentstatus[1] == True:
        buttonhandin.configure(state = "enabled", text = "Withdraw Assignment") #If the assignment is handed in, withdraw it.
    else:
        buttonhandin.configure(state = "enabled", text = "Hand In Assignment") #If the assignmnet is outstanding, hand it in.
    htmlviewer.load_file(dldir + selection)
    imagetoolbar.lift()
    buttonsatchelone.lift()
    buttonhandin.lift()
    whydoesntthisworknormally()
    buttoncreatehw.lift()
    root.update()

#Callback for handing in and withdrawing assignments

def hand_in():
    global currentstatus
    global currentid
    currentstatus = hw.getTodos(myprinthwurl=printhwurl, taskid=currentid)
    taskstatus = hw.handin(classtaskid=currentstatus[0], myprinthwurl=printhwurl, status=currentstatus[1])
    if taskstatus == True:
        buttonhandin.configure(text = "Withdraw Assignment")
        root.update()
    else:
        buttonhandin.configure(text = "Hand In Assignment")
        root.update()

# Themeing options

def themecallback():
    with open("config.yaml", "r") as conf:
        s2config = yaml.safe_load(conf)

    if s2config["currentTheme"] == "Light":
        ctk.set_appearance_mode("Dark")

        icon = PhotoImage(file = dir + "/Assets/Dark.png")
        root.iconphoto(True, icon)
        with open("config.yaml", "w") as conf:
            s2config["currentTheme"] = "Dark"
            yaml.safe_dump(s2config, conf)        
        htmlviewer.configure(dark_theme_enabled = True)
        htmlviewer.reload()
        root.update()
    else:
        ctk.set_appearance_mode("Light")
        
        icon = PhotoImage(file = dir + "/Assets/Light.png")
        root.iconphoto(True, icon)
        with open("config.yaml", "w") as conf:
            s2config["currentTheme"] = "Light"
            yaml.safe_dump(s2config, conf)
        htmlviewer.configure(dark_theme_enabled = False)
        htmlviewer.reload()
        root.update()

# Callback to open the assignment on Satchel:One

def onecallback():
    df = pd.read_csv(calendarlocation, encoding="utf-8", usecols=["URL"])
    URLList = df["URL"].tolist()
    satchelpage = URLList[summarypos]
    webbrowser.open(str(satchelpage), new = 0, autoraise = True)

def createcallback():
    print("How did you press this? This isn't even finished yet!")
    buttoncreatehw.lift()

# Main GUI initialisation

ImageFile.LOAD_TRUNCATED_IMAGES = True
root = ctk.CTk()
root.geometry("800x640")
root.title("Satchel:Two")
root.config(bg="#ffffff")
root.configure(fg_color=("#ffffff", "#232323"))
root.resizable(False, False)
if sys.platform == "win32":
    root.after(201, lambda :root.iconbitmap(dir + "/Assets/newlogowin32ico.ico"))


# Telling CTK where the assets are

lg = ctk.CTkImage(light_image = Image.open(str(dir + "/Assets/newlogolight.png")), dark_image = Image.open(str(dir + "/Assets/newlogodark.png")), size=(128,80))
sb = ctk.CTkImage(light_image = Image.open(str(dir + "/Assets/sidebarlight.png")), dark_image = Image.open(str(dir + "/Assets/sidebardark.png")), size=(160,640))
tb = ctk.CTkImage(light_image = Image.open(str(dir + "/Assets/toolbarlight.png")), dark_image = Image.open(str(dir + "/Assets/toolbardark.png")), size=(635,35))
imagelogo = ctk.CTkLabel(root, image = lg, text="")
imagesidebar = ctk.CTkLabel(root, image = sb, text="")
imagetoolbar = ctk.CTkLabel(root, image = tb, text="")

# Exit Button
buttonexit = ctk.CTkButton(root, text = "Exit", command = root.destroy , fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Assignments Button
buttonassignments = ctk.CTkButton(root, text = "Fetch Assignments", command = assignments, fg_color=("#ffffff", "#232323"), bg_color = ("#8A92E9", "#31386A"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Accounts Button
buttonaccount = ctk.CTkButton(root, text = "Log Out", command = lambda: login(startup=False), fg_color=("#ffffff", "#232323"), bg_color = ("#8A92E9", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# About Button
buttonabout = ctk.CTkButton(root, text = "Settings", command = openSettings, fg_color=("#ffffff", "#232323"), bg_color = ("#8A92E9", "#31386A"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Theme Toggle button
buttonthemetoggle = ctk.CTkButton(root, text = "Change Theme", command = themecallback, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#31386A"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Hand in button
buttonhandin = ctk.CTkButton(root, text = "Hand In", command = hand_in, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Go to Satchel:One button
buttonsatchelone = ctk.CTkButton(root, text = "View on Satchel:One", command = onecallback, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Homework Creation button
buttoncreatehw = ctk.CTkButton(root, text = "Create Assignment", command = createcallback, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
buttoncreatehw.configure(state = "disabled")

# Placing defined widgets

imagesidebar.place(x = 80, y = 320, anchor = CENTER)
imagelogo.place(x = 80, y = 60, anchor = CENTER)
imagelogo.lift() # Simply here so the logo displays over the sidebar
imagetoolbar.place(x = 475, y = 616, anchor = CENTER)
buttonassignments.place(x = 80, y = 140, anchor = CENTER)
buttonaccount.place(x = 80, y = 575, anchor = CENTER)
buttonabout.place(x = 80, y = 180, anchor = CENTER)
buttonsatchelone.place(x = 450, y = 616, anchor = CENTER)
buttonhandin.place(x = 600, y = 616, anchor = CENTER)
buttoncreatehw.place(x = 300, y = 616, anchor = CENTER)
buttonthemetoggle.place(x = 80, y = 220, anchor = CENTER)
buttonexit.place(x = 80, y = 615, anchor = CENTER)

# Other stuff that needs configuring

sfpro = ctk.CTkFont(family="SF Pro Rounded Regular", size=19)
sfprotitle = ctk.CTkFont(family="SF Pro Rounded Regular", size=28)
robototitle = ctk.CTkFont(family="Roboto", size=28)

# Disabling while on landing page
buttonsatchelone.configure(state = "disabled")
buttonhandin.configure(state = "disabled")
# For some reason, customtkinter refuses to raise this button under any circumstances
# Unless it's in a function. I have no clue why.
def whydoesntthisworknormally():
    buttoncreatehw.lift()
buttoncreatehw.lift()

# Calling the login prompt from startup

login(startup=True)

# Clock and greeting string

hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
time = (str(hour), ":", str(minute))
if hour < 12:
    greet = "Good Morning"
elif hour >= 12 and not hour > 17:
    greet = "Good Afternoon"
else:
    greet = "Good Evening"

if sys.platform == "win32" or sys.platform == "linux":
    greeting = ctk.CTkLabel(root, text = greet + ", " + str(forename), font = robototitle)
else:
    greeting = ctk.CTkLabel(root, text = greet + ", " + str(forename), font = sfprotitle)
greeting.place(x = 165, y = 40)

# Initialising theme and HTML viewer

with open("config.yaml", "r") as conf:
    s2config = yaml.safe_load(conf)
    htmlscale = s2config["htmlScale"]
    conf.close()

# Handling opening hyperlinks in the default web browser instead of TkinterWeb

def open_link_external(hyperlink):
    webbrowser.open(hyperlink)
    return "break"

global htmlviewer
htmlviewer = HtmlFrame(root, messages_enabled=False, javascript_enabled=True, images_enabled=True, zoom=htmlscale, on_link_click=open_link_external)
htmlviewer.place(x = 475, y = 300, height= 580, width = 630, anchor=CENTER)
htmlviewer.load_url("about:blank")
htmlviewer.lower()


with open("config.yaml", "r") as conf:
    s2config = yaml.safe_load(conf)

    if s2config["currentTheme"] == "Dark":
        ctk.set_appearance_mode("Dark")
        htmlviewer.configure(dark_theme_enabled = True)
        htmlviewer.reload()
        icon = PhotoImage(file = dir + "/Assets/Dark.png")
        root.iconphoto(True, icon)
        with open("config.yaml", "w") as conf:
            s2config["currentTheme"] = "Dark"
            yaml.safe_dump(s2config, conf)
        root.update()
        htmlviewer.reload()
    else:
        ctk.set_appearance_mode("Light")
        htmlviewer.configure(dark_theme_enabled = False)
        htmlviewer.reload()
        icon = PhotoImage(file = dir + "/Assets/Light.png")
        root.iconphoto(True, icon)
        with open("config.yaml", "w") as conf:
            s2config["currentTheme"] = "Light"
            yaml.safe_dump(s2config, conf)
        root.update()
        htmlviewer.reload()
    conf.close()

whydoesntthisworknormally()

root.mainloop()