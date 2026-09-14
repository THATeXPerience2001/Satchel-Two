# Satchel:Two GUI
# Finally a GUI that actually looks nice!

#Just importing all the libraries I may need

print(r"  _________       __         .__           .__       ___________               ")
print(r" /   _____/____ _/  |_  ____ |  |__   ____ |  |   /\ \__    ___/_  _  ______   ")
print(r" \_____  \\__  \\   __\/ ___\|  |  \_/ __ \|  |   \/   |    |  \ \/ \/ /  _ \  ")
print(r" /        \/ __ \|  | \  \___|   Y  \  ___/|  |__ /\   |    |   \     (  <_> ) ")
print(r"/_______  (____  /__|  \___  >___|  /\___  >____/ \/   |____|    \/\_/ \____/  ")

print("Satchel:Two GUI CONSOLE LOG")
print("Version: 1.0b - Suitcase")


try:
    from tkinter import *
    import customtkinter as ctk
    import icalendar
    from PIL import Image, ImageTk, ImageFile
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
    print("All modules initialised!")

except Exception as e:
    print(f"Satchel:Two encountered an error while importing necessary modules or libraries: {e}")

# All the config lines ect...

projfile = os.path.realpath(__file__)
dir = os.path.dirname(projfile)
# ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
deftheme = str(dir + "/breaktime.json")
ctk.set_default_color_theme(deftheme)
hw = homeworklib.homework()
# Thanks for Andereoo for helping patch the dark style colours!
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

print("Configuration Loaded!")

if sys.platform == "win32":
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo\Download"')
    ctk.deactivate_automatic_dpi_awareness()
else:
    os.system("mkdir ~/SatchelTwo/")
    os.system("mkdir ~/SatchelTwo/Download/")

# Windows uses a different file 

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

# About window

def openAbout():

    # Config for About window

    about = ctk.CTkToplevel(root)
    about.configure(fg_color=("#ffffff", "#232323"))
    about.title("About Satchel:Two")
    about.geometry("320x180")  
    about.resizable(False, False)
    appearance = ctk.get_appearance_mode()
    if appearance == "Dark":
        aLg = PhotoImage(file = dir + "/Assets/newlogoblack.png")
        icon = PhotoImage(file = dir + "/Assets/Dark.png")
        root.iconphoto(True, icon)
    else:
        aLg = PhotoImage(file = dir + "/Assets/newlogotransparent.png")
        icon = PhotoImage(file = dir + "/Assets/Light.png")
        root.iconphoto(True, icon)
    aboutLogo = Label(about, image = aLg, borderwidth = 0)    
    aboutText = ctk.CTkLabel(about, text="Satchel:Two GUI", bg_color=("#ffffff", "#232323"))
    aboutVersion = ctk.CTkLabel(about, text = "Version 1.0b - Suitcase", bg_color=("#ffffff", "#232323"))
    aboutUs = ctk.CTkLabel(about, text = "Made in the UK by ProjectSCR", bg_color=("#ffffff", "#232323"))
    aboutLogo.place(x = 160, y = 60, anchor = CENTER)
    aboutLogo.lift()
    aboutUs.place(x = 160, y = 120, anchor = CENTER)
    aboutText.place(x = 160, y = 140, anchor = CENTER)
    aboutVersion.place(x = 160, y = 160, anchor = CENTER)
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
    # Checking for a stored api url in the key.txt 
    # It isn't encrypted because it doesn't store any credentials plus it's not shared online
    # which may seem controversial but it expires after a month and requires this program to really
    # do anything with it. ¯\_(ツ)_/¯
    if os.path.isfile("key.txt") == True and startup == True:
        with open("key.txt", "r", encoding="utf-8") as file:
            apitoken = file.read()
            file.close()
    elif os.path.isfile("key.txt") == True and startup != True:
        loginprompt = ctk.CTkInputDialog(title = "Satchel:Two Login", text = "Welcome back! Please enter your Print Homework URL to log in.", fg_color=("#ffffff", "#232323"), button_fg_color = "#6D78CF", button_hover_color = "#4D589C")
        apitoken = loginprompt.get_input()
        with open("key.txt", "w+", encoding="utf-8") as file:
            file.write(apitoken)
            file.close()
    else:
        loginprompt = ctk.CTkInputDialog(title = "Satchel:Two Login", text = "Welcome back! Please enter your Print Homework URL to log in.", fg_color=("#ffffff", "#232323"), button_fg_color = "#6D78CF", button_hover_color = "#4D589C")
        apitoken = loginprompt.get_input()
        with open("key.txt", "w+", encoding="utf-8") as file:
            file.write(apitoken)
            file.close()
    global printhwurl
    global studenttoken
    
    #  Checking if the apitoken is nothing because the user does not understand the concept of "pasting".

    if apitoken == None:
        loginprompt.destroy()
        apitoken = ""
        buttonassignments.configure(state = "disabled")
        throwError("badApin")
    else:
        # Decoding the 3 variants of the url to obtain the api token.
        # Issue #10 patched by changing method.
        printhwurl = apitoken
        auth = str((apitoken.split("smhw_token=", 1)[1]))
        #if "homeworks" in apitoken:
        #    auth = apitoken[65:289]
        #elif "flexible_tasks" in apitoken:
        #    auth = apitoken[70:294]
        #elif "classworks" in apitoken:
        #    auth = apitoken[66:290]
        #else:
        #    apitoken = ""
        #    buttonassignments.configure(state = "disabled")
        #    throwError("badApi")
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
                fullname = (forename, surname)

                # Reporting back to the debug log and updating UI for user

                print("Welcome back,", forename, surname, "!")
                #print(auth)
                urllib.request.urlretrieve(avatar, dldir + "avatar.jpeg")
                avtr = ctk.CTkImage(Image.open(str(dldir + "avatar.jpeg")), size=(96,136))
                name = ctk.CTkLabel(root, text = fullname, text_color=("#232323", "#ffffff"), corner_radius=6, width = 140, height = 45, wraplength = 120, bg_color = ("#6472CD", "#384079"), fg_color=("#ffffff", "#232323"))
                avatarframe = ctk.CTkFrame(root, border_color = "#ffffff", border_width = 2, corner_radius=6, width = 100, height = 140, bg_color="#5D67B4")
                avatarpic = ctk.CTkLabel(avatarframe, image = avtr, text="")
                avatarframe.place(x = 80, y = 360, anchor=CENTER)
                avatarpic.place(x = 50, y = 70, anchor=CENTER)
                name.place(x = 80, y = 460, anchor=CENTER)
                name.lift()
                root.update()
    
    
