FILES=main.pdf

all: ${FILES}

%.pdf: %.tex
	pdflatex $<
	bibtex $(subst .tex, , ${<})
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.aux *.bbl *.log *.blg *.toc *.nav *.out *.snm *.vrb *~

cleaner: clean
	rm -f ${FILES}

.PHONY: clean cleaner


