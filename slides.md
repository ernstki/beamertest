---
title: Presentation Title
subtitle: A presentation on presentations
subject: A presentation about presentations with Markdown + Pandoc + Beamer
date: 2021-08-22
institute: Weirauch Lab
author:
  - Kevin Ernst
---

# Section One Title

## Intro slide title

A presentation about presentations.

## Slide one
* point one
* point two

## Slide two
This will not reveal incrementally, because it’s in a blockquote.

> * point one
> * point two

## Slide with a pause
\framesubtitle{Look Ma, a subtitle!} 

content before the pause

. . . 

### content after the pause

* with
* bullets

# Section Two

## Two-A

:::: columns

::: column

- it's a column!

:::

::: column

- look, another one!

:::

::::

# Section Three Title

## Mermaid diagram

Using a `data:` URI [doesn't work][gh270] on GitHub, so use `loc=` to generate
an external file.

This _does_ show up in the Beamer slides, but weirdly positioned/sized, no matter what I do.

~~~{.mermaid loc=img filename=mermaid format=png width=400}
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
~~~

## Mermaid diagram (PDF version)

Here a `.mermaid format=svg` hidden from slides in a "notes" section, but shows
up in the README. 

::: notes
~~~{.mermaid loc=img filename=mermaid format=svg}
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
~~~
:::

The Makefile generates a PDF version that can be embedded[^0] into the next
slide with LaTeX's `\includegraphics`. So sometimes you have to `make` twice.

[^0]: https://tex.stackexchange.com/questions/2099/how-to-include-svg-diagrams-in-latex

## Mermaid diagram (PDF version, cont'd)

Here's the `\includegraphics` version, using the PDF, which shows up in the
PDF slides but not the README. Hat tip to Jeromy Anglim.[^1]</small>

\centerline{\includegraphics[width=3in]{img/mermaid.pdf}}

[^1]: https://jeromyanglim.blogspot.com/2012/07/beamer-pandoc-markdown.html

## A plain slide, bottom-aligned {.plain}
Just a plain old slide.[^2]

[^2]: Do footnotes work? (not in GitHub, they don't)

## Conclusion
QED.

## References / See Also

::: nonincremental
* <https://garrettgman.github.io/rmarkdown/authoring_pandoc_markdown.html>
    * [incremental lists](https://garrettgman.github.io/rmarkdown/authoring_pandoc_markdown.html#incremental_lists)
    * [structuring the slide show](https://garrettgman.github.io/rmarkdown/authoring_pandoc_markdown.html#structuring_the_slide_show)
* <https://github.com/jgm/pandoc/issues/5031>
    * basically, `\framesubtitle{The frame's subtitle}` is the only way
* [beameruserguide.pdf](http://ctan.math.utah.edu/ctan/tex-archive/macros/latex/contrib/beamer/doc/beameruserguide.pdf)
* <https://deic-web.uab.cat/~iblanes/beamer_gallery/>
* [mermaid-filter][mf]
    * [github/markup #270][gh270] - GitHub doesn't support `data:` URIs in Markdown
    * [How to include SVG diagrams in LaTeX?](https://tex.stackexchange.com/a/2107)
        * I just ended up using librsvg's `svg2pdf` in the Makefile
:::

[mf]: https://github.com/raghur/mermaid-filter
[gh270]: https://github.com/github/markup/issues/270
