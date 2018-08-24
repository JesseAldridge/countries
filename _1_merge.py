import json, re

name_to_merged = {}

def normalize_name(name):
  norm_name = name.lower()
  alias_to_norm_name = {
    'usa': 'united states',
  }
  return alias_to_norm_name.get(norm_name, norm_name)

# Mipex

with open('_0_countries_mipex.json') as f:
  countries_mipex = json.loads(f.read())

for country_mipex in countries_mipex:
  country_mipex['mipex_score'] = int(country_mipex['score'].split()[0])
  del country_mipex['score']

for country_mipex in countries_mipex:
  norm_name = normalize_name(country_mipex['name'])
  del country_mipex['name']
  name_to_merged.setdefault(norm_name, {})
  for key, attr in country_mipex.iteritems():
    name_to_merged[norm_name][key] = attr
  name_to_merged[norm_name]['name'] = norm_name

# US News

with open('_0_countries_us_news.json') as f:
  countries_us_news = json.loads(f.read())

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

countries_json = json.dumps(name_to_merged, indent=2)
with open('_1_countries_merged.json', 'w') as f:
  f.write(countries_json)
