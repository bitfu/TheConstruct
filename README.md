# TheConstruct
The Construct encrypted remote command shell tool by bitfu <br>
<https://keybase.io/bitfu> <br>
<https://twitter.com/bitfu_> <br>
<https://github.com/bitfu> <br> <br>
Tool to quickly construct encrypted TCP remote command shells for network troubleshooting in Windows environments. <br> <br>

Requirements:
1) To run - either: a) Python installed on each host, b) create a portable Windows executable file from TheContruct.py, or c) something else that works for you :)
2) Ncat.exe located on an accessible web server - see: https://nmap.org/ncat
3) Replace the web server address with your preferred URL for Ncat.exe download - in line: 'urllib.urlretrieve("https://0.0.0.0/ncat.exe", filename="c:/temp/ncat.exe")'
