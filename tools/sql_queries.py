from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM chats;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_user (username):
    query = f"""SELECT * 
    FROM chats
    WHERE username = '{username}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_messages_from_date (date):
    query = f"""SELECT * 
    FROM chats
    WHERE date like '{date}%';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_messages_score ():
    query = f"""SELECT username, AVG(message_score)
    FROM chats
    GROUP BY username
    ORDER BY AVG(message_score) DESC;"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_emojis_score ():
    query = f"""SELECT username, AVG(emojis_score)
    FROM chats
    GROUP BY username
    ORDER BY AVG(emojis_score) DESC;"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def insert_one_row (id,date, username, message, emojis, message_translated, message_score, emojis_score):
    query = f"""INSERT INTO chats
     (id,date,username,message,emojis,message_translated,message_score,emojis_score) 
        VALUES ({id}, '{date}', '{username}', '{message}', '{emojis}', '{message_translated}', {message_score}, {emojis_score});
    """
    engine.execute(query)
    return f"Correctly introduced!"


    