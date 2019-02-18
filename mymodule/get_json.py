import hidden
import requests
from requests_oauthlib import OAuth1
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json?screen_name='


def get_object(acct):
    f = open('subs.json', 'w')
    # get api keys
    keys = hidden.oauth().values()

    # get json object
    auth = OAuth1(*keys)
    url = TWITTER_URL + acct
    req = requests.get(url, auth=auth).text

    # write data from json in file
    js = json.loads(req)
    txt = json.dumps(js, indent=4)
    f.write(txt)
    f.close()

    # return json object
    return js


if __name__ == '__main__':
    get_object('usacheva_v')
