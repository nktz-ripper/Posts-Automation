import pandas as pd
from fetcher import url_list
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'Posts Automation v2\client_secret_file.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

mainTasklistId = 'ZHBMcEhtSlRLSnNWcWpJcQ'



"""
Insert Method
"""

title = ''
notes = ''
due = ''
status = 'needsAction'
deleted = False
response = ''


def post_all(url_list):
    for item in url_list:
        response = service.tasks().insert(
            tasklist=mainTasklistId,
            body=construct_request_body(item)
        ).execute()
        print(response)

    

def construct_request_body(title, notes=None, due=None, status='needsAction', deleted=False):
    try:
        request_body = {
        'title': title,
        'notes': notes,
        'due': due,
        'deleted': deleted,
        'status': status
        }
        return request_body
    except Exception:
        return None