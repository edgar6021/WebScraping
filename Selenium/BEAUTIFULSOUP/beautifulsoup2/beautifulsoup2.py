import urllib.request
from bs4 import BeautifulSoup

# User input for the webpage URL
pagina_web_url = input('Enter - ')
codigo = urllib.request.urlopen(pagina_web_url)

# Parse the HTML
Beaut = BeautifulSoup(codigo, 'html.parser')

# Find all <a> tags in the HTML
elemento = Beaut.find_all('a')

# Iterate over each <a> tag
for x in elemento:
    # Print the href attribute (the link URL)
    print('href: ', x.get('href'))
    # Print the link text
    print('Text: ', x.get_text())
    # Print the class attribute
    print('Class: ', x.get('class'))
    # Print the id attribute
    print('ID: ', x.get('id'))
    # Print any other attributes you are interested in
    print('Title: ', x.get('title'))
    print('Target: ', x.get('target'))
    print('Rel: ', x.get('rel'))
    print('\n')
