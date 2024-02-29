from news.utils import extractFindAllData
from bs4 import BeautifulSoup
from requests import get

def getScrappingData(link):
    res = []
    try:
        url = get(link)
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main").text
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        image_url = content_container.find('img', class_="mw-file-element").get('src')
        res.append({
            "title": title,
            "content": extractFindAllData(content),
            "image_url" : image_url,
        })
    except Exception as error:
        print(error)
        res.append({
            "message": "error!",
        })
    return res[0]

def scrappingData(links):
    res = []
    for link in links:
        print(link)
        res.append(getScrappingData(link))

    return res
