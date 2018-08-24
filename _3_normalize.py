import re

import utils

countries_numbers = utils.load_json('_2_countries_numbers.json')

attr_to_dist = {}
for country_name, country_dict in countries_numbers.iteritems():
  for key, val in country_dict.iteritems():
    print 'attr_to_dist:', attr_to_dist

    attr_to_dist.setdefault(key, {})
    dist_dict = attr_to_dist[key]

    old_min = dist_dict.get('min')
    new_min = val if old_min is None else min(val, old_min)
    dist_dict['min'] = new_min

    old_max = dist_dict.get('max')
    new_max = val if old_max is None else max(val, old_max)
    dist_dict['max'] = new_max

for country_name, country_dict in countries_numbers.iteritems():
  for key, val in country_dict.iteritems():
    # Only handle numbers
    try:
      float(val)
    except ValueError:
      continue

    dist_dict = attr_to_dist[key]
    country_dict[key] = {
      'raw': val,
      'norm': (
        (country_dict[key] - dist_dict['min']) /
        (dist_dict['max'] - dist_dict['min'])
      )
    }

utils.write_json('_3_countries_normalized.json', countries_numbers)
