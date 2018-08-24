import json, re

import utils

name_to_merged = {}

def normalize_name(name):
  norm_name = name.lower()
  alias_to_norm_name = {
    'usa': 'united states',
  }
  return alias_to_norm_name.get(norm_name, norm_name)

# Mipex

countries_mipex = utils.load_json('_0_countries_mipex.json')
for country_mipex in countries_mipex:
  country_mipex['mipex_score'] = int(country_mipex['score'].split()[0])
  del country_mipex['score']

# Augmenting Mipex with guesses

extra_mipex = utils.load_json('_0_countries_mipex_guess.json')
countries_mipex += extra_mipex

for country_mipex in countries_mipex:
  norm_name = normalize_name(country_mipex['name'])
  del country_mipex['name']
  name_to_merged.setdefault(norm_name, {})
  for key, attr in country_mipex.iteritems():
    name_to_merged[norm_name][key] = attr
  name_to_merged[norm_name]['name'] = norm_name

# US News

countries_us_news = utils.load_json('_0_countries_us_news.json')
for country_us_news in countries_us_news:
  del country_us_news['notes']
  country_us_news['ppp'] = int(re.sub('[^0-9]', '', country_us_news['ppp']))

for country_us_news in countries_us_news:
  norm_name = normalize_name(country_us_news['country_name'])
  del country_us_news['country_name']
  name_to_merged.setdefault(norm_name, {})
  for key, attr in country_us_news.iteritems():
    name_to_merged[norm_name][key] = attr
  name_to_merged[norm_name]['name'] = norm_name

for country_dict in name_to_merged.values():
  assert len(country_dict) > 2

utils.write_json('_1_countries_merged.json', name_to_merged)
