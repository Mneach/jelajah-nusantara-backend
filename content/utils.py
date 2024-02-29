from news.utils import extractFindAllData
from bs4 import BeautifulSoup
from requests import get

def getScrappingData(link):
    res = {}
    try:
        url = get(link)
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main")
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        image_url = content_container.find('img', class_="mw-file-element")

        # Handle title
        if(title):
            title = title.text
        else:
            title = soup.find('h1', class_="firstHeading mw-first-heading").text

        # Handle image
        if(image_url):
            image_url = image_url.get('src')
        else:
            image_url = ""
        

        res = {
            "title": title,
            "content": "\n".join(extractFindAllData(content)),
            "image_url" : image_url,
        }
    except Exception as error:
        print(error)
        res = {
            "message": "error!",
        }
    return res

def scrappingData(links):
    res = []
    for link in links:
        # print(link)
        res.append(getScrappingData(link))

    return res
