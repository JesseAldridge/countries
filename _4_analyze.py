import utils

country_dicts = utils.load_json('_3_countries_normalized.json')

def score(country_dict):
  factor_names = ['mipex_score', 'gdp', 'ppp']
  vals = [
    country_dict[factor_name]['norm'] for factor_name in factor_names if factor_name in country_dict
  ]
  return sum(vals) / len(vals)

for country_dict in sorted(country_dicts.values(), key=score, reverse=True)[:20]:
  print country_dict['name'], round(score(country_dict), 2)
