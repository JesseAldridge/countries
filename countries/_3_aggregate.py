import re

import _0_utils

countries_numbers = _0_utils.load_json('_2_countries_numbers.json')

attr_to_aggrs = {}
for country_name, country_dict in countries_numbers.items():
  for key, val in country_dict.items():
    # Only handle numbers
    try:
      float(val)
    except ValueError:
      continue

    print('attr_to_aggrs:', attr_to_aggrs)

    attr_to_aggrs.setdefault(key, {})
    dist_dict = attr_to_aggrs[key]

    old_min = dist_dict.get('min')
    new_min = val if old_min is None else min(val, old_min)
    dist_dict['min'] = new_min

    old_max = dist_dict.get('max')
    new_max = val if old_max is None else max(val, old_max)
    dist_dict['max'] = new_max

    dist_dict.setdefault('sum', 0)
    dist_dict['sum'] += val
    dist_dict.setdefault('n', 0)
    dist_dict['n'] += 1

countries_dict = {
  'attr_to_aggrs': attr_to_aggrs,
  'countries': countries_numbers,
}

_0_utils.write_csv('_3_countries_aggregated.json', countries_dict)
