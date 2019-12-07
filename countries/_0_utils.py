import json, codecs, csv

def load_json(path):
  with codecs.open(path, encoding='utf8') as f:
    text = f.read()
  return json.loads(text)

def write_json(path, data_obj):
  json_str = json.dumps(data_obj, indent=2, ensure_ascii=False, separators=(',', ': '))
  with codecs.open(path, encoding='utf8', mode='w') as f:
    f.write(json_str)

def load_csv(path):
  with open(path) as f:
    rows = [row for row in csv.reader(f)]
  labels = rows[0]
  dicts = []
  for i in range(1, len(rows)):
    row = rows[i]
    dict_ = {}
    for key, val in zip(labels, row):
      dict_[key] = val
    dicts.append(dict_)
  return dicts

def write_csv(path, data_obj):
  list_of_dicts = []
  column_labels = set()
  for key, dict_ in data_obj.items():
    list_of_dicts.append(dict_)
    dict_['name'] = key
    column_labels = column_labels | dict_.keys()
  column_labels = list(column_labels)

  with open(path, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(column_labels)
    for dict_ in list_of_dicts:
      row = [dict_.get(key) for key in column_labels]
      writer.writerow(row)

if __name__ == '__main__':
  def test():
    test_filename = '_0_countries_manual.json'
    dict1 = load_json(test_filename)
    write_json(test_filename, dict1)
    dict2 = load_json(test_filename)
    print('dict1:', dict1)
    print('dict2:', dict2)
    assert dict1 == dict2

    dicts = load_csv('_0_hdi.csv')
    print(len(dicts))
    print(dicts[0])
    assert len(dicts) == 178
    assert dicts[0] == {'name': 'Norway', 'hdi': '.953'}
    print('dicts:', len(dicts))
  test()
