"""
projekt_3.py: 3. projekt do Engeto Online Python Akademie
author: Anastassiya Manakova
email: anastassiyamanakova@gmail.com
discord: Anastassiya M.#8059
"""

import requests
from bs4 import BeautifulSoup as bs
import sys
import csv
import re


def clean_number(number_str):
    cleaned_str = re.sub(r'\s', '', number_str).replace(',', '.')
    return cleaned_str


def get_parties_data(municipality_name, election_data):
    link = election_data[municipality_name]['link']

    parties_data = {}

    response = requests.get(link)
    soup = bs(response.text, 'html.parser')

    tables = soup.find_all('table', class_='table')

    if len(tables) >= 3:
        table_1 = tables[1]
        table_2 = tables[2]

        party_results = []

        rows_1 = table_1.find_all('tr')
        for row in rows_1:
            cells = row.find_all('td')
            if cells and len(cells) >= 3:
                party_name = cells[1].text.strip()
                party_result = cells[2].text.strip()
                party_result = clean_number(party_result)
                party_results.append({'party_name': party_name, 'party_result': party_result})

        rows_2 = table_2.find_all('tr')
        for row in rows_2:
            cells = row.find_all('td')
            if cells and len(cells) >= 3:
                party_name = cells[1].text.strip()
                party_result = cells[2].text.strip()
                party_result = clean_number(party_result)
                party_results.append({'party_name': party_name, 'party_result': party_result})

        for result in party_results:
            parties_data[result['party_name']] = result['party_result']

    return parties_data


def get_voters_data(municipality_name, election_data):
    link = election_data[municipality_name]['link']

    voters_data = {}

    response = requests.get(link)
    soup = bs(response.text, 'html.parser')

    table = soup.find('table', id='ps311_t1', class_='table')

    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        if cells:
            registered = cells[3].text.strip()
            envelopes = cells[4].text.strip()
            valid = cells[7].text.strip()

            registered = clean_number(registered)
            envelopes = clean_number(envelopes)
            valid = clean_number(valid)

            voters_data = {'registered': registered, 'envelopes': envelopes, 'valid': valid}

    return voters_data


def get_election_data(data, city, url):
    link = data[city]

    election_data = {}

    response = requests.get(link)
    soup = bs(response.text, 'html.parser')

    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')

            if len(cells) >= 2:
                municipality_name = cells[1].text.strip()
                municipality_code = cells[0].text.strip()

                election_result_link_element = cells[0].find('a')
                if election_result_link_element:
                    election_result_link = url[:31] + election_result_link_element['href']

                    if municipality_name not in election_data:
                        election_data[municipality_name] = {'code': municipality_code, 'link': election_result_link,
                                                            'voters_data': {}, 'parties_data': {}}

                    voters_data = get_voters_data(municipality_name, election_data)

                    parties_data = get_parties_data(municipality_name, election_data)

                    election_data[municipality_name]['voters_data'] = voters_data
                    election_data[municipality_name]['parties_data'] = parties_data

    return election_data


def get_cities_data(url):
    data = {}
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            if cells:
                city_name = cells[1].string
                city_link = url[:31] + cells[3].find('a')['href']

                data[city_name] = city_link

    return data


def export_to_csv(election_data, output_file):
    all_party_names = set()

    for data in election_data.values():
        all_party_names.update(data['parties_data'].keys())

    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['code', 'municipality', 'registered', 'envelopes', 'valid'] + list(all_party_names)

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for municipality_name, data in election_data.items():
            row = {
                'code': data['code'],
                'municipality': municipality_name,
                'registered': data['voters_data']['registered'],
                'envelopes': data['voters_data']['envelopes'],
                'valid': data['voters_data']['valid']
            }

            row.update(data['parties_data'])

            writer.writerow(row)


def main():
    if len(sys.argv) != 3:
        print('Incorrect usage. Please provide two arguments.')
        print('Usage: "python elections_scraper.py <city> <output_file_name.csv>"')
        return

    url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    cities = get_cities_data(url)
    user_city = sys.argv[1]
    user_output_file = sys.argv[2]

    if user_city in cities:
        print (f'Exporting data for {user_city}...')
        election_data = get_election_data(cities, user_city, url)
        export_to_csv(election_data, user_output_file)
        print(f'CSV file "{user_output_file}" has been created.')
    else:
        print(f'The city "{user_city}" is not in the list of valid cities.')


if __name__ == "__main__":
    main()
