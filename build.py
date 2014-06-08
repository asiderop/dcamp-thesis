#!/usr/bin/env python3

import sh
from os.path import exists, join, relpath, dirname, abspath
from os import makedirs, chdir
from time import sleep
from sys import argv, stdout

chdir(dirname(abspath(__file__)))
basedir = dirname(relpath(__file__))

img_indir = join(basedir, 'images')
img_outdir = join(basedir, 'out/img')
outdir = join(basedir, 'out')

a2s = sh.Command("/Volumes/Repositories/Personal/asciitosvg/a2s")
s2p = sh.Command("/usr/local/bin/svg2pdf")
pdftex = sh.pdflatex.bake('-output-directory', outdir, 'thesis')
bibtex = sh.bibtex.bake(join(outdir, 'thesis'))

images = [
    'topo',
    'config',
    'data',
    'branch-recovery',
    'root-recovery',
    'node-role-service',
]

def check(cmd):
    try:
        cmd(_no_out=True, _no_err=True, _no_pipe=True)
    except sh.ErrorReturnCode:
        print('Error')
        exit(1)

def pprog(msg):
    print(msg, end='')
    stdout.flush()

def build_images(given=None):

    pprog('building IMAGES: ')

    for img in (given or images):
        asci = join(img_indir, img + '.ascii')
        svg = join(img_outdir, img + '.svg')
        pdf = join(img_outdir, img + '.pdf')

        if not exists(asci):
            print('\nError: file does not exist: {}'.format(asci))
            exit(1)

        pprog(img+' ')

        check(sh.rm.bake('-f', pdf, svg))
        check(a2s.bake('-i'+asci, '-o'+svg))
        sleep(0.1)  # don't know
        check(s2p.bake(svg, pdf))

    print('DONE')

def build_tex():
    pprog('building TEX: ')

    pprog('tex(1) ')
    check(pdftex)

    pprog('bib ')
    check(bibtex)

    pprog('tex(2) ')
    check(pdftex)

    pprog('tex(3) ')
    check(pdftex)

    print('DONE')

#####
# BEGIN MAIN

if not exists(img_outdir):
	makedirs(img_outdir)  # makes out/ too

if len(argv) > 1:
    if argv[1] in ('images', 'images/'):
        i = None
        if len(argv) > 2:
            i = argv[2:]
        build_images(i)
    if argv[1] in ('tex', 'tex/'):
        build_tex()
    else:
        print('unknown options: {}'.format(argv[1:]))
        exit(1)

else:
    build_images()
    build_tex()

print('all done')

