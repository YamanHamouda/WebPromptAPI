import requests
from bs4 import BeautifulSoup

url = "https://www.britannica.com/topic/Islam" #example
def fetch_url_soup(url) -> BeautifulSoup: #1
    

    response = requests.get(url)
    html_string = response.text

    soup = BeautifulSoup(html_string, "html.parser")
    return soup


def strip_uneeded_tags(soup) -> None: #
    uneeded_tags = [
        "script", "style", "noscript",
        "header", "footer", "nav", "aside",
        "form", "button", "input"
    ]
    for tag in soup(uneeded_tags):
        tag.decompose() #changes soup in memory


def parse_url(url):
    soup = fetch_url_soup(url) 
    strip_uneeded_tags(soup) #no return

parse_url(url)