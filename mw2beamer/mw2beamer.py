#!/usr/bin/env python3
"""
Convert the named article from your wiki to a Beamer presentation

Author:   Kevin Ernst
Date:     22 August 2021
License:  MIT
"""
from __future__ import annotations
import os

HOMEPAGE = 'https://github.com/ernstki/beamertest'
DEFAULT_USER = os.getenv('USER')
DEFAULT_SITE = os.getenv('MW2BEAMER_SITE', 'en.wikipedia.org')
DEFAULT_OUTPUT_FILE = 'mw2beamer.pdf'


def get_site(site: str, user: str, passwd: str) -> mwclient.Site:
    import mwclient
    # FIXME: not everybody uses this auth method
    s = mwclient.Site(site, httpauth=(user, passwd)
    )
    return s


def get_article_wikitext(s: mwclient.Site, title: str) -> OrderedDict:
    r = s.api('query', prop='revisions', titles=title, rvprop='content',
              rvslots='*', formatversion=2)
    wt = r['query']['pages'][0]['revisions'][0]['slots']['main']['content']
    return wt


if __name__ == '__main__':
    import getpass
    import subprocess
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
            formatter_class=ArgumentDefaultsHelpFormatter,
            description="Convert an article from your wiki to Beamer slides",
            epilog="Homepage: {}".format(HOMEPAGE)
    )

    parser.add_argument('-u', '--user', default=DEFAULT_USER,
            help='the username to authenticate as')
    parser.add_argument('-s', '--site', default=DEFAULT_SITE,
            help='the hostname to connect to')
    parser.add_argument('-o', '--output-file', default=DEFAULT_OUTPUT_FILE,
            help='write to this output filename')
    parser.add_argument('title', help='the article title to convert')

    opts = parser.parse_args()

    print("Authenticating as {} to {}".format(opts.user, opts.site))
    passwd = getpass.getpass("Enter password for {} > ".format(opts.user))
    site = get_site(opts.site, opts.user, passwd)
    wt = get_article_wikitext(site, opts.title)

    proc = subprocess.Popen(
            ['pandoc', '-f', 'mediawiki', '-t', 'beamer', '-o',
              opts.output_file],
            stdin=subprocess.PIPE
    )
    proc.communicate(wt.encode('utf8'))
