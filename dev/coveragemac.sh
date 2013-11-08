DIX=~/apertium/apertium-tur/apertium-tur.tur.lexc
BIN=~/apertium/apertium-tur/tur.automorf.hfst
cat tr.crp  | apertium-destxt | hfst-proc -w $BIN | apertium-retxt | gsed 's/\$\W*\^/$\n^/g' > /tmp/tr.coverage.txt

EDICT=`cat $DIX | grep -e ' N[0-9] ; ' -e ' A[0-9] ; ' -e ' NUM ; ' -e ' PRON-.* ;' -e ' ADV[0-9] ; ' -e ' NP[0-9].* ;' -e ' V.* ; ' | wc -l`; 

EPAR=`cat $DIX | grep 'LEXICON ' | wc -l`;
TOTAL=`cat /tmp/tr.coverage.txt | wc -l`;
KNOWN=`cat /tmp/tr.coverage.txt | grep -v '*' | wc -l`;
COV=`calc $KNOWN / $TOTAL`;
DATE=`date`;

echo -e $DATE"\t"$EPAR":"$EDICT"\t"$KNOWN"/"$TOTAL"\t"$COV >> history.log
tail -1 history.log
date
