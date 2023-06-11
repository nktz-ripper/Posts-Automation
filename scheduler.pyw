import schedule
import time
import fetcher
import tasklist_updater
import pywhatkit as pwk

def standard_schedule():
    articles = fetcher.fetcher()
    #print(articles)

    #df = fetcher.news_parser(articles)
    #print(df)

    url_list = fetcher.get_url_list(articles)
    #print(url_list)

    tasklist_updater.post_all(url_list)

    try:
        # sending message in Whatsapp in India so using Indian dial code (+91)
        pwk.sendwhatmsg("+5566992544563", f"Bom dia Duda! Segue links de postagens para hoje\n\nGentileza escolher a melhor para hoje, mas pode ser que algumas sejam repetidas de ontem.\n\n{url_list}", 7, 5)
    
        print("Message Sent!") #Prints success message in console
    
        # error message
    except: 
        print("Error in sending the message")

schedule.every().day.at("07:00").do(standard_schedule)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

