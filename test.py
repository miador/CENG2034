import os
import platform
import requests

from urllib.request import urlopen

def get_pid():          #Gets current PID and print it.
    pid = os.getpid()
    print("Current PID: ", pid)

def get_os_name():      #Gets OS name and print it
    global os_name
    os_name = platform.system()
    print("Operating system is: ", os_name)

def print_loadavg():    #Prints 1,5,15 minutes loadaverages if th erunning OS is Linux
    if (os_name == "Linux"):
        global load1, load5, load15
        load1, load5, load15 = os.getloadavg()
        print("Load average in last 1 minute: ", load1)
        print("Load average in last 5 minutes: ", load5)
        print("Load average in last 15 minutes: ", load15)

def handle_loadavg():
    nproc = os.cpu_count()
    print("CPU core count: ", nproc)
    if (nproc - load5 < 1):
        quit()

def check_url():
    urls = ["http://api.github.com", "http://bilgisayar.mu.edu.tr", "https://python.org", "http://akrepnalan.com/ceng2034", "https://github.com/caesarsalad/wow"]
    for url in urls:
        r = requests.head(url)
        status_code = r.status_code
        if(status_code/100 >= 4):
            print("Following URL is not exist ->", url)
        else:
            print("Following URL is exist -> ", url)



get_os_name()
get_pid()
print_loadavg()
handle_loadavg()
check_url()
