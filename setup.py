import sqlite3

def create_table():
    conn = sqlite3.connect("channels.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS custom_channels (
                user_id INTEGER,
                channel_name TEXT,
                user_limit INTEGER,
                channel_id INTEGER)""")
    conn.commit()
    conn.close()

create_table()