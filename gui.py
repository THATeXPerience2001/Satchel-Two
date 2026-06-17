# Satchel:Two GUI
# Finally a GUI that actually looks nice!

#Just importing all the libraries I may need

print(r"  _________       __         .__           .__       ___________               ")
print(r" /   _____/____ _/  |_  ____ |  |__   ____ |  |   /\ \__    ___/_  _  ______   ")
print(r" \_____  \\__  \\   __\/ ___\|  |  \_/ __ \|  |   \/   |    |  \ \/ \/ /  _ \  ")
print(r" /        \/ __ \|  | \  \___|   Y  \  ___/|  |__ /\   |    |   \     (  <_> ) ")
print(r"/_______  (____  /__|  \___  >___|  /\___  >____/ \/   |____|    \/\_/ \____/  ")

print("Satchel:Two GUI CONSOLE LOG")
print("Version: Release Candidate 2 (DEV)")


try:
    from tkinter import *
    import customtkinter as ctk
    import icalendar
    from PIL import Image, ImageTk, ImageFile
    import urllib.request
    import sys
    import os
    import ssl
    import pandas as pd
    from pathlib import Path
    import tkpdfmod as pdf
    import infolib
    import fetchlib2 as fetchlib
    import pymupdf as fitz
    import numpy
    import base64
    import requests
    import webbrowser
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

print("Configuration Loaded!")

if sys.platform == "win32":
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo\Download"')
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

# About window

def openAbout():

    about = ctk.CTkToplevel(root)  # Create a new window
    about.configure(fg_color=("#ffffff", "#232323"))
    about.title("About Satchel:Two")
    about.geometry("320x180")  
    about.resizable(False, False)
    appearance = ctk.get_appearance_mode()
    if appearance == "Dark":
        aLg = PhotoImage(file = dir + "/Assets/newlogoblack.png")
    else:
        aLg = PhotoImage(file = dir + "/Assets/newlogotransparent.png")
    aboutLogo = Label(about, image = aLg, borderwidth = 0)    
    aboutText = ctk.CTkLabel(about, text="Satchel:Two GUI", bg_color=("#ffffff", "#232323"))
    aboutVersion = ctk.CTkLabel(about, text = "Release Candidate 2 (DEV)", bg_color=("#ffffff", "#232323"))
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
    if code == "badApin":
        eBadApin.place(x = 180, y = 40, anchor = CENTER)
        relog.place(x = 180, y = 80, anchor = CENTER)
        print("ERROR: No API token recieved!")
    if code == "hwFetched":
        pHwFetched.place(x = 180, y = 40, anchor = CENTER)
        close.place(x = 180, y = 80, anchor = CENTER)

# Basic login function that also validates the Print Homework URL before extracting the API Token

def login():
    loginprompt = ctk.CTkInputDialog(title = "Satchel:Two Login", text = "Welcome back! Please enter your print homework url to log in!", fg_color=("#ffffff", "#232323"), button_fg_color = "#6D78CF", button_hover_color = "#4D589C")
    global apitoken
    global printhwurl
    global studenttoken
    apitoken = loginprompt.get_input()
    if apitoken == None:
        loginprompt.destroy()
        apitoken = ""
        buttonassignments.configure(state = "disabled")
    else:
        printhwurl = apitoken
        if "homeworks" in apitoken:
            auth = apitoken[65:289]
        elif "flexible_tasks" in apitoken:
            auth = apitoken[70:294]
        elif "classworks" in apitoken:
            auth = apitoken[66:290]
        dec = str(base64.b64decode(auth))
        studenttoken = dec[10:18]
        apitoken = auth
        print("DEBUG: API TOKEN = ", apitoken)

    # Checks if the input is nothing to avoid a type error
    if len(apitoken) < 1:
        apitoken = ""
        buttonassignments.configure(state = "disabled")
        throwError("badApin")

    else:   # If it passes, check if it's divisible by 4 so it can be base64 decoded
        if len(apitoken) % 4 != 0:
            apitoken = ""
            buttonassignments.configure(state = "disabled")
            throwError("badApi")
        else:
            decoded = dec

            # Checks if the decoded token begins with user_id to verify it's valid

            if decoded[2:9] != "user_id":
                apitoken = ""
                throwError("badApi")
                buttonassignments.configure(state = "disabled")
                print("Invalid login detected!")
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

            print("Welcome back,", forename, surname, "!")
            urllib.request.urlretrieve(avatar, dldir + "avatar.jpeg")
            avtr = ctk.CTkImage(Image.open(str(dldir + "avatar.jpeg")), size=(96,136))
            name = ctk.CTkLabel(root, text = fullname, text_color=("#232323", "#ffffff"), corner_radius=6, bg_color="#5D67B4", fg_color=("#ffffff", "#232323"))
            avatarframe = ctk.CTkFrame(root, border_color = "#ffffff", border_width = 2, corner_radius=6, width = 100, height = 140, bg_color="#5D67B4")
            avatarpic = ctk.CTkLabel(avatarframe, image = avtr, text="")
            avatarframe.place(x = 80, y = 360, anchor=CENTER)
            avatarpic.place(x = 50, y = 70, anchor=CENTER)
            name.place(x = 80, y = 460, anchor=CENTER)
            name.lift()
            root.update()
    
    
