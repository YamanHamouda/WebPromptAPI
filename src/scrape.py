import requests
from bs4 import BeautifulSoup

url = "https://www.britannica.com/topic/Islam" #example
def fetch_url_soup(url : str) -> BeautifulSoup: #1
    

    response = requests.get(url)
    html_string = response.text

    soup = BeautifulSoup(html_string, "html.parser")
    return soup

def get_main_container(soup : BeautifulSoup) -> BeautifulSoup: #2
    return (
        soup.find("main")
        or soup.find("article")
        or soup.find("div", id="content")
        or soup.find("div", class_="content")
        or soup.body
    )

def strip_uneeded_tags(soup : BeautifulSoup) -> None: #3
    uneeded_tags = [
        "script", "style", "noscript",
        "header", "footer", "nav", "aside",
        "form", "button", "input"
    ]
    for tag in soup(uneeded_tags):
        tag.decompose() #changes soup in memory

def extract_text(container : BeautifulSoup) -> str:
    allowed_tags = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote"]
    chunks = []

    for tag in container.find_all(allowed_tags):
        text = tag.get_text(
            separator = " ", #places a space in spots where words lose their spaces
            strip=True #strips away extra whitespace
            )

        #Too short => useless => don't use it.
        if len(text) < 30:
            continue
        chunks.append(text)
    return "\n".join(chunks)

def parse_url(url : str) -> str:
    soup = fetch_url_soup(url)  #gets the full URL's HTML

    main_soup = get_main_container(soup) #focuses on specifically the main section of a URL

    strip_uneeded_tags(main_soup) #returns by reference. gets rid of tags unlikely to have important article text

    website_text = extract_text(main_soup) #focus on text tags and extract only the text from all of them.

    return website_text