import requests
from bs4 import BeautifulSoup

# url = "https://www.britannica.com/topic/Islam" #example
def fetch_url_soup(url):
    

    response = requests.get(url)
    html_string = response.text
    # print(html_string)

    soup = BeautifulSoup(html_string, "html.parser")
    return soup

