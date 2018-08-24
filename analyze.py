with open('countries_merged.json') as f:
  text = f.read()
country_dicts = json.loads(text)

def score(country_dict):
  factors = ['mipex_score', 'ppp']
  country_dict


for country_dict in country_dicts:
