import pandas as pd
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = '/client_secret_file.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

mainTasklistId = 'ejl0Yjl5RWZ4cmI1Sk1oeg'


"""
Insert Method
"""

title = 'San Francisco'
notes = ''
due = ''
status = 'needsAction'
deleted = False

request_body = {
    'title': title,
    'notes': notes,
    'due': due,
    'deleted': deleted,
    'status': status
}

response = service.tasks().insert(
    tasklist=mainTasklistId,
    body=request_body
).execute()

responseSanFrancisco = response

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


responseNewYork = service.tasks().insert(
    tasklist=mainTasklistId,
    body=construct_request_body('New York City'),
    previous=responseSanFrancisco.get('id')
).execute()

responseChicago = service.tasks().insert(
    tasklist=mainTasklistId,
    body=construct_request_body('Chicago'),
    previous=responseNewYork.get('id')
).execute()


"""
Tasks Demo: Restaurants To Try:
    San Francisco
        - Pearl San Francisco
        - Burma Superstar
        - House of Prime Rib
    Chicago
    New York
"""

responsePearl = service.tasks().insert(
    tasklist=mainTasklistId,
    parent=responseSanFrancisco.get('id'),
    body=construct_request_body(
        'Pearl San Francisco',
    notes = '''
        Address: 94121 CASan Francisco6101 California St
        Phone: +1 (415) 592-9777
        Cuisines: Café, Mediterranean, Seafood
        Website: https://pearl-sf.com
    ''',
    due=convert_to_RFC_datetime(2020, 8, 21, 20, 30)
    )
).execute()

notes = '''
Address: 94118 CASan Francisco309 Clement St
Phone: +1 (415) 387-2147
Website: https://burmasuperstar.com
Pickup or delivery: Order online
'''

service.tasks().insert(
    tasklist=mainTasklistId,
    body=construct_request_body('Burma Superstar', notes=notes, due=convert_to_RFC_datetime(2020, 8, 10, 21, 30)),
    parent=responseSanFrancisco.get('id')
).execute()


notes = '''
Address: 94109 CASan Francisco1906 Van Ness Ave
Phone: +1 (415) 885-4605
Cuisines: Steak House, American, British
Reservations: Book at OpenTable
Website: https://houseofprimerib.net
'''

service.tasks().insert(
    tasklist=mainTasklistId,
    body=construct_request_body('House of Prime Rib', notes=notes, due=convert_to_RFC_datetime(2020, 8, 10, 21, 30)),
    parent=responseSanFrancisco.get('id')
).execute()

for i in range(100):
    service.tasks().insert(
        tasklist=mainTasklistId,
        parent=responseSanFrancisco.get('id'),
        body=construct_request_body(
            'Dummy Task #{0}'.format(i+1), due=convert_to_RFC_datetime(2020, (i%12)+1)
        )
    ).execute()


"""
List Method
"""
response = service.tasks().list(
    tasklist=mainTasklistId,
    dueMax=convert_to_RFC_datetime(2020, 5, 1),
    showCompleted=False
).execute()
lstItems = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.tasks().list(
    tasklist=mainTasklistId,
    dueMax=convert_to_RFC_datetime(2020, 5, 1),
    showCompleted=False,
    pageToken=nextPageToken
    ).execute()
    lstItems = response.get('items')
    nextPageToken = response.get('nextPageToken')

print(pd.DataFrame(lstItem))
