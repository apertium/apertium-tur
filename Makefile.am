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
## Turkish transducer
###############################################################################

.deps/$(LANG1).twol.hfst: $(BASENAME).$(LANG1).twol
	test -d .deps || mkdir .deps
	hfst-twolc $< -o $@

.deps/$(LANG1).RL.lexc: $(BASENAME).$(LANG1).lexc
	test -d .deps || mkdir .deps
	cat $< | grep -v 'Dir/LR' > $@

.deps/$(LANG1).LR.lexc: $(BASENAME).$(LANG1).lexc
	test -d .deps || mkdir .deps
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
#
#   apertium_tur_libdir: This is where the compiled binaries go
#   apertium_tur_srcdir: This is where the source files go

apertium_turdir=$(prefix)/lib/apertium/$(BASENAME)/
apertium_tur_srcdir=$(prefix)/share/apertium/$(BASENAME)/

apertium_tur_DATA=$(LANG1).automorf.hfst $(LANG1).autogen.hfst \
		    $(LANG1).rlx.bin

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = $(BASENAME).pc

# Modes are not installed since they're all just "debug modes". All
# modes are created by this goal.
modes/$(LANG1)-morph.mode: modes.xml
	apertium-validate-modes modes.xml
	apertium-gen-modes modes.xml

noinst_DATA=modes/$(LANG1)-morph.mode

install-data-local:
	test -d $(DESTDIR)$(apertium_tur_srcdir) || mkdir -p $(DESTDIR)$(apertium_tur_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).lexc $(DESTDIR)$(apertium_tur_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).twol $(DESTDIR)$(apertium_tur_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).rlx $(DESTDIR)$(apertium_tur_srcdir)

CLEANFILES = $(TARGETS_COMMON)
clean-local:
	-rm -rf .deps modes
