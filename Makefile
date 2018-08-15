documentation: imta_documentation.tex
	pdflatex -shell-escape imta_documentation.tex
	pdflatex -shell-escape imta_documentation.tex

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.toc

install:
	python3 imta_install.py

deps:
	python3 -c 'import imta_install; imta_install.install_deps()'
