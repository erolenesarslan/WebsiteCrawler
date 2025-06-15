import requests
from bs4 import BeautifulSoup

target_url = "https://www.browse.ai/"
foundlinks= []

def make_request(url):
    response = requests.get(target_url)
    #HTML Parsing
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawler(url):
    links = make_request(url)
    for link in links.find_all("a"):
        foundurl = link.get("href")
        if foundurl:
            if "#" in foundurl:
                foundurl = foundurl.split("#")[0]
            if target_url in foundurl and foundurl not in foundlinks:
                foundlinks.append(foundurl)
                print(foundurl)
                crawler(foundurl)

crawler(target_url)

