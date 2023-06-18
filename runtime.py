import fetcher
#import tasklist_updater
import pywhatkit as pwk



articles = fetcher.fetcher()
#print(articles)

#df = fetcher.news_parser(articles)
#print(df)

url_list = fetcher.get_url_list(articles)
print(url_list)

img_url = 'https://tm.ibxk.com.br/2023/06/15/15090304237019.jpg?ims=1120x420'

#tasklist_updater.post_all(url_list)

try:
     #pwk.sendwhatmsg("+5544999292798", f"Bom dia Duda! Segue links de postagens para hoje\n\nGentileza escolher a melhor para hoje, mas pode ser que algumas sejam repetidas de ontem.\n\nDesconsiderar as notícias que forem impertinentes ao nosso tema de direito, tecnologia e inteligencia articial. Às vezes algumas passam.\n\n{url_list}\n\nObrigado pelo seu trabalho!", 20, 42)
     print("Message Sent!") #Prints success message in console

     # error message
except: 
     print("Error in sending the message")



#try:
#     pwk.sendwhatmsg("+5544999292798", f"Bom dia ! Segue links de postagens para hoje\n\nGentileza escolher a melhor para hoje, mas pode ser que algumas sejam repetidas de ontem.\n\nDesconsiderar as notícias que forem impertinentes ao nosso tema de direito, tecnologia e inteligencia articial. Às vezes algumas passam.\n\n{url_list}\n\nObrigado pelo seu trabalho!", 17, 54)

#     print("Message Sent!") #Prints success message in console

     # error message
#except: 
#     print("Error in sending the message")