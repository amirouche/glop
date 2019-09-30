#!/usr/bin/env python3
import sys
import json


f = open(sys.argv[1])
next(f)  # skip first line

for line in f:
    item = json.loads(line.strip()[:-1])
    uid = 'https://wikidata.org/wiki/' + item['id']
    aliases = set()
    for lang in ('en', 'en-us', 'en-uk'):
        out = item.get('labels', {}).get(lang, {}).get('value')
        if out is not None:
            aliases.add(out.lower())
        for x in item['aliases'].get(lang, []):
            aliases.add(x['value'].lower())
    for alias in aliases:
        print('{}\t{}'.format(uid, alias))
