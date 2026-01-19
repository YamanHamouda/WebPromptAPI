import requests
from bs4 import BeautifulSoup

url = "https://www.britannica.com/topic/Islam" #example
def fetch_url_soup(url) -> BeautifulSoup: #1
    

    response = requests.get(url)
    html_string = response.text

    soup = BeautifulSoup(html_string, "html.parser")
    return soup

def get_main_container(soup) -> BeautifulSoup: #2
    return (
        soup.find("main")
        or soup.find("article")
        or soup.find("div", id="content")
        or soup.find("div", class_="content")
        or soup.body
    )

def strip_uneeded_tags(soup) -> None: #3
    uneeded_tags = [
        "script", "style", "noscript",
        "header", "footer", "nav", "aside",
        "form", "button", "input"
    ]
    for tag in soup(uneeded_tags):
        tag.decompose() #changes soup in memory


def parse_url(url):
    soup = fetch_url_soup(url) 
    soup = get_main_container(soup)
    strip_uneeded_tags(soup) #no return

parse_url(url)