import re

import utils

countries_merged = utils.load_json('countries_merged.json')

for country_name, country_dict in countries_merged.iteritems():
  for key, val in country_dict.iteritems():
    if isinstance(val, basestring):
      # "$186.7 billion" -> "186.7 billion"
      # "#36" -> "36"
      if re.match(r'^[\$#]', val):
        val = val[1:]

      # "22,349" -> "22349"
      val = re.sub(',', '', val)

      split = val.split()
      base_val = float(split[0])

      if split[-1].isalpha():
        # "186.7 billion" -> 1,867,000,000
        last_word = split[-1].lower()
        if last_word[-1] == 's':
          last_word = last_word[:-1]
        word_to_val = {
          'trillion': 10**12,
          'billion': 10**9,
          'million': 10**6,
          'thousand': 10**3,
        }
        base_val *= word_to_val[last_word]
        base_val = round(base_val, 4) # floating point imprecision
      country_dict[key] = base_val

utils.write_json('countries_numbers.json', countries_merged)
