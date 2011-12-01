all:
	hfst-lexc ninfl.lexc -o ninfl.hfst
	hfst-twolc turmorph.twol -o turmorph.hfst
	hfst-compose-intersect -1 ninfl.hfst -2 turmorph.hfst -o turmorph.gen
