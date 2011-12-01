all:
	hfst-lexc turmorph.lexc -o turmorph.lexc.hfst
	hfst-twolc turmorph.twol -o turmorph.twol.hfst
	hfst-compose-intersect -1 turmorph.lexc.hfst -2 turmorph.twol.hfst -o turmorph.gen.hfst
	hfst-invert turmorph.gen.hfst -o turmorph.mor.hfst
	hfst-fst2fst -O turmorph.gen.hfst -o tr.autogen.hfst
	hfst-fst2fst -O turmorph.mor.hfst -o tr.automorf.hfst

clean:
	rm turmorph.lexc.hfst turmorph.twol.hfst turmorph.gen.hfst turmorph.mor.hfst tr.autogen.hfst tr.automorf.hfst
