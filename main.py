import requests, time
from bs4 import BeautifulSoup

#HTML TO START THE PAGE
startNewPage = '''
<!DOCTYPE html>
    <html>
        <head>
            <title>Quiz Questions</title>
            <link rel="stylesheet" href="stylesheet.css">
        </head>
    <body>
    '''

#HTML TO END THE PAGE
endNewPage = '''
    </body>
</html>
'''

logSession = input("Please enter your logSession Cookie data\n")
#logSession = ''
legacySession = input("Please enter your legacySession Cookie data\n")
#legacySession = ''
canvasSession = input("Please enter your canvasSession Cookie data\n")
#canvasSession = ''
csrf = input("Please enter your csrf Cookie data\n")
#csrf = ''
quizLink = input('Please enter the url of the quiz\n')
#quizLink = ''


def getPage(link):
    #HEADERS FOR AUTHENTICATION
    headers = {
        'authority': 'missouri.instructure.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'log_session_id={0}; _legacy_normandy_session={1}; canvas_session={2}; _csrf_token={3}'.format(logSession, legacySession, canvasSession, csrf),
    }

    response = requests.get(link, headers=headers)
    return response.text

created = startNewPage 

text = getPage(quizLink)
soup = BeautifulSoup(text, "html.parser")

#GET ALL THE QUESTION LINKS
uls = soup.find_all('ul')
c = 1
for ul in uls:
    hrefs = ul.find_all('a', {'class' : 'no-warning'})
    for href in hrefs:
        link = href['href']
        link = 'https://missouri.instructure.com'+link
        print('Getting {} Question {}'.format(link,c))
        text = getPage(link)
        soup = BeautifulSoup(text, "html.parser")
        #READ PAGE - GRAB QUESTION ELEMENT & CREATE NEW PAGE
        x = soup.find('div', {'class' : 'quiz_sortable question_holder'})
        created = created + str(x)
        #IF YOU WOULD LIKE TO WRITE TO THE FILE AT EVERY URL
        #with open("Output.html", "w") as text_file:
        #    text_file.write("%s" % created)
        c += 1
        time.sleep(5)
    
created = created + endNewPage
#IF YOU WOULD LIKE TO WRITE TO THE FILE AT THE END OF THE LOOP
with open("Output.html", "w") as text_file:
    text_file.write("%s" % created)