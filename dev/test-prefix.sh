#!/bin/bash

SED=gsed
which $SED >/dev/null;
if [[ $? -eq 1 ]]; then
	SED="sed";
fi

TMPSCRIPT=`mktemp /tmp/tmp.XXXXXXXXXX`;
echo "import sys;
tag = False;
c = sys.stdin.read(1);
while c != '':
        if c == '<':
                sys.stdout.write('%<');
                tag = True;
                c = sys.stdin.read(1);
        if c == '>':
                sys.stdout.write('%> ');
                tag = False;
                c = sys.stdin.read(1);
                continue;
        if tag:             
                sys.stdout.write(c);
        else:
                sys.stdout.write(c + ' ');
        c = sys.stdin.read(1);
        if c == '\n':
                break;
" > $TMPSCRIPT;

TMPFILTER=`mktemp /tmp/tmp.f.XXXXXXXXXX`;
TMPREGEX=`mktemp /tmp/tmp.r.XXXXXXXXXX`;
TMPOUT1=`mktemp /tmp/tmp.o1.XXXXXXXXXX`;
TMPOUT2=`mktemp /tmp/tmp.o2.XXXXXXXXXX`;
TMPINVERT=`mktemp /tmp/tmp.i.XXXXXXXXXX`;

echo "~[ \$[ %<num%> ] |
 \$ [ %<subst%> ] |
 \$ [ %<neg%> ] |
 \$ [ %<p2%> ] |
 \$ [ %<p3%> ] |
 \$ [ %<qst%> ] 
] ;" | hfst-regexp2fst -S -o $TMPFILTER
printf "$1" | python3.3 $TMPSCRIPT | $SED 's/^/"/g' | $SED 's/$/?*"/g';
echo ""
printf $1 | python3.3 $TMPSCRIPT | $SED 's/$/?*/g' |  hfst-regexp2fst -o $TMPREGEX
hfst-invert .deps/tur.LR.hfst -o $TMPINVERT
hfst-compose-intersect -1 $TMPINVERT -2 $TMPREGEX -o $TMPOUT1
hfst-compose-intersect -1 $TMPOUT1 -2 $TMPFILTER -o $TMPOUT2
hfst-fst2strings $TMPOUT2 

#rm $TMPFILTER $TMPREGEX $TMPOUT1 $TMPOUT2 $TMPINVERT $TMPSCRIPT
