#!/usr/bin/env python

"""
crossref-client.py - Implement a tool for interaction with the api.crossref.org

Usage:
    crossref-client.py -h | --help
    crossref-client.py [-c]

Options:
    -h --help                   Show the help message
    -c --count-publishers       Display the number of publishers available
                                [default:False]
"""

__author__ = "University of Florida CTS-IT Team"

import json
import requests
from docopt import docopt
from publisher import Publisher

API_URL_MEMBERS = 'http://api.crossref.org/members'


def main():
    args = docopt(__doc__, help=True)

    pub_count = count_publishers(API_URL_MEMBERS)

    if args['--count-publishers']:
        print("Total publishers @ {}: {}".format(API_URL_MEMBERS, pub_count))
    else:
        print("List of {} publishers: ".format(pub_count))
        groups = pub_count/1000 + 1

        for offset in range(0, groups):
            publishers = get_publishers(API_URL_MEMBERS, offset*1000)

            for idx, pub in enumerate(publishers):
                print("{}: {}".format(idx, pub.to_string()))


def count_publishers(url):
    """
    @return the total number of publishers
    """
    params = {'rows': 0}
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data['message']['total-results']


def get_publishers(url, offset):
    """
    @return a list of publishers
    """
    pubs = []
    params = {'rows': 1000, 'offset': offset}
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    for pub_data in data['message']['items']:
        pub = Publisher(pub_data)
        pubs.append(pub)

    return pubs


if __name__ == "__main__":
    main()
