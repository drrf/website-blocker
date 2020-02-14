import time
from datetime import datetime as dt

hosts_temp=r"hosts"
hosts_path=r"/etc/hosts"	#for windows use the path: C:\Windows\System32\drivers\etc
redirect="127.0.0.1"
website_list=[	
	"facebook.com",
	"youtube.com",	
	"amazon.com",
	"bing.com"
	]

am = dt(dt.now().year,dt.now().month,dt.now().day,9)
pm = dt(dt.now().year,dt.now().month,dt.now().day,17)

while True:
    if (am < dt.now() < pm):
        print("Time to work ...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Free time have a fun...")
    time.sleep(5*60) #every 5 minute