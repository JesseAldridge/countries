# -*- coding: utf-8 -*- #
import json

# https://www.usnews.com/news/best-countries/quality-of-life-full-list

class Parser:
  def __init__(self, text):
    self.lines = text.splitlines()
    self.line_index = 0

  def line(self):
    return self.lines[self.line_index]

  def apply_cmd(self, cmd_str, params):
    getattr(self, cmd_str)(*params)

  def advance(self):
    self.line_index += 1

  def stop_after(self, stop_line):
    for _ in range(10 ** 6):
      if self.lines[self.line_index].strip() == stop_line:
        break
      self.line_index += 1
    self.line_index += 1

  def is_done(self):
    return self.line_index >= len(self.lines)

  def status_str(self):
    return 'line {}/{}'.format(self.line_index, len(self.lines))

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

def main():
  with open('us_news_dump.txt') as f:
    text = f.read()
  parser = Parser(text)
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

if __name__ == '__main__':
  main()
