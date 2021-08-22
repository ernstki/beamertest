#!/usr/bin/env python3
"""
Convert the named article from your wiki to a Beamer presentation

Author:   Kevin Ernst
Date:     22 August 2021
License:  MIT
"""
import os

HOMEPAGE = 'https://github.com/ernstki/beamertest'
DEFAULT_USER = os.getenv('USER')
DEFAULT_SITE = os.getenv('MW2BEAMER_SITE', 'en.wikipedia.org')


def get_site(site, user, passwd):
    import mwclient
    # FIXME: not everybody uses this auth method
    s = mwclient.Site(site, scheme='http', httpauth=(user, passwd)
    )
    return s


def get_article_wikitext(s, title):
    wt = s.api('query', prop='revisions', titles=title, rvprop='content',
               rvslots='*', formatversion=2)
    return wt


if __name__ == '__main__':
    import getpass
    import subprocess
    from argparse import ArgumentParser

    parser = ArgumentParser(
            description="Convert an article from your wiki to Beamer slides",
            epilog="Homepage: {}".format(HOMEPAGE)
    )

    parser.add_argument('-u', '--user', default=DEFAULT_USER,
            help='the username to authenticate as')
    parser.add_argument('-s', '--site', default=DEFAULT_SITE,
            help='the hostname of the wiki to connect to')
    parser.add_argument('title', help='the article title to convert')

    opts = parser.parse_args()

    print("Authenticating as {} to {}".format(opts.user, opts.site))
    passwd = getpass.getpass("Enter password for {} > ".format(opts.user))
    s = get_site(site, opts.user, passwd)
    wt = get_article_wikitext(s, opts.title).split("\n")
    print(wt[0:10])

