from constants import newsapi_key, editpad_key, q, domains

import requests
import json
from datetime import datetime
import pandas as pd
import codecs
from inputimeout import inputimeout, TimeoutOccurred

current_date = datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day

articles = ''
title_list = []
content_list = []
urlToImage_list = []
url_list = []
pre_array = []
df = ''


#q = '+(lei OR judicial OR advogado OR juridico OR juiz OR desembargador OR justiça OR decisao OR multa OR punição) AND (tecnologia OR inteligência artificial OR bitcoin OR cripto OR gpt OR ethereum OR IA OR AI) AND (empresa OR empresario OR impacto OR negocios OR mercado OR crise OR economia OR setor) NOT (review OR faculdades OR universidades OR saiba quem tem direito OR formação)'


def fetcher():
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    if day < 3:
        day = 28
        month = month - 1
        if month < 1:
            month = 12
            year = year - 1
    else:
        day = day - 2
        if day < 10:
            day = str(f'0{month}')

        if month < 10:
            month = str(f'0{month}')
    print(f'{year}, {month}, {day}')
    newsapi_url = ('https://newsapi.org/v2/everything?'
        'language=pt&'
        #'category=technology'
        #'domains=bbc.com&'
        f'q={q}&'
        'searchIn=description&'
        #'domains=bbc.com&'
        f'Domains={domains}&'
        f'from={year}-{month}-{day}&'
        'sortBy=popularity&'
        f'apiKey={newsapi_key}')
    response = requests.get(newsapi_url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles')
        return articles
    else:
        print('News API Server Error:', response.status_code)


#STANDARD SEARCH PARAMS

def alter_q():
    try:
        c = inputimeout(prompt='Press Any Key to personalize the keywords.\nProceeding in 5 seconds.....', timeout=5)
        q_text = '''
Keywords or phrases to search for in the article title and body.

Advanced search is supported here:

- Surround phrases with quotes (") for exact match.
- Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
- Prepend words that must not appear with a - symbol. Eg: -bitcoin
- Alternatively, you can use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.
- The complete value for q must be URL-encoded. Max length: 500 chars.

Type your keywords: '''
        q = input(q_text)
        return q
    except TimeoutOccurred:
        c = 'Timeout. No changes made. Proceeding.....'
        print(c)
        return q


def alter_excludeDomains():
    try:
        c = inputimeout(prompt='Press Any Key to personalize the ignored domains.\nProceeding in 5 seconds.....', timeout=5)
        excludeDomains = input('A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to remove from the results.')
    except TimeoutOccurred:
        c = 'Timeout. No changes made. Proceeding.....'
        print(c)
    


    ### TOP HEADLINES SEARCH OPTION
def fetcher_topnews():
    day = current_date.day
    if day < 3:
        day = 28
        month = month - 1
        if month < 1:
            month = 12
            year = year - 1
    else:
        day = day - 2
        if day < 10:
            day = str(f'0{month}')

        if month < 10:
            month = str(f'0{month}')
            
    newsapi_url = ('https://newsapi.org/v2/top-headlines?'
        'country=br&'
        'category=technology'
        f'q={q}&'
        f'apiKey={newsapi_key}')
    response = requests.get(newsapi_url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles')
        return articles
    else:
        print('News API Server Error:', response.status_code)


def news_parser(articles):
    for title in articles:
        title_list.append(title['title'])
        content_list.append(title['content'])
        urlToImage_list.append(title['urlToImage'])
        url_list.append(title['url'])

    ### LIST OF LISTS    
    pre_array.append(title_list)
    pre_array.append(urlToImage_list)
    pre_array.append(url_list)

    ### CONVERT LIST OF LISTS TO ARRAY
    df = pd.DataFrame(pre_array).transpose()
    df.columns = ['title', 'urlToImage', 'url']
    df.to_csv(f'C:/Users/nktz/Meu Drive (nakasotovlogs@gmail.com)/Apps Coding/Posts Automation/Fetched CSVs/{current_date.year}.{current_date.month}.{current_date.day} - news.csv', ';')

    return df

### PARSE URL NEWS TO RETURN VALUE TO TASKLIST_UPDATER    
def get_url_list(articles):
    for title in articles:
        url_list.append(title['url'])
    return url_list