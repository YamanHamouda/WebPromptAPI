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

def extract_text(container):
    allowed_tags = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote"]
    chunks = []

    for tag in container.find_all(allowed_tags):
        text = tag.get_text(" ", strip=True)

        #Too short => useless => don't use it.
        if len(text) < 30:
            continue

        chunks.append(text)

    return "\n".join(chunks)

def parse_url(url):
    soup = fetch_url_soup(url) 
    main_soup = get_main_container(soup)
    strip_uneeded_tags(main_soup) #no return
    x = extract_text(main_soup)
    print(x)

parse_url(url)