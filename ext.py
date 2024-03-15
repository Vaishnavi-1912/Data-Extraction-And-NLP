import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


# Function to extract title from the webpage
def extract_title(soup):
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.text.strip()
    else:
        return 'Title not found'


# Function to extract article text from the webpage
def extract_article_text(soup):
    article_tag = soup.find('article')
    if article_tag:
        return article_tag.text.strip()
    else:
        return 'Article text not found'


# Step 1: Data Extraction
input_df = pd.read_excel('input.xlsx')

for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract title and article text from the webpage
        page_title = extract_title(soup)
        article_text = extract_article_text(soup)

        # Save the extracted text into a text file
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(f'Title: {page_title}\n\nURL: {url}\n\nArticle Text:\n{article_text}')

    else:
        print(f"Failed to fetch URL: {url}")


