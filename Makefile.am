###############################################################################
## Makefile for apertium-tur
###############################################################################

VERSION=0.1.0
LANG=tur
BASENAME=apertium-$(LANG)

TARGETS_COMMON = $(LANG).automorf.hfst $(LANG).autogen.hfst \
        $(LANG).rlx.bin

###############################################################################
## tur transducer
###############################################################################

.deps/$(LANG).twol.hfst: $(BASENAME).$(LANG).twol
	if [ ! -d .deps ]; then mkdir .deps; fi
	hfst-twolc $< -o $@
 
.deps/$(LANG).RL.lexc: $(BASENAME).$(LANG).lexc
	if [ ! -d .deps ]; then mkdir .deps; fi
	cat $< | grep -v 'Dir/LR' > $@
 
.deps/$(LANG).LR.lexc: $(BASENAME).$(LANG).lexc
	if [ ! -d .deps ]; then mkdir .deps; fi
	cat $< | grep -v 'Dir/RL' > $@

.deps/$(LANG).RL.lexc.hfst: .deps/$(LANG).RL.lexc
	hfst-lexc --format foma $< -o $@

.deps/$(LANG).LR.lexc.hfst: .deps/$(LANG).LR.lexc
	hfst-lexc --format foma $< -o $@

.deps/$(LANG).RL.hfst: .deps/$(LANG).RL.lexc.hfst .deps/$(LANG).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG).RL.lexc.hfst -2 .deps/$(LANG).twol.hfst -o $@

.deps/$(LANG).LR.hfst: .deps/$(LANG).LR.lexc.hfst .deps/$(LANG).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG).LR.lexc.hfst -2 .deps/$(LANG).twol.hfst -o $@

$(LANG).autogen.hfst: .deps/$(LANG).RL.hfst
	hfst-fst2fst -O $< -o $@

$(LANG).automorf.hfst: .deps/$(LANG).LR.hfst
	hfst-invert $< | hfst-fst2fst -O -o $@

###############################################################################
## Disambiguation rules 
###############################################################################

$(LANG).rlx.bin: $(BASENAME).$(LANG).rlx
	cg-comp $< $@


###############################################################################
## Installation stuff
###############################################################################

apertium_tr_ttdir=$(prefix)/lib/apertium/$(BASENAME)/
apertium_tr_ttsrcdir=$(prefix)/share/apertium/$(BASENAME)/

apertium_tr_tt_DATA=$(LANG).automorf.hfst $(LANG).autogen.hfst \
		    $(LANG).rlx.bin


install-data-local:
	if [ ! -d $(DESTDIR)$(apertium_tr_ttsrcdir) ]; then mkdir -p $(DESTDIR)$(apertium_tr_ttsrcdir); fi
	$(INSTALL_DATA) $(BASENAME).$(LANG).lexc $(DESTDIR)$(apertium_tr_ttsrcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG).twol $(DESTDIR)$(apertium_tr_ttsrcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG).rlx $(DESTDIR)$(apertium_tr_ttsrcdir)

