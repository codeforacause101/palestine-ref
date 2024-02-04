import requests
from bs4 import BeautifulSoup
import sys

def validate_url(url):
    # if url contains "/tags" then apply this code block
    if not "/tags" in url or not "/posts/books" in url : 
        try:
            response = requests.head(url)
            return response.status_code != 404
        except requests.ConnectionError:
            return False
    return True

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    urls = [link.get('href') for link in soup.find_all('a')]
    return urls

def validate_urls(urls):
    invalid_urls = [url for url in urls if not validate_url(url)]
    if invalid_urls:
        print(f"Error: {len(invalid_urls)} URLs are invalid.")
        for url in invalid_urls:
            print(url)
    else:
        print("All URLs are valid.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        urls = parse_html(response.text)
        validate_urls(urls)
    else:
        print("No URL provided. Please provide a URL as an argument.")