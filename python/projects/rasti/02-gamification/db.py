import psycopg2
from db_config import config
import json

params = config()

'''try:
    cur.execute("create database gamification_events;")
    conn.commit()
except:
    print("database gamification_events already available.")
'''

def create_table():
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        query = '''
        drop table if exists user_actions;
        create table if not exists user_actions (
        id serial not null primary key,
        user_id text unique not null,
        actions json,
        passed_levels integer default 0  
        )
        '''
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        print("User table created.")
    except:
        raise ConnectionError

def get_user(user_id):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        query = '''
        select actions, passed_levels from user_actions where user_id = %s
        '''
        cur.execute(query, (user_id,))
        user_actions = cur.fetchone()
        cur.close()
        conn.commit()
        conn.close()
        return user_actions
    except:
        raise ConnectionError
    
def insert_user(user_id):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        query = '''
        insert into user_actions (user_id, actions) values (%s, '[{}]')
        '''
        cur.execute(query, (user_id,))
        cur.close()
        conn.commit()
        conn.close()
        print(f"user with user_id = {user_id} inserted to database.")
    except:
        raise ConnectionError
    
def update_user(user_id, user_actions, passed_levels):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        query = '''
        update user_actions set actions = %s , passed_levels = %s where user_id = %s
        '''
        cur.execute(query, (user_actions, passed_levels, str(user_id)))
        cur.close()
        conn.commit()
        conn.close()
        
    except:
        raise ConnectionError

def get_db_len():
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        query = '''
        select count(*) from user_actions
        '''
        cur.execute(query)
        print(f"total number of users in db = {cur.fetchone()}")
        cur.close()
        conn.commit()
        conn.close()
        
    except:
        raise ConnectionError

if __name__ == "__main__":
    create_table()
    for i in range(5):
        insert_user(i+1)
    update_user(1, json.dumps([{7:1}]), 0)
    update_user(3, json.dumps([{7:1, 14:1}, {42:2, 4:1}]), 2)


    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    query = '''
    select * from user_actions
    '''
    cur.execute(query)
    print(cur.fetchall())
    cur.close()
    conn.commit()
    conn.close()