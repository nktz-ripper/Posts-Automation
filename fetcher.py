from constants import newsapi_key, editpad_key

import requests
import json
from datetime import datetime
import pandas as pd
import codecs
from inputimeout import inputimeout, TimeoutOccurred


def fetcher():
    articles = ''
    title_list = []
    content_list = []
    urlToImage_list = []
    url_list = []
    pre_array = []
    df = ''


    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    if day < 3:
        day = 30
        month = month =- 1
        if month < 1:
            month = 12
            year = year =- 1
    else:
        day = day =- 2
        if day < 10:
            day = str(f'0{month}')

        if month < 10:
            month = str(f'0{month}')
    print(f'Today is {current_date}.....\n')
    print(f'Search engine will scrape headlines from {day}/{month}/{year}\n')


#STANDARD SEARCH PARAMS

    q = '+(lei OR judicial OR impacto) AND (tecnologia OR inteligência artificial OR bitcoin OR cripto) AND (empresa OR empresario OR trabalho) NOT (review OR faculdades OR universidades OR saiba quem tem direito)'
    excludeDomains = 'megacurioso.com.br'
    print(f'Would you like to personalize search paramaters?\nStandard are:\nKeywords: {q}\nIgnored Domains: {excludeDomains}.\n')
    personalize = ''
    if personalize == '':
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
        except TimeoutOccurred:
            c = 'Timeout. No changes made. Proceeding.....'
            print(c)

        try:
            c = inputimeout(prompt='Press Any Key to personalize the ignored domains.\nProceeding in 5 seconds.....', timeout=5)
            excludeDomains = input('A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to remove from the results.')
        except TimeoutOccurred:
            c = 'Timeout. No changes made. Proceeding.....'
            print(c)
        else:
            pass


    ### TOP HEADLINES SEARCH OPTION
        try:
            c = inputimeout(prompt='Press Any Key to search only "Top Headlines".\nProceeding to standard search 5 seconds.....', timeout=5)
            newsapi_url = ('https://newsapi.org/v2/top-headlines?'
                'country=br&'
                'category=technology'
                f'q={q}&'
                f'apiKey={newsapi_key}')
            response = requests.get(newsapi_url)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles')
                print(articles)
                print('News API search completed.....')
            else:
                print('News API Server Error:', response.status_code)

    ### STANDARD GET NEWS API
        except TimeoutOccurred:
            newsapi_url = ('https://newsapi.org/v2/everything?'
                'language=pt&'
                #'category=technology'
                #'domains=bbc.com&'
                f'q={q}&'
                'searchIn=description&'
                #'domains=bbc.com&'
                f'excludeDomains={excludeDomains}&'
                f'from={year}-{month}-{day}&'
                'sortBy=popularity&'
                f'apiKey={newsapi_key}')
            response = requests.get(newsapi_url)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles')
                print(articles)
                print('News API search completed.....')
            else:
                print('News API Server Error:', response.status_code)



    for title in articles:
        title_list.append(title['title'])
        content_list.append(title['content'])
        urlToImage_list.append(title['urlToImage'])
        url_list.append(title['url'])
        
    pre_array.append(title_list)
    pre_array.append(urlToImage_list)
    pre_array.append(url_list)

    print('Processing URLs.....')

    df = pd.DataFrame(pre_array).transpose()
    df.columns = ['title', 'urlToImage', 'url']
    print(df)
    df.to_csv(f'C:/Users/nktz/Meu Drive (nakasotovlogs@gmail.com)/Apps Coding/Posts Automation/Fetched CSVs/{current_date.year}.{current_date.month}.{current_date.day} - news.csv', ';')

    print('saving CSV.....')



#       df = pandas.read_json(json.dumps(articles))
#       df_simpler = df.drop(['source', 'author', 'content', 'publishedAt', 'urlToImage', 'description'], axis=1)
#       print(df_simpler)

#i have to get the content from the news api to parse in the rewriter


#print('Saving to CSV.....')

