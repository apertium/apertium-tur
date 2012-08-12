FILE=Clean_FILE
all:
	hfst-lexc -f foma $(FILE).lexc -o $(FILE).lexc.hfst
	hfst-twolc -f foma -i ../../apertium-tur.tur.twol -o $(FILE).twol.hfst
	hfst-compose-intersect -1 $(FILE).lexc.hfst -2 $(FILE).twol.hfst -o $(FILE).gen.hfst
	hfst-invert $(FILE).gen.hfst | hfst-fst2fst -O -o $(FILE).hfst

clean:
	rm *.hfst
