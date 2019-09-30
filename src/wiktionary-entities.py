#!/usr/bin/env python3
import sys

import requests



def eprint(message):
    print(message, file=sys.stderr)


if len(sys.argv) == 2:
    base_url = sys.argv[1]
    eprint("Starting '{}' from scratch".format(base_url))
else:
    eprint("Usage: ./dump.py BASE_URL")
    sys.exit(1)

if not base_url.endswith("/"):
    base_url += "/"

WIKI_ALL_PAGES = (
    "{}w/api.php?action=query&list=allpages&format=json&aplimit=500&apfrom={}"
)


def iter_titles():
    apfrom = ''
    while True:
        url = WIKI_ALL_PAGES.format(base_url, apfrom)
        response = requests.get(url)
        items = response.json()
        for item in items["query"]["allpages"]:
            yield item["title"]
        # continue?
        apfrom = items.get("continue", {}).get("apcontinue")
        if apfrom is None:
            break


for title in iter_titles():
    surface = title.replace('_', ' ').lower()
    if any(x not in 'abcdefhijklmnopqrstuvwxyz ' for x in surface):
        eprint('skip {}'.format(surface))
        continue
    uid = base_url + 'wiki/' + title
    print("{}\t{}".format(uid, surface))
