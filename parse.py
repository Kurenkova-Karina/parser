import requests
from bs4 import BeautifulSoup
import csv


# GLOBAL VARIABLES
base_url = 'your url'

#function to get the html of a page
def get_html(url):
    r = requests.get(url)
    return r.text

#making the parser go through all the pages. Getting total number of the pages.
def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('tag', class_='class').find_all('tag', class_='class')[-2].get('tag')
    total_pages = pages.split('(')[1].split(')')[0]

    return int(total_pages)

total_pages = get_total_page(html)

#let`s generate our urls
def gen_url(total_pages):
    for i in range(1, total_pages):
        url_final = base_url + str(i)
        return url_final


#this is a function to write a csv.file. We will need it later
def write_csv(data):
    with open('file.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow((data['value one'],
                         data['value two'],
                         data['value three']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    items = soup.find('tag', class_='class').find_all('tag', class_='class')

    for item in items:
        try:
            value_one = item.find('tag', class_='class').find('tag', 'class').find('tag').text.strip()
        except:
            value_one =''
        try:
            value_two = item.find('tag', class_='class').find('tag', class_='class').find('tag', class_='class').text.strip()
        except:
            value_two = ''
        try:
            value_three = item.find('tag', class_='class').find('tag', class_='class').find('tag').text.strip()
        except:
            value_three = ''

        data = {'value one': value_one,
                'value two': value_two,
                'value three': value_three}
        write_csv(data)


