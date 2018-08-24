# -*- coding: utf-8 -*- #
import json

import parse

# https://www.usnews.com/news/best-countries/quality-of-life-full-list

'''
format:
---
Canada
#1
in
Quality of Life Rankings
No Change in Rank from 2017
READ MORE
Canada takes up about two-fifths of the North American continent, making it the second-largest country in the world after Russia. The country is sparsely populated, with most of its 35.5 million residents living within 125 miles of the U.S. border. Canada’s expansive wilderness to the north plays a large role in Canadian identity, as does the country’s reputation of welcoming immigrants.

GDP
$1.5 trillion
POPULATION
36.3 million
GDP PER CAPITA, PPP
$46,441


Denmark
...
'''

def txt_dump_to_dicts():
  with open('us_news_dump.txt') as f:
    text = f.read()
  parser = parse.Parser(text)
  country_dicts = []
  for _ in range(10 ** 6):
    print parser.status_str()
    if parser.is_done():
      break

    section_descriptions = [
      'country_name', 'rank', '_', '_', '_', '_', ('notes', 'stop_after', 'GDP'), 'gdp', '_',
      'population', '_', 'ppp', '_', '_',
    ]

    country_dict = {}
    for section_description in section_descriptions:
      label = section_description
      parser_cmd = 'advance'
      parser_params = []
      if isinstance(section_description, tuple):
        label, parser_cmd = section_description[:2]
        parser_params = section_description[2:]

      line = parser.line()
      if label != '_':
        country_dict[label] = line

      parser.apply_cmd(parser_cmd, parser_params)

    if not country_dict:
      break
    print ' country_dict:', json.dumps(country_dict, indent=2)
    assert country_dict['ppp'].startswith('$')
    country_dicts.append(country_dict)
  return country_dicts

def main():
  country_dicts = txt_dump_to_dicts()
  countries_json = json.dumps(country_dicts, indent=2)
  with open('countries_us_news.json', 'w') as f:
    f.write(countries_json)

if __name__ == '__main__':
  main()
