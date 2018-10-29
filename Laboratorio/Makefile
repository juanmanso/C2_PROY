# Makefile para los datos relevados

OUTPUT_DIR = ./Mediciones/
SAVE_DIR = ../Octave/Mediciones
FILE = ./Mediciones/*


all: clean
	cp $(OUTPUT_DIR)* $(SAVE_DIR)

clean:
	-rm -f *~
	-rm -f $(SAVE_DIR)/*


graph:
	octave graph.m 
