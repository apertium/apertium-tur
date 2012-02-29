all:
	hfst-lexc apertium-tur.tur.lexc -o tur.lexc.hfst
	hfst-twolc apertium-tur.tur.twol -o tur.twol.hfst
	hfst-compose-intersect -1 tur.lexc.hfst -2 tur.twol.hfst -o tur.gen.hfst
	hfst-invert tur.gen.hfst -o tur.mor.hfst
	hfst-fst2fst -O tur.gen.hfst -o tr.autogen.hfst
	hfst-fst2fst -O tur.mor.hfst -o tr.automorf.hfst

clean:
	rm tur.lexc.hfst tur.twol.hfst tur.gen.hfst tur.mor.hfst tr.autogen.hfst tr.automorf.hfst
