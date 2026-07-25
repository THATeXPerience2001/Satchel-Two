# Satchel:Two Installer script
# "I'm trying to make it cross-platform, I swear!" - Aaron McCormick, 2026

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
print("Welcome to the Satchel:Two Pre-Installer!")
print()
print("Please follow the guide at https://github.com/THATeXPerience2001/Satchel-Two/wiki/SatchelTwo-CLI#installing-the-cli")
print()
time.sleep(1)
print("STAGE 1: Running platform checks...")
print()

archOK = False
osOK = False
pyOK = False
systemOK = False

# Architecture check: amd64 and arm64 will pass, x86 will not
arch = platform.machine() # arm64, amd64, i386 ect
if arch != "arm64" and arch != "AMD64":
    archOK = False
else:
    archOK = True

# OS Check: Doesn't really matter as long as it's 64-bit and runs Python 3.13.5
if sys.platform == "win32":
    if arch == "arm64":
        osOK = False
        archOK = False
    else:
        archOK = True
        osOK = True
elif sys.platform == "darwin":
    archOK = True
    osOK = True
elif sys.platform == "linux":
    archOK = True
    osOK = True
else:
    osOK = False
    archOK = False

# Python version check: Checks to see if Python is 3.13.5 or newer
pyver = list(platform.python_version_tuple())
pyvermaj = int(pyver[0])
pyvermin = int(pyver[1])
pyverpch = int(pyver[2])
if pyvermaj >= 3:
    if pyvermin >= 13:
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
        print("ERROR: Your system is supported but your python version is outdated. Please upgrade to 3.13.5 or later.")
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
    if sys.platform == "darwin" or "linux":
        print("However, MacOS and Linux systems will install the required libraries using --break-system-packages.")
        print("This hasn't been reported to be an issue, but this is a very subtle warning!")
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
    if sys.platform == "win32":
        os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org customtkinter")
        os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org icalendar")
        os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pillow")
        os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pandas")
        os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests")
        os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org tkinterweb[recommended]")
    else:
        os.system("pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org customtkinter --break-system-packages")
        os.system("pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org icalendar --break-system-packages")
        os.system("pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pillow --break-system-packages")
        os.system("pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pandas --break-system-packages")
        os.system("pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests --break-system-packages")
        os.system("pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org tkinterweb[recommended] --break-system-packages")


except Exception as e:
    print("This error occured while installing libraries:", e)
    print("Installation aborted.")
    exit()

print("")
print("Library install complete!")
print("Satchel:Two is now ready to install!")

if sys.platform == "linux":
    print("Since you are running Linux, this script can also download and setup Satchel:Two automatically.")
    print("Please make sure you have Git and Pip installed first for your respective distro.")
    autoinstall = input("Are you sure these are installed? Y/N: ")
    if autoinstall == "Y":
        print("STAGE 3: Preparing automatic install...")
        os.system("cd ~ && git clone --recursive https://github.com/THATeXPerience2001/Satchel-Two.git")
        print("Installation finished!")
        print("To start, simply run: cd ~/Satchel-Two/ && python3 gui.py")
        print("Thank you for installing Satchel:Two!")
        exit()
    else:
        print("Installation finished!")
        print("Thank you for installing Satchel:Two!")
        exit()

time.sleep(1)
print()
print("STAGE 3: Redirecting to installer...")
print()
print("You are being redirected to the GitHub Releases.")
time.sleep(1)
print("Please run the downloaded installer once finished!")
time.sleep(3)
if sys.platform == "win32":
    webbrowser.open("https://github.com/THATeXPerience2001/Satchel-Two/releases/latest/download/SatchelTwoWin64.exe", new = 0, autoraise = True)
if sys.platform == "darwin":
    webbrowser.open("https://github.com/THATeXPerience2001/Satchel-Two/releases/latest/download/SatchelTwoMacOS.pkg", new = 0, autoraise = True)
