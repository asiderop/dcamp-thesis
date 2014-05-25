#!/bin/bash

A2S=/Volumes/Repositories/Personal/asciitosvg/a2s
S2P=/usr/local/bin/svg2pdf

INDIR="./images"
OUTDIR="./out/img"

if [ ! -e ${OUTDIR} ]
then
	mkdir -p ${OUTDIR}
fi

TOPOA2S="${A2S} < ${INDIR}/topo.ascii > ${OUTDIR}/topo.svg"
TOPOS2P="${S2P} ${OUTDIR}/topo.svg ${OUTDIR}/topo.pdf"

CONFA2S="${A2S} < ${INDIR}/config.ascii > ${OUTDIR}/config.svg"
CONFS2P="${S2P} ${OUTDIR}/config.svg ${OUTDIR}/config.pdf"

DATAA2S="${A2S} < ${INDIR}/data.ascii > ${OUTDIR}/data.svg"
DATAS2P="${S2P} ${OUTDIR}/data.svg ${OUTDIR}/data.pdf"

runall.sh "rm -f ${OUTDIR}/*.pdf" "rm -f ${OUTDIR}/*.svg" "$TOPOA2S" "$TOPOS2P" "$CONFA2S" "$CONFS2P" "$DATAA2S" "$DATAS2P"
