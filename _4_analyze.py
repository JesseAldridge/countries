import _0_utils

def normalize(val, aggr_to_val):
  return (val - aggr_to_val['min']) / (aggr_to_val['max'] - aggr_to_val['min'])

def score(country_dict, attr_to_aggrs):
  factor_names = ['mipex_score', 'gdp', 'gdp_ppp']
  normal_vals = []
  for factor_name in factor_names:
    # Ignore the factor if it is unknown for this country.
    if factor_name not in country_dict:
      continue
    aggr_to_val = attr_to_aggrs[factor_name]
    val = country_dict[factor_name]
    normal_vals.append(normalize(val, aggr_to_val))
  if len(normal_vals) == 0:
    return 0
  return sum(normal_vals) / len(normal_vals)

def main():
  country_data = _0_utils.load_json('_3_countries_aggregated.json')
  attr_to_aggrs = country_data['attr_to_aggrs']
  country_dicts = country_data['countries']

  def score_country(country_dict):
    return score(country_dict, attr_to_aggrs)

  for country_dict in sorted(country_dicts.values(), key=score_country, reverse=True)[:20]:
    print country_dict['name'], round(score_country(country_dict), 2)

if __name__ == '__main__':
  main()
