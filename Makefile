all:
	hfst-lexc turmorph.lexc -o turmorph.hfst
	hfst-twolc turmorph.twol -o turmorph.hfst
	hfst-compose-intersect -1 turmorph.hfst -2 turmorph.hfst -o turmorph.gen
	hfst-invert turmorph.gen -o turmorph.mor
