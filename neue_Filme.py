#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import json
import os, time
import datetime
import pandas



filmliste = []
file_path = "/tmp/neueFilme.csv"
tmpfile = "/tmp/Filmliste-diff"
file = "/tmp/Filmliste-diff.xz"
### check file is up to date
now = datetime.datetime.now()
now_string = now.strftime("%Y-%m-%d")
print(now_string)

def createDB():
    filename = "/tmp/neueFilme.sqlite"
    con = sqlite3.connect(filename)
    cur = con.cursor()
    df = pandas.read_csv(file_path, encoding = 'utf-8', delimiter = '\t', error_bad_lines=False)
    df.to_sql("Filme", con, if_exists='append', index=False)


def downloadList():
    url = "http://verteiler1.mediathekview.de/Filmliste-diff.xz"
    cmd = "%s;%s %s" % ("cd /tmp", "wget", url)
    os.system("[ -e /tmp/Filmliste-diff.xz ] && rm /tmp/Filmliste-diff.xz")
    os.system("[ -e /tmp/neueFilme.sqlite ] && rm /tmp/neueFilme.sqlite")
    os.system(cmd)
    os.system("unxz -q -k -f /tmp/Filmliste-diff.xz")
    os.system("perl -i -pe 's/\"X/$& . ++$n/ge' /tmp/Filmliste-diff")
    
    with open(tmpfile) as data_file:
        data = json.load(data_file)
        mydata = ''
        
    
    for e in data:
        mydata = (data[e])
        thema = str(mydata[1])
        title = str(mydata[2])
        url = str(mydata[8])
        filmliste.append("%s\t%s\t%s" % (thema, title, url))
        
    
    with open(file_path, "w") as text_file:
        if text_file.write('\n'.join(filmliste)):
            print("Filmliste gespeichert")
            createDB()

if os.path.isfile(file):
    print(os.path.getmtime(file))
    cr = datetime.datetime.strptime(time.ctime(os.path.getctime(file)), "%c")
    print("created: %s" % cr)
    mydate = str(cr)[:10]
    print(mydate)
    
    if not now_string == mydate:
        print("is not up to date")
        downloadList()
    else:
        print("is up to date")
else:
    print("is not up to date")
    downloadList()