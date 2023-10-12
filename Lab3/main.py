import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = 'https://999.md/'


def extract_urls(url, page=1, accumulated_urls=None):
    if accumulated_urls is None:
        accumulated_urls = []

    full_url = f"{url}?page={page}"

    print(f"Scraping page {page}")

    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    for link in links:
        href = link.get('href')

        if href and not href.startswith('javascript:'):
          href = urljoin(BASE_URL, href)

          if re.match(r'^https://999\.md/ro/\d+$', href):
            accumulated_urls.append(href)

            if 'booster' not in href.lower():
                accumulated_urls.append(href)


    next_page = soup.find('a', string='Next')

    if next_page:
        next_page_url = next_page['href']
        next_page_num = page + 1

        return extract_urls(url, page=next_page_num, accumulated_urls=accumulated_urls)

    return accumulated_urls


start_url = 'https://999.md/ro/list/transport/cars'
all_urls = extract_urls(start_url, page=1)

print(all_urls)