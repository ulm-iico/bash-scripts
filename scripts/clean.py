import numpy as np
import os,sys
listextensions=[
'*.aux',
'*.lof',
'*.log',
'*.lot',
'*.fls',
'*.out',
'*.toc',
'*.fmt',
'*.fot',
'*.cb',
'*.brf',
'*.mlf',
'*.cb2',
'*.ist',
'*.slo',
'.*.lb',
'*.dvi',
'*.xdv',
'*-converted-to.*',
'*.bbl',
'*.bcf',
'*.blg',
'*-blx.aux',
'*-blx.bib',
'*.run.xml',
'*.fdb_latexmk',
'*.synctex',
'*.synctex(busy)',
'*.synctex.gz',
'*.synctex.gz(busy)',
'*.pdfsync',
'*.alg',
'*.loa',
'acs-*.bib',
'*.thm',
'*.nav',
'*.pre',
'*.snm',
'*.vrb',
'*.soc',
'*.cut',
'*.cpt',
'*.spl',
'*.ent',
'*.lox',
'*.acn',
'*.acr',
'*.glg',
'*.glo',
'*.gls',
'*.glsdefs',
'*.lzo',
'*.lzs',
'*-gnuplottex-*',
'*.gaux',
'*.gtex',
'*.gtex',
'*.idx',
'*.ilg',
'*.ind',
'*.maf',
'*.mlf',
'*.mlt',
'*.mtc[0-9]*',
'*.slf[0-9]*',
'*.slt[0-9]*',
'*.stc[0-9]*',
'*.mtc',
'_minted*',
'*.pyg',
'*.mw',
'*.nlg',
'*.nlo',
'*.nls',
'*.pax',
'*.pdfpc',
'*.sagetex.sage',
'*.sagetex.py',
'*.sagetex.scmd',
'*.wrt',
'*.sout',
'*.sympy',
'*.upa',
'*.upb',
'*.pytxcode',
'pythontex-files-*/',
'*.listing',
'*.loe',
'*.dpth',
'*.md5',
'*.auxlock',
'*.lod',
'*.xcp',
'*.xmpi',
'*.xdy',
'*.xyc',
'*.xyd',
'*.ttt',
'*.fff',
'*.backup',
'.*.swp',
'*~[0-9]*',
'*.tps',
'./auto/*',
'*.el',
'*.sta',
'*.lpz'
]

path= (sys.argv[1])
removedfiles=[]
for i in os.listdir(path):
    for j in listextensions:
        if j.split('.')[-1] in i:
            print('%s removed by ---> %s extension'%(i,j))
            removedfiles.append(i)

response=input("The above files will be deleted, you're sure? [Y]/n: ")
if response=="Y" or response=="y":
    for i in removedfiles:
        print("Remove %s:"%i)
        os.system("rm -R %s"%i)
else:
    exit
