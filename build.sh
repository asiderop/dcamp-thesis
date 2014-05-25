#!/bin/bash

PDFTEX=pdflatex
BIBTEX=bibtex

if [ ! -e out ]
then
	mkdir out
fi

if [ "xclean" == "x$1" ]
then
	rm out/*
fi

TEXCMD="${PDFTEX} -output-directory ./out thesis"
BIBCMD="${BIBTEX} ./out/thesis"

runall.sh ./build-images.sh "${TEXCMD}" "${BIBCMD}" "${TEXCMD}" "${TEXCMD}"
