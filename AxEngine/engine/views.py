from django.shortcuts import render, HttpResponse
from googlesearch import search
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def searchQuery(request):
    if request.method=="GET":
        query = request.GET.get('query')
        from selenium import webdriver
        from bs4 import BeautifulSoup
        import time
        from bs4.element import Tag

        driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
        google_url = "https://www.google.com/search?q="+ query + "&num=" + str(10)
        driver.get(google_url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source,'lxml')
        result_div = soup.find_all('div', attrs={'class': 'g'})


        links = []
        titles = []
        descriptions = []
        for r in result_div:
            # Checks if each element is present, else, raise exception
            try:
                link = r.find('a', href=True)
                title = None
                title = r.find('h3')

                if isinstance(title,Tag):
                    title = title.get_text()

                description = None
                description = r.find('span', attrs={'class': 'aCOpRe'})

                if isinstance(description, Tag):
                    description = description.get_text()

                # Check to make sure everything is present before appending
                if link != '' and title != '' and description != '':
                    links.append(link['href'])
                    titles.append(title)
                    descriptions.append(description)
            # Next loop if one element is not present
            except Exception as e:
                print(e)
                continue
        driver.close()
        context = {
            "link1" : links[0],
            "link2" : links[1],
            "link3" : links[2],
            "link4" : links[3],
            "link5" : links[4],
            "link6" : links[5],
            "title1" : titles[0],
            "title2" : titles[1],
            "title3" : titles[2],
            "title4" : titles[3],
            "title5" : titles[4],
            "title6" : titles[5],
            "descriptions1" : descriptions[0],
            "descriptions2" : descriptions[1],
            "descriptions3" : descriptions[2],
            "descriptions4" : descriptions[3],
            "descriptions5" : descriptions[4],
            "descriptions6" : descriptions[5],
            "query" : query
            # LC20lb DKV0Md
        }
        return render(request, 'search.html', context)
