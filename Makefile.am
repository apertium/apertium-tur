###############################################################################
## Makefile for apertium-tur
###############################################################################

RELEASE=1.0
VERSION=1.0.0
LANG1=tur
BASENAME=apertium-$(LANG1)

TARGETS_COMMON = $(LANG1).automorf.hfst $(LANG1).autogen.hfst \
        $(LANG1).rlx.bin

###############################################################################
## tur transducer
###############################################################################

.deps/$(LANG1).twol.hfst: $(BASENAME).$(LANG1).twol
	if [ ! -d .deps ]; then mkdir .deps; fi
	hfst-twolc $< -o $@
 
.deps/$(LANG1).RL.lexc: $(BASENAME).$(LANG1).lexc
	if [ ! -d .deps ]; then mkdir .deps; fi
	cat $< | grep -v 'Dir/LR' > $@
 
.deps/$(LANG1).LR.lexc: $(BASENAME).$(LANG1).lexc
	if [ ! -d .deps ]; then mkdir .deps; fi
	cat $< | grep -v 'Dir/RL' > $@

.deps/$(LANG1).RL.lexc.hfst: .deps/$(LANG1).RL.lexc
	hfst-lexc --format foma $< -o $@

.deps/$(LANG1).LR.lexc.hfst: .deps/$(LANG1).LR.lexc
	hfst-lexc --format foma $< -o $@

.deps/$(LANG1).RL.hfst: .deps/$(LANG1).RL.lexc.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).RL.lexc.hfst -2 .deps/$(LANG1).twol.hfst -o $@

.deps/$(LANG1).LR.hfst: .deps/$(LANG1).LR.lexc.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).LR.lexc.hfst -2 .deps/$(LANG1).twol.hfst -o $@

$(LANG1).autogen.hfst: .deps/$(LANG1).RL.hfst
	hfst-fst2fst -O $< -o $@

$(LANG1).automorf.hfst: .deps/$(LANG1).LR.hfst
	hfst-invert $< | hfst-fst2fst -O -o $@

###############################################################################
## Disambiguation rules 
###############################################################################

$(LANG1).rlx.bin: $(BASENAME).$(LANG1).rlx
	cg-comp $< $@


###############################################################################
## Installation stuff
###############################################################################

apertium_tr_ttdir=$(prefix)/lib/apertium/$(BASENAME)/
apertium_tr_ttsrcdir=$(prefix)/share/apertium/$(BASENAME)/

apertium_tr_tt_DATA=$(LANG1).automorf.hfst $(LANG1).autogen.hfst \
		    $(LANG1).rlx.bin

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = $(BASENAME)-$(RELEASE).pc

install-data-local:
	if [ ! -d $(DESTDIR)$(apertium_tr_ttsrcdir) ]; then mkdir -p $(DESTDIR)$(apertium_tr_ttsrcdir); fi
	$(INSTALL_DATA) $(BASENAME).$(LANG1).lexc $(DESTDIR)$(apertium_tr_ttsrcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).twol $(DESTDIR)$(apertium_tr_ttsrcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).rlx $(DESTDIR)$(apertium_tr_ttsrcdir)


