documentation: imta_documentation.tex
	pdflatex -shell-escape imta_documentation.tex
	pdflatex -shell-escape imta_documentation.tex

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.toc
