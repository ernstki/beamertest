# mw2beamer

Convert an arbitrary article on your MediaWiki wiki to [Beamer][] slides using
[Pandoc][] (Pandoc, which is awesome by the way). In short, [this][wikitext]
becomes [this][pdf].

Prompts for credentials for a local site protected with HTTP Basic
authentication, but does not cache or save these anywhere.

See [`beamertest`](beamertest) for some experiments with Markdown, Pandoc, and
Beamer. You might find the [`Makefile`](beamertest/Makefile) useful.

## Installation

Make sure you have:

* a `python3` in your search path
* [mwclient][]==0.10.*; `pip install --user mwclient` is fine

Put it in your `$PATH`:

* Copy [`mw2beamer.py`](https://raw.githubusercontent.com/ernstki/mw2beamer/master/mw2beamer/mw2beamer.py)
to some directory in your default search path, _e.g._, `~/bin`
* make it executable with `chmod a+x`
    * you don't need the ".py" extension (on Unix/macOS anyway), so feel free
      to remove that

Try `mw2beamer.py --help`, or `mw2beamer --help` if you removed the `.py` when
you copied it in place.

## Usage

```
usage: mw2beamer.py [-h] [-v] [-q] [-u USER] [-s SITE] [-a AUTHOR]
                    [-i INSTITUTE] [-d DATE] [-t TITLE] [--theme THEME]
                    [--colortheme COLORTHEME] [-l SLIDE_LEVEL]
                    [-o OUTPUT_FILE]
                    article

Convert an article from your wiki to Beamer slides

positional arguments:
  article               the article name to convert

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         print detailed progress (try '-vv')
  -q, --quiet, --silent
                        silence all non-error output
  -u USER, --user USER  the username to authenticate as (default: $USER)
  -s SITE, --site SITE  the hostname to connect to (default: $MW2BEAMER_SITE,
                        else tfwiki.cchmc.org)
  -a AUTHOR, --author AUTHOR
                        the author's name (default: $MW2BEAMER_AUTHOR, else
                        fetched from MediaWiki API)
  -i INSTITUTE, --institute INSTITUTE
                        the author's institute (default: $MW2BEAMER_INSTITUTE)
  -d DATE, --date DATE  date on title slide (default: today's date)
  -t TITLE, --title TITLE
                        The presentation title (default: $MW2BEAMER_TITLE,
                        else the article title with parent pages stripped)
  --theme THEME         the Beamer theme to use; see https://deic-
                        web.uab.cat/~iblanes/beamer_gallery (default:
                        'Copenhagen')
  --colortheme COLORTHEME, --color-theme COLORTHEME
                        the Beamer color theme to use; see https://deic-
                        web.uab.cat/~iblanes/beamer_gallery (default:
                        'default')
  -l SLIDE_LEVEL, --slide-level SLIDE_LEVEL
                        corresponds to Pandoc's '--slide-level' option; see
                        "Structuring the slide show" in pandoc(1) for details
                        (default: based on content)
  -o OUTPUT_FILE, --output-file OUTPUT_FILE, --output OUTPUT_FILE
                        write to this output filename (default: mw2beamer.pdf)

Homepage: https://github.com/ernstki/mw2beamer
```

## See also

* <https://pandoc.org/MANUAL.html#slide-shows>
    * <https://pandoc.org/MANUAL.html#variables-for-beamer-slides>
* <http://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf>
* <https://deic-web.uab.cat/~iblanes/beamer_gallery/>

## Author

Kevin Ernst ([ernstki -at- mail.uc.edu](mailto:ernstki%20-at-%20mail.uc.edu))

## License

[MIT](LICENSE).

[beamer]: https://www.ctan.org/pkg/beamer
[pandoc]: https://pandoc.org/
[wikitext]: mw2beamer/example.wiki_
[pdf]: https://raw.githubusercontent.com/ernstki/mw2beamer/master/mw2beamer/example.pdf
[mwclient]: https://github.com/mwclient/mwclient
