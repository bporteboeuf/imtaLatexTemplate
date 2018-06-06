# imtaLatexTemplate
LaTeX template for IMT Atlantique reports


## Installation

This package contains two LaTeX files: `imta_core.sty` and `imta_extra.sty`.
The `core` file provides the main features for producing a report that conforms to the official IMT Atlantique style.
The `extra` file provides advanced features, including code formatting.

You can either simply copy and paste the files in your local working repository, or install this template once for all your documents using the provided Python script. Simply run `imta_install.py` and everything should be done automatically.
This script is compatible with Python 2 and 3, and supports both MikTeX and TeXLive installations.


## Compilation

This template is intended to be compiled with `pdflatex`.
Furthermore, it makes use of the `minted` package.
As a consequence, the compiler needs to be passed the `--shell-escape` flag.
In addition, as usual when wishing a table of contents, the main document should be compiled twice, so as to make sure that the references refer to the right labels.
If your main document is called `report.tex`, use the following command to compile it:

    $ pdflatex --shell-escape report.tex


## New to LaTeX?

If you are new to LaTeX, we recommend you to have a look at the following resources:
  - __Share Latex__, _Learn LaTeX in 30 minutes_, https://fr.sharelatex.com/learn/Learn_LaTeX_in_30_minutes
  - __Zeste de Savoir__, _Introduction à LaTeX_, https://zestedesavoir.com/tutoriels/826/introduction-a-latex/
  - __Wiki Books__, _LaTeX_, https://en.wikibooks.org/wiki/LaTeX
