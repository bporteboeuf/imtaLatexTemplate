# imtaLatexTemplate
LaTeX template for IMT Atlantique reports - *version française en bas*


## Installation

This package contains two LaTeX files: `imta_core.sty` and `imta_extra.sty`.
The `core` file provides the main features for producing a report that conforms to the official IMT Atlantique style.
The `extra` file provides advanced features, including code formatting.

You can either simply copy and paste the files in your local working repository, or install this template once for all your documents using the provided Python script. Simply run `imta_install.py` and everything should be done automatically.
This script is compatible with Python 2 and 3, and supports both MikTeX and TeXLive installations.


## Compilation

This template is intended to be compiled with `pdflatex`.
Furthermore, the `extra` file makes use of the `minted` package. As a consequence, the compiler needs to be passed the `--shell-escape` flag.
In addition, as usual when wishing a table of contents, the main document should be compiled twice, so as to make sure that the references refer to the right labels.
If your main document is called `report.tex`, use the following command to compile it:

    $ pdflatex --shell-escape report.tex


## New to LaTeX?

If you are new to LaTeX, we recommend you to have a look at the following resources:
  - __Share Latex__, _Learn LaTeX in 30 minutes_, https://fr.sharelatex.com/learn/Learn_LaTeX_in_30_minutes
  - __Zeste de Savoir__, _Introduction à LaTeX_, https://zestedesavoir.com/tutoriels/826/introduction-a-latex/
  - __Wiki Books__, _LaTeX_, https://en.wikibooks.org/wiki/LaTeX
  
  Also, you might want to have a look to the provided `skeleton.tex` file for a ready-to-use first document. 


<br>
<br>
<br>
__________________________

## Installation

Ce module contient deux fichiers LaTeX : `imta_core.sty` et `imta_extra.sty`.
Le fichier `core` donne accès à toutes les principales fonctionnalités pour produire un document conforme à l'identité graphique de l'IMT Atlantique.
Le fichier `extra` donne accès à des fonctionnalités additionnelles, notamment la coloration syntaxique.

Vous pouvez soit simplement copier les fichiers dans votre répertoire de travail, ou bien installer ce module pour l'ensemble de votre distribution LaTeX en éxécutant le script Python `imta_install.py` fourni.
Ce script est compatible avec Python 2 et 3, et supporte les distributions MikTeX et LaTeX.


## Compilation

Ce template est censé être compilé avec `pdflatex`.
De plus, le fichier `extra` utilise le module `minted`. Il est donc nécessaire de passer l'option `--shell-escape` au compilateur.
Enfin, comme tous les autres documents LaTeX, il peut être nécessaire de compiler le document plusieurs fois pour que toutes les références (comme dans la table des matières) soient évaluées correctement.
Si votre document se nomme `rapport.tex`, vous pouvez le compiler via la ligne de commande suivante :

    $ pdflatex --shell-escape rapport.tex


## Débutant en LaTeX ?

Si vous débutez en LaTeX, nous vous recommandons de regarder les ressources suivantes :
  - __Share Latex__, _Learn LaTeX in 30 minutes_, https://fr.sharelatex.com/learn/Learn_LaTeX_in_30_minutes
  - __Zeste de Savoir__, _Introduction à LaTeX_, https://zestedesavoir.com/tutoriels/826/introduction-a-latex/
  - __Wiki Books__, _LaTeX_, https://en.wikibooks.org/wiki/LaTeX
  
  Vous serez aussi peut-être intéressé par le fichier `skeleton.tex` qui propose un squelette de document, prêt à l'emploi.
  
