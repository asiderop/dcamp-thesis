#!/bin/bash

if [ "xclean" == "x$1" ]
then
	rm out/*
fi

pdflatex -output-directory out thesis
bibtex out/thesis
pdflatex -output-directory out thesis
pdflatex -output-directory out thesis
