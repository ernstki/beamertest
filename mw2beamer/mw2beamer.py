#!/usr/bin/env python3
"""
Convert the named article from your wiki to a Beamer presentation

Author:   Kevin Ernst
Date:     22 August 2021
License:  MIT
"""
from __future__ import annotations

import os
import logging
from datetime import datetime as dt

HOMEPAGE = 'https://github.com/ernstki/mw2beamer'
DEFAULT_USER = os.getenv('USER')
DEFAULT_SITE = os.getenv('MW2BEAMER_SITE', 'your.site.local')
# added to slides (first slide, titles) and PDF metadata
DEFAULT_TITLE = os.getenv('MW2BEAMER_TITLE')
DEFAULT_AUTHOR = os.getenv('MW2BEAMER_AUTHOR')
DEFAULT_INSTITUTE = os.getenv('MW2BEAMER_INSTITUTE')
DEFAULT_DATE = dt.strftime(dt.now(), '%e %b %Y')
# see also https://hartwork.org/beamer-theme-matrix/
BEAMER_GALLERY = 'https://deic-web.uab.cat/~iblanes/beamer_gallery'
DEFAULT_BEAMER_THEME = 'Copenhagen'
DEFAULT_BEAMER_COLORTHEME = 'default'
DEFAULT_OUTPUT_FILE = 'mw2beamer.pdf'
DEFAULT_LOG_LEVEL = logging.WARNING
VERBOSE_LOG_FMT = '[%(levelname)s] %(asctime)s - %(message)s'


def get_site(site: str, user: str, passwd: str) -> mwclient.Site:
    import mwclient
    # FIXME: not everybody uses this auth method
    s = mwclient.Site(site, httpauth=(user, passwd))
    return s


def get_author_name(site: mwclient.Site) -> OrderedDict:
    r = site.api('query', meta='userinfo', uiprop='realname')
    realname = r['query']['userinfo']['realname']
    # FIXME: what happens here if it's empty?
    return realname


def get_article_wikitext(site: mwclient.Site, title: str) -> OrderedDict:
    r = site.api('query', prop='revisions', titles=title, rvprop='content',
              rvslots='*', formatversion=2)
    wt = r['query']['pages'][0]['revisions'][0]['slots']['main']['content']
    return wt


if __name__ == '__main__':
    import getpass
    import subprocess
    from argparse import ArgumentParser #, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
            description="Convert an article from your wiki to Beamer slides",
            epilog="Homepage: {}".format(HOMEPAGE)
            # I need more control over certain ones, so I'm doing this by hand
            #formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-v', '--verbose', action='count',  # <-- type=int
            help="print detailed progress (try '-vv')")
    parser.add_argument('-q', '--quiet', '--silent', action='store_true',
            help='silence all non-error output')
    parser.add_argument('-u', '--user', default=DEFAULT_USER,
            help='the username to authenticate as (default: $USER)')
    parser.add_argument('-s', '--site', default=DEFAULT_SITE,
            help='the hostname to connect to (default: $MW2BEAMER_SITE, '
                 "else {})".format(DEFAULT_SITE))
    parser.add_argument('-a', '--author', default=DEFAULT_AUTHOR,
            help="the author's name (default: $MW2BEAMER_AUTHOR, else "
                 'fetched from MediaWiki API)')
    parser.add_argument('-i', '--institute', default=DEFAULT_INSTITUTE,
            help="the author's institute (default: $MW2BEAMER_INSTITUTE)")
    parser.add_argument('-d', '--date', default=DEFAULT_DATE,
            help="date on title slide (default: today's date)")
    parser.add_argument('-t', '--title', default=DEFAULT_TITLE,
            help='The presentation title (default: $MW2BEAMER_TITLE, else '
                  'the article title with parent pages stripped)')
    parser.add_argument('--theme', default=DEFAULT_BEAMER_THEME,
            help="the Beamer theme to use; see {} (default: '{}')"
                 .format(BEAMER_GALLERY, DEFAULT_BEAMER_THEME))
    parser.add_argument('--colortheme', '--color-theme',
            default=DEFAULT_BEAMER_COLORTHEME,
            help="the Beamer color theme to use; see {} (default: '{}')"
                 .format(BEAMER_GALLERY, DEFAULT_BEAMER_COLORTHEME))
    parser.add_argument('-l', '--slide-level', type=int,
            help="corresponds to Pandoc's '--slide-level' option; see "
                 '"Structuring the slide show" in pandoc(1) for details '
                 '(default: based on content)')
    parser.add_argument('-o', '--output-file', '--output',
            default=DEFAULT_OUTPUT_FILE,
            help="write to this output filename (default: {})"
                 .format(DEFAULT_OUTPUT_FILE))
    parser.add_argument('article', help='the article name to convert')

    opts = parser.parse_args()
    # parse out the debug level from the '-v', '-vv' option
    if opts.verbose:
        # start with the default (logging.WARNING==30), subtract 10 per '-v'
        logging.basicConfig(level=DEFAULT_LOG_LEVEL - opts.verbose*10,
                            format=VERBOSE_LOG_FMT)
    else:
        logging.basicConfig(format="%(message)s")

    print("Authenticating as {} to {}".format(opts.user, opts.site))
    passwd = getpass.getpass("Enter password for {}> ".format(opts.user))

    logging.info("Logging in to {} as {}".format(opts.site, opts.user))
    site = get_site(opts.site, opts.user, passwd)

    # get the user full name if it's still empty
    if not opts.author:
        opts.author = get_author_name(site)

    # FIXME: maybe get rendered HTML instead, that way links & images work
    logging.info("Querying revisions for '{}'".format(opts.article))
    wt = get_article_wikitext(site, opts.article)

    pandoc_args = [
        '-f', 'mediawiki',
        '-t', 'beamer',
        '-o', opts.output_file,
        '-V', "theme={}".format(opts.theme),
        '-V', "colortheme={}".format(opts.colortheme),
        '-M', "title={}".format(
            opts.title if opts.title else opts.article.split('/')[-1]),
        '-M', "author={}".format(opts.author),
        '-M', "institute={}".format(opts.institute),
        '-M', "date={}".format(opts.date),
    ]

    # controls which slides get turned into slides, sections, subsections, or
    # what Beamer calls "blocks" (a styled box within a slide)
    if opts.slide_level:
        pandoc_args += [ "--slide-level={}".format(opts.slide_level) ]

    logging.info("Running Pandoc to create '{}".format(opts.output_file))
    # show (quoted) command line arguments if '-vv' optiongiven
    logging.debug("Command: pandoc {}".format(
        ' '.join(["'{}'".format(x) if ' ' in x else x for x in pandoc_args])))
    proc = subprocess.Popen(['pandoc', *pandoc_args], stdin=subprocess.PIPE)
    proc.communicate(wt.encode('utf8'))

    if not opts.quiet:
        logging.info("Wrote '{}'.".format(opts.output_file))