# The incredibly long system to fetch all of the assignments

def assignments():
    # Getti ng the UI ready
    root.update()
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

    # Setting encoding because WINDOWS

    if sys.platform == "win32":
        df = pd.read_csv(calendarlocation, encoding="cp1252", usecols=["UID", "Homework Title"])
    else:
        df = pd.read_csv(calendarlocation, usecols=["UID", "Homework Title"])
    uid_list = df["UID"].tolist()
    global summarylist
    summarylist = df["Homework Title"].tolist()

    # Cleaning up the downloads DIR to prevent an infinite ammount of PDF's

    todelete = os.listdir(dldir)

    for item in todelete:
        if item.endswith(".pdf"):
            os.remove(os.path.join(dldir, item))

    count = 0

    # Initialising the downloads

    global downloads
    downloads = []

    # attempt to download all the homework files as PDF's

    try:
        while count < (len(uid_list)):
            print("Downloading assignment:", count)
            uid_current = str(uid_list[count])
            urllib.request.urlretrieve(r"https://api.satchelone.com/api/homeworks/" + uid_current + ".pdf?smhw_token=" + apitoken, dldir + uid_current + ".pdf")
            downloads.append(uid_current + ".pdf")
            count = count + 1
            root.update()
        print("Todos fetched successfully!")
        global ok
        ok = True
    # Throw an error for BadGateways (Frequent)
    except urllib.error.HTTPError as e:
        if e.code == 502:
            throwError("badGateway")
            summarylist = []
            ok = False
            progressbar.stop()
            progressbar.destroy()
            pleasewait.destroy()
        else:   # Throw an error for internet connection
            throwError("network")
            summarylist = []
            ok = False
            progressbar.stop()
            progressbar.destroy()
            pleasewait.destroy()
    except ("ConnectionAbortedError", "ConnectionError", "ConnectionRefusedError", "ConnectionResetError"):
        throwError("network") # Treat any other errors as network errors
        summarylist = []
        ok = False
        progressbar.stop()
        progressbar.destroy()
        pleasewait.destroy()

    # Create a list of all of the PDF's in the downloads directory
    pdflist = []
    global pdfs
    pdfs = os.listdir(dldir)
    for item in pdfs:
        if item.endswith(".pdf"):
            pdflist.append(item)

    # Stop the UI after updating
    progressbar.stop()
    progressbar.destroy()
    pleasewait.destroy()
    root.update()
    global dcmt # Initialise the PDF viewer
    dcmt = pdf.ShowPdf()
    resx = root.winfo_screenwidth()
    resy = root.winfo_screenheight()
    if resx == 1920 and resy == 1080 or resx == 1920 and resy == 1200:
        document = dcmt.pdf_view(root, pdf_location = dldir + (downloads[0]), width = 75, height = 35, bar = False)
    else:
        document = dcmt.pdf_view(root, pdf_location = dldir + (downloads[0]), width = 90, height = 50, bar = False)
    assignmentslist = ctk.CTkOptionMenu(root, values = summarylist, command=assignments_callback, width = 140, height = 20, fg_color = ("#FFFFFF", "#232323"), button_color = "#6472CD", button_hover_color = "#4D589C", bg_color = "#6472CD", dropdown_fg_color = ("#FFFFFF", "#232323"), dropdown_hover_color = "#ADADAD", text_color = ("#000000", "#FFFFFF" ), dynamic_resizing=False, hover = True)
    assignmentslist.place(x = 80, y = 500, anchor = CENTER) 
    if ok == True:
        throwError("hwFetched") # Uses the throwError as a leftover function but less complicated
        if resx == 1920 and resy == 1080 or resx == 1920 and resy == 1200:
            document.place(x = 475, y = 300, anchor = CENTER)
        else:
            document.place(x = 480, y = 320, anchor = CENTER)
        ok = False
        buttonsatchelone.configure(state = "enabled")
        imagetoolbar.lift()
        buttonsatchelone.lift()
        buttonhandin.lift()
        buttonassignments.configure(state = "disabled")
        global summarypos
        summarypos = 0
        root.update()
    root.update()
   
