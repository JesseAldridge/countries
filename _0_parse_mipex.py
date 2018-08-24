import json

import parse, utils

'''
1
Sweden
78  0
2
Portugal
75  1
3
...
'''

def txt_dump_to_dicts():
  with open('mipex_dump.txt') as f:
    text = f.read()
  parser = parse.Parser(text)
  country_dicts = []
  for _ in range(10 ** 6):
    print parser.status_str()
    if parser.is_done():
      break

    section_descriptions = ['rank', 'name', 'score']

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
    assert country_dict['name'].split()[0].isalpha()
    country_dicts.append(country_dict)
  return country_dicts

def main():
  country_dicts = txt_dump_to_dicts()
  utils.write_json('_0_countries_mipex.json', country_dicts)

if __name__ == '__main__':
  main()
