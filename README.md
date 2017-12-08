# imtaLatexTemplate
LaTeX template for IMT Atlantique reports


## Project creation

This package contains two LaTeX files: `imta_core.sty` and `imta_extra.sty`.
The `core` file provides the main features for producing a report that conforms to the official IMT Atlantique style.
The `extra` file provides advanced features, including code formatting.


## Compilation

This template is intended to be compiled with `pdflatex`.
Furthermore, it makes use of the `minted` package.
As a consequence, the compiler needs to be passed the `-shell-escape` flag.
In addition, as usual when wishing a table of contents, the main document should be compiled twice, so as to make sure that the references refer to the right labels.
If your main document is called `report.tex`, use the following command to compile it:

    $ pdflatex -shell-escape report.tex

In order to make the compilation step easier, this repository provides the `compile.py` script, written in Python 3.
Running this script by simply invoking `./compile` in a shell will take care of all the obnoxious compilation details.
You can see this as a Makefile, run with the `make` command.
At the first execution, the script will ask you the path of the main file, that is, the `.tex` file you would pass to `pdflatex`.

    $ ./compile 
    Is skeleton.tex the main file?
    [yes/no]> n
    Detected .tex files:
    	imta_documentation.tex
    Type in the path of the main file
    > 

This will create a `.latexCompileSetup` file, that contains a pickled Python object, representing the settings for your project.
