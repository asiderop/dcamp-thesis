#!/bin/bash

if [ ! -e out ]
then
	mkdir out
fi

if [ "xclean" == "x$1" ]
then
	rm out/*
fi

pdflatex -output-directory out thesis
bibtex out/thesis
pdflatex -output-directory out thesis
pdflatex -output-directory out thesis
