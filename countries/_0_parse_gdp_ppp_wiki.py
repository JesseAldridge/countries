# -*- coding: utf-8 -*-
import json, re, codecs

import _0_utils

'''
1  China[n 1] 23,159,107
—  European Union[n 2]  20,982,857
2  United States  19,390,600
3  India  9,459,002
4  Japan  5,428,813
...
'''

def txt_dump_to_dicts():
  with codecs.open('gdp_ppp_2017_wiki_dump.txt', encoding='utf8') as f:
    text = f.read()

  country_dicts = []
  for line in text.splitlines():
    line = re.sub(r'\[.+?\]', '', line)
    line, gdp_ppp = line.rsplit(' ', 1)
    name = line.split(' ', 1)[-1]
    country_dict = {'gdp_ppp': gdp_ppp.strip(), 'name': name.strip()}
    country_dicts.append(country_dict)
  return country_dicts

def main():
  country_dicts = txt_dump_to_dicts()
  _0_utils.write_json('_0_countries_gdp_ppp.json', country_dicts)

if __name__ == '__main__':
  main()
