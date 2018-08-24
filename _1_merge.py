import json, re

import _0_utils

def merge_with_main(country_dict, name_to_country):
  for name_key in country_dict:
    if 'name' in name_key:
      break
  lower_name = country_dict[name_key].lower()
  alias_to_norm_name = {
    'usa': 'united states',
  }
  del country_dict[name_key]
  norm_name = alias_to_norm_name.get(lower_name, lower_name)
  country_dict['norm_name'] = norm_name
  name_to_country.setdefault(norm_name, {'name': norm_name})
  for key, attr in country_dict.iteritems():
    name_to_country[norm_name][key] = attr


def merge_all_with_main(country_dicts, name_to_country):
  for country_dict in country_dicts:
    merge_with_main(country_dict, name_to_country)

def main():
  name_to_country = {}

  # Mipex

  countries_mipex = _0_utils.load_json('_0_countries_mipex.json')
  for country_mipex in countries_mipex:
    country_mipex['mipex_score'] = int(country_mipex['score'].split()[0])
    del country_mipex['score']

  # Augmenting Mipex with guesses
  extra_mipex = _0_utils.load_json('_0_countries_mipex_guess.json')

  merge_all_with_main(countries_mipex + extra_mipex, name_to_country)

  # US News

  countries_us_news = _0_utils.load_json('_0_countries_us_news.json')
  for country_us_news in countries_us_news:
    del country_us_news['notes']

  # Augment US News with manually looked up facts
  countries_extra = _0_utils.load_json('_0_countries_manual.json')

  merge_all_with_main(countries_us_news + countries_extra, name_to_country)

  # GDP PPP from Wikipedia
  countries_gdp_ppp = _0_utils.load_json('_0_countries_gdp_ppp.json')
  merge_all_with_main(countries_gdp_ppp, name_to_country)

  # Sanity check
  for country_dict in name_to_country.values():
    assert len(country_dict) > 2

  # Output
  _0_utils.write_json('_1_countries_merged.json', name_to_country)

if __name__ == '__main__':
  main()
