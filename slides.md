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

Inline, with a `data:` URI; shows up in the Beamer slides, but weirdly sized.

~~~mermaid
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
~~~

## Mermaid diagram (PDF version)

`.mermaid format=svg` hidden from slides in a "notes" section, but shows up in README.

::: notes
~~~{.mermaid loc=img filename=mermaid format=svg}
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
~~~
:::

\centerline{\includegraphics[width=3in]{img/mermaid.pdf}}

<small>Hat tip to Jeromy Anglim for the size/alignment tip using
`\includegraphics`[^1]</small>

[^1]: https://jeromyanglim.blogspot.com/2012/07/beamer-pandoc-markdown.html

## A plain slide, bottom-aligned {.plain}
Just a plain old slide.[^2]

[^2]: Do footnotes work?

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
* [mermaid-filter](https://github.com/raghur/mermaid-filter)
    * [How to include SVG diagrams in LaTeX?](https://tex.stackexchange.com/a/2107)
        * I just ended up using librsvg's `svg2pdf` in the Makefile
:::