# Creating a callback for the assignments list
def assignments_callback(choice):
    global summarypos
    summarypos = summarylist.index(choice)
    selection = downloads[summarypos]
    dcmt = pdf.ShowPdf()
    resx = root.winfo_screenwidth()
    resy = root.winfo_screenheight()
    if resx == 1920 and resy == 1080 or resx == 1920 and resy == 1200:
        document = dcmt.pdf_view(root, pdf_location = dldir + selection, width = 75, height = 35, bar = False)
        document.place(x = 475, y = 300, anchor = CENTER)
    else:
        document = dcmt.pdf_view(root, pdf_location = dldir + selection, width = 90, height = 50, bar = False)
        document.place(x = 480, y = 320, anchor = CENTER)
    imagetoolbar.lift()
    buttonsatchelone.lift()
    buttonhandin.lift()
    root.update()

# Themeing options (Slightly broken currently)

def themecallback():
    appearance = ctk.get_appearance_mode()
    if appearance == "Light":
        ctk.set_appearance_mode("Dark")
        icon = PhotoImage(file = dir + "/Assets/Dark.png")
        root.iconphoto(True, icon)
    else:
        ctk.set_appearance_mode("Light")
        icon = PhotoImage(file = dir + "/Assets/Light.png")
        root.iconphoto(True, icon)

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

# Telling CTK where the assets are

lg = ctk.CTkImage(Image.open(str(dir + "/Assets/newlogoblue.png")), size=(128,80))
sb = ctk.CTkImage(Image.open(str(dir + "/Assets/sidebar.png")), size=(160,640))
tb = ctk.CTkImage(Image.open(str(dir + "/Assets/toolbar.png")), size=(635,35))
imagelogo = ctk.CTkLabel(root, image = lg, text="")
imagesidebar = ctk.CTkLabel(root, image = sb, text="")
imagetoolbar = ctk.CTkLabel(root, image = tb, text="")

# Exit Button
buttonexit = ctk.CTkButton(root, text = "Exit", command = root.destroy , fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Assignments Button
buttonassignments = ctk.CTkButton(root, text = "Fetch Assignments", command = assignments, fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Accounts Button
buttonaccount = ctk.CTkButton(root, text = "Log Out", command = login, fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# About Button
buttonabout = ctk.CTkButton(root, text = "About", command = openAbout, fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Theme Toggle button
buttonthemetoggle = ctk.CTkButton(root, text = "Change Theme", command = themecallback, fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Hand in button
buttonhandin = ctk.CTkButton(root, text = "Toggle Hand In", fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
# Go to Satchel:One button
buttonsatchelone = ctk.CTkButton(root, text = "View on Satchel:One", command = onecallback, fg_color=("#ffffff", "#232323"), bg_color = "#6472CD", hover_color = ("#F0EEE5", "#232323"), text_color = ("#232323", "#ffffff"))
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

login()

root.mainloop()


