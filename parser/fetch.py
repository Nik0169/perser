import requests

def get_page(url):
    my_headers = {"User-Agent": "parser/1.0"}
    response = requests.get(url, headers=my_headers, timeout=10)
    response.raise_for_status()
    html = response.text
    return html


if __name__ == '__main__':
    print(get_page("https://books.toscrape.com/")[:500])