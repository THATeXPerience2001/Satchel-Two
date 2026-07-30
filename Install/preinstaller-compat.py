# Satchel:Two Compatibility Installer script
# Ah yes let me just check my homework on WINDOWS VISTA

# Libraries, you know the drill..

import sys
import os
import platform
import time
import webbrowser

# Setting up the dir's

projfile = os.path.realpath(__file__)
dir = os.path.dirname(projfile)
dir = str(dir)

# Prepping the installer

print()
print("Welcome to the Satchel:Two Compatibility Pre-Installer!")
print()
print("Please follow the guide at https://github.com/THATeXPerience2001/Satchel-Two/wiki/SatchelTwo-CLI#installing-the-cli")
print()
print("Please note this installer is intended ONLY for LEGACY WINDOWS SYSTEMS (AKA Older than 7)")
print()
time.sleep(1)
print("STAGE 1: Running platform checks...")
print()

archOK = False
osOK = False
pyOK = False
systemOK = False

# Architecture check: amd64 will pass, x86 and arm64 will not
arch = platform.machine() # arm64, amd64, i386 ect
if arch != "AMD64":
    archOK = False
else:
    archOK = True

# OS Check: Doesn't really matter as long as it's 64-bit and runs Python 3.8.10
if sys.platform == "win32":
    archOK = True
    osOK = True
else:
    archOK = False
    osOK = False

# Python version check: Checks to see if Python is 3.13.5 or newer
pyver = list(platform.python_version_tuple())
pyvermaj = int(pyver[0])
pyvermin = int(pyver[1])
pyverpch = int(pyver[2])
if pyvermaj >= 3:
    if pyvermin >= 8:
            pyOK = True
    else:
        pyOK = False
else:
    pyOK = False
pyver = (str(pyvermaj) + "." + str(pyvermin) + "." + str(pyverpch))



print("SYSTEM SUMMARY ================ ")
if pyOK == False:
    if osOK == False and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (FAILED) ")
        time.sleep(1)
        print("ERROR: Your system architecture is not supported.")
    if osOK == True and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (FAILED) ")
        time.sleep(1)
        print("ERROR: Your OS is supported, but your architecture is not.")
    if osOK == True and archOK == True:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (PASSED) ")
        time.sleep(1)
        print("System Architecture", arch, " (PASSED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (FAILED) ")
        time.sleep(1)
        print("ERROR: Your system is supported but your python version is outdated. Please upgrade to 3.8.10 or later.")
if pyOK == True:
    if osOK == False and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (PASSED) ")
        time.sleep(1)
        print("ERROR: Your system architecture is not supported.")
    if osOK == True and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (PASSED) ")
        time.sleep(1)
        print("ERROR: Your OS is supported, but your architecture is not.")
    if osOK == True and archOK == True:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (PASSED) ")
        time.sleep(1)
        print("System Architecture", arch, " (PASSED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (PASSED) ")
        time.sleep(1)
        systemOK = True
        print("ALL TESTS PASSED!")
print()

if systemOK == True:
    print("Your system has passed the initial tests and can continue to the second step of installation.")
    time.sleep(1)
else:
    print("Your system has failed the tests above. The installation cannot continue.")
    exit()

print()
passed1 = str(input("Would you like to continue? Y/N : "))
if passed1 != "Y":
    print("Installation aborted manually.")
    exit()

print()
print("STAGE 2: Installing Libraries...")

## Yeah, I'm not sure how to use VENV's properly yet

try: 
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org customtkinter") # Python 3.7+
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org icalendar==6.3.2") # Python 3.8+
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pillow==10.4.0") # Python 3.8+
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pandas==2.0.3") # Python 3.8+
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests==2.32.4") # Python 3.10
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org tkinterweb[recommended]") # Python 3.2

except Exception as e:
    print("This error occured while installing libraries:", e)
    print("Installation aborted.")
    exit()

print("")
print("Library install complete!")
print("Satchel:Two is now ready to install!")

time.sleep(1)
print()
print("STAGE 3: Redirecting to installer...")
print()
print("You are being redirected to the GitHub Releases.")
time.sleep(1)
print("Please run the downloaded installer once finished!")
time.sleep(3)
webbrowser.open("https://github.com/THATeXPerience2001/Satchel-Two/releases/latest/download/SatchelTwoWin64.exe", new = 0, autoraise = True)
