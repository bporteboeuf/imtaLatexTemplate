# imtaLatexTemplate
LaTeX template for IMT Atlantique reports

\author{Armand FOUCAULT}
\date{October 05, 2017}
\title{\LaTeX{} report template}
\subtitle{Description of the \LaTeX{} template for IMT Atlantique reports}

\imtaSetIMTStyle


# Project creation and compilation

## Project creation

In order to use this template, create a new directory, and copy into it the following files:

- \imtaInlinecode{bash}{imta.tex}: this file declares all the data that composes the template.
  It needs to be included to the main document, by calling \imtaInlinecode{latex}{\include{imta}}.
- \imtaInlinecode{bash}{titlepage.pdf}: the title page of the document.
  It is a blank version of the IMT Atlantique report template, over which an overlay title is written
  by the \imtaInlinecode{latex}{\imtaMaketitlepage} command.

Your document should be a `.tex` file, with the following skeleton:

    \documentclass{article}
    
    \include{imta}
    
    \author{Author name}
    \date{Writing date}
    \title{Document name}
    \subtitle{Short description or subtitle}
    
    \begin{document}
    
    \imtaMaketitlepage
    
    \section{First section}
    
    ...
    
    \end{document}
    
    \end{minted}


## Compilation

This template is intended to be compiled with `pdflatex`.
Furthermore, it makes use of the `minted` package.
As a consequence, the compiler needs to be passed the `-shell-escape` flag.
In addition, as usual when wishing a table of contents, the main document should be compiled twice, so as to make sure that the references refer to the right labels.
If your main document is called `main.tex`, use the following command to compile it:

    $ pdflatex -shell-escape main.tex



# Packages

This template uses a number of packages, with specific options.
Besides, some packages are further configured, through specific commands.
These can be found in the source code itself, at the \imtaInlinecode{latex}{PACKAGES SETTINGS} section.
The following is an abstract from the \imtaInlinecode{latex}{PACKAGES} section of the \imtaInlinecode{bash}{imta.tex} file.

    \usepackage[a4paper, margin=2cm, top=3cm]{geometry}
    \usepackage{graphicx}
    \usepackage{float}
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage{pdfpages}
    \usepackage{fancyhdr}
    \usepackage{minted}
    \usepackage{tikz}
    \usepackage{titling}
    \usepackage{anyfontsize}
    \usepackage{mdframed}

## `anyfontsize`

The \imtaInlinecode{latex}{anyfontsize} package allows picking an arbitrary size for a local font.
It provides the \imtaInlinecode{latex}{\fontsize} command, used for generating the title page inside of a \imtaInlinecode{latex}{tikzpicture} environment.

## `fancyhdr`

The \imtaInlinecode{latex}{fancyhdr} package lets define custom headers and footers.
For instance, the IMT Atlantique header and footer style is defined as follows (inside of the \imtaInlinecode{latex}{\imtaSetIMTStyle} command):

    \pagestyle{fancy}                       % Select the fancy style provided by fancyhdr
    
    \fancyhead{}                            % Clear the current header style
    \fancyfoot{}                            % Clear the current footer style
    
    \fancyhead[L]{\nouppercase\leftmark}    % Define the content of the header:
                                            %     the current section title, on the left
    \fancyfoot[R]{\thepage}                 % Define the content of the footer:
                                            %     the current page number, on the right
    
    \fancypagestyle{imtaFirstpage}{%        % Define the style for the first page
        \fancyhf{}                          % Clear the current style
        \renewcommand{\headrulewidth}{0pt}  % Clear the horizontal rule under the header
    }

## `float`
## `fontenc`
## `geometry`
## `graphicx`
## `inputenc`
## `mdframed`
## `minted`
## `pdfpages`
## `tikz`
## `titling`



# Commands

This template provides a handful of new commands.

## Generic commands

### Metadata commands

This template defines a \imtaInlinecode{latex}{\subtitle} macro, that receives the subtitle of the document.
The latter will be displayed on the title page.
The purpose of this macro is to provide a consistent way of defining a subtitle, with regard to the \imtaInlinecode{latex}{\title}, %
\imtaInlinecode{latex}{\author}, and \imtaInlinecode{latex}{\date} standard macros.
It takes a single parameter, that is the subtitle to display.

## `imta` commands

### Typeset inline code with `imtaInlinecode`###

### Output the title page with `imtaMaketitlepage`

### Answer questions with `imtaQuestion` and `imtaQuestionReset`

The \imtaInlinecode{latex}{\imtaQuestion} command outputs and formats a question counter.
It's meant to be used in reports for assignment with questions.
The counter should be reset with the \imtaInlinecode{latex}{\imtaQuestionReset}.



# Environments

## Generic environments

### Typeset code listings with `minted`



# IMT Atlantique styling

The official IMT Atlantique styling is not really \LaTeX-ish, and takes the decision to use a sans-serif font for body text.
Therefore, I chose to use the default \LaTeX{} font settings, which look much more professional.
Of course, this style does not suit the official report style.
Thus, I decided to provide a command that enables that official style.

The main aspects of the official style are:

- \item Use of the Helvetica font for the body;
- \item Section titles in green (\imtaInlinecode{latex}{\imtaGreen}) and other heading titles in gray (\imtaInlinecode{latex}{\imtaGray});
- \item Section title in the header;
- \item Page number at the right corner of the footer.

For comparison, the default style of the template is:

- \item Use of the default Computer Modern font for the body;
- \item Default style for headings: all in black;
- \item Document title at the left corner and author's name at the right corner of the header;
- \item Page number at the center of the footer.

The official IMT Atlantique style can be toggled with the \imtaInlinecode{latex}{\imtaSetIMTStyle} command.
Since it makes use of the \imtaInlinecode{latex}{\usepackage} macro, it needs to be called in the preamble.
No way is provided to disable later in the document the official style.
As a consequence, you cannot have half of the document with the official style, and the other half in the default style.
