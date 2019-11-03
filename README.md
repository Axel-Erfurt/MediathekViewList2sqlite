# MediathekViewList2sqlite
download and convert MediathekView List to sqlite DB

### Requirements
- python 3
- pandas
- sqlite3
- json

The scripts does the follwing:

- download the latest list from MediathekView Server (if outdated)
- convert it to csv and sqlite files

akt is the full list
diff is the short list with the latest additions

### Usage
**full list:**

>python3 alleFilme.py

**short list:**

>python3 neueFilme.py
