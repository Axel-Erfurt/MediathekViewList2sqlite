# MediathekViewList2sqlite
download and convert MediathekView List to sqlite DB and CSV

* *I only use the fields 'Theme' 'Title' and 'Url'* *

(If you nedd more you can add it)

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

>python3 alle_Filme.py

creates the files 
- /tmp/alleFilme.csv
- /tmp/alleFilme.sqlite

**short list:**

>python3 neue_Filme.py

creates the files 
- /tmp/neueFilme.csv
- /tmp/neueFilme.sqlite