# The incredibly long system to fetch all of the assignments

def assignments():
    # Getting the UI ready
    root.update()
    htmlviewer.load_url("about:blank")
    progressbar = ctk.CTkProgressBar(root, orientation="horizontal", border_color = "#000000", progress_color = "#6D78CF", mode = "indeterminate")
    pleasewait = ctk.CTkLabel(root, text = "Please wait... Downloading assignments...", text_color = ("#232323", "#ffffff"), bg_color=("#ffffff", "#232323"))
    progressbar.place(x = 480, y = 340, anchor = CENTER)
    progressbar.lift(aboveThis = None)
    pleasewait.place(x = 480, y = 300, anchor = CENTER)
    pleasewait.place(aboveThis = None)
    progressbar.start()
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

    # Setting encoding because Windows hates me

    if sys.platform == "win32":
        df = pd.read_csv(calendarlocation, encoding="cp1252", usecols=["UID", "Homework Title", "URL"])
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
            if item.startswith("blank") == False:
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
            root.update()
        print("Todos fetched successfully!")
        global ok
        ok = True
    # Throw an error for BadGateways (Low chance now due to change in methods)
    except urllib.error.HTTPError as e:
        if e.code == 502:
            throwError("badGateway")
            summarylist = []
            ok = False
            progressbar.stop()
            progressbar.destroy()
            pleasewait.destroy()
        if e.code == 404:
            pass
        else:   # Throw an error for internet connection
            throwError("network")
            summarylist = []
            ok = False
            progressbar.stop()
            progressbar.destroy()
            pleasewait.destroy()
    except ("ConnectionAbortedError", "ConnectionError", "ConnectionRefusedError", "ConnectionResetError"):
        throwError("network") # Treat any other errors as network errors which are most likely.
        summarylist = []
        ok = False
        progressbar.stop()
        progressbar.destroy()
        pleasewait.destroy()

    # Create a list of all of the HTML's in the downloads directory
    htmllist = []
    global htmls
    htmls = os.listdir(dldir)
    for item in htmls:
        if item.endswith(".html"):
            htmllist.append(item)

    # Stop the UI after updating
    progressbar.stop()
    progressbar.destroy()
    pleasewait.destroy()
    root.update()
    assignmentslist = ctk.CTkOptionMenu(root, values = summarylist, command=assignments_callback, width = 140, height = 20, fg_color = ("#FFFFFF", "#232323"), button_color = "#6472CD", button_hover_color = "#4D589C", bg_color = ("#6472CD", "#444D8B"), dropdown_fg_color = ("#FFFFFF", "#232323"), dropdown_hover_color = "#ADADAD", text_color = ("#000000", "#FFFFFF" ), dynamic_resizing=False, hover = False)
    assignmentslist.place(x = 80, y = 500, anchor = CENTER) 
    if ok == True:
        throwError("hwFetched") # Uses the throwError as a leftover function but less complicated
        htmlviewer.load_file(dldir + (downloads[0]))
        buttonsatchelone.configure(state = "enabled")
        buttonhandin.configure(state = "disabled")
        imagetoolbar.lift()
        buttonsatchelone.lift()
        buttonhandin.lift()
        global summarypos
        summarypos = 0
        htmlviewer.load_url("about:blank")
        root.update()
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
    appearance = ctk.get_appearance_mode()
    if appearance == "Light":
        ctk.set_appearance_mode("Dark")
        htmlviewer.configure(dark_theme_enabled = True)
        #tkinterweb.utilities.DARK_STYLE.replace("#0d0b1a", "#232323")
        htmlviewer.reload()
        icon = PhotoImage(file = dir + "/Assets/Dark.png")
        root.iconphoto(True, icon)
        root.update()
    else:
        ctk.set_appearance_mode("Light")
        htmlviewer.configure(dark_theme_enabled = False)
        htmlviewer.reload()
        icon = PhotoImage(file = dir + "/Assets/Light.png")
        root.iconphoto(True, icon)
        root.update()

