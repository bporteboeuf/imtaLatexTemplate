documentation: imta_documentation.tex
	pdflatex -shell-escape imta_documentation.tex
	pdflatex -shell-escape imta_documentation.tex

clean:
	rm *.aux
	rm *.log
	rm *.out
	rm *.toc
