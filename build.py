#!/usr/bin/env python3

import sh
from os.path import exists, join, relpath, dirname
from os import makedirs
from time import sleep
from sys import argv

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

def build_images(given=None):
    check(sh.rm.bake('-f', sh.glob(join(img_outdir, '*.pdf')), sh.glob(join(img_outdir, '*.svg'))))

    for img in (given or images):
        asci = join(img_indir, img + '.ascii')
        svg = join(img_outdir, img + '.svg')
        pdf = join(img_outdir, img + '.pdf')

        if not exists(asci):
            print('Error: file does not exist: {}'.format(asci))
            exit(1)

        check(a2s.bake('-i'+asci, '-o'+svg))
        sleep(0.1)  # don't know
        check(s2p.bake(svg, pdf))

    print('images done')

def build_tex():
    check(pdftex)
    check(bibtex)
    print('bib done')
    check(pdftex)
    check(pdftex)
    print('tex done')

if not exists(img_outdir):
	makedirs(img_outdir)  # makes out/ too

if len(argv) > 1:
    if 'images' == argv[1]:
        i = None
        if len(argv) > 2:
            i = [argv[2]]
        build_images(i)
    elif 'tex' == argv[1]:
        build_tex()
    else:
        print('unknown options: {}'.format(argv[1:]))
        exit(1)

else:
    build_images()
    build_tex()

print('all done')

