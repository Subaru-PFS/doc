PYTHON = python3

PFS_Abbreviations.tex : abbrevToTex.py PFS_Abbreviations.tsv
	python3 abbrevToTex.py  PFS_Abbreviations.tsv \
		--cat general ics pfi pfs software subaru > PFS_Abbreviations.tex 
