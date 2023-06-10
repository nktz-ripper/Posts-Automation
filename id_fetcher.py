import pandas as pd
from Google import Create_Service

CLIENT_SECRET_FILE = '/client_secret_file.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

response = service.tasklists().list().execute()
listItems = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.tasklists.list(
        maxResults=30,
        pageToken=nextPageToken
    ).execute()
    listItems.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

print(pd.DataFrame(listItems))