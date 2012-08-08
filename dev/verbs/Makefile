all:
	hfst-lexc VERBS-scraps.lexc -o VERBS-scraps.lexc.hfst
	hfst-twolc -i ../../apertium-tur.tur.twol -o VERBS-scraps.twol.hfst
	hfst-compose-intersect -1 VERBS-scraps.lexc.hfst -2 VERBS-scraps.twol.hfst -o VERBS-scraps.gen.hfst
	hfst-invert VERBS-scraps.gen.hfst | hfst-fst2fst -O -o VERBS-scraps.hfst

clean:
	rm *.hfst