# Callback to open the assignment on Satchel:One

def onecallback():
    if sys.platform == "win32":
        df = pd.read_csv(calendarlocation, encoding="cp1252", usecols=["URL"])
    else:
        df = pd.read_csv(calendarlocation, usecols=["URL"])
    URLList = df["URL"].tolist()
    satchelpage = URLList[summarypos]
    print("Redirecting to assignment: " + satchelpage)
    webbrowser.open(str(satchelpage), new = 0, autoraise = True)

# Main GUI initialisation

ImageFile.LOAD_TRUNCATED_IMAGES = True
root = ctk.CTk()
root.geometry("800x640")
root.title("Satchel:Two")
root.config(bg="#ffffff")
root.configure(fg_color=("#ffffff", "#232323"))
root.resizable(False, False)
icon = PhotoImage(file = dir + "/Assets/Light.png")
root.iconphoto(True, icon)
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
buttonaccount = ctk.CTkButton(root, text = "Log Out", command = lambda: login(startup=False), fg_color=("#ffffff", "#232323"), bg_color = ("#8A92E9", "#31386A"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# About Button
buttonabout = ctk.CTkButton(root, text = "About", command = openAbout, fg_color=("#ffffff", "#232323"), bg_color = ("#8A92E9", "#31386A"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Theme Toggle button
buttonthemetoggle = ctk.CTkButton(root, text = "Change Theme", command = themecallback, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Hand in button
buttonhandin = ctk.CTkButton(root, text = "Hand In", command = hand_in, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Go to Satchel:One button
buttonsatchelone = ctk.CTkButton(root, text = "View on Satchel:One", command = onecallback, fg_color=("#ffffff", "#232323"), bg_color = ("#6472CD", "#444D8B"), hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))

# Placing defined widgets

imagesidebar.place(x = 80, y = 320, anchor = CENTER)
imagelogo.place(x = 80, y = 60, anchor = CENTER)
imagelogo.lift() # Simply here so the logo displays over the sidebar
imagetoolbar.place(x = 475, y = 616, anchor = CENTER)
buttonassignments.place(x = 80, y = 140, anchor = CENTER)
buttonaccount.place(x = 80, y = 180, anchor = CENTER)
buttonabout.place(x = 80, y = 220, anchor = CENTER)
buttonsatchelone.place(x = 340, y = 616, anchor = CENTER)
buttonhandin.place(x = 580, y = 616, anchor = CENTER)
buttonthemetoggle.place(x = 80, y = 575, anchor = CENTER)
buttonexit.place(x = 80, y = 615, anchor = CENTER)

# Other stuff that needs configuring

sfpro = ctk.CTkFont(family="SF Pro Rounded Regular", size=19)

# Disabling while on landing page
buttonsatchelone.configure(state = "disabled")
buttonhandin.configure(state = "disabled")

# Calling the login prompt from startup

login(startup=True)

# Initialising theme and HTML viewer

global htmlviewer
htmlviewer = HtmlFrame(root, messages_enabled=False, javascript_enabled=True, images_enabled=True)
htmlviewer.place(x = 475, y = 300, height= 580, width = 630, anchor=CENTER)

appearance = ctk.get_appearance_mode()
if appearance == "Dark":
    ctk.set_appearance_mode("Dark")
    htmlviewer.configure(dark_theme_enabled = True)
    htmlviewer.load_url("about:blank")
    htmlviewer.reload()
    icon = PhotoImage(file = dir + "/Assets/Dark.png")
    root.iconphoto(True, icon)
    root.update()
else:
    ctk.set_appearance_mode("Light")
    htmlviewer.configure(dark_theme_enabled = False)
    htmlviewer.load_url("about:blank")
    htmlviewer.reload()
    icon = PhotoImage(file = dir + "/Assets/Light.png")
    root.iconphoto(True, icon)
    root.update()

htmlviewer.reload()

root.mainloop()