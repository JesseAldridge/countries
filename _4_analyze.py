import utils

def normalize(val, aggr_to_val):
  return (val - aggr_to_val['min']) / (aggr_to_val['max'] - aggr_to_val['min'])

def score(country_dict, attr_to_aggrs):
  factor_names = ['mipex_score', 'gdp', 'ppp']
  normal_vals = []
  for factor_name in factor_names:
    aggr_to_val = attr_to_aggrs[factor_name]
    # assume the mean value from the country's peers if the factor is unknown
    val = country_dict['factor_name'] if factor_name in country_dict else aggr_to_val['mean']
    normal_vals.append(normalize(val, aggr_to_val))
  return sum(normal_vals) / len(normal_vals)

def main():
  country_data = utils.load_json('_3_countries_normalized.json')
  attr_to_aggrs = country_data['attr_to_aggrs']
  country_dicts = country_data['countries']

  for country_dict in sorted(country_dicts.values(), key=score, reverse=True)[:20]:
    print country_dict['name'], round(score(country_dict), 2)




      dist_dict['mean'] = dist_dict['sum'] / dist_dict['n']
      country_dict[key] = {
        'raw': val,
        'norm': (
          (country_dict[key] - dist_dict['min']) /
          (dist_dict['max'] - dist_dict['min'])
