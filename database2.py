import json
import sqlite3
import timeit  # for simplification I left out how I implemented timing for this code.

print("Started Processing")
with open(r"scraped_data_utf8.json",'r',encoding='utf-8') as content_file:
    records = []
    for line in content_file:
        jo = json.loads(line)
        record = (jo.get('productId'), jo.get('name'), jo.get('price'), jo.get('description'), jo.get('image'),jo.get('stock'),jo.get('categoryId'))
        records.append(record)

    try:
        conn = sqlite3.connect("content_test.db")
        c = conn.cursor()
        c.executemany("INSERT INTO MainContent VALUES (?, ?, ?, ?, ?,?,?)", records)
        conn.commit()
        conn.close()
    except:
        # TODO: logging here
        raise

print("Finished Processing")